CREATE TABLES "produtos" (
    "codigo" INTEGER PRIMARY KEY,
    "nome" TEXT NOT NULL,
    "descricao" TEXT NOT NULL,
    "preco" NUMERIC NOT NULL,
    "imagem" TEXT NOT NULL
);