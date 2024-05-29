import customtkinter as ctk
import mysql.connector as myconn
import smtplib
import email.message as emessage
from tela_administrador import AdmTela
from tela_usuario import UserTela

#conexão ao database
class Login:
    def main(self):
        conexao = myconn.connect(host="localhost", user="root", passwd="@NikolaTesla369", database="teste")
        cursor = conexao.cursor()

        #criando interface
        janela = ctk.CTk()
        janela.title("Tela de login")
        janela.geometry("600x400")
        janela.maxsize(width=600, height=400)
        janela.minsize(width=600, height=400)

        #construindo a janela
        ctk.CTkLabel(janela, text="Login", font=("segoe ui", 30)).pack(pady=20)
        nome_input = ctk.CTkEntry(janela, width=200, placeholder_text="Digite seu nome (Registro)...")
        nome_input.pack(pady=10)
        email_input = ctk.CTkEntry(janela, width=200, placeholder_text="Digite seu email...")
        email_input.pack(pady=10)
        senha_input = ctk.CTkEntry(janela, width=200, placeholder_text="Digite a sua senha...", show="*")
        senha_input.pack(pady=10)
        lab = ctk.CTkLabel(janela, width=100, font=("segoe ui", 12), text="")

        def esqueci_senha():
            email= email_input.get()
            sql = f"SELECT senha FROM users WHERE email = '{email}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if resultado:
                senha = resultado[0]
                corpo_email = f"""
                <p>Ignora esta mensagem</p>
                <p>A senha do sistema de biblioteca é: <strong>{senha}</strong></p>
                <img src = "https://ci3.googleusercontent.com/meips/ADKq_Nbcrfh0oyG1dCGyCJm5rJKNbPVWl2kRyt5SPFsZUbErG4cDQkwBZGQ1osMmn00sAtfcLuksunGuqtSJH9JRWP_Nec9SZjDHjkFhvkyPmSWEXahBKPmpH-ARPygimtuIXcf_=s0-d-e1-ft#https://i.pinimg.com/originals/35/6a/38/356a384ff231ef42c4b91c772b5fbfa7.jpg" width="400" height="400" />"""
                msg = emessage.Message()
                msg['Subject'] = "Mensagem automática - Sistema de Biblioteca" 
                msg['From'] = "henryuniavantestes@gmail.com"
                msg['To']= f"{email}"
                password = "olctkajowqxtkinw"
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(corpo_email)

                s = smtplib.SMTP('smtp.gmail.com: 587')
                s.starttls()
                s.login(msg["From"], password)
                s.sendmail(msg["From"], [msg['To']],msg.as_string().encode('utf-8'))
                lab.configure(text="Email enviado!")
            else:
                lab.configure(text="E-mail não encontrado\nou sem senha associada.")
            
            
        def acesso(tipo):
            sql = f"SELECT nome, email, senha FROM users WHERE email = '{email_input.get()}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()

            if resultado:
                return
            else:
                if len(nome_input.get()) >= 1 and len(senha_input.get())>=4:
                    sql = f"INSERT INTO `users`(`nome`,`email`, `senha`, `tipo`) VALUES ('{nome_input.get()}','{email_input.get()}', '{senha_input.get()}', '{tipo}')"
                    cursor.execute(sql)
                    conexao.commit()
                else:
                    lab.configure(text="Dados insuficiente...")


        def login_user():
            email = email_input.get()
            sql = f"SELECT nome, email, senha, tipo FROM users WHERE email = '{email}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if resultado:
                nome, email, senha, tipo= resultado
                if senha != senha_input.get():
                    lab.configure(text="Senha incorreta...")
                else:
                    if tipo == "USER":
                        acesso("USER")
                        janela.destroy()
                        nova_janela = UserTela(nome, email, senha)
                        nova_janela.user()
            else:
                acesso("USER")
                login_user()

        def login_adm():
            email = email_input.get()
            sql = f"SELECT nome, email, senha, tipo FROM users WHERE email = '{email}'"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            if resultado:
                nome, email, senha, tipo = resultado
                if senha != senha_input.get():
                    lab.configure(text="Senha incorreta...")
                else:
                    if tipo =="ADMIN":
                        acesso("ADMIN")
                        janela.destroy()
                        nova_janela = AdmTela(nome, email, senha)
                        nova_janela.adm()
            else:
                acesso("ADMIN")
                login_adm()

        def puts():
            esqueci_senha()

        botao_login_user = ctk.CTkButton(janela, width=90, text="Login USER", command=login_user).place(x = 200,y=320)
        botao_login_adm = ctk.CTkButton(janela, width=90, text="Login ADM", command=login_adm).place(x = 310,y=320)
        botao_esqueci_senha = ctk.CTkButton(janela, width=70, height= 10, text="Esqueci senha", command=puts, fg_color="transparent").place(x = 310,y=250)
        lab.place(x=250, y=270)

        janela.mainloop()   

if __name__ == "__main__":
    user = Login()
    user.main()