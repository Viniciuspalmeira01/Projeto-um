import tkinter
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time

# Configurações iniciais do CustomTkinter
set_appearance_mode('dark')  # Pode ser 'dark', 'light' ou 'system'
set_default_color_theme('green')

#variáveis:
usuarios = {'vinicius@gmail':'2006'}
perfil_de_entrada = {}
#funções para acesso e parada de usuários
def entrada():
        perfil_de_entrada = perfil_de_entrada = {entrada1.get(): entrada2.get()}
        return perfil_de_entrada

def user():
         for cadastrado in usuarios:
                if perfil_de_entrada == cadastrado:
                        time.sleep(3)
                        messagebox.showinfo('Login', 'Bem vindo de volta!')
                else:
                        time.sleep(3)
                        messagebox.showinfo('Login' , 'Usuário não encontrado')
# Criação da janela principal
window = CTk()
window.geometry('933x670')
window.title('Login')
window.resizable(False , False)


# Carregamento da imagem de fundo
imagem = Image.open('pattern-4u7ed6koskqhcez1.jpg')
imagem = imagem.resize((950, 670))  # Redimensionando a imagem para caber na janela
imagem_tk = ImageTk.PhotoImage(imagem)

google = Image.open('Google.png')
google = google.resize((20,20), Image.LANCZOS)
googleTk =ImageTk.PhotoImage(google) 

facebook = Image.open('facebook_icone.png')
facebook = facebook.resize((20,20), Image.LANCZOS)
facebookTk =ImageTk.PhotoImage(facebook)
# Label para exibir a imagem de fundo
l1 = CTkLabel(master=window, image=imagem_tk, text='')
l1.place(x=0, y=0, relwidth=1, relheight=1)

# Frame centralizado para os widgets de login
frame = CTkFrame(master=l1, width=380, height=440, corner_radius=32, border_color='green')
frame.place(relx=0.24, rely=0.51,anchor = tkinter.CENTER) 

# Label de título dentro do frame
l2 = CTkLabel(frame, text='Login into your Account', font=('Century Gothic', 24))
l2.place(relx=0.5, y=45, anchor=tkinter.CENTER)

entrada1 = CTkEntry(master=frame, width=250,height=39, placeholder_text='Username', corner_radius=32, text_color = 'black', fg_color='white', placeholder_text_color='black')
entrada1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

# Campo de entrada para a senha
entrada2 = CTkEntry(master=frame, width=250, height=39, placeholder_text='Password', corner_radius=32,text_color = 'black', fg_color='white', placeholder_text_color='black')
entrada2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Botão de login
login_button = CTkButton(master=frame, text='Login', width=230 ,height=36, corner_radius=33, hover_color='blue', command = user)
login_button.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)# a cada widget cerca de px de distância

button_google = CTkButton(frame,width=135, height=33, image= googleTk, text='Google', corner_radius=6, compound='left')
button_google.place(relx=0.1, rely=0.9)

button_facebook = CTkButton(frame,width=130, height=33, image= facebookTk, text='Facebook', corner_radius=6, compound='left')
button_facebook.place(relx=0.5, rely=0.9,)

#random_password = CTkButton(frame , command = back )
#random_password.place()
#Botão 'lembrar de mim'

check_var = StringVar(value='off')
check = CTkCheckBox(master = frame ,variable=check_var , onvalue= 'on' , offvalue='off', text='Lembrar-se de mim ', corner_radius=33 )
check.place(relx = 0.3 , rely = 0.8 , anchor = tkinter.CENTER)

# Iniciando o loop principal da interface
window.mainloop()