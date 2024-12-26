import re
import csv
from tkinter import *
import customtkinter as  ctk
from tkinter import messagebox
from PIL import Image

# Fonction d'inscription
def register():
    username = smiya.get()
    email = ladrisa.get()
    password = ra9m_siri.get()
    confirm_password = ay3awd_ira9m_siri.get()
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")
    elif password != confirm_password:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas !")
    elif not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        messagebox.showerror('Erreur','email invalide')
    else:
        # Sauvegarde des données dans un fichier_csv CSV
        with open('fichier_csv/Gobet_data.csv', 'a', newline='', encoding='utf-8') as f:
            go = csv.writer(f,delimiter=';')
            go.writerow([username, email, password,'','', '', '', '','' ,'' ,'' ,'' ,'','IMG/utilisateur (1).png'])
        with open('fichier_csv/Solde.csv', 'a', newline='', encoding='utf-8') as f:
            go = csv.writer(f,delimiter=';')
            go.writerow([username,10000])
        messagebox.showinfo("Succès", "Inscription réussie ! \n\n Nous vous offrons  un bonus de 10000$ 😉")
        window.destroy()
        import bet_Se_connecter
def artawi():
    window.destroy()
    import bet_Se_connecter
# Création de la fenêtre principale
window = ctk.CTk()
window.title("GoBet | Inscription")
window.minsize(600, 700)
window.maxsize(600, 700)
window.iconbitmap("IMG/icon.ico")

window.config(bg='#09111e')

# Création du cadre
frame = ctk.CTkFrame(
    window,
    width=400,
    height=500,
    corner_radius=10,
    bg_color= '#09111e',
    fg_color='#0c1b2c',
)
frame.place(relx=0.5, rely=0.6, anchor=CENTER)

img_Titre=ctk.CTkImage(
    light_image=Image.open('IMG/Artboard 1.png'),
    size=(190,110)
)

# LABELS
inscri = ctk.CTkLabel(frame, text="S'inscrire", font=("AlterousText", 38), bg_color='#0c1b2c', text_color='white')
# INPUTS
smiya = ctk.CTkEntry(frame, width=300, height=35, placeholder_text="user name", corner_radius=8,font=('Nexa Heavy',16),placeholder_text_color='white',border_color='#14a714',bg_color='#0c1b2c', fg_color='#0c1b2c',text_color='white')
ladrisa = ctk.CTkEntry(frame, width=300, height=35, placeholder_text="E-mail", corner_radius=8,font=('Nexa Heavy',16),placeholder_text_color='white',border_color='#14a714',bg_color='#0c1b2c', fg_color='#0c1b2c',text_color='white')
ra9m_siri = ctk.CTkEntry(frame, show='*', width=300, height=35, placeholder_text="Password", corner_radius=8,font=('Nexa Heavy',16),placeholder_text_color='white',border_color='#14a714',bg_color='#0c1b2c', fg_color='#0c1b2c',text_color='white')
ay3awd_ira9m_siri = ctk.CTkEntry(frame, show='*', width=300, height=35, placeholder_text="Confirmation Password", corner_radius=8,font=('Nexa Heavy',16),placeholder_text_color='white',border_color='#14a714',bg_color='#0c1b2c', fg_color='#0c1b2c',text_color='white')

# Le bouton
GOBET=ctk.CTkButton(window,image=img_Titre,text='',fg_color='#09111e',bg_color='#09111e',hover_color='#09111e')
but_save = ctk.CTkButton(frame, text="S'inscrire", width=300 ,height=35, corner_radius=8, command=register,border_width=2,font=("Nexa Heavy", 16),border_color='#0c1b2c',bg_color='#0c1b2c',fg_color='#14a714', hover_color='#193314',text_color='white')
con= ctk.CTkButton(frame,text="déja inscrit",width=120,height=35, corner_radius=8,font=("Nexa Heavy", 16),command=artawi,bg_color='#0c1b2c',fg_color='#0c1b2c',hover_color="#0c1b2c",text_color='white')
    # Positionnement des labels
GOBET.place(relx=0.5,rely=0.13,anchor=CENTER)
inscri.place(relx=0.5,rely=0.1,anchor=CENTER)
    #Positionnement des inputs
smiya.place(relx=0.5, rely=0.28, anchor=CENTER)
ladrisa.place(relx=0.5, rely=0.4, anchor=CENTER)
ra9m_siri.place(relx=0.5, rely=0.52, anchor=CENTER)
ay3awd_ira9m_siri.place(relx=0.5, rely=0.64, anchor=CENTER)
    #Positionnement du button
but_save.place(relx=0.5, rely=0.8, anchor=CENTER)
con.place(relx=0.72,rely=0.9,anchor=CENTER)

# Lancer la boucle principale
window.mainloop()
