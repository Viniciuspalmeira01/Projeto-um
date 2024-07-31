import tkinter
from time import sleep
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
from peewee import * 
from database import Anuncio , db , Usuario


db.connect()
db.create_tables([Usuario , Anuncio]) 
def salvar_cadastros():
          usuario4 = Usuario.create(nome = Nome.get() , email = Email.get() , senha = Senha.get() )
          usuario4.save()
          sleep(2)
          messagebox.showinfo('Register your account' , 'Login realizado')

# Configurações iniciais do CustomTkinter
set_appearance_mode('dark')  # Pode ser 'dark', 'light' ou 'system'
set_default_color_theme('green')

# Criação da janela principal
window = CTk()
window.geometry('950x672')
window.title('Login')

# Carregamento da imagem de fundo
imagem = Image.open('New_wallpaper.jpg')
imagem = imagem.resize((950, 672), Image.LANCZOS)  # Redimensionando a imagem para caber na janela
imagem_tk = ImageTk.PhotoImage(imagem)

# Label para exibir a imagem de fundo
l1 = CTkLabel(master=window, image=imagem_tk, text='')
l1.place(x=0, y=0, relwidth=1, relheight=1)

# Frame centralizado para os widgets de login
frame = CTkFrame(master=l1, width=360, height=440, corner_radius=32)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Label de título dentro do frame
l2 = CTkLabel(frame, text='Register your account !!', font=('Century Gothic', 23))
l2.place(relx=0.5, y=45, anchor=tkinter.CENTER)

# Campo de entrada para o nome de usuário
Nome = CTkEntry(master=frame, width=240,height=37, placeholder_text='Name')
Nome.place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)

Email = CTkEntry(master=frame, width=240, height=37, placeholder_text='Username or Email')
Email.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)

# Campo de entrada para a senha
Senha = CTkEntry(master=frame, width=240,height=37, placeholder_text='Password', show='*')
Senha.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER)

# Botão de login
login_button = CTkButton(master=frame, text='Create', width=240, height=36, command = salvar_cadastros)
login_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# Iniciando o loop principal da interface
window.mainloop()