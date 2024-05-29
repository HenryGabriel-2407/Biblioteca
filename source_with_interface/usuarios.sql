use teste;
CREATE TABLE `users`(
    nome VARCHAR(40) NOT NULL default "usuario",
    email VARCHAR(40) PRIMARY KEY,
    senha VARCHAR(20) default "senha",
    tipo ENUM("USER", "ADMIN")
);
