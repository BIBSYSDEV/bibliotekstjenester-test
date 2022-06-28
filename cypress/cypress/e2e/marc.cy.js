import path from 'path';
const marPresenteationBaseUrl = "https://marcpresentation.test.bibs.aws.unit.no";
const downloadsFolder = Cypress.config('downloadsFolder');
const fileNameXML = 'marcpresentation.xml';
const fileNameLineFormat = 'marcpresentation.txt';


context('end to end testing, marc', ()=> {

    before('Clear downloads folder', () => {
        cy.exec(`rm ${downloadsFolder}/*`, { log: true, failOnNonZeroExit: false });
    });


    it('successfully shows a full page with data from alma-api', () => {
        cy.visit(`${marPresenteationBaseUrl}?mms_id=543543534`);
        cy.get('[data-testid="page-header"]').should('exist');
        cy.get('[data-testid="metadata-title"]').contains('Lensvik indremisjon');
        cy.get('[data-testid="metadata-author"]').contains('Singstad');
        cy.get('[data-testid="metadata-year"]').contains('1991');
        cy.get('[data-testid="marc-preview"]').should('exist');
        cy.get('[data-testid="download-xml-format-button"]').should('exist');
        cy.get('[data-testid="download-line-format-button"]').should('exist');
    });

    it('successfully shows a full page with data from authority-api', () => {
        cy.visit(`${marPresenteationBaseUrl}?auth_id=1093967`);
        cy.get('[data-testid="page-header"]').should('exist');
        cy.get('[data-testid="metadata-author"]').contains('Fisher, Jude');
        cy.get('[data-testid="marc-preview"]').should('exist');
        cy.get('[data-testid="download-xml-format-button"]').should('exist');
        cy.get('[data-testid="download-line-format-button"]').should('exist');
    });

    it('can show different views', () => {
        cy.visit(`${marPresenteationBaseUrl}?mms_id=543543534&institution=xxx`);
        cy.get('[data-testid="marc-preview"]').contains('<record xmlns="http://www.loc.gov/MARC21/slim">');
        cy.get('[data-testid="radio-button-line-format"]').click();
        cy.get('[data-testid="marc-preview"]').contains('*ldr 01626cam a2200433 c 4500');
        cy.get('[data-testid="radio-button-xml-format"]').click();
        cy.get('[data-testid="marc-preview"]').contains('<record xmlns="http://www.loc.gov/MARC21/slim">');
    });

    it('can download files', () => {
        cy.visit(`${marPresenteationBaseUrl}?mms_id=543543534`);
        cy.get('[data-testid="download-xml-format-button"]').click();
        cy.get('[data-testid="download-line-format-button"]').click();
        cy.readFile(path.join(downloadsFolder, fileNameXML)).should(
            'contain',
            '<record xmlns="http://www.loc.gov/MARC21/slim">'
        );

        cy.readFile(path.join(downloadsFolder, fileNameLineFormat)).should(
            'contain',
           '*ldr 01626cam a2200433 c 4500'
        );
    });

    it('shows errormessage when empty response', () => {
        cy.visit(`${marPresenteationBaseUrl}?auth_id=1199960`);
        cy.contains('Check that the input parameter(URL) is correct');
    });

    it('shows errormessage when parameter is missing', () => {
        cy.visit(`${marPresenteationBaseUrl}?mms_id=`);
        cy.contains('Search parameters have not been included in the URL');
        cy.visit(`${marPresenteationBaseUrl}?random_text`);
        cy.contains('Search parameters have not been included in the URL');
        cy.visit(marPresenteationBaseUrl);
        cy.contains('Search parameters have not been included in the URL');
    });
})