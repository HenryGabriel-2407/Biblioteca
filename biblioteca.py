from livros import Livro
from typing import Type

class Biblioteca():
    def __init__(self) -> None: #Construtor
        self.__livro = []

    def add_livro(self, livro: Type[Livro]) -> None: #Adicionando livro
        self.__livro.append(livro)

    def remove_livro(self) -> None: #Removendo livro
        if self.__livro == []: #se a biblioteca estiver vazia
            print("Não há livros para remover\n")
            return
        busca = int(input("Digite o ISBN do livro:")) #quando a biblioteca estiver elementos
        for book in self.__livro:
            if busca == book._Livro__isbn:
                nome_removido = book._Livro__isbn
                self.__livro.remove(book)
                print(f"O {nome_removido} foi removido com sucesso!\n")
                return
        print("Livro não existe na biblioteca.") #quando o livro não está na lista
        
    def listar_livros(self) -> None: #listar todos os livros na biblioteca
        for book in self.__livro:
            if book._Livro__quantidade < 1:
                continue
            print(f"{book.info_livro()}\n")
        print(" ")
    
    def livros_disponiveis(self) -> None: #listar todos os livros se a quantidade for maior do que 1
        for book in self.__livro:
            if book._Livro__quantidade > 1:
                print(book.info_livro())
                print(f"\tQuantidade: {book._Livro__quantidade}\n")
            elif book._Livro__quantidade == 1:
                print(book.info_livro())
                print("\tQuantidade: 1 (Apenas para o uso local)\n")
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
                print(f"{book.info_livro()}\n")
        
    def __pesquisa_autor(self) -> None:
        busca = str(input("Digite o nome do autor: "))
        for book in self.__livro:
            if busca.lower() in book._Livro__autor.lower():
                print(f"{book.info_livro()}\n")

    def __pesquisa_genero(self) -> None:
        busca = str(input("Digite o gênero: "))
        for book in self.__livro:
            if busca.lower() in book._Livro__genero.lower():
                print(f"{book.info_livro()}\n")

    def __pesquisa_ano(self) -> None:
        busca = int(input("Digite o ano: "))
        for book in self.__livro:
            if busca == book._Livro__ano:
                print(f"{book.info_livro()}\n")

    def __pesquisa_ISBN(self) -> None:
        busca = int(input("Digite o ISBN: "))
        for book in self.__livro:
            if busca == book._Livro__isbn:
                print(f"{book.info_livro()}\n")

    def __pesquisa_avaliacao(self) -> None:
        busca = int(input("Digite a quantidade de estrela [0 a 10]: "))
        for book in self.__livro:
            if busca == len(book._Livro__avaliacao):
                print(f"{book.info_livro()}\n")

