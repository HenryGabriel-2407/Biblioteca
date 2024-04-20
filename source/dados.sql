create database bd;
use bd;
CREATE TABLE `user` (
  `id` SERIAL PRIMARY KEY,
  `name` VARCHAR(30) NOT NULL,
  `cpf` VARCHAR(20) NOT NULL 
);
INSERT INTO `user` (`name`, `cpf`) VALUES ('Leta Lestrange', '012.236.987-44'), ('Newt Scamander', '021.545.258-55'),
('Hermione Granger', '024.547.658-77');