CREATE DATABASE IF NOT EXISTS sistema_revisoes_db;
USE sistema_revisoes_db;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR (100),
    senha VARCHAR (100)
);

CREATE TABLE IF NOT EXISTS materias(
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    nome VARCHAR(100),
    conteudos_registrados VARCHAR (100),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS revisoes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    materia_id INT,
    descricao_revisao VARCHAR(255) NOT NULL,
    status ENUM('pendente', 'feita') DEFAULT 'pendente',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_revisao DATETIME NOT NULL,
    FOREIGN KEY(materia_id) REFERENCES materias(id) ON DELETE CASCADE
);


