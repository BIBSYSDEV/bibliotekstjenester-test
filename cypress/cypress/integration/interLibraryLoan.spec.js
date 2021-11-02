import mockIds from '../../../Stubs/resources/mock_ids.json'

const interLibraryLoanFrontendBaseUrl = "https://ill.test.bibs.aws.unit.no"

context('End to end testing, interlibrary loan', () => {
  beforeEach(() => {
    cy.visit(`${interLibraryLoanFrontendBaseUrl}/?patronid=${mockIds.libraries.ncip_only_library}&recordid=123`);
    cy.wait(1000) // waiting is because of slow lambda api, this should be removed once acceptable performance has been achieved
  });


  it('shows metadata', () => {
    cy.get('[data-testid="metaData"]').contains('Creator');
    cy.get('[data-testid="metaData"]').contains("Kroppens funksjon og oppbygning");
    cy.get('[data-testid="metaData"]').contains("2018");
    cy.get('[data-testid="metaData"]').contains("382");
    cy.get('[data-testid="metaData"]').contains("Oslo");
    cy.get('[data-testid="metaData"]').contains("978-82-05-50862-0");
    cy.get('[data-testid="metaData"]').contains("Gyldendal akademisk");
    cy.get('[data-testid="metaData"]').contains("Gunnar Nicolaysen (1940-) (redaktor/forfatter av forord/forfatter)");
    cy.get('[data-testid="alert"]').should('not.exist');
  });

  it('shows errormessage when metadata-server responds with error', () => {
    cy.visit(`${interLibraryLoanFrontendBaseUrl}/?patronid=${mockIds.libraries.ncip_only_library}&recordid=${mockIds.pnx.trigger_empty_pnx_response}`);
    cy.get('[data-testid="alert"]').should('exist').contains('500');
  });

  it('shows schema', () => {
    cy.get(`[data-testid="patron-field"]`).type('testuser');
    cy.get(`[data-testid="library-option-${mockIds.libraries.library_that_trigger_failure_response_from_ncip}"]`).click();
  });

  it('library show holdings', () => {
    cy.get(`[data-testid="library-label-${mockIds.combination_parameters_that_must_be_used_togheter.success_libraries.library_codes[0]}"]`).contains('1 of 1 available');
  });

  it('library show no info', () => {
    cy.get(`[data-testid="library-label-${mockIds.libraries.ncip_only_library}"]`).contains("No holding information. Contact the library");
  });

  it('library show closed', () => {
    cy.get(`[data-testid="library-label-${mockIds.libraries.trigger_closed_library_response}"]`).contains("Closed for interlibrary loan");
  });

  it('lib_user-access-api shows servererror', () => {
    cy.visit(`${interLibraryLoanFrontendBaseUrl}/?recordid=123&patronid=${mockIds.libraries.trigger_garbled_base_bibliotek_response}`);
    cy.get('[data-testid="alert"]').should('exist').contains('400');
  });

  it('lib_user does not have access to ill', () => {
    cy.visit(`${interLibraryLoanFrontendBaseUrl}/?recordid=123&patronid=${mockIds.libraries.neither_alma_nor_ncip_library}`);
    cy.get('[data-testid="warning"]').should('exist').contains('not available');
  });

  it('lib_user is alma-library and should get a read-only schema', () => {
    cy.visit(`${interLibraryLoanFrontendBaseUrl}/?recordid=123&patronid=1232`);
    cy.get('[data-testid="warning"]').should('exist').contains('Alma libraries');
  });

  it('user needs to fill out form before pressing request-button', () => {
    cy.get(`[data-testid="library-option-${mockIds.libraries.alma_and_ncip_library}"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.get('input:invalid').should('have.length', 1);
    cy.get(`[data-testid="patron-field"]`).type('someText');
    cy.get('input:invalid').should('have.length', 0);
    cy.get(`[data-testid="ncip-request-button"]`).click();
  });

  it('user sends a unsuccessful NCIP-request', () => {
    cy.get(`[data-testid="patron-field"]`).type("userIdentifierForNCIPServerError");
    cy.get(`[data-testid="library-option-${mockIds.libraries.library_that_trigger_failure_response_from_ncip}"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.wait(1000) // waiting is because of slow lambda api, this should be removed once acceptable performance has been achieved
    cy.get('[data-testid="ncip-error-alert"]').should('exist');
  });

  it('user sends a successful NCIP-request', () => {
    cy.get(`[data-testid="patron-field"]`).type('test user');
    cy.get(`[data-testid="library-option-${mockIds.libraries.alma_and_ncip_library}"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.url().should('include', 'success');
    cy.get('[data-testid="ncip-success-alert"]').should('exist');
  });
});
