from livros import Livro
from biblioteca import Biblioteca

armazem = Biblioteca()

titulo = str(input("Digite o título de livro: "))
autor = str(input("Digite o nome do autor(a): "))
genero = str(input("Digite o gênero: "))
ano = int(input("Digite o ano: "))
avaliacao = int(input("Digite a nota de avaliação [0, 10]: "))
quantidade = int(input("Digite a quantidade: "))

livro_novo = Livro(titulo, autor, genero, ano, avaliacao, quantidade)
#armazem.remove_livro()
armazem.add_livro(livro_novo)
armazem.listar_livros()
