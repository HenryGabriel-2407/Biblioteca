import mysql.connector as myconn
import customtkinter as ctk

class AdmTela:
    def __init__(self, nome, email, senha):
        self.conexao = myconn.connect(host="localhost", user="root", passwd="senha", database="teste")
        self.cursor = self.conexao.cursor()

        self.janela = ctk.CTk()
        self.janela.title("Tela do ADM")
        self.janela.geometry("800x600")
        self.janela.maxsize(width=1000, height=700)

        self.nome = nome
        self.email = email
        self.senha = senha


    def adm(self):
        from tela_login import Login
        #construindo a janela
        ctk.CTkLabel(self.janela, text=f"Olá, senhor(a) {self.nome} 😎", font=('segoe ui', 30)).pack(pady=30)
        #Inserindo tabviews
        tabview = ctk.CTkTabview(self.janela, width=650, height=600, border_color="white", border_width=2)
        tabview.pack()
        tabview.add("Adicionar livro")
        tabview.add("Excluir livro")
        tabview.add("Lista de livros")
        tabview.add("Editar livro")
        tabview.add("Empréstimo/Devolução de livro")
        tabview.add("Pesquisa")
        tabview.add("Minha Conta")

        #adicionando frames
        add_frame = ctk.CTkFrame(tabview.tab("Adicionar livro"))
        excluir_frame = ctk.CTkFrame(tabview.tab("Excluir livro"))
        listar_frame = ctk.CTkFrame(tabview.tab("Lista de livros"))
        editar_frame = ctk.CTkFrame(tabview.tab("Editar livro"))
        emprestimo_devolucao_frame = ctk.CTkFrame(tabview.tab("Empréstimo/Devolução de livro"))
        pesquisa_frame = ctk.CTkFrame(tabview.tab("Pesquisa"))
        minha_conta_frame = ctk.CTkFrame(tabview.tab("Minha Conta"))
        add_frame.grid(sticky="nsew")
        excluir_frame.grid(sticky="nsew")
        listar_frame.grid(sticky="nsew")
        editar_frame.grid(sticky="nsew")
        emprestimo_devolucao_frame.grid(sticky="nsew")
        pesquisa_frame.grid(sticky="nsew")
        minha_conta_frame.grid(sticky="nsew")


        # Na aba "Adicionar livro"
        nome_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite o título do livro...")
        autor_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite o nome do autor...")
        genero_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite o gênero...")
        isbn_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite o ISBN...")
        ano_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite o ano de publicação...")
        avaliacao_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite a avaliação de 0 a 10...")
        quantidade_entry = ctk.CTkEntry(add_frame, width=300, placeholder_text="Digite a quantidade no estoque...")
        lab = ctk.CTkLabel(add_frame, text="", font=("segoe ui", 20))

        def criar_livro():
            if len(isbn_entry.get()) < 10 and len(nome_entry.get()) < 1 and len(autor_entry.get()) < 1 and len(genero_entry.get()) < 1 and len(ano_entry.get()) < 0 and len(avaliacao_entry.get()) < 0 and len(quantidade_entry.get()) < 0:
                lab.configure(text="Falta dados a inserir!")
                return  # Interrompe a execução da função
            sql = f"SELECT isbn FROM livro WHERE isbn = '{isbn_entry.get()}'"
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            if resultado:
                lab.configure(text="Este livro já existe!")
            elif not resultado:
                sql = f"INSERT INTO `livro`(`isbn`, `titulo`, `autor`, `genero`, `ano`, `avaliacao`, `quantidade`) VALUES('{isbn_entry.get()}', '{nome_entry.get()}', '{autor_entry.get()}', '{genero_entry.get()}', '{ano_entry.get()}', '{avaliacao_entry.get()}', '{quantidade_entry.get()}')"
                try:
                    self.cursor.execute(sql)
                    self.conexao.commit()
                    lab.configure(text="Livro criado com sucesso!")
                except:
                    lab.configure(text="Deu ruim")
            else:
                lab.configure(text="Rapaz... erro!")

        criar_botao = ctk.CTkButton(add_frame, width=200, text="CRIAR LIVRO", command=criar_livro)
        nome_entry.pack(pady=5, padx = 150)
        autor_entry.pack(pady=5)
        genero_entry.pack(pady=5)
        isbn_entry.pack(pady=5)
        ano_entry.pack(pady=5)
        avaliacao_entry.pack(pady=5)
        quantidade_entry.pack(pady=5)
        criar_botao.pack(pady = 30)
        lab.pack(pady=10)


        # Na aba "Excluir livro"
        lab_pesquisa = ctk.CTkLabel(excluir_frame, width=200, text="Pesquisa o ISBN", font=("segoe ui", 16))
        lab_pesquisa.grid(row=0, column=0, padx=200, sticky = "ew", columnspan=2)
        isbn_entry_ = ctk.CTkEntry(excluir_frame, width=300, placeholder_text="Digite o ISBN...")
        isbn_entry_.grid(row=1, column=0, sticky = "w")
        botao_excluir = None
        def pesquisar():
            sql = f"SELECT * FROM livro WHERE isbn ='{isbn_entry_.get()}'"
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()     
            if resultado:
                global botao_excluir
                radio = ctk.IntVar()
                isbn_lista = []
                for i, (isbn, titulo, autor, genero, ano, avaliacao, quantidade) in enumerate(resultado):
                    isbn_lista.append(isbn)
                    botao = ctk.CTkRadioButton(excluir_frame, width=400, text=f"{'='*30}\nTítulo: {titulo}\n\tISBN: {isbn}\n\tAutor: {autor}\n\tGênero: {genero}\n\tAno: {ano}\n\tAvaliação: {avaliacao} estrelas\n\tQuantidade: {quantidade}\n{'='*30}", value=i, variable=radio)
                    botao.grid(row=i+2, column=0, sticky = "w")
                def apagar():
                    for widget in excluir_frame.winfo_children():
                        if isinstance(widget, ctk.CTkRadioButton):
                            widget.grid_forget()
                    botao_excluir.grid_forget()
                    valor_selecionado = isbn_lista[radio.get()]
                    sql_delete = f"DELETE FROM livro WHERE isbn = '{valor_selecionado}'"
                    self.cursor.execute(sql_delete)
                    self.conexao.commit()
                    # Atualiza a interface após a exclusão
                    pesquisar()
                botao_excluir = ctk.CTkButton(excluir_frame, width=150, text="Excluir", command=apagar)
                botao_excluir.grid(row=30, column= 1,sticky = "ew")
            else:
                for widget in excluir_frame.winfo_children():
                    if isinstance(widget, ctk.CTkRadioButton):
                        widget.grid_forget()
                if botao_excluir:
                    botao_excluir.grid_forget()
                mensagem = ctk.CTkLabel(excluir_frame, text="Nenhum livro encontrado.", font=("segoe ui", 16))
                mensagem.grid(row=2, column=0, padx=100, sticky="ew")
        pesquisar_botao = ctk.CTkButton(excluir_frame, width=200, text="pesquisar", command=pesquisar)
        pesquisar_botao.grid(row=1, column=1, sticky = "ew")


        #Na aba "Lista de livros"
        lab_lista = ctk.CTkTextbox(listar_frame, width=650, height=400, font=("segoe ui", 14))
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
                livro_info += f"Quantidade: {quantidade}\n\n"
                resultado.append(livro_info)
            lab_lista.configure(state="normal")
            lab_lista.delete(1.0, ctk.END)  # Limpa o texto existente
            lab_lista.insert(ctk.END, '\n'.join(resultado))
            lab_lista.configure(state="disabled")

        def mostrar_livros_mais_1():
            #listar todos os livros na biblioteca 
            sql = "SELECT isbn, titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE quantidade > 1"
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
                livro_info += f"Quantidade: {quantidade}\n\n"
                resultado.append(livro_info)
            lab_lista.configure(state="normal")
            lab_lista.delete(1.0, ctk.END)  # Limpa o texto existente
            lab_lista.insert(ctk.END, '\n'.join(resultado))
            lab_lista.configure(state="disabled")

        botao_listar = ctk.CTkButton(listar_frame, text="Todos os livros existente", command=mostrar_livros)
        botao_listar_mais_1 = ctk.CTkButton(listar_frame, text="Mostrar os livros que pode realizar empréstimo", command=mostrar_livros_mais_1)
        botao_listar.grid(row=0, column=0, sticky = "w", padx = 60)
        botao_listar_mais_1.grid(row=0, column=1, sticky = "w")
        lab_lista.grid(row=1, column=0, sticky = "ew", pady=20, columnspan=2)
        

        #Na aba "Editar livro"
        nome_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite o título a ser editado...")
        nome_editar_entry.grid(row=0, column=0, sticky = "ew", columnspan=3, pady=5)
        autor_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite o nome do autor...")
        autor_editar_entry.grid(row=1, column=0, sticky = "ew", columnspan=3, pady=5)
        genero_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite o gênero...")
        genero_editar_entry.grid(row=2, column=0, sticky = "ew", columnspan=3, pady=5)
        isbn_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite o ISBN do livro a ser editado (obrigatório)...")
        isbn_editar_entry.grid(row=3, column=0, sticky = "ew", columnspan=3, pady=5)
        ano_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite o ano de publicação...")
        ano_editar_entry.grid(row=4, column=0, sticky = "ew", columnspan=3, pady=5)
        avaliacao_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite a avaliação de 0 a 10...")
        avaliacao_editar_entry.grid(row=5, column=0, sticky = "ew", columnspan=3, pady=5)
        quantidade_editar_entry = ctk.CTkEntry(editar_frame, width=300, placeholder_text="Digite a quantidade no estoque...")
        quantidade_editar_entry.grid(row=6, column=0, sticky = "ew", columnspan=3, pady=5)
        label_checkbox = ctk.CTkLabel(editar_frame, text="Selecione as checkbox que deseja modicar", font=("segoe ui", 14)).grid(row=7, column=2, columnspan=3, pady=10)
        checkvar1 = ctk.StringVar()
        checkvar2 = ctk.StringVar()
        checkvar3 = ctk.StringVar()
        checkvar4 = ctk.StringVar()
        checkvar5 = ctk.StringVar()
        checkvar6 = ctk.StringVar()
        checkbox_1 = ctk.CTkCheckBox(editar_frame, text="Nome", onvalue="Ativado", variable=checkvar1).grid(row=8, column=0, sticky = "ew")
        checkbox_2 = ctk.CTkCheckBox(editar_frame, text="Autor", onvalue="Ativado", variable=checkvar2).grid(row=8, column=1, sticky = "ew")
        checkbox_3 = ctk.CTkCheckBox(editar_frame, text="Gênero", onvalue="Ativado", variable=checkvar3).grid(row=8, column=2, sticky = "ew")
        checkbox_4 = ctk.CTkCheckBox(editar_frame, text="Ano", onvalue="Ativado", variable=checkvar4).grid(row=8, column=3, sticky = "ew")
        checkbox_5 = ctk.CTkCheckBox(editar_frame, text="Avaliação", onvalue="Ativado", variable=checkvar5).grid(row=8, column=4, sticky = "ew")
        checkbox_6 = ctk.CTkCheckBox(editar_frame, text="Quantidade", onvalue="Ativado", variable=checkvar6).grid(row=8, column=5, sticky = "ew")
        label_editar_frame = ctk.CTkLabel(editar_frame, text="", font=("segoe ui", 16))

        def editar():
            try:
                if len(isbn_editar_entry.get()) < 10:
                    label_editar_frame.configure(text="ISBN inválido")
                    return
                if checkvar1.get() == "Ativado" and len(nome_editar_entry.get())>1:
                    sql =f"UPDATE livro SET titulo = '{nome_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                if checkvar2.get() == "Ativado" and len(autor_editar_entry.get()) > 1:
                    sql =f"UPDATE livro SET autor = '{autor_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                if checkvar3.get() == "Ativado" and len(genero_editar_entry.get()) > 1:
                    sql =f"UPDATE livro SET genero = '{genero_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                if checkvar4.get() == "Ativado" and len(ano_editar_entry.get())>1:
                    sql =f"UPDATE livro SET ano = '{ano_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                if checkvar5.get() == "Ativado" and len(avaliacao_editar_entry.get())>=1:
                    sql =f"UPDATE livro SET avaliacao = '{avaliacao_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                if checkvar6.get() == "Ativado" and len(quantidade_editar_entry.get())>=1:
                    sql =f"UPDATE livro SET quantidade = '{quantidade_editar_entry.get()}' WHERE isbn = '{isbn_editar_entry.get()}'"
                    self.cursor.execute(sql)
                    self.conexao.commit()
                
                label_editar_frame.configure(text="Livro editado com sucesso!")
            except:
                label_editar_frame.configure(text="Dados insuficiente!")
            
        botao_editar = ctk.CTkButton(editar_frame, width=200, text="Editar", command=editar).grid(row=9, column=2, sticky = "ew", pady=30, columnspan=2)
        label_editar_frame.grid(row=10, column=2, sticky="ew", columnspan=2)


        #Na aba "Empréstimo/devolução de livro"
        email_entry = ctk.CTkEntry(emprestimo_devolucao_frame, width=300, placeholder_text="Digite o email do usuário...")
        isbn_empres_devol_entry = ctk.CTkEntry(emprestimo_devolucao_frame, width=300, placeholder_text="Digite o isbn...")
        quantidade_input_output_entry = ctk.CTkEntry(emprestimo_devolucao_frame, width=300, placeholder_text="Digite a quantidade...")
        tipo_var = ctk.StringVar(value="Escolha entrada/saída")
        tipo = ctk.CTkOptionMenu(emprestimo_devolucao_frame, width=300, values=["Entrada", "Saída"], variable=tipo_var)
        label_emprest_devol = ctk.CTkLabel(emprestimo_devolucao_frame, text="", font=("segoe ui", 16))

        def entrar_sair_livros():
            sql = "SELECT nome FROM users"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchone()
            if email_entry.get() not in resultados:
                label_emprest_devol.configure(text="Usuário inválido!")
                return
            if len(isbn_empres_devol_entry.get()) < 10:
                label_emprest_devol.configure(text="ISBN inválido!")
                return
            try:
                if tipo_var.get() == "Entrada":
                    sql = f"SELECT isbn_livro, quantidade_livros, id_usuario FROM emprestimos WHERE id_usuario = '{email_entry.get()}' AND isbn_livro = '{isbn_empres_devol_entry.get()}'"
                    self.cursor.execute(sql)
                    resultado = self.cursor.fetchone()
                    if not resultado:
                        label_emprest_devol.configure(text=f"Operação Inválida: {email_entry.get()} \nnão possui este livro!")
                    elif resultado:
                        isbn, quantidade_livro, nome_usuario = resultado
                        sql= f"SELECT quantidade FROM livro WHERE isbn = '{isbn_empres_devol_entry.get()}'"
                        self.cursor.execute(sql)
                        resultado_2 = self.cursor.fetchone()
                        quantidade = resultado_2[0]
                        if (quantidade_livro - int(quantidade_input_output_entry.get()) <= 0):
                            label_emprest_devol.configure(text="Operção Inválida: O usuário está devolvendo mais do que ele possui!")
                        else:
                            sql = f"UPDATE livro SET quantidade = {quantidade + int(quantidade_input_output_entry.get())} WHERE isbn='{isbn_empres_devol_entry.get()}'"
                            self.cursor.execute(sql)
                            sql2 = f"UPDATE emprestimos SET quantidade_livros = '{quantidade_livro - int(quantidade_input_output_entry.get())}' WHERE id_usuario = '{nome_usuario}' AND isbn_livro = '{isbn}'"
                            self.cursor.execute(sql2)
                            if (quantidade_livro - int(quantidade_input_output_entry.get()) == 0):
                                sql = f"DELETE FROM emprestimos WHERE isbn_livro ='{isbn}' AND id_usuario = '{nome_usuario}'"
                                self.cursor.fetchone(sql)
                            label_emprest_devol.configure("Registro atualizado com sucesso!")
                        self.conexao.commit()
                
                elif tipo_var.get() == "Saída":
                    sql = f"SELECT quantidade FROM livro WHERE isbn = '{isbn_empres_devol_entry.get()}'"
                    self.cursor.execute(sql)
                    resultado = self.cursor.fetchone()
                    if not resultado:
                        label_emprest_devol.configure(text="O livro não existe")
                    elif resultado:
                        quantidade = resultado[0]
                        if (quantidade - int(quantidade_input_output_entry.get()) <= 1):
                            label_emprest_devol.configure(text="Operação Inválida: a quantidade a ser removida é maior do que a biblioteca possui")
                        else:
                            sql = f"SELECT id_usuario, isbn_livro, quantidade_livros FROM emprestimos WHERE id_usuario = '{email_entry.get()}' AND isbn_livro = '{isbn_empres_devol_entry.get()}'"
                            self.cursor.execute(sql)
                            resultado_2 = self.cursor.fetchone()
                            if resultado_2:
                                id_usuario, isbn_livro, quantidade_livro = resultado_2
                                sql2 = f"UPDATE emprestimos SET quantidade_livros = '{quantidade_livro + int(quantidade_input_output_entry.get())}' WHERE id_usuario = '{email_entry.get()}' AND isbn_livro = '{isbn_empres_devol_entry.get()}'" 
                                self.cursor.execute(sql2)
                                sql2 = f"UPDATE livro SET quantidade = '{quantidade - int(quantidade_input_output_entry.get())}' WHERE isbn = '{isbn_empres_devol_entry.get()}'"
                                self.cursor.execute(sql2)
                                self.conexao.commit()
                                label_emprest_devol.configure(text="Registro atualizado com sucesso!")
                            else:
                                sql2 = f"INSERT INTO `emprestimos` (`id_usuario`, `isbn_livro`, `quantidade_livros`) VALUES ('{email_entry.get()}', '{isbn_empres_devol_entry.get()}', '{int(quantidade_input_output_entry.get())}')"
                                self.cursor.execute(sql2)
                                self.conexao.commit()

                                sql2 = f"UPDATE livro SET quantidade = '{quantidade - int(quantidade_input_output_entry.get())}' WHERE isbn = '{isbn_empres_devol_entry.get()}'"
                                self.cursor.execute(sql2)
                                self.conexao.commit()
                                label_emprest_devol.configure(text="Novo registro criado com sucesso!")
            except:
                label_emprest_devol.configure("Dados insuficiente")
        botao_emprest_devol = ctk.CTkButton(emprestimo_devolucao_frame, width=200, text="Inserir", command=entrar_sair_livros)

        email_entry.grid(row=0, column=0, sticky="w", padx = 150)
        isbn_empres_devol_entry.grid(row=1, column=0, sticky="w", padx = 150)
        quantidade_input_output_entry.grid(row=2, column=0, sticky="w", padx = 150)
        tipo.grid(row=3, column=0, pady=10, sticky="w", padx = 150)
        botao_emprest_devol.grid(row=4, column=0, pady=30, sticky="w", padx = 200)
        label_emprest_devol.grid(row=5, column=0, sticky="w", padx = 170)


        #Na aba "Pesquisa"
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
                livro_info += f"Quantidade: {quantidade}\n\n"
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
        label_nome = ctk.CTkLabel(minha_conta_frame, text="Nome do administrador", font=("segoe ui", 20)).pack(pady=2)
        novo_nome_entry = ctk.CTkEntry(minha_conta_frame, width=200, placeholder_text=f"{self.nome}")
        novo_nome_entry.pack()
        label_senha = ctk.CTkLabel(minha_conta_frame, text="Senha do administrador", font=("segoe ui", 20)).pack(pady=2)
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