Projet Administration des système d'exploitation


PARTIE I : 
	
	le script : sondeUser.sh ====> retourne le nombre d'utilisateur connecté
	le script : sondeDisk.sh ====> retourne l'espave utiliser en G
	le script : sondeRAM.py =====> retourne la ram utilisé en %
	le script : sondeCPU.py =====> retourne la cpu utilisé en %
	le script : datesonde.sh =====> retourne la date et l'heur en temp réel
	le script : varsondes.sh =====> stock les sondes dans des variable
	le script : sondes.sh ========> retoune toutes les sondes et stock les informations dans un fichier .txt (infoSys.txt)

	
PARTIE II :

	le script : pythonsqlite =====> permet de creer la table info(user, disk, ram, cpu, date) et permet aussi de mettre à jour l'historique
	commment fonctionne l'historique ?
		une table valeurmax est creer, avec une colone lignemax, une fois le nombre de ligne de la base = à lignmax :
		on supprime la premiere ligne de la base de donnée et en inserts les nouvelles valeurs à la dernieres ligne
	le script : sauvegarde.sh ======> permet de sauvegarder ma base de donnée dans un fichier txt tout les jour à 16h00 en utilisant crontab
	le script : effacer.sh ======>permet d'effacer et de restaurer ma base de donnée

	
PARTIE III : 
	
	le script : mail.py ========> en utilisant le smtp de l'université d'avignon, je recois un mail d'alerte si la ram et la cpu en atteint 
					une valeur presente dans la table valeurmax(voir ligne 17)
	le script : affichage.sh ======> permet d'afficher ma base de donnée
	le script : graphique.py =====> s'execute toutes les 5 minutes et affiche l'evolution des valeurs de la ram et de la cpu (en %) de notre
					base de donnée en fonction de la date ou les informations on été enregistré

PARTIE IV : 
	
	creation d'un site web (en utilisant flask sous python et avec les graphiques et en faisant réferences de la base de donnée)
	le script : pageWeb.py =========>permet de crée un site web avec la page htmlSE.html(repertoire templates) ou  en affiche les graphiques
					(RAM et CPU) ainsi que les informations du dernier utilisateur enregistrer sur la base de donnée 		


