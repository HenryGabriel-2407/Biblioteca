from livros import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()
print("=======BIBLIOTECA UNIAVAN=======\n")
while True:
    escolha = int(input("[1]- Adicionar um livro \n[2]- Remover um livro \n[3]- Pesquisar \n[4]- Editar \n[5]- Listar todos os livros \n[6]- Listar os livros disponíveis \n[7]- Empréstimo \n[8]- Devolução \n[9]- Sair do Sistema \n--->"))
    if escolha == 1:
        titulo = str(input("Digite o título de livro: "))
        autor = str(input("Digite o nome do autor(a): "))
        genero = str(input("Digite o gênero: "))
        #ISBN não está funcionando ainda, por isso, tente por nome completo do livro
        ano = int(input("Digite o ano: "))
        avaliacao = int(input("Digite a nota de avaliação [0, 10]: "))
        quantidade = int(input("Digite a quantidade: "))
        livro_novo = Livro(titulo, autor, genero, ano, avaliacao, quantidade)
        biblioteca.add_livro(livro_novo)
    elif escolha == 2:
        biblioteca.remover_livro()
    elif escolha == 3:
        biblioteca.pesquisar_livro()
    elif escolha == 4:
        biblioteca.editar_livro()
    elif escolha == 5:
        biblioteca.listar_livros()
    elif escolha == 6:
        biblioteca.livros_disponiveis()
    elif escolha == 7:
        biblioteca.emprestimo_livro()
    elif escolha == 8:
        biblioteca.devolucao_livro()
    elif escolha == 9:
        break
    else:
        continue