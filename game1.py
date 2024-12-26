from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image,ImageDraw
import random
import csv

window=ctk.CTk()
window.title('GoBet')
window.minsize(980, 720)
window.maxsize(980, 720)
window.config(background='#09111e')
window.iconbitmap("IMG/icon.ico")


frame0=ctk.CTkFrame(
    window,
    width=899,
    height=100,
    bg_color='#09111e',
    fg_color='#0c1b2c',
    corner_radius=15
)

frame0.place(relx=0.508,rely=0.12,anchor=CENTER)
#****************************************************
frame1=ctk.CTkFrame(
    window,
    width=350,
    height=495,
    bg_color='#09111e',
    fg_color='#0c1b2c',
    corner_radius=15
)
frame1.place(relx=0.23,rely=0.58,anchor=CENTER)
#****************************************************
frame2=ctk.CTkFrame(
    window,
    width=700,
    height=600,
    bg_color='#09111e',
    fg_color='#09111e',
    # corner_radius=10
)
frame2.place(relx=0.78 ,rely=0.63,anchor=CENTER)
#****************************************************
    #IMAGE
image1=ctk.CTkImage(
    light_image=Image.open("IMG/Diamonde01.png"),
    size=(50,50)
)
image2=ctk.CTkImage(
    light_image=Image.open("IMG/Boom02.png"),
    size=(80,80)
)
img_Titre=ctk.CTkImage(
    light_image=Image.open('IMG/Artboard 1.png'),
    size=(150,100)
)
image_defaut=ctk.CTkImage(
    light_image=Image.open('IMG/utilisateur (1).png').resize((80,80)),
    size=(80,80)
)
# #**********************les dictionnaires****************************** dic5==40/dic4==35/dic3==30/dic2==30/dic1==30
dic5=[image1,image1,image1,image1,image1, image1,image1,image1,image1,image1, image1,image1,image1,image1,image1,image1, image1, image2, image1, image1, image2, image1, image1, image1, image1, image1, image1, image2, image1, image1, image1, image2, image1, image1, image1,image1, image1, image1, image2, image1,
]
dic4=[ image1,image1,image1,image1,image1,image1,image1,image1,image1,image1,image1, image1, image2, image1, image1, image2, image1, image1, image1, image1, image1, image1, image2, image1, image1, image1, image2, image1, image1, image1,image1, image1, image1, image1, image1,
]
dic3=[ image1,image1,image1,image1,image1,image1, image1, image1, image1, image1, image2, image1, image1, image1, image1, image1, image1, image2, image1, image1, image1, image2, image1, image1, image1,image1, image1, image1, image1, image1,
]
dic2=[ image1,image1,image1,image1,image1,image1, image1, image1, image2, image1, image1, image1, image1, image1, image1, image1, image1, image2, image1, image1, image1, image1, image1, image1, image1,image1, image1, image1, image1, image1,
]
dic1=[ image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image1, image2, image1, image1, image1,image1, image1, image1, image1, image1,
    ]
dic_remp=[]
#------------------------------FONCTIONS-------------------------------------
#fonction qui rend l'image cercle (L3Z ONSEEER L CHATGPT)
def round_corners(image):
    # Créer une image de même taille que l'image d'origine
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    # Dessiner des coins arrondis
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    # Appliquer le masque
    rounded_image = Image.new('RGBA', image.size)
    rounded_image.paste(image, (0, 0), mask)

    return rounded_image
# Fonction pour demander une image
def image_profile():
    try:
        with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
            lec=list(csv.reader(f,delimiter=';'))
            for i in lec:
                if i[0]== wlu :
                    chemin=i[-1]
                    PIC=Image.open(chemin).resize((80, 80)).convert("RGBA")
                    rounded_image = round_corners(PIC)
                    img=ctk.CTkImage(
                        light_image=rounded_image,
                         size=(80, 80)
                    )
                    return img
    except Exception as e:
        print(f'exception image profile est perdu : {e}')
        return image_defaut

