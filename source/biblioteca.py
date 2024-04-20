from livros import Livro
from typing import Type
import mysql.connector

conexao = mysql.connector.connect(host="localhost", user="root", passwd="@NikolaTesla369", database="bd")
cursor = conexao.cursor()

class Biblioteca():
    def add_livro(self, livro: Type[Livro]) -> None: #STATUS: FUNCIONANDO
        # Primeiro vai verificar se o livro já existe no banco
        titulo_novo, autor_novo, genero_novo = str(livro._Livro__titulo), livro._Livro__autor, livro._Livro__genero
        sql = f"SELECT titulo, autor, genero FROM livro WHERE titulo = '{titulo_novo}' AND autor = '{autor_novo}' AND genero = '{genero_novo}'"
        cursor.execute(sql)
        if cursor.fetchone():
            print("Esse livro já está na biblioteca")
            return
        #Se o livro não existe na biblioteca
        sql = f"INSERT INTO `livro` (`titulo`, `autor`, `genero`, `ano`, `avaliacao`, `quantidade`) VALUES ('{livro._Livro__titulo}', '{livro._Livro__autor}', '{livro._Livro__genero}', {livro._Livro__ano}, {livro._Livro__avaliacao}, {livro._Livro__quantidade})"
        cursor.execute(sql)
        print("Livro inserido no banco de dados com sucesso.")
        conexao.commit()


    def listar_livros(self) -> None: #STATUS: FUNCIONANDO
        #listar todos os livros na biblioteca 
        sql = "SELECT titulo, autor, genero, ano, avaliacao, quantidade FROM livro"
        cursor.execute(sql)
        for (titulo, autor, genero, ano, avaliacao, quantidade) in cursor:
            estrelas = str('\U0001F31F' * int(avaliacao))
            print(f"Nome do Livro: {titulo}")
            print(f"\tAutor(a): {autor}")
            print(f"\tGênero: {genero}")
            print(f"\tAno: {ano}")
            print(f"\tAvaliação: {estrelas}")
            print(f"\tQuantidade: {quantidade}\n")


    def livros_disponiveis(self) -> None: #STATUS: FUNCIONANDO
        #listar todos os livros se a quantidade for maior do que 1
        sql = "SELECT titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE quantidade > 1"
        cursor.execute(sql)
        for (titulo, autor, genero, ano, avaliacao, quantidade) in cursor:
            estrelas = str('\U0001F31F' * int(avaliacao))
            print(f"Nome do Livro: {titulo}")
            print(f"\tAutor(a): {autor}")
            print(f"\tGênero: {genero}")
            print(f"\tAno: {ano}")
            print(f"\tAvaliação: {estrelas}")
            print(f"\tQuantidade: {quantidade}\n")


    def remover_livro(self) -> None: #STATUS: FUNCIONANDO
        nome_livro = str(input("Digite o nome do livro a ser excluído: "))
        try:
            sql = f"DELETE FROM livro WHERE titulo = '{nome_livro}'"
            cursor.execute(sql)
            conexao.commit()
        except:
            print("Erro, tente novamente...")


    def pesquisar_livro(self) -> None: #STATUS: FUNCIONANDO
        escolha = int(input("Digite [1]Título do Livro / [2]Autor / [3]Gênero \nResposta: "))
        if escolha == 1:
            nome = str(input("Digite o nome do livro: "))
            completar_comando = f"titulo = '{nome}'"
        elif escolha == 2:
            nome_autor = str(input("Digite o autor do livro: "))
            completar_comando = f"autor = '{nome_autor}'"
        elif escolha == 3: 
            nome_genero = str(input("Digite o gênero do livro: "))
            completar_comando = f"genero = '{nome_genero}'"
        else:
            print("Erro, tente novamente...")
            return
        try:
            sql = f"SELECT titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE {completar_comando}"
            cursor.execute(sql)
            for (titulo, autor, genero, ano, avaliacao, quantidade) in cursor:
                estrelas = str('\U0001F31F' * int(avaliacao))
                print(f"Nome do Livro: {titulo}")
                print(f"\tAutor(a): {autor}")
                print(f"\tGênero: {genero}")
                print(f"\tAno: {ano}")
                print(f"\tAvaliação: {estrelas}")
                print(f"\tQuantidade: {quantidade}\n")
        except Exception as e:
            print("Erro: ", e)


    def editar_livro(self) -> None: #STATUS: FUNCIONANDO
        pesquisar_nome = str(input("Digite o nome do livro: "))
        try:
            sql = f"SELECT titulo, autor, genero, ano, avaliacao, quantidade FROM livro WHERE titulo = '{pesquisar_nome}'"
            cursor.execute(sql)
            for (titulo, autor, genero, ano, avaliacao, quantidade) in cursor:
                estrelas = str('\U0001F31F' * int(avaliacao))
                print(f"Nome do Livro: {titulo}")
                print(f"\tAutor(a): {autor}")
                print(f"\tGênero: {genero}")
                print(f"\tAno: {ano}")
                print(f"\tAvaliação: {estrelas}")
                print(f"\tQuantidade: {quantidade}\n")
            titulo_modificado = str(input("Digite o título: "))
            autor = str(input("Digite o nome do autor(a): "))
            genero = str(input("Digite o gênero: "))
            ano = int(input("Digite o ano: "))
            avaliacao = int(input("Digite a avaliação [0, 10]: "))
            quantidade = int(input("Digite a quantidade: "))
            sql = f"UPDATE livro SET titulo = '{titulo_modificado}', autor = '{autor}', genero = '{genero}', ano = {ano}, avaliacao = {avaliacao}, quantidade = {quantidade} WHERE titulo = '{pesquisar_nome}'"
            cursor.execute(sql)
            print("Modificado!")
            conexao.commit()
        except:
            print("Erro, tente novamente...")
    
    def emprestimo_livro(self):
        pesquisar_nome = str(input("Digite o título do livro: "))
        try:
            sql = f"SELECT * FROM livro WHERE titulo = '{pesquisar_nome}'"
            cursor.execute(sql)
            for (titulo, autor, genero, ano, avaliacao, quantidade) in cursor:
                estrelas = str('\U0001F31F' * int(avaliacao))
                print(f"Nome do Livro: {titulo}")
                print(f"\tAutor(a): {autor}")
                print(f"\tGênero: {genero}")
                print(f"\tAno: {ano}")
                print(f"\tAvaliação: {estrelas}")
                print(f"\tQuantidade: {quantidade}")
            levar_ou_nao = str(input("Deseja levar? [Y/N]: "))
            if levar_ou_nao == 'Y' and quantidade > 1:
                sql = f"UPDATE livro SET quantidade = {quantidade - 1} WHERE titulo = '{pesquisar_nome}'"
                cursor.execute(sql)
                conexao.commit()
            elif levar_ou_nao == "N":
                print("OK!")
            else:
                print(f"Infelizmente não poderá levar o {pesquisar_nome}")
        except:
            print("Erro, tente novamente...")


    def devolucao_livro(self):
        pesquisar_nome = str(input("Digite o título do livro: "))
        try:
            sql = f"SELECT quantidade FROM livro WHERE titulo = '{pesquisar_nome}'"
            cursor.execute(sql)

