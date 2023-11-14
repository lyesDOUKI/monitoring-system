import smtplib
import psutil
import sqlite3
connexion = sqlite3.connect("maBD.db")
curseur = connexion.cursor()
curseur.execute("select ram from info order by la_date desc limit 1 ;")
server = smtplib.SMTP_SSL('smtpz.univ-avignon.fr',465)
laram = curseur.fetchall()[0][0]
server.login("lyes.douki@alumni.univ-avignon.fr", "lyesDOUKI030/2001LYESdouki")
curseur.execute("select ramMax from valeurmax;")
x = curseur.fetchall()[0][0]
if(laram>=x):
    message = "subject : alerte linux-ubuntu \nattention le systeme utilise plus de 30% de ram !"
    server.sendmail("lyes.douki@alumni.univ-avignon.fr", "lyesdouki03082001@gmail.com", message)
server.quit()
server.close()
connexion.close()