def modif_profile():
    reponse = messagebox.askyesno("QST", "Voulez-vous modifier votre profile ?")
    if reponse:
        window.destroy()
        import Profile
    else:
        return
def import_info():
    global wlu
    wlu=''
    with open('fichier_csv/connection.csv', 'r', newline='', encoding='utf-8') as fc:
        login =list (csv.reader(fc, delimiter=';'))
        for i in login:
            for y in i:
                wlu+=y
    return  wlu
#____________________________________________
def Alpha(Montatee):
    NBommb = Bonusse()

    new_solde = (Montatee * NBommb)
    return new_solde
# ______________________________________
def option():
    return ['1', '2', '3', '4', '5']

# _____
def Bonusse():
    onchklisi9omer = nb_coeur.get()
    onchklisi9omer = int(onchklisi9omer)
    if onchklisi9omer == 5:
        bonusNsPerbet = float(0.086)
        return bonusNsPerbet

    if onchklisi9omer == 4:
        bonusNsPerbet =  float(0.076)
        return bonusNsPerbet

    if onchklisi9omer == 3:
        bonusNsPerbet = float(0.061)
        return bonusNsPerbet

    if onchklisi9omer == 2:
        bonusNsPerbet =  float(0.057)
        return bonusNsPerbet

    if onchklisi9omer == 1:
        bonusNsPerbet = float(0.042)
        return bonusNsPerbet
def retoure():
    c = nb_coeur.get()
    c = int(c)
    if c == 5:
        return dic5
    if c == 4:
        return dic4
    if c == 3:
        return dic3
    if c == 2:
        return dic2
    if c == 1:
        return dic1
def solde_in_file():
    with open('fichier_csv/Solde.csv', 'r', newline='', encoding='utf-8') as f:
        go = csv.reader(f, delimiter=';')
        for i in go:
            if i[0]==import_info():
                solde =float(i[1])
    return solde
dic_solde = {"solde":solde_in_file()}
# _________
NombreDeWin = []

def fichier_button(but):
    if retoure():
        img_rand=random.choice(list(retoure()))
        retoure().remove(img_rand)
        dic_remp.append(img_rand)
        print(f'gi7 remplacement{len(dic_remp)}')
        print(f'{len(retoure())}')
        a = 0
        if img_rand == image2:
            a = 0
            but.configure(image=img_rand, text='', state='disabled')
            messagebox.showinfo('Go|Bet', 'ooooh!! tu as perdu 😂😂😂😂😂')
            NombreDeWin.clear()
            print(NombreDeWin)
            for i in [but1, but2, but3, but4, but5, but6, but7,
                      but8, but9, but10, but11, but12, but13, but14, but15, but16,
                      but17, but18, but19, but20, but21, but22, but23, but24, but25]:
                i.configure(image=None, text='', state='disabled', border_color="#2e2e2e")
                bet.configure(state="normal")
                nb_coeur.configure(state="normal")
                quitter.configure(state='disabled')
                Pari.configure(state="normal")
                a += 1
            for i in dic_remp:
                retoure().append(i)
            dic_remp.clear()
        if a == 0:
            but.configure(image=img_rand, text='', state='disabled', border_color="#14a714")
            NombreDeWin.append(1)
            print(NombreDeWin)
    else:
        messagebox.showinfo('erreur','dic viiide')
# ______________________________________
def pari():
    M = bet.get().strip()
    c = nb_coeur.get()
    while True:
        # Vérifier si les entrées sont vides ou non valides
        if not M.isdigit() or not c.isdigit():
            messagebox.showerror("Erreur", "Veuillez remplir correctement les champs pour jouer !")
            return
        M = int(M)
        c = int(c)
        # Vérification des valeurs saisies
        if M <= 0 or M > dic_solde["solde"] or c <= 0:
            messagebox.showerror("Erreur",
                                 "Le montant doit être compris entre 1 et votre solde, et le nombre de cœurs doit être supérieur à 0.")
        else:
            for i in [but1, but2, but3, but4, but5, but6, but7,
                      but8, but9, but10, but11, but12, but13, but14, but15, but16,
                      but17, but18, but19, but20, but21, but22, but23, but24, but25]:
                i.configure(text='', state='normal', )
            bet.configure(state="readonly")
            nb_coeur.configure(state="disabled")
            Pari.configure(state="disabled")
            quitter.configure(state='normal')
            dic_solde["solde"] -= M
            SolD.set(dic_solde['solde'])
            with open('fichier_csv/Solde.csv', 'r', newline='', encoding='utf-8') as f:
                go = list(csv.reader(f, delimiter=';'))
                for i in go:
                    if i[0] == import_info():
                        go.remove(i)
            with open('fichier_csv/Solde.csv', 'w', newline='', encoding='utf-8') as fr:
                ecr = csv.writer(fr, delimiter=';')
                ecr.writerows(go)
                ecr.writerow([import_info(),dic_solde['solde']])
            break
def gagner():
    M = bet.get().strip()
    c = Bonusse()
    M = int(M)
    if not NombreDeWin:
        messagebox.showinfo('QUITTER', 'N hesite pas de jouer pour gagner plus 🤑 !! ')
        dic_solde["solde"] += M
        for i in [but1, but2, but3, but4, but5, but6, but7,
                  but8, but9, but10, but11, but12, but13, but14, but15, but16,
                  but17, but18, but19, but20, but21, but22, but23, but24, but25
                  ]:
            i.configure(image=None, text='', state='disabled', border_color="#2e2e2e")
        SolD.set(dic_solde["solde"])
        with open('fichier_csv/Solde.csv', 'r', newline='', encoding='utf-8') as f:
            go = list(csv.reader(f, delimiter=';'))
            for i in go:
                if i[0] == import_info():
                    go.remove(i)
        with open('fichier_csv/Solde.csv', 'w', newline='', encoding='utf-8') as fr:
            ecr = csv.writer(fr, delimiter=';')
            ecr.writerows(go)
            ecr.writerow([import_info(), dic_solde['solde']])
        bet.configure(state="normal")
        nb_coeur.configure(state="normal")
        quitter.configure(state='disabled')
        Pari.configure(state="normal")
    else:
        messagebox.showinfo('Winner', 'Bingoooooooo !!  \n\n Bien jouer tu as gagner une partie 🤑', )
        for i in [but1, but2, but3, but4, but5, but6, but7,
                but8, but9, but10, but11, but12, but13, but14, but15, but16,
                but17, but18, but19, but20, but21, but22, but23, but24, but25
                ]:
                i.configure(image=None, text='', state='disabled', border_color="#2e2e2e")
        bet.configure(state="normal")
        nb_coeur.configure(state="normal")
        quitter.configure(state='disabled')
        Pari.configure(state="normal")
        print(NombreDeWin)
        if NombreDeWin[-1] == 1:
            dic_solde["solde"] += (len(NombreDeWin) *M*c)+M
            SolD.set(dic_solde['solde'])
            with open('fichier_csv/Solde.csv', 'r', newline='', encoding='utf-8') as f:
                go = list(csv.reader(f, delimiter=';'))
                for i in go:
                    if i[0] == import_info():
                        go.remove(i)
            with open('fichier_csv/Solde.csv', 'w', newline='', encoding='utf-8') as fr:
                ecr = csv.writer(fr, delimiter=';')
                ecr.writerows(go)
                ecr.writerow([import_info(),dic_solde['solde']])
            NombreDeWin.clear()
            print(NombreDeWin)
    for i in dic_remp:
        retoure().append(i)
    dic_remp.clear()
#****************************************************
# Frame 1
    #label
montant=ctk.CTkLabel(frame1,text='Montant Pari',font=("Nexa Heavy",14),bg_color='#0c1b2c',text_color='#656565')
coeur=ctk.CTkLabel(frame1,text='bombes',font=("Nexa Heavy",14),bg_color='#0c1b2c',text_color='#656565')
# logo=ctk.CTkLabel(frame0,text='GoBet',font=("DESIGNER",50),bg_color='#0c1b2c',text_color='white')

    #input
bet=ctk.CTkEntry(frame1,width=250,height=45,placeholder_text='0,00000000',font=('Nexa Heavy',16),corner_radius=8,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
nb_coeur=ctk.CTkComboBox(frame1,values=option(),state="readonly",font=('Nexa Heavy',14),width=250,height=45,corner_radius=8,fg_color='#09111e',text_color='white',border_color='#14a714')
nb_coeur.set("Nomber des bombes")

info=StringVar()
info_perso=ctk.CTkEntry(frame0,width=150,height=40,state='readonly',textvariable=info,font=('Nexa Heavy',22),border_width=0,fg_color='#0c1b2c',bg_color='#0c1b2c',text_color='white')
info.set(f'{import_info()}')

SolD = StringVar()
Solde = ctk.CTkEntry(frame0,textvariable=SolD,width=185,height=40,border_color="#14a714",font=('Nexa Heavy',16),corner_radius=8,placeholder_text_color='white',fg_color='#09111e',text_color='white',state="readonly")
SolD.set(dic_solde['solde'])

crypto= StringVar()
GB = ctk.CTkEntry(frame0,textvariable=crypto,width=50,height=32,placeholder_text='',border_color="#14a714",font=('Nexa Heavy',18),corner_radius=5,placeholder_text_color='white',bg_color='#0c1b2c',fg_color='#14a714',text_color='white',state="disabled")
crypto.set(' GB')

# nb_coeur=ctk.CTkEntry(frame1,width=250,height=40,placeholder_text='0,00000000',font=('Nexa Heavy',16),corner_radius=8,placeholder_text_color='white',fg_color='#09111e',text_color='white')
    #button_logo
GOBET=ctk.CTkButton(frame0,image=img_Titre,text='',fg_color='#0c1b2c',bg_color='#0c1b2c',hover_color='#0c1b2c')
    #button
pic=ctk.CTkButton(frame0,image=image_profile(),command=lambda :  modif_profile(),text='',width=80,height=80,corner_radius=0,border_width=0,fg_color='#0c1b2c',bg_color='#0c1b2c',hover_color='#0c1b2c',border_color='#14a714')
quitter =ctk.CTkButton(frame1,text='Quitter',command=gagner,state='disabled',width=120,height=45,font=('Nexa Heavy',16),corner_radius=8,border_width=2,bg_color='#0c1b2c',fg_color='#0c1b2c',border_color='#14a714',hover_color='#193314',text_color='white')
Pari=ctk.CTkButton(frame1,command=pari,text='Pari',width=120,height=45,font=('Nexa Heavy',16),corner_radius=8,bg_color='#0c1b2c',fg_color='#14a714',hover_color='#193314',text_color='white')
but1=ctk.CTkButton(frame2,command=lambda: fichier_button(but1),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but2=ctk.CTkButton(frame2,command=lambda: fichier_button(but2),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but3=ctk.CTkButton(frame2,command=lambda: fichier_button(but3),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but4=ctk.CTkButton(frame2,command=lambda: fichier_button(but4),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but5=ctk.CTkButton(frame2,command=lambda: fichier_button(but5),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
#**************************
but6=ctk.CTkButton(frame2,command=lambda: fichier_button(but6),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but7=ctk.CTkButton(frame2,command=lambda: fichier_button(but7),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but8=ctk.CTkButton(frame2,command=lambda: fichier_button(but8),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but9=ctk.CTkButton(frame2,command=lambda: fichier_button(but9),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but10=ctk.CTkButton(frame2,command=lambda: fichier_button(but10),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
#***************************
but11=ctk.CTkButton(frame2,command=lambda: fichier_button(but11),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but12=ctk.CTkButton(frame2,command=lambda: fichier_button(but12),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but13=ctk.CTkButton(frame2,command=lambda: fichier_button(but13),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but14=ctk.CTkButton(frame2,command=lambda: fichier_button(but14),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but15=ctk.CTkButton(frame2,command=lambda: fichier_button(but15),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
#***************************
but16=ctk.CTkButton(frame2,command=lambda: fichier_button(but16),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but17=ctk.CTkButton(frame2,command=lambda: fichier_button(but17),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but18=ctk.CTkButton(frame2,command=lambda: fichier_button(but18),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but19=ctk.CTkButton(frame2,command=lambda: fichier_button(but19),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but20=ctk.CTkButton(frame2,command=lambda: fichier_button(but20),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
#***************************
but21=ctk.CTkButton(frame2,command=lambda: fichier_button(but21),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but22=ctk.CTkButton(frame2,command=lambda: fichier_button(but22),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but23=ctk.CTkButton(frame2,command=lambda: fichier_button(but23),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but24=ctk.CTkButton(frame2,command=lambda: fichier_button(but24),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#043d56' )
but25=ctk.CTkButton(frame2,command=lambda: fichier_button(but25),state='disabled',text='',width=85,height=85,corner_radius=10,border_width=1,border_color='#2e2e2e',bg_color='#09111e',fg_color='#0c1b2c',hover_color='#2' )

#****************************** POSITIONNEMENT ******************************
#labes
montant.place(relx=0.31,rely=0.1,anchor=CENTER)
coeur.place(relx=0.25,rely=0.25,anchor=CENTER)
GOBET.place(relx=0.5,rely=0.45,anchor=CENTER)
#inputs
bet.place(relx=0.5,rely=0.17,anchor=CENTER)
nb_coeur.place(relx=0.5,rely=0.32,anchor=CENTER)
Solde.place(relx=0.86,rely=0.49,anchor=CENTER)
GB.place(relx=0.93,rely=0.49,anchor=CENTER)
info_perso.place(relx=0.21,rely=0.49,anchor=CENTER)
#button
pic.place(relx=0.058,rely=0.49,anchor=CENTER)
quitter.place(relx=0.69,rely=0.46,anchor=CENTER)
Pari.place(relx=0.31,rely=0.46,anchor=CENTER)
#***************************
but1.place(relx=0.1,rely=0.1,anchor=CENTER)
but2.place(relx=0.1,rely=0.27,anchor=CENTER)
but3.place(relx=0.1,rely=0.44,anchor=CENTER)
but4.place(relx=0.1,rely=0.61,anchor=CENTER)
but5.place(relx=0.1,rely=0.78,anchor=CENTER)
#**************************
but6.place(relx=0.25,rely=0.1,anchor=CENTER)
but7.place(relx=0.25,rely=0.27,anchor=CENTER)
but8.place(relx=0.25,rely=0.44,anchor=CENTER)
but9.place(relx=0.25,rely=0.61,anchor=CENTER)
but10.place(relx=0.25,rely=0.78,anchor=CENTER)
#***************************
but11.place(relx=0.40,rely=0.1,anchor=CENTER)
but12.place(relx=0.40,rely=0.27,anchor=CENTER)
but13.place(relx=0.40,rely=0.44,anchor=CENTER)
but14.place(relx=0.40,rely=0.61,anchor=CENTER)
but15.place(relx=0.40,rely=0.78,anchor=CENTER)
#***************************
but16.place(relx=0.55,rely=0.1,anchor=CENTER)
but17.place(relx=0.55,rely=0.27,anchor=CENTER)
but18.place(relx=0.55,rely=0.44,anchor=CENTER)
but19.place(relx=0.55,rely=0.61,anchor=CENTER)
but20.place(relx=0.55,rely=0.78,anchor=CENTER)
#***************************
but21.place(relx=0.70,rely=0.1,anchor=CENTER)
but22.place(relx=0.70,rely=0.27,anchor=CENTER)
but23.place(relx=0.70,rely=0.44,anchor=CENTER)
but24.place(relx=0.70,rely=0.61,anchor=CENTER)
but25.place(relx=0.70,rely=0.78,anchor=CENTER)
#***************************
#bouclage de la fenetre
window.mainloop()