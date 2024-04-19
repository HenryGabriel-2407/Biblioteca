class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, ano: int, avaliacao: str, quantidade: int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano = ano
        #self.__isbn = isbn --> problema a ser resolvido com MySql
        self.__avaliacao = avaliacao
        self.__quantidade = quantidade