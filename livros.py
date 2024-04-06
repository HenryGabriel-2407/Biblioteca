class Livro:
    def __init__(self, titulo: str, autor: str, isbn: int, genero: str, ano: int, avaliacao: str) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano = ano
        self.__isbn = isbn
        self.__avaliacao = avaliacao
    
    def info_livro(self):
        info = f"Livro: {self.__titulo}\n"
        info += f"\tAutor: {self.__autor}\n"
        info += f"\tGênero: {self.__genero}\n"
        info += f"\tAno: {self.__ano}\n"
        info += f"\tISBN: {self.__isbn}\n"
        info += f"\tAvaliação: {self.__avaliacao}\n"
        return info