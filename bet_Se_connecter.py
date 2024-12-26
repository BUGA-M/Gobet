from tkinter import*
import customtkinter as ctk
from tkinter import messagebox
import csv
from PIL import Image



def MEssageErrurvide():
    smiya.configure(frame,border_color='red')
    cooode.configure(frame,border_color='red')
    exeption2 = ctk.CTkLabel(frame, text="Nom d'utilisateur ou mot de passe incorrect", font=("AlterousText", 13), bg_color='#0c1b2c', text_color='#0c1b2c')
    exeption = ctk.CTkLabel(frame, text="Remplire tout input", font=("AlterousText", 13), bg_color='#0c1b2c', text_color='red')
    exeption.place(relx=0.22,rely=0.64,anchor=CENTER)
    exeption2.place(relx=0.40,rely=0.64,anchor=CENTER)
def MEssageErrurfalse():
    smiya.configure(frame,border_color='red')
    cooode.configure(frame,border_color='red')
    exeption2 = ctk.CTkLabel(frame, text="Nom d'utilisateur ou mot de passe incorrect", font=("AlterousText", 13), bg_color='#0c1b2c', text_color='red')
    exeption2.place(relx=0.40,rely=0.64,anchor=CENTER)


# def connecter():
#     try:
#         alism = smiya.get()
#         al9an_siri = cooode.get()
#
#         # Vérification des champs vides
#         if not alism or not al9an_siri:
#             MEssageErrurvide()
#             return
#
#         # Lecture du fichier CSV
#         with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
#             bet = list(csv.reader(f, delimiter=';'))
#
#         connexion_reussie = False
#
#         for utilisateur in bet:
#             # Vérifier si l'utilisateur a le bon format de données
#             if len(utilisateur) < 4:
#                 continue
#
#             # Vérification des identifiants
#             if utilisateur[0] == alism:
#                 if (utilisateur[2] == al9an_siri and not utilisateur[3]) or (utilisateur[3] == al9an_siri):
#                     connexion_reussie = True
#                     break
#
#         if connexion_reussie:
#             messagebox.showinfo("Succès", "Connexion réussie !")
#             # Enregistrement de la connexion
#             with open('fichier_csv/connection.csv', 'w', newline='', encoding='utf-8') as fc:
#                 login = csv.writer(fc, delimiter=';')
#                 login.writerow([alism])  # Écrire comme une liste
#             window.destroy()
#             import game1
#         else:
#             MEssageErrurfalse()
#
#     except Exception as e:
#         print(f"Erreur : {str(e)}")  # Pour le débogage
#         MEssageErrurfalse()
def connecter():
    try:
        alism = smiya.get()
        al9an_siri = cooode.get()
        if not alism or not al9an_siri:
            MEssageErrurvide()
            return
        with open('fichier_csv/Gobet_data.csv', 'r', newline='', encoding='utf-8') as f:
            bet=list(csv.reader(f,delimiter=';'))
        for i in bet:
            if i[0] == alism and i[2]==al9an_siri and not i[3] :
                messagebox.showinfo("Succès", "Connexion réussie !")
                with open('fichier_csv/connection.csv', 'w', newline='', encoding='utf-8')as fc:
                    login=csv.writer(fc,delimiter=';')
                    login.writerow(alism)
                window.destroy()
                import game1
                return
            elif i[0] == alism and i[3] == al9an_siri:
                messagebox.showinfo("Succès", "Connexion réussie !")
                with open('fichier_csv/connection.csv', 'w', newline='', encoding='utf-8') as fc:
                    login = csv.writer(fc, delimiter=';')
                    login.writerow(alism)
                window.destroy()
                import game1
                return
        MEssageErrurfalse()
    except Exception :
        MEssageErrurfalse()

# Création de la fenêtre principale
window=ctk.CTk()
window.title('GoBet | Connection')
window.minsize(600, 700)
window.maxsize(600, 700)
window.config(bg='#09111e')
window.iconbitmap("IMG/icon.ico")
frame=ctk.CTkFrame(
    window,
    width=350,
    height=400,
    bg_color='#09111e',
    fg_color='#0c1b2c',
    corner_radius=10
)
frame.place(relx=0.5,rely=0.6,anchor=CENTER)

img_Titre=ctk.CTkImage(
    light_image=Image.open('IMG/Artboard 1.png'),
    size=(190,110)
)

    # LES LABELS
conect = ctk.CTkLabel(frame, text="Se Connecter", font=("AlterousText", 38), bg_color='#0c1b2c', text_color='white')
    # les inputs
smiya=ctk.CTkEntry(frame,width=300,height=35,font=("Nexa Heavy", 16),placeholder_text='user_name',placeholder_text_color='white',corner_radius=8,border_color='#14a714',bg_color='#0c1b2c',fg_color='#0c1b2c',text_color='white')
cooode=ctk.CTkEntry(frame, show='*',width=300,height=35,font=("Nexa Heavy", 16),placeholder_text='Password',placeholder_text_color='white',corner_radius=8,border_color='#14a714',bg_color='#0c1b2c',fg_color='#0c1b2c',text_color='white')
    #les buttons
GOBET=ctk.CTkButton(window,image=img_Titre,text='',fg_color='#09111e',bg_color='#09111e',hover_color='#09111e')
Se_Connecter=ctk.CTkButton(frame,text='Se Connecter',command=connecter,width=300,height=35,font=("Nexa Heavy", 16),bg_color='#0c1b2c',fg_color='#14a714',hover_color='#193314',text_color='white')
    #Positionnement des labels
GOBET.place(relx=0.5,rely=0.2,anchor=CENTER)
conect.place(relx=0.5,rely=0.15,anchor=CENTER)
    #Positionnement des inputs
smiya.place(relx=0.5,rely=0.37,anchor=CENTER)
cooode.place(relx=0.5,rely=0.55,anchor=CENTER)
    #Positionnement du button
Se_Connecter.place(relx=0.5,rely=0.8,anchor=CENTER)
#bouclage de la fenetre
window.mainloop()