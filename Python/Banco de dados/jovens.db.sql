--
-- Arquivo gerado com SQLiteStudio v3.4.4 em seg nov 11 16:08:09 2024
--
-- Codificação de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: jovens
CREATE TABLE IF NOT EXISTS jovens (
    Id       INTEGER    PRIMARY KEY
                        CONSTRAINT [AUTOINCREMENT] UNIQUE,
    nome     TEXT (100),
    endereço TEXT (150) 
);


-- Índice: sqlite_autoindex_jovens_1
CREATE UNIQUE INDEX IF NOT EXISTS sqlite_autoindex_jovens_1 ON jovens (
    Id COLLATE BINARY
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
