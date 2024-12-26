import re
import customtkinter as ctk
from tkinter import *
from PIL import Image,ImageDraw
from tkinter import filedialog,messagebox
from datetime import datetime
import csv

from customtkinter import CTkLabel

window=ctk.CTk()
window.title('GoBet | PROFILE')
window.minsize(1160, 720)
window.maxsize(1920, 1080)
window.config(background='#09111e')
window.iconbitmap("IMG/icon.ico")
#************* frames ***********
frame1=ctk.CTkFrame(
    window,
    width=1105,
    height=599,
    bg_color='#09111e',
    fg_color='#0c1b2c',
    corner_radius=25,
    border_width=0,

)
frame2=ctk.CTkFrame(
    frame1,
    width=720,
    height=590,
    bg_color='#0c1b2c',
    fg_color='#09111e',
    border_color='#0c1b2c',
    corner_radius=15,
    border_width=2

)

frame3=ctk.CTkFrame(
    frame2,
    width=420,
    height=120,
    bg_color='#09111E',
    fg_color='#09111E',
    border_color='#09111E',
    corner_radius=15,
    border_width=2

)
image_defaut=ctk.CTkImage(
    light_image=Image.open('IMG/utilisateur (1).png').resize((150,150)),
    size=(150,150)
)
chemin_image =''
#*********************** FONCTIONS ************************
def setter_donner():
    wlu=''
    try:
        with open('fichier_csv/connection.csv', 'r', newline='', encoding='utf-8') as f:
            reader = list(csv.reader(f, delimiter=';'))
            for i in reader:
                for y in i:
                    wlu+=y
        with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
            lect=list(csv.reader(f,delimiter=';'))
            for i in lect:
                if i[0] == wlu:
                    smiya.set(i[0])
                    gmail.set(i[1])
                    code_9dim.set(i[2])
                    # --------new password------------
                    if not i[3]:
                        pass
                    else:
                       code_9dim.set(i[3])
                    # ---------------pays-----------------
                    if not i[4]:
                        print('i[4]=pays vide')
                        Pays.set('Sélectionnez votre payer')
                    else:
                        Pays.set(i[4])
                    # # --------fullname------------
                    if not i[5]:
                        print('i[5]=vide')
                        fullname.configure(
                            placeholder_text='Full Name...'
                        )
                    else:
                        fullname.configure(
                            textvariable=smiya_kamla
                        )
                        smiya_kamla.set(i[5])
                    # # ---------jour-----------
                    if not i[6]:
                        jour.configure(
                            placeholder_text='Jour...'
                        )
                        print('i[6]=vide')
                    else:
                        jour.configure(
                            textvariable=nhaar
                        )
                        nhaar.set(i[6])
                    # # --------mois------------
                    if not i[7]:
                        print('i[7]=vide')
                        mois.configure(
                            placeholder_text = 'Mois...'
                        )
                    else:
                        mois.configure(
                            textvariable=chhher
                        )
                        chhher.set(i[7])
                    # # --------annee------------
                    if not i[8]:
                        print('i[8]==vide')
                        anner.configure(
                            placeholder_text='Anner...'
                        )
                    else:
                        anner.configure(
                            textvariable=l3am
                        )
                        l3am.set(i[8])
                    # # ----------telephone----------
                    if not i[9]:
                        print('i[9]==vide')
                        phone.configure(
                            placeholder_text='Phone...'
                        )
                    else:
                        phone.configure(
                            textvariable=tele
                        )
                        tele.set(i[9])
                    # -----------adresse---------
                    if not i[10]:
                        print('i[10]==vide')
                        adresse.configure(
                            placeholder_text='Adress...'
                        )
                    else:
                        adresse.configure(
                            textvariable=ladrissa
                        )
                        ladrissa.set(i[10])
                    # ------------ville--------
                    if not i[11]:
                        print('i[11]==vide')
                        ville.configure(
                            placeholder_text = 'Ville...'
                        )
                        city.set(i[11])
                    else:
                        ville.configure(
                            textvariable=city
                        )
                        city.set(i[11])
                    # # ---------- code postale----------
                    if not i[12]:
                        print('i[12]==vide')
                        code_postal.configure(
                            placeholder_text='Code Postal...'
                        )
                    else:
                        code_postal.configure(
                            textvariable=codepostale
                        )
                        codepostale.set(i[12])
                    # ------------ image profile--------
                    if not i[13]:
                        print('i[13]==chemin dimage est vide')
                        pic.configure(
                            image=image_defaut,
                            text=''
                        )
                    else:
                        chemin = i[13]
                        PIC = Image.open(chemin).resize((150, 150)).convert("RGBA")
                        rounded_image = round_corners(PIC)
                        img = ctk.CTkImage(
                            light_image=rounded_image,
                            size=(150, 150)
                        )
                        pic.configure(
                            image=img,
                            text=''
                        )
                    # --------------------
    except Exception as e:
        print(f'exception est : {e}')
        messagebox.showerror("Erreur", "Une erreur s'est produite lors de la lecture des fichiers.")
        # return None
