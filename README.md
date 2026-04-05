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
#git commit --allow-empty -m "trigger CI"
#git push 

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

ssh-keygen -t rsa -f ~/.ssh/id_rsa -N ""

ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "lagia@FIXE"
cat ~/.ssh/id_ed25519.pub


wsl
sudo apt install ansible -y

cp /mnt/c/Users/Lagia/.ssh/id_ed25519_pasta ~/.ssh/
cp /mnt/c/Users/Lagia/.ssh/id_ed25519_pasta.pub ~/.ssh/
chmod 600 ~/.ssh/id_ed25519_pasta

cd /mnt/c/Users/Lagia/Desktop/DOSSIER\ PROJET/PROJET
ansible-playbook playbook.yml -i terraform/inventory.ini
ansible-playbook playbook.yml -i terraform/inventory.ini --private-key ~/.ssh/id_ed25519_pasta