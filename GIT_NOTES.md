# Git Huskelapp – Copy & Forklaring

## Sjekk status
```bash
git status
# Viser hvilke filer som er endret, lagt til, eller klar for commit

git add .
# Legger til alle endrede filer for neste commit

git commit -m "Din melding her"
# Oppretter en commit med beskjed om hva du har gjort

git push
# Sender endringene til remote repo på GitHub

git pull --rebase
# Henter oppdateringer fra GitHub og legger dine commits på toppen

git push
# Sender endringene til GitHub etter rebase

git reset --soft HEAD~1
# Fjerner siste commit men beholder endringene i arbeidsmappen

git reset --hard HEAD~1
# Fjerner siste commit OG endringene, irreversibelt!

git commit --amend -m "Ny meldigit ng"
# Endrer meldingen på siste commit

git config --global user.name "Ditt Navn"
git config --global user.email "din@email.com"
# Setter navn og e-post for commits

fatal: No rebase in progress
# Oppstår hvis du prøver å avslutte eller fortsette en rebase som ikke eksisterer