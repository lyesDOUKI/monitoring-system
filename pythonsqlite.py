import sqlite3
connexion = sqlite3.connect('maBD.db')
curseur = connexion.cursor()
#requete = "create table info(user text, disk text, RAM real, CPU real, la_date date)"
curseur.execute("select count(*) from info ; ")
row = curseur.fetchone()
nbligne = row[0]
curseur.execute("select ligneMax from valeurmax")
x = curseur.fetchall()[0][0]
if(nbligne==x):
    curseur.execute("delete from info limit 1 ; ")

connexion.commit()
connexion.close()

