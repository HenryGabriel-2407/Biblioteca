use teste;
CREATE TABLE emprestimos (
    id_usuario VARCHAR(40),
    isbn_livro VARCHAR(15),
    quantidade_livros INT default 0
);