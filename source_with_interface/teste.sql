use teste;
CREATE TABLE `livro` (
  isbn VARCHAR(15) PRIMARY KEY,
  titulo VARCHAR(40) NOT NULL,
  autor VARCHAR(30) NOT NULL,
  genero VARCHAR(15) NOT NULL,
  ano INT NOT NULL,
  avaliacao INT NOT NULL,
  quantidade INT NOT NULL
)default charset = utf16;
SELECT * FROM livro;
DELETE FROM livro WHERE isbn = ""