import sqlite3
import matplotlib.pyplot as plt

connexion = sqlite3.connect("maBD.db")
curseur = connexion.cursor()
curseur.execute("select ram from info;")
l = curseur.fetchall()
listeram = list()
for i in range(len(l)):
    listeram.insert(i, l[i][0])

curseur.execute("select cpu from info;")
l = curseur.fetchall()
listecpu = list()
for i in range(len(l)):
    listecpu.insert(i, l[i][0])

curseur.execute("select la_date from info;")
l = curseur.fetchall()
listedate = list()
for i in range(len(l)):
    chaine = str(l[i][0])
    chaine = chaine.replace(" ","\n")
    listedate.insert(i, chaine)

#graphique pour la ram

plt.plot(listedate, listeram, label="ram")
plt.title("historique de la RAM % ")
plt.legend()
f = plt.gcf()
h, w = f.get_size_inches()
f.set_size_inches(h*2,w*2, forward=True)
plt.savefig("static/RAM.png")
plt.show()
plt.close()
plt.title("historique de la CPU % ")
plt.plot(listedate,listecpu, label="cpu")
plt.legend()
f = plt.gcf()
h, w = f.get_size_inches()
f.set_size_inches(h*2,w*2, forward=True)
plt.savefig("static/CPU.png")
plt.show()
plt.close()
#lesdeuxgraphe
plt.title("historique de la RAM et de la CPU %")
plt.plot(listedate, listeram, label="ram")
plt.plot(listedate,listecpu, label="cpu")
plt.legend()
f = plt.gcf()
h, w = f.get_size_inches()
f.set_size_inches(h*2,w*2, forward=True)
plt.savefig("static/deuxGraphe.png")
plt.show()
connexion.close()