def getter_les_donner():
    #************************* exception pour le jour *************************
    try:
        nhar = jour.get().strip()
        if nhar=='' :
            jour.configure(border_color='#14a714', border_width=2)
        else:
            try:
                n=int(nhar)
                if n < 1 or n > 31  :
                    jour.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur','Veuillez entrer un jour valide entre 1 et 31')
                    return
                jour.configure(border_color='#14a714', border_width=2)
            except ValueError:
                jour.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer un jour valide (uniquement des chiffres).')
                return
    #************************* exception pour le mois *************************
        chher = mois.get().strip()
        if chher=='' :
            mois.configure(border_color='#14a714', border_width=2)
        else:
            try:
                m = int(chher)
                if m > 31 or m < 1:
                    mois.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur', 'Veuillez entrer un jour valide entre 1 et 12')
                    return
                mois.configure(border_color='#14a714', border_width=2)
            except ValueError:
                mois.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer un mois valide (uniquement des chiffres).')
                return
    #************************* exception pour l'anner *************************
        eam = anner.get().strip()
        if eam=='':
            anner.configure(border_color='#14a714', border_width=2)
        else:
            try:
                a = int(eam)
                anner_actuelle = datetime.now().year
                age = anner_actuelle - a
                if   age <18 or age > 100:
                    anner.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur', "L'utilisateur doit avoir entre 18 et 100 ans.")
                    return
                anner.configure(border_color='#14a714', border_width=2)
            except ValueError:
                anner.configure(border_color='red', border_width=2)
                messagebox.showinfo('Erreur', 'Veuillez entrer une anner valide (uniquement des chiffres).')
                return
    except Exception as e:
        print(f'Exception pr birthday est : {e}')
    #************************* exception pour le pseudo *************************
    try:
        user = pseudo.get()
        if user== '':
            pseudo.configure(border_color='red',border_width=2)
            messagebox.showinfo('Erreur', 'Veuillez entrer le pseudo !!')
            return
        else:
            pseudo.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr pseudo est : {e}')
    #************************* exception pour le email *************************
    try:
        tabrat = mail.get()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", tabrat):
            mail.configure(border_color='red', border_width=2)
            messagebox.showinfo('Erreur', 'Veuillez corriger l email !!')
            return
        else:
            mail.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr pseudo est : {e}')
    #************************* exception pour lE TELEPHONE *************************
    try:
        telephone = phone.get()
        if telephone=='':
            phone.configure(border_color='#14a714', border_width=2)
        else:
            caracteres_valides = ['0','1','','2','3','4','5','6','7','8','9','+','-','(',')',' ']
            for i in telephone:
                if i not in caracteres_valides:
                    phone.configure(border_color='red', border_width=2)
                    messagebox.showinfo('Erreur','Veuillez corriger le numero !!')
                    return
        phone.configure(border_color='#14a714', border_width=2)
    except Exception as e:
        print(f'Exception pr TELE est : {e}')
    #************************* exception globl *************************
    try:
        nhar = jour.get().strip()
        chher = mois.get().strip()
        eam = anner.get().strip()
        user = pseudo.get()
        tabrat = mail.get()
        telephon = phone.get()
        NOM_COMPLET = fullname.get()
        KOUD_KDIM = Password.get()
        koud = new_Password.get()
        conf_koud = conf_password.get()
        ALBALAD= Pays.get()
        ladrisa = adresse.get()
        mdina = ville.get()
        postal = code_postal.get()
        if koud != conf_koud:
            messagebox.showinfo('Erreur', 'Les mots de passe ne correspondent pas !')
            return
        else:
            with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
                red = list(csv.reader(f, delimiter=';'))
                for i in red:
                    if i[0] == user_name():
                        if not chemin_image:
                            picture=i[-1]
                        else:
                            picture=chemin_image

                        red.remove(i)
                        break
            with open('fichier_csv/Gobet_data.csv', 'w', newline='', encoding='utf-8') as fa:
                ecr = csv.writer(fa, delimiter=';')
                ecr.writerows(red)
                ecr.writerow(
                    [user, tabrat, KOUD_KDIM, koud,ALBALAD, NOM_COMPLET, nhar, chher, eam, telephon, ladrisa, mdina, postal,
                     picture])
            name=''
            for i in user:
                name+=i
            with open('fichier_csv/connection.csv', 'w', newline='', encoding='utf-8') as fc:
                katib= csv.writer(fc,delimiter=';')
                katib.writerow(name)
            messagebox.showinfo('Modification', 'Modification avec succes !!')
    except Exception as e:
        print(f'Exception survenu est : {e}')

