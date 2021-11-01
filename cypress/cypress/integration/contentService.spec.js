const contentServiceBaseUrl = "https://contents.test.bibs.aws.unit.no/"
const AudioBookIsbn = '9788202614324'
const bookThatDoesNotExist = "177658546"
const detailedBook = '1402010575'

context('content service', () => {

    it('successfully shows a full page', () => {
        cy.wait(2000);
        cy.visit(`${contentServiceBaseUrl}?isbn=${detailedBook}`);
        cy.get('[data-testid="page-header"]').should('exist');
        cy.get('[data-testid="page-footer"]').should('exist');
        cy.get('[data-testid="description-short-box"]').should('exist');
        cy.get('[data-testid="description-short-box-contents"]').should('exist');
        cy.get('[data-testid="description-long-box"]').should('exist');
        cy.get('[data-testid="description-long-box-contents"]').should('not.exist');
        cy.get('[data-testid="description-toc-box"]').should('exist');
        cy.get('[data-testid="description-toc-box-contents"]').should('not.exist');
        cy.get('[data-testid="cover-image-container"]').should('exist');
    });

    it('successfully shows an audio book', () => {
        cy.visit(`${contentServiceBaseUrl}?isbn=${AudioBookIsbn}`);

        cy.get('[data-testid="description-long-box"]').should('exist');
        cy.get('[data-testid="description-long-box"]').should('exist');
        cy.get('[data-testid="description-audio-file-box"]').should('exist');
        cy.get('[data-testid="description-audio-file-box"] button').click();
        cy.get('[data-testid="description-audio-file-box-audio"]').should('exist');
        cy.get('[data-testid="audio-source"]').should('exist');
    });

    it('shows errormessage when api-call fails', () => {
        cy.visit(`${contentServiceBaseUrl}?isbn=${bookThatDoesNotExist}`);
        cy.contains('Failed to retrieve the resource, please try again.');
    });

    it('shows errormessage when isbn-parameter is missing', () => {
        cy.visit(`${contentServiceBaseUrl}?isbn=`);
        cy.contains('Parameter specifying isbn was not provided');
        cy.visit(`${contentServiceBaseUrl}`);
        cy.contains('Parameter specifying isbn was not provided');
    });

    it('hides header and closes all expandables if oria-parameter is set', () => {
        cy.visit(`${contentServiceBaseUrl}?isbn=${detailedBook}&system=oria`);
        cy.get('[data-testid="description-short-box"]').should('exist');
        cy.get('[data-testid="description-short-box-contents"]').should('not.exist');
        cy.get('[data-testid="description-long-box"]').should('exist');
        cy.get('[data-testid="description-long-box-contents"]').should('not.exist');
        cy.get('[data-testid="page-footer"]').should('exist');
        cy.get('[data-testid="page-header"]').should('not.exist');
        cy.get('[data-testid="cover-image-container"]').should('not.exist');
    });

    it('can collapse boxes', () => {
        cy.visit(`${contentServiceBaseUrl}?isbn=${detailedBook}&system=oria`);
        cy.get('[data-testid="description-short-box"]').should('exist');
        cy.get('[data-testid="description-short-box-contents"]').should('not.exist');
        cy.get('[data-testid="description-short-box"] button').click();
        cy.get('[data-testid="description-short-box-contents"]').should('exist');
        cy.get('[data-testid="description-short-box"] button').click();
        cy.get('[data-testid="description-short-box-contents"]').should('not.exist');
    });
});