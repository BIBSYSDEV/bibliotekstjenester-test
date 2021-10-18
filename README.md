# Bibliotekstjenester Test

Dette repoet inneholder tester.
Alle utgående internett-kall er stubbed for interLibraryLoan-applikasjon. 
Cypress tester for å kjøre end-to-end teste mot InterLibraryLoan.
Karate tester for å kjøre tester mot interne og eksterne APIer.

pnx-service under karate-testen trenger api-key. Denne må legges inn som systemvariabel ("apiKey") 
i codebuild-oppsettet.

Det finnes et eget TEST-miljø i AWS (Bibliotekstjenester TEST). Det er tenkt at testene kjøres her 
automatisk mot frontend og eksterne og interne api-er. En Scheduler (AWS EventBridge) kjøre disse 
daglig kl 7:00.
Med hjelp av AWS chatbot blir failure status fra CodeBuild meldt til slack-kanal "devops-team-smile".