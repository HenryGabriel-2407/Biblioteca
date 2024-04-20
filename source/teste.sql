create database teste;
use teste;
CREATE TABLE `livro` (
  `id` SERIAL PRIMARY KEY,
  `titulo` VARCHAR(40) NOT NULL,
  `autor` VARCHAR(30) NOT NULL,
  `genero` VARCHAR(15) NOT NULL,
  `ano` INT,
  `avaliacao` INT,
  `quantidade` INT
);