def modifier():
    modif_password.place(relx=0.75, rely=0.53, anchor=CENTER)
    Password.configure(
        show='',
        state='readonly',
        border_width=2,

    )
    new_Password.configure(
        state='normal',
        border_width=2,
        placeholder_text='New Password...'
    )
    conf_password.configure(
        state='normal',
        border_width=2,
        placeholder_text='Confirmation Password...'
    )

def dowal():
    return ['Maroc','France','Egypt','Espagne','Algérie','Portugal',]

def user_name():
    utilisateur = ''
    with open('fichier_csv/connection.csv', 'r', newline='', encoding='utf-8') as fc:
        con = list(csv.reader(fc, delimiter=';'))
        for i in con:
            for y in i:
                utilisateur += y
    return utilisateur

#fonction qui rend l'image cercle (L3Z ONSEEER L CHATGPT)
def round_corners(image):
    #rendre l'image carrees
    min_side = min(image.size)
    square_image = image.crop((0, 0, min_side, min_side))
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
def choisir_image():
    global chemin_image
    # Ouvrir une boîte de dialogue pour choisir un fichier_csv image
    chemin_image = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("IMG", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if chemin_image:
        try:
            image = Image.open(chemin_image).convert("RGBA")
            # Arrondir les coins de l'image
            rounded_image = round_corners(image)  # Ajustez le rayon ici
            # Vérifier si un fichier_csv a été sélectionné
            img = ctk.CTkImage(
                light_image=rounded_image,
                size=(180,180)
            )
            pic.configure(
                image=img,
                text='',
                border_width=0,
                fg_color='#0c1b2c',
                width=10,
                height=20,
                hover_color='#173955'
            )
        except Exception as e:
            print(f'erreur de choix dimage{e}')
            return  None
def image_profile():
    try:
        with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
            lec=list(csv.reader(f,delimiter=';'))
            for i in lec:
                # if not i[-1] :
                if i[0]== user_name() :
                    chemin=i[-1]
                    PIC=Image.open(chemin).resize((150, 150)).convert("RGBA")
                    rounded_image = round_corners(PIC)
                    img=ctk.CTkImage(
                        light_image=rounded_image,
                         size=(150, 150)
                    )
                    return img
    except Exception as e:
        print(f'exception est : {e}')

def iwri():
    window.destroy()
    import game1

# **************** stingvar *************************

smiya = StringVar()
gmail = StringVar()
code_9dim = StringVar()
koud_jdid = StringVar()
smiya_kamla = StringVar()
nhaar = StringVar()
chhher = StringVar()
l3am = StringVar()
tele = StringVar()
ladrissa= StringVar()
city = StringVar()
codepostale = StringVar()
blad=StringVar()

#***********************************************************************
    # LES LABELS
birthday=ctk.CTkLabel(frame1,text="-------------------BIRTHDAY-------------------", font=("AlterousText", 18), bg_color='#0c1b2c', text_color='white')
Cordonnees=ctk.CTkLabel(frame2,text="-----------------------------------------------LES CORDONNEES-----------------------------------------------", font=("AlterousText", 18), bg_color='#09111e', text_color='white')
Bank=ctk.CTkLabel(frame2,text="---------------------------------------------Methode de paiment---------------------------------------------", font=("AlterousText", 18), bg_color='#09111e', text_color='white')
PAIMENT=CTkLabel(frame3,text='En cours de traitement...',font=("AlterousText", 34), bg_color='#09111e', text_color='white')
    # input
fullname=ctk.CTkEntry(frame1,width=300,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
pseudo=ctk.CTkEntry(frame1,textvariable=smiya,width=300,height=45,placeholder_text='User Name...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
jour=ctk.CTkEntry(frame1,width=90,height=45,font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
mois=ctk.CTkEntry(frame1,width=90,height=45,font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
anner=ctk.CTkEntry(frame1,width=90,height=45,font=('Nexa Heavy',14),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
mail=ctk.CTkEntry(frame2,textvariable=gmail,width=320,height=45,placeholder_text='E-mail...',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')

#*********
phone=ctk.CTkEntry(frame2,width=320,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*************************************************************
adresse=ctk.CTkEntry(frame2,width=320,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
ville=ctk.CTkEntry(frame2,width=150,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
code_postal=ctk.CTkEntry(frame2,width=150,height=45,font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
#*********
Password=ctk.CTkEntry(frame2,textvariable = code_9dim,width=320,height=45,show='*',state='readonly',font=('Nexa Heavy',16),corner_radius=25,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')

#*********
new_Password=ctk.CTkEntry(frame2,width=320,height=45,state='readonly',font=('Nexa Heavy',16),corner_radius=25,border_width=0,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
conf_password=ctk.CTkEntry(frame2,width=320,height=45,state='readonly',font=('Nexa Heavy',16),corner_radius=25,border_width=0,placeholder_text_color='white',fg_color='#09111e',text_color='white',border_color='#14a714')
    # button
pic=ctk.CTkButton(frame1,text='',command=lambda :choisir_image(),width=160,height=160,corner_radius=80,border_width=0,fg_color='#0c1b2c',bg_color='#0c1b2c',hover_color='#0c1b2c')
Save=ctk.CTkButton(frame1,text='Enregistrer',command=lambda : getter_les_donner(),width=140,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#14a714',bg_color='#0c1b2c',hover_color='#0d4914',border_color='#14a714')
back=ctk.CTkButton(frame1,text='Retourner',command= lambda : iwri(),width=140,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#0d4914',bg_color='#0c1b2c',hover_color='#14a714',border_color='#0d4914')
modif_password=ctk.CTkButton(frame2,text='Modifier Password',command=lambda :modifier(),width=320,height=45,corner_radius=25,border_width=2,font=('Nexa Heavy',16),fg_color='#0d3112',bg_color='#09111e',hover_color='#0d4914',border_color='#0d3112')
    #combobox
Pays=ctk.CTkComboBox(frame2,values=dowal(),state="readonly",font=('Nexa Heavy',16),width=320,height=45,corner_radius=25,fg_color='#09111e',text_color='white',border_color='#14a714')


#***************positionnement***************
    #frame
frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
frame2.place(relx=0.666,rely=0.499,anchor=CENTER)
frame3.place(relx=0.5,rely=0.8,anchor=CENTER)
    #labels
birthday.place(relx=0.175,rely=0.620,anchor=CENTER)
Cordonnees.place(relx=0.5,rely=0.05,anchor=CENTER)
Bank.place(relx=0.5,rely=0.62,anchor=CENTER)
PAIMENT.place(relx=0.5,rely=0.5,anchor=CENTER)
    #input
#**face1
fullname.place(relx=0.175,rely=0.45,anchor=CENTER)
pseudo.place(relx=0.175,rely=0.55,anchor=CENTER)
jour.place(relx=0.08,rely=0.7,anchor=CENTER)
mois.place(relx=0.175,rely=0.7,anchor=CENTER)
anner.place(relx=0.27,rely=0.7,anchor=CENTER)
#***face2
mail.place(relx=0.25,rely=0.13,anchor=CENTER)
phone.place(relx=0.25,rely=0.23,anchor=CENTER)
adresse.place(relx=0.25,rely=0.33,anchor=CENTER)
ville.place(relx=0.13,rely=0.53,anchor=CENTER)
code_postal.place(relx=0.37,rely=0.53,anchor=CENTER)
#***face3
Password.place(relx=0.75,rely=0.13,anchor=CENTER)
new_Password.place(relx=0.75,rely=0.23,anchor=CENTER)
conf_password.place(relx=0.75,rely=0.33,anchor=CENTER)
    # button
pic.place(relx=0.175,rely=0.18,anchor=CENTER)
Save.place(relx=0.1,rely=0.85,anchor=CENTER)
back.place(relx=0.245,rely=0.85,anchor=CENTER)
modif_password.place(relx=0.75,rely=0.23,anchor=CENTER)
    #combobox
Pays.place(relx=0.25,rely=0.43,anchor=CENTER)
setter_donner()
#***************boucler la feneter****************
window.mainloop()


