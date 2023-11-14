from flask import Flask;
from flask import render_template;
import os
import sqlite3
connexion = sqlite3.connect("maBD.db")
curseur = connexion.cursor()
curseur.execute("select user from info order by la_date desc limit 1 ;")
utilisateur = curseur.fetchall()[0][0]
curseur.execute("select disk from info order by la_date desc limit 1 ;")
espace = curseur.fetchall()[0][0]
curseur.execute("select ram from info order by la_date desc limit 1 ;")
ram = curseur.fetchall()[0][0]
curseur.execute("select cpu from info order by la_date desc limit 1 ;")
cpu = curseur.fetchall()[0][0]
curseur.execute("select la_date from info order by la_date desc limit 1 ;")
date = curseur.fetchall()[0][0]
imagefolder = os.path.join('static')
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = imagefolder
@app.route('/')
def home():
    imgram = os.path.join(app.config['UPLOAD_FOLDER'],'RAM.png')
    imgcpu = os.path.join(app.config['UPLOAD_FOLDER'],'CPU.png') 
    imgboth = os.path.join(app.config['UPLOAD_FOLDER'],'deuxGraphe.png')
    return render_template('htmlSE.html', postRam = imgram, postCpu = imgcpu, postBoth = imgboth, util = utilisateur, disk = espace, ram = ram, cpu = cpu, date = date)
if __name__ == "__main__":
    app.run(debug=True)