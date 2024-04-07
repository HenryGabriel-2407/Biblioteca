from livros import Livro
from biblioteca import Biblioteca

armazem = Biblioteca()
estrelas = '\U0001F31F'

outras_pessoas = Livro("Outras Pessoas", "C. J. Tudor", 9788551006504, "Suspense", 2020, (estrelas * 10), 3)
hp1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 9788532523051, "Ficção", 1997, (estrelas * 8), 1)
hp2 = Livro("Harry Potter e o Cálice de Fogo", "J. K. Rowling", 9788532530813, "Ficção", 2000, (estrelas * 9), 0)
crime_castigo = Livro("Crime e Castigo", "Fiódor Dostoviésk", 9788420741468, "Suspense", 1866, (estrelas * 8), 2)
o_jogador = Livro("O Jogador", "Fiódor Dostoviésk", 9788420635491, "Drama", 1866, (estrelas * 6), 1)
o_principe = Livro("O Príncipe","Nicolau Maquiavel", 9788573266764, "Clássico", 1532, (estrelas * 7), 4)

armazem.remove_livro()
armazem.add_livro(outras_pessoas)
armazem.add_livro(hp1)
armazem.add_livro(hp2)
armazem.add_livro(crime_castigo)
armazem.add_livro(o_jogador)
armazem.add_livro(o_principe)

armazem.listar_livros()
armazem.pesquisa_livro()
armazem.remove_livro()
armazem.listar_livros()
armazem.livros_disponiveis()