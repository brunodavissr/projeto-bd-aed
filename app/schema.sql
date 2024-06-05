CREATE TABLE IF NOT EXISTS "produtos" (
    "codigo" INTEGER PRIMARY KEY,
    "nome" TEXT NOT NULL,
    "descricao" TEXT NOT NULL,
    "preco" REAL NOT NULL,
    "imagem" TEXT NOT NULL
);