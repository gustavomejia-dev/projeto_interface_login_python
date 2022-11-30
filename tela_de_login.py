import mysql.connector
from tkinter import *
from tkinter import messagebox


interface = Tk()


class Login:
    def __init__(self):
        self.interface = interface
        self.tela()
        self.frames()
        self.input_and_lb()
        self.btn_login()
        self.img()
        interface.mainloop()

    def img(self):
        self.logo = PhotoImage(file='logo_empire.gif')
        self.imagem = Label(self.interface, image=self.logo)
        self.imagem.place(relx=0.05, rely=0.06, relwidth=0.550, relheight=0.800)

    def tela(self):
        self.interface.title('Login')
        self.interface.configure(bg='white')
        self.interface.geometry("900x340")
        self.interface.resizable(False, False)

    def frames(self):
        self.frame = Frame(self.interface, bg='white')
        self.frame.place(relx=0.50, rely=0.01, relwidth=0.96, relheight=0.90)

    def btn_login(self):
        self.login = Button(self.frame, highlightbackground='#192C47', fg='#181087', text='Login',
                            highlightcolor='#1434b5', bg='White',
                            highlightthickness=5, font=('Arial Italic', 12, 'bold'), command=self.conecta, )
        self.login.place(relx=0.30, rely=0.68, relwidth=0.10, relheight=0.12)

    @staticmethod
    # Fecha a Interface de Login
    def fecha(jan):
        jan.destroy()

    def conecta(self):
        try:
            self.con = mysql.connector.connect(host='localhost', database='db_usuario', user='root', password='')
            db_info = self.con.get_server_info()
            print("Conectado ao servidor MySQL", db_info)
        except:
            messagebox.showerror('Critical Error', 'Erro ao Conectar ao servidor, Contate o Administrador do Sistema')
        cursor = self.con.cursor()
        name = self.usuario.get()
        senha = self.senha.get()
        savequery = "select * from usuarios where usuario = %s and senha = %s "
        vals = (name, senha)
        cursor.execute(savequery, vals)
        myresult = cursor.fetchall()
        if myresult:
            messagebox.showinfo('Aviso', 'Acesso Liberado')
            exit()
        else:
            messagebox.showinfo('Aviso', 'Credenciais incorretas')

    def input_and_lb(self):
        self.lb_logar = Label(self.frame, text='Efetue o Login', bg='white', font=('Arial', 16, 'bold'),
                              fg='#2B3378')
        self.lb_logar.place(relx=0.09, rely=0.14, relwidth=0.30, relheight=0.10)
        self.lb_usuario = Label(self.frame, text='Usuario', bg='white', font=('Microsoft Yahei UI Light', 11, 'bold'),
                                fg='#2B3378')
        self.lb_usuario.place(relx=0.14, rely=0.25, relwidth=0.10, relheight=0.10)
        self.usuario = Entry(self.frame, fg='black', bg='white', font=('Microsoft Yahei UI Light', 10, 'bold'),
                             highlightthickness=1, highlightcolor='#0090F7', highlightbackground='#192C47')
        self.usuario.place(relx=0.15, rely=0.33, relwidth=0.20, relheight=0.10)

        self.lb_senha = Label(self.frame, text='Senha', bg='white', font=('Microsoft Yahei UI Light', 11, 'bold'),
                              fg='#2B3378')

        self.lb_senha.place(relx=0.13, rely=0.47, relwidth=0.10, relheight=0.10)
        self.senha = Entry(self.frame, fg='black', bg='white', font=('Microsoft Yahei UI Light', 10, 'bold'),
                           highlightthickness=1, highlightcolor='#0090F7', highlightbackground='#192C47', show='*')
        self.senha.place(relx=0.15, rely=0.55, relwidth=0.20, relheight=0.10)


Login()
