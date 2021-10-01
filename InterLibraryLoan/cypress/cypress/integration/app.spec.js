
context('End to end testing', () => {
  beforeEach(() => {
    cy.visit('https://ill.test.bibs.aws.unit.no/?patronid=1234571&recordid=123');
    cy.wait(5000)
  });


  it('shows metadata', () => {
    cy.get('[data-testid="metaData"]').contains('Creator');
    cy.get('[data-testid="metaData"]').contains("Kroppens funksjon og oppbygning");
    cy.get('[data-testid="metaData"]').contains("2018");
    cy.get('[data-testid="metaData"]').contains("382");
    cy.get('[data-testid="metaData"]').contains("Oslo");
    cy.get('[data-testid="metaData"]').contains("978-82-05-50862-0");
    cy.get('[data-testid="metaData"]').contains("BIBSYS_ILS");
    cy.get('[data-testid="metaData"]').contains("Gyldendal akademisk");
    cy.get('[data-testid="metaData"]').contains("Gunnar Nicolaysen (1940-) (redaktor/forfatter av forord/forfatter)$$QGunnar Nicolaysen (1940-), Per Holck (1942-) (redaktor/redaktor/forfatter)$$QPer Holck (1942-)");
    cy.get('[data-testid="alert"]').should('not.exist');
  });

  it('shows errormessage when metadata-server responds with error', () => {
    cy.visit(`https://ill.test.bibs.aws.unit.no/?patronid=1234571&recordid=123?recordid=emptypnx123&patronid=123`);
    cy.get('[data-testid="alert"]').should('exist').contains('500');
  });

  it('shows schema', () => {
    cy.get(`[data-testid="patron-field"]`).type('testuser');
    cy.get(`[data-testid="library-option-1234568"]`).click();
  });

  it('library show holdings', () => {
    cy.get(`[data-testid="library-label-1234570"]`).contains('1 of 1 available');
  });

  it('library show server error', () => {
    cy.get(`[data-testid="library-label-${"mockMetadata.libraries[5].library_code"}"]`).contains("TEXT.FETCH_SRU_ERROR");
  });

  it('library show no info', () => {
    cy.get(`[data-testid="library-label-1234571"]`).contains("No holding information. Contact the library");
  });

  it('library show closed', () => {
    cy.get(`[data-testid="library-label-1234567"]`).contains("Closed for interlibrary loan");
  });

  it('lib_user-access-api shows servererror', () => {
    cy.visit(`https://ill.test.bibs.aws.unit.no/?recordid=123&patronid=2321564`);
    cy.get('[data-testid="alert"]').should('exist').contains('500');
  });

  it('lib_user does not have access to ill', () => {
    cy.visit(`https://ill.test.bibs.aws.unit.no/?recordid=123&patronid=1234572`);
    cy.get('[data-testid="warning"]').should('exist').contains('not available');
  });

  it('lib_user is alma-library and should get a read-only schema', () => {
    cy.visit(`https://ill.test.bibs.aws.unit.no/?recordid=123&patronid=1232`);
    cy.get('[data-testid="warning"]').should('exist').contains('Alma libraries');
  });

  it('user needs to fill out form before pressing request-button', () => {
    cy.get(`[data-testid="library-option-1234569"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.get('input:invalid').should('have.length', 1);
    cy.get(`[data-testid="patron-field"]`).type('someText');
    cy.get('input:invalid').should('have.length', 0);
    cy.get(`[data-testid="ncip-request-button"]`).click();
  });

  it('user sends a unsuccessful NCIP-request', () => {
    cy.get(`[data-testid="patron-field"]`).type("userIdentifierForNCIPServerError");
    cy.get(`[data-testid="library-option-1234568"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.get('[data-testid="ncip-error-alert"]').should('exist');
  });

  it('user sends a successful NCIP-request', () => {
    cy.get(`[data-testid="patron-field"]`).type('test user');
    cy.get(`[data-testid="library-option-1234569"]`).click();
    cy.get(`[data-testid="ncip-request-button"]`).click();
    cy.url().should('include', 'success');
    cy.get('[data-testid="ncip-success-alert"]').should('exist');
  });
});
