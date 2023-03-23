ARCHITECTURE DIAGRAM:

          Utente
            |
            v
   +------------------+
   | Sito WordPress   |
   +------------------+
            |
            v
     +------------+     +---------+
     |  Database  | <-- | Storage |
     +------------+     +---------+
            |
            v
     +------------+
     | Web Server |
     +------------+
            |
            v
   +------------------+
   | Load Balancer    |
   +------------------+


ISTRUZIONI:
1. installa Terraform sulla macchina locale

2. clona il codice Terraform dalla GitHub Repository 
    `` git clone https://github.com/nomeutente/nomerepository.git ``
    git copierà l'intera repository nella cartella selezionata

3. vai alla directory ` terraform `

4. per inizializzare Terraform e scaricare i providers richiesti, eseguire il comando ` terraform init `

5. per eseguire il provisioning e distribuire Wordpress, eseguire il comando ` terraform apply `

6. attendere che il comando venga completato. In output si riceverà il nome DNS del load balancer dell'applicazione

7. copia il nome DNS e incollalo nel browser per accedere al sito WordPress

8. seguire la procedura guidata di installazione di WordPress per completare il processo di installazione

