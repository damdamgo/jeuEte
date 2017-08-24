from tkinter import Tk,Label,Button,Frame
from tkinter import *
import random
import time
import numpy as np
import numpy

def mot():
    manch=manche.get()
    global n
    if manch=="1":
        if n==5:
            manchefin()
        else:
            nomatrouver.set(liste[n])
            avanc=str(n+1)
            n=n+1
            avancementjeu.set("%s / 40"%avanc)
            bmot.grid_forget()
            btrouve.grid(row=3, column=0)
            chronogo()
    else:
        global listemanche2
        if listemanche2==[]:
            manchefin()
        else:
            bmot.grid_forget()
            btrouve.grid(row=3, column=0)
            bpasser.grid(row=4, column=0)
            try:
                nomatrouver.set(listemanche2[n])###prendre au hasard ou melanger a la fin
                n=n+1
                chronogo()
            except:
                n=0
                random.shuffle(listemanche2)
                nomatrouver.set(listemanche2[n])
                chronogo()
def chronogo():
    global timere
    chrono.set(timere)
    chronofonc()
def chronofonc():
    timere=chrono.get()
    if timere!="trouvé":
        timere=int(timere)
        timere=timere-1
        chrono.set(timere)
        if timere==0:
            chronoend()
        else:
            chronoframe.after(1000,chronofonc)
def chronoend():
    equipe=equipejoue.get()
    if equipe=="Equipe 1":
        equipejoue.set("Equipe 2")
    else:
        equipejoue.set("Equipe 1")
    chrono.set("31")
    chronofonc()
def trouve():
    global timere
    global listemanche2
    manch=manche.get()
    timere=chrono.get()
    chrono.set("trouvé")
    time.sleep(1)
    btrouve.grid_forget()
    bpasser.grid_forget()
    bmot.grid(row=3, column=0)
    equipe=equipejoue.get()
    if equipe=="Equipe 1":
        score=scoreequipe1.get()
        score=int(score)
        score=score+1
        score=str(score)
        scoreequipe1.set(score)
    else:
        score=scoreequipe2.get()
        score=int(score)
        score=score+1
        score=str(score)
        scoreequipe2.set(score)
    if manch=="2":
        global n2
        mot=nomatrouver.get()
        listemanche2.remove(mot)
        avanc=str(n2+1)
        n2=n2+1
        avancementjeu.set("%s / 40"%avanc)
def manchefin():
    global n
    global listemanche2
    n=0
    manch=manche.get()
    if manch=="1":
        avancementjeu.set("0 / 40")
        random.shuffle(listemanche2)
        nomatrouver.set("-------")
        manche.set("2")
    else:
        if manch=="2":
            global n2
            n2=0
            avancementjeu.set("0 / 40")
            manche.set("3")
            liste=numpy.load("liste.npy")
            liste=liste.tolist()
            print(liste)
            listemanche2=liste######probleme
            print(listemanche2)
            nomatrouver.set("-------")
            random.shuffle(listemanche2)
        else:
            ##fin
def passer():
    global n
    global listemanche2
    try:
        nomatrouver.set(listemanche2[n])###prendre au hasard ou melanger a la fin
        n=n+1
    except:
        n=0
        random.shuffle(listemanche2)
        nomatrouver.set(listemanche2[n])
##############################fenetre principale
couleurprin="#DEB887"
couleursec="#FEFEE0"
couleurfrm="#99512B"
root = Tk()###on indique que root est une fenetre
root.configure()
root.resizable(False, False)###on peut pas modifier la taille de la fenetre
root.title('recplound')
frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame 1000*600 (taille de la fenetre)
frameprincipale.pack()
frameprincipale.pack_propagate(0)
##############################liste
listenom = open("liste.txt",'r')
lignes  = listenom.readlines()
listenom.close()
nbtotal=0
liste=[]
while nbtotal!=5:
    nb = random.randint(1,582)
    nom=lignes[nb]
    liste.append(nom)
    nbtotal=nbtotal+1
listemanche2=[]
listemanche2=liste
listemanche3=[]
listemanche3=liste
numpy.save("liste.npy",listemanche3)
n=0
n2=0
manche=StringVar()
manche.set("1")
timere=30
##############################score
framescore=Frame(frameprincipale)
framescore.pack(side=LEFT)
scoreframe=Frame(framescore)
scoreframe.grid(padx=10)
ecritureinfo= ("Helvetica", 16)
ecriturechrono= ("Helvetica", 100)
scoreequipe1=StringVar()
scoreequipe1.set("0")
scoreequipe2=StringVar()
scoreequipe2.set("0")
labelscore=Label(scoreframe,text="SCORE",font=ecritureinfo)
labelscore.grid(row=0, column=1)
labelequipe1=Label(scoreframe,text="Equipe 1")
labelequipe1.grid(row=1, column=0)
labelequipe2=Label(scoreframe,text="Equipe 2")
labelequipe2.grid(row=1, column=2)
labelldeco1=Label(scoreframe,text="|")
labelldeco1.grid(row=1, column=1)
labelldeco2=Label(scoreframe,text="|\n|\n|\n|\n|\n|\n")
labelldeco2.grid(row=2, column=1)
labelscoreequipe1=Label(scoreframe,textvariable=scoreequipe1,font=ecritureinfo)
labelscoreequipe1.grid(row=2, column=0)
labelscoreequipe2=Label(scoreframe,textvariable=scoreequipe2,font=ecritureinfo)
labelscoreequipe2.grid(row=2, column=2)

#################################jeu nom
framejeu=Frame(frameprincipale)
framejeu.pack()
jeuframe=Frame(framejeu)
jeuframe.grid()
avancementjeu=StringVar()
avancementjeu.set("0 / 40")
labelavancementjeu=Label(jeuframe,textvariable=avancementjeu,font=ecritureinfo)
labelavancementjeu.grid(row=0, column=0)
equipejoue=StringVar()
equipejoue.set("Equipe 1")
labelequipejoue=Label(jeuframe,textvariable=equipejoue,font=ecritureinfo)
labelequipejoue.grid(row=1, column=0)
nomatrouver=StringVar()
labelnomatrouver=Label(jeuframe,textvariable=nomatrouver,font=ecritureinfo)
labelnomatrouver.grid(row=2, column=0)
bmot=Button(jeuframe,text="mot suivant",command=mot)
bmot.grid(row=3, column=0)
btrouve=Button(jeuframe,text="trouvé",command=trouve)
bpasser=Button(jeuframe,text="passer",command=passer)
####################################avancement et chrono
frameprin=Frame(frameprincipale)
frameprin.pack(side=RIGHT)
frameavancement=Frame(frameprin)
frameavancement.grid(row=0, column=0)
labelmanche=Label(frameavancement,textvariable=manche)
labelmanche.grid(row=0, column=0)
chronoframe=Frame(frameprin)
chronoframe.grid(row=1, column=0)
chrono=StringVar()
chrono.set("30")
labelchrono=Label(chronoframe,textvariable=chrono,font=ecriturechrono)
labelchrono.grid(row=0, column=0,pax=20)


root.mainloop()
