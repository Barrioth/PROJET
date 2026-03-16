Powershell Prompt

#git remote add origin https://github.com/Barrioth/PROJET.git

#dossier local d'import
PS C:\Users\Lagia\Desktop\PROJET STUDI>
PS C:\Users\Lagia\Desktop\DOSSIER PROJET\PROJET> 


#Necessite docker desktop d'ouvert
docker build -t pasta-web:local .
docker run --rm -p 8000:8000 pasta-web:local
#http://127.0.0.1:8000/
          

#pour declencher le CI
#git remote -v
#git remote add gitlab https://gitlab.com/Barrioth/PROJET.git
#git push gitlab main