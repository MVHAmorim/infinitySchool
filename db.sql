
PRAGMA foreign_keys=ON;

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS cardapio (
    codigo TEXT PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL
);

INSERT INTO cardapio (codigo, nome, descricao) VALUES 
('hamburguer', 'hamburguer', 'Burguers das casa'),
('fritura', 'fritura', 'Frituras das casa'),
('bebida', 'bebida', 'Bebidas das casa');

CREATE TABLE IF NOT EXISTS produto (
    codigo TEXT PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    restricao TEXT NOT NULL,
    cardapio TEXT NOT NULL,

    FOREIGN KEY (cardapio) references cardapio(codigo)
    ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS usuario (
    nome_usuario TEXT PRIMARY KEY NOT NULL,
    nome_completo TEXT NOT NULL UNIQUE,
    cargo TEXT NOT NULL,
    salt_senha BLOB NOT NULL,
    hash_senha BLOB NOT NULL
);

INSERT INTO produto (codigo, nome, descricao, preco, restricao, cardapio) VALUES 
('hamburguer', 'Hamburguer', 'X-Salada', 15.90, 'padrão', 'hamburguer'),
('batata-frita', 'Batata Frita', 'Batata Frita Rústica', 19.90, 'vegano', 'fritura'),
('fanta-laranja', 'Fanta Laranja', 'Refrigerante sabor laranja', 7.90, 'padrão', 'bebida'),
('nugget', 'Nugget', 'mini empanados de frango com 6 unidades', 11.90, 'padrão', 'fritura');

COMMIT;