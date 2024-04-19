from livros import Livro
from typing import Type
import mysql.connector

conexao = mysql.connector.connect(host="localhost", user="root", passwd="@NikolaTesla369", database="bd")
cursor = conexao.cursor()

class Biblioteca():
    def add_livro(self, livro: Type[Livro]) -> None:
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

    def listar_livros(self) -> None: #listar todos os livros na biblioteca
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
                
    def livros_disponiveis(self) -> None: #listar todos os livros se a quantidade for maior do que 1
        sql = "SELECT * FROM livro WHERE quantidade > 1"
        cursor.execute(sql)
        for titulo, autor, genero, ano, avaliacao, quantidade in cursor: 
            estrelas = '\U0001F31F' * int(avaliacao)
            print(f"Nome do Livro: {titulo}")
            print(f"\tAutor(a): {autor}")
            print(f"\tGênero: {genero}")
            print(f"\tAno: {ano}")
            print(f"\tAvaliação: {estrelas}")
            print(f"\tQuantidade: {quantidade}")
            
    def remover_livro(self) -> None:
        nome_livro = str(input("Digite o nome do livro a ser excluído: "))
        sql = f"DELETE FROM livro WHERE titulo = {nome_livro}"
        cursor.execute(sql)
        conexao.commit()

    def pesquisar_livro(self) -> None:
        nome_livro = str(input("Digite o nome do livro: "))
        sql = f"SELECT * FROM livro WHERE  titulo LIKE {nome_livro}"
        cursor.execute(sql)
        for titulo, autor, genero, ano, avaliacao, quantidade in cursor: 
            estrelas = '\U0001F31F' * int(avaliacao)
            print(f"Nome do Livro: {titulo}")
            print(f"\tAutor(a): {autor}")
            print(f"\tGênero: {genero}")
            print(f"\tAno: {ano}")
            print(f"\tAvaliação: {estrelas}")
            print(f"\tQuantidade: {quantidade}")

    def editar_livro(self) -> None:
        pass