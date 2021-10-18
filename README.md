# Bibliotekstjenester Test

Dette repoet inneholder tester.

pnx-service under karate-testen trenger api-key. Denne må legges inn som systemvariabel ("apiKey") 
i codebuild-oppsettet.

Det finnes et eget TEST-miljø i AWS (Bibliotekstjenester TEST). Det er tenkt at testene kjøres her 
automatisk mot frontend og eksterne og interne api-er.