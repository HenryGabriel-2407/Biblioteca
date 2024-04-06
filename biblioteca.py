from livros import Livro
from typing import Type
class Biblioteca():
    def __init__(self) -> None:
        self.__livro = []

    def add_livro(self, livro: Type[Livro]) -> None:
        self.__livro.append(livro)

    def remove_livro(self) -> None:
        if self.__livro == []:
            print("Não há livros para remover\n")
            return
        livro_removido = self.__livro.pop()
        print(f"{livro_removido._Livro__titulo} foi removido com sucesso!\n")
        
    def listar_livros(self) -> None:
        for book in self.__livro:
            print(book.info_livro())
        print(" ")

    def pesquisa_livro(self) -> None:
        opcao = int(input("Pesquisar por...\n [1]título do livro\n [2]Autor\n [3]Gênero\n [4]Ano\n [5]ISBN\n [6]Avaliação\n Resposta: "))
        if opcao == 1: 
            self.__pesquisa_titulo()
        elif opcao == 2:    
            self.__pesquisa_autor()
        elif opcao == 3:    
            self.__pesquisa_genero()
        elif opcao == 4:    
            self.__pesquisa_ano()
        elif opcao == 5:    
            self.__pesquisa_ISBN()
        elif opcao == 6:    
            self.__pesquisa_avaliacao()
        else:   
            print("Opção Inválida.")

    def __pesquisa_titulo(self) -> None:
        busca = str(input("Digite o nome do livro: "))
        for book in self.__livro:
            if busca.lower() in book._Livro__titulo.lower():
                print(book.info_livro())
        
    def __pesquisa_autor(self) -> None:
        busca = str(input("Digite o nome do autor: "))
        for book in self.__livro:
            if busca.lower() in book._Livro__autor.lower():
                print(book.info_livro())

    def __pesquisa_genero(self) -> None:
        busca = str(input("Digite o gênero: "))
        for book in self.__livro:
            if busca.lower() in book._Livro__genero.lower():
                print(book.info_livro())

    def __pesquisa_ano(self) -> None:
        busca = int(input("Digite o ano: "))
        for book in self.__livro:
            if busca == book._Livro__ano:
                print(book.info_livro())

    def __pesquisa_ISBN(self) -> None:
        busca = int(input("Digite o ISBN: "))
        for book in self.__livro:
            if busca == book._Livro__isbn:
                print(book.info_livro())

    def __pesquisa_avaliacao(self) -> None:
        busca = int(input("Digite a quantidade de estrela [0 a 10]: "))
        for book in self.__livro:
            if busca == len(book._Livro__avaliacao):
                print(book.info_livro())

