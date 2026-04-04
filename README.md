Powershell Prompt

#git remote add origin https://github.com/Barrioth/PROJET.git

#git clone --single-branch --branch <branch_name> <repository_url>       (base 1)(nginx / compose 2)

#dossier local d'import
PS C:\Users\Lagia\Desktop\PROJET STUDI>
PS C:\Users\Lagia\Desktop\DOSSIER PROJET\PROJET> 


#Necessite docker desktop d'ouvert
docker build -t pasta-web:local .
docker run --rm -p 8000:8000 pasta-web:local
#http://127.0.0.1:8000/
          
#runners
PS C:\GitLab-Runner> .\gitlab-runner.exe run

#railway prends les push et automatise le deployment
prthomas.up.railway.app

#pour declencher le CI
#git remote -v
#git remote add gitlab https://gitlab.com/Barrioth/PROJET.git
#git push gitlab 1 ou 2

#Ajout de Nginx necessite wsl (nginx port 80) (flask port 8000)
docker compose up --build
http://localhost/



winget install -e --id Hashicorp.Terraform

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Get-Command terraform

terraform init 
terraform plan (terraform validate si ca passe pas)
terraform apply






GCP
https://cloud.google.com/sdk/docs/install
gcloud init                                     si ca ne se lance pas automatiquement apres l'install sdk
gcloud auth application-default login
instaler compute engine API

terraform init 
terraform plan (terraform validate si ca passe pas)
terraform apply

terraform output public_ip

WSL
sudo apt install ansible -y

ssh-keygen -t rsa -f ~/.ssh/id_rsa -N ""

ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "lagia@FIXE"
cat ~/.ssh/id_ed25519.pub