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

Det kjøres også tester mot sandbox/dev miljøet. På denne måten kan vi fange opp feil tidlig før vi forbereder en release.

Sandbox/dev testene er satt opp slik at feil ikke stopper kjøringene.

For å kjøre frontend tester (noen tester må kjøres i pipeline for å virke):

    cd cypress
    npm test

For å kjøre frontend tester mot sandbox/dev miljø (skal kunne kjøres lokalt uten problemer):


    cd cypress
    npm run sandboxTest

For å kjøre backend tester (trenger miljøvariabler for å kunne kjøres lokalt):

    cd karate
    ./gradlew test --info

For å kjøre backend tester mot sandbox/dev miljø (skal kunne kjøres lokalt uten problemer):

    cd karate
    ./gradlew sandboxTest --info

Trenger man miljøvariabler må man legge inn dette på forhånd.