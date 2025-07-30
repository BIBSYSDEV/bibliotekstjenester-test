# Bibliotekstjenester Test

Dette repoet inneholder tester.
Alle utgående internett-kall er stubbed for interLibraryLoan-applikasjon. 
Cypress tester for å kjøre end-to-end teste mot InterLibraryLoan.
Karate tester for å kjøre tester mot interne og eksterne APIer.

Pnx-service under karate-testen trenger api-key. Denne må legges inn som systemvariabel ("primoApiKey") 
i codebuild-oppsettet.
Alma-rest under karate-testen trenger api-key. Denne må legges inn som systemvariabel ("almaApiKey") 
i codebuild-oppsettet. OBS! Den kjører en post mot Alma, så bruk ALMA-SANDBOX api-key.

Det finnes et eget TEST-miljø i AWS (Bibliotekstjenester TEST). Det er tenkt at testene kjøres her 
automatisk mot frontend og eksterne og interne api-er. En Scheduler (AWS EventBridge) kjøre disse 
daglig kl 7:00.
Med hjelp av AWS chatbot blir failure status fra CodeBuild meldt til slack-kanal "devops-team-smile".

Running frontend tests against test environment (some tests need to be run in pipeline to work):

    cd cypress
    npm test

Running frontend tests against sandbox/dev environment (should be able to run this locally without issues): 

    cd cypress
    npm run testSandbox