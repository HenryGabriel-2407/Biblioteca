import mysql.connector as myconn
import customtkinter as ctk

class UserTela:
    def __init__(self, nome, email, senha):
        self.conexao = myconn.connect(host="localhost", user="root", passwd="senha", database="teste")
        self.cursor = self.conexao.cursor()
        
        self.janela = ctk.CTk()
        self.janela.title("Tela de usuário")
        self.janela.geometry("800x600")
        self.janela.maxsize(width=1000, height=700)

        self.nome = nome
        self.email = email
        self.senha = senha


    def user(self):
        from tela_login import Login
        #construindo a janela
        ctk.CTkLabel(self.janela, text=f"Olá, {self.nome} 😎", font=('segoe ui', 30)).pack(pady=30)
        tabview = ctk.CTkTabview(self.janela, width=650, height=600, border_color="white", border_width=2)
        tabview.pack()
        tabview.add("Minha biblioteca")
        tabview.add("Lista de livros")
        tabview.add("Pesquisa")
        tabview.add("Minha conta")

        #Criando frames
        minha_biblioteca_frame = ctk.CTkFrame(tabview.tab("Minha biblioteca"))
        lista_livros_frame = ctk.CTkFrame(tabview.tab("Lista de livros"))
        pesquisa_frame = ctk.CTkFrame(tabview.tab("Pesquisa"))
        minha_conta_frame = ctk.CTkFrame(tabview.tab("Minha conta"))
        minha_biblioteca_frame.grid(sticky="nsew")
        lista_livros_frame.grid(sticky="nsew")
        pesquisa_frame.grid(sticky="nsew")
        minha_conta_frame.grid(sticky="nsew")


        #Na aba Minha biblioteca
        minha_biblioteca_textbox = ctk.CTkTextbox(minha_biblioteca_frame, width=650, height=400, font=("segoe ui", 14))
        def atualizar_minha_biblioteca():
            try:
                sql = f"SELECT isbn_livro, quantidade_livros FROM emprestimos WHERE id_usuario = '{self.email}'"
                self.cursor.execute(sql)
                quantidade_lista = []
                resultado_2 = []
                rows = self.cursor.fetchall()
                for row in rows:
                    isbn, quantidade = row
                    quantidade_lista.append(quantidade)
                    sql2 = f"SELECT titulo, autor, genero, ano FROM livro WHERE isbn = '{str(isbn)}'"
                    self.cursor.execute(sql2)
                    resultado_2.append(self.cursor.fetchall())
                info_livro = []
                for i, resultado in enumerate(resultado_2):
                    for livro in resultado:
                        titulo, autor, genero, ano = livro
                        info_livro.append(f"Título: {titulo}\n")
                        info_livro.append(f"Autor(a): {autor}\n")
                        info_livro.append(f"Gênero: {genero}\n")
                        info_livro.append(f"Ano: {ano}\n")
                        info_livro.append(f"Quantidade: {quantidade_lista[i]}\n\n")
                minha_biblioteca_textbox.configure(state="normal")
                minha_biblioteca_textbox.delete(1.0, ctk.END)
                minha_biblioteca_textbox.insert(ctk.END, "".join(info_livro))
                minha_biblioteca_textbox.configure(state="disabled")

            except Exception as e:
                minha_biblioteca_textbox.configure(state="normal")
                minha_biblioteca_textbox.delete(1.0, ctk.END)
                minha_biblioteca_textbox.insert(ctk.END, f"Não há livros para mostrar {e}")
                minha_biblioteca_textbox.configure(state="disabled")
        botao_atualiza_minha_biblio = ctk.CTkButton(minha_biblioteca_frame, width=200, text="Atualiza", command=atualizar_minha_biblioteca)
        botao_atualiza_minha_biblio.grid(row=0, column=1, padx=50, pady=5)
        minha_biblioteca_textbox.grid(row=1, column=0, columnspan=3)
        minha_biblioteca_textbox.configure(state="disabled")


        #Na aba lista de livros
        lista_textbox = ctk.CTkTextbox(lista_livros_frame, width=650, height=400, font=("segoe ui", 14))
        
        def mostrar_livros():
            #listar todos os livros na biblioteca 
            sql = "SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro"
            self.cursor.execute(sql)
            resultado = []
            for (isbn, titulo, autor, genero, ano, avaliacao, quantidade) in self.cursor:
                estrelas = str('\U0001F31F' * int(avaliacao))
                livro_info = f"Nome do Livro: {titulo}\n"
                livro_info += f"Autor(a): {autor}\n"
                livro_info += f"ISBN: {isbn}\n"
                livro_info += f"Gênero: {genero}\n"
                livro_info += f"Ano: {ano}\n"
                livro_info += f"Avaliação: {estrelas}\n"
                livro_info += f"Quantidade: {quantidade}\n"
                if quantidade <= 1:
                    livro_info += f"LEIA NO LOCAL\n\n"
                resultado.append(livro_info)
            lista_textbox.configure(state="normal")
            lista_textbox.delete(1.0, ctk.END)  # Limpa o texto existente
            lista_textbox.insert(ctk.END, '\n'.join(resultado))
            lista_textbox.configure(state="disabled")

        botao_listar = ctk.CTkButton(lista_livros_frame, text="Todos os livros existente", command=mostrar_livros)
        botao_listar.grid(row=0, column=0, sticky = "ew", padx = 250)
        lista_textbox.grid(row=1, column=0, sticky = "ew", pady=20, columnspan=2)


        #Na aba Pesquisa
        pesquisa_nome_entry = ctk.CTkEntry(pesquisa_frame, width=300, placeholder_text="Digite o nome ou uma palavra do título do livro")
        pesquisa_isbn_entry = ctk.CTkEntry(pesquisa_frame, width=300, placeholder_text="Digite o ISBN do livro")
        pesquisa_genero_entry = ctk.CTkEntry(pesquisa_frame,  width=300, placeholder_text="Digite o gênero do livro")
        pesquisa_autor_entry = ctk.CTkEntry(pesquisa_frame,  width=300, placeholder_text="Digite o autor do livro")
        pesquisa_nome_entry.grid(row=0, column=0, sticky="w")
        pesquisa_isbn_entry.grid(row=1, column=0, sticky="w")
        pesquisa_genero_entry.grid(row=2, column=0, sticky="w")
        pesquisa_autor_entry.grid(row=3, column=0, sticky="w")

        resposta_pesquisa = ctk.CTkTextbox(pesquisa_frame, width=650, height=400, font=("segoe ui", 14))
        resposta_pesquisa.grid(row = 4, column=0, columnspan= 2, sticky="ew")
        resposta_pesquisa.configure(state="disabled")

        def pesquisar_nome_isbn_genero_autor(valor_botao):
            if valor_botao == 0 and len(pesquisa_nome_entry.get()) > 1:
                sql = f"SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE titulo LIKE '%{pesquisa_nome_entry.get()}%'"
            elif valor_botao == 1 and len(pesquisa_isbn_entry.get()) > 1:
                sql=f"SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE isbn LIKE '%{pesquisa_isbn_entry.get()}%'"
            elif valor_botao == 2 and len(pesquisa_genero_entry.get()) > 1:
                sql=f"SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE genero LIKE '%{pesquisa_genero_entry.get()}%'"
            elif valor_botao == 3 and len(pesquisa_autor_entry.get()) > 1:
                sql=f"SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE autor LIKE '%{pesquisa_autor_entry.get()}%'"
            else:
                resposta_pesquisa.configure(state="normal")
                resposta_pesquisa.delete(1.0, ctk.END)  # Limpa o texto existente
                resposta_pesquisa.insert(ctk.END, "Falta dados a inserir!")
                resposta_pesquisa.configure(state="disabled")
                return
            self.cursor.execute(sql)
            resultado_pesquisa = []
            for (isbn, titulo, autor, genero, ano, avaliacao, quantidade) in self.cursor:
                estrelas = str('\U0001F31F' * int(avaliacao))
                livro_info = f"Nome do Livro: {titulo}\n"
                livro_info += f"Autor(a): {autor}\n"
                livro_info += f"ISBN: {isbn}\n"
                livro_info += f"Gênero: {genero}\n"
                livro_info += f"Ano: {ano}\n"
                livro_info += f"Avaliação: {estrelas}\n"
                livro_info += f"Quantidade: {quantidade}\n"
                if quantidade <= 1:
                    livro_info += f"LEIA NO LOCAL\n\n"
                resultado_pesquisa.append(livro_info)
            resposta_pesquisa.configure(state="normal")
            resposta_pesquisa.delete(1.0, ctk.END)  # Limpa o texto existente
            resposta_pesquisa.insert(ctk.END, '\n'.join(resultado_pesquisa))
            resposta_pesquisa.configure(state="disabled")
        def nome_pesquisar():
            pesquisar_nome_isbn_genero_autor(0)
        def isbn_pesquisar():
            pesquisar_nome_isbn_genero_autor(1)
        def genero_pesquisar():
            pesquisar_nome_isbn_genero_autor(2)
        def autor_pesquisar():
            pesquisar_nome_isbn_genero_autor(3)
        botao_nome_pesquisa = ctk.CTkButton(pesquisa_frame, width=200, text="Pesquisa nome", command=nome_pesquisar)
        botao_isbn_pesquisa = ctk.CTkButton(pesquisa_frame, width=200, text="Pesquisa ISBN", command=isbn_pesquisar)
        botao_genero_pesquisa = ctk.CTkButton(pesquisa_frame, width=200, text="Pesquisa gênero", command=genero_pesquisar)
        botao_autor_pesquisa = ctk.CTkButton(pesquisa_frame, width=200, text="Pesquisa autor(a)", command=autor_pesquisar)

        botao_nome_pesquisa.grid(row=0, column=1, sticky="w")
        botao_isbn_pesquisa.grid(row=1, column=1, sticky="w")
        botao_genero_pesquisa.grid(row=2, column=1, sticky="w")
        botao_autor_pesquisa.grid(row=3, column=1, sticky="w")


        #Na aba Minha conta
        ctk.CTkLabel(minha_conta_frame, text=f"CONTA DO {self.nome}", font=("segoe ui", 30)).pack(pady=5,padx=200)
        label_nome = ctk.CTkLabel(minha_conta_frame, text="Nome do usuário", font=("segoe ui", 20)).pack(pady=2)
        novo_nome_entry = ctk.CTkEntry(minha_conta_frame, width=200, placeholder_text=f"{self.nome}")
        novo_nome_entry.pack()
        label_senha = ctk.CTkLabel(minha_conta_frame, text="Senha do usuário", font=("segoe ui", 20)).pack(pady=2)
        nova_senha_entry = ctk.CTkEntry(minha_conta_frame, width=200, placeholder_text=f"{self.senha}")
        nova_senha_entry.pack()
        label_email = ctk.CTkLabel(minha_conta_frame, text="Email de login", font=("segoe ui", 20)).pack(pady=2)
        label_email_registrado = ctk.CTkLabel(minha_conta_frame, text=f"{self.email}", font=("segoe ui", 16)).pack()
        label_atualizado = ctk.CTkLabel(minha_conta_frame, text="", font=("segoe ui", 14))

        def excluir_conta():
            sql = f"DELETE FROM users WHERE email ='{self.email}'"
            self.cursor.execute(sql)
            self.conexao.commit()
            self.janela.destroy()
            login = Login()
            login.main()
        def atualizar_conta():
            if len(novo_nome_entry.get())>=1:
                sql = f"UPDATE users SET nome = '{novo_nome_entry.get()}' WHERE email = '{self.email}'"
                self.cursor.execute(sql)
                self.conexao.commit()
                label_atualizado.configure(text="Atualizado com sucesso!")
            elif len(nova_senha_entry.get()) >= 4:
                sql = f"UPDATE users SET senha = '{nova_senha_entry.get()}' WHERE email = '{self.email}'"
                self.cursor.execute(sql)
                self.conexao.commit()
                label_atualizado.configure(text="Atualizado com sucesso!")
            else:
                label_atualizado.configure(text="Dados insuficiente! Senha tem que ser maior do que 3 caractere.")
        
        botao_excluir = ctk.CTkButton(minha_conta_frame, width=200, text="Excluir", fg_color="red", command=excluir_conta).pack()
        botao_atualizar = ctk.CTkButton(minha_conta_frame, width=200, text="Atualizar", fg_color="green", command=atualizar_conta).pack(pady=5)
        label_atualizado.pack(pady=10)


        self.janela.mainloop()