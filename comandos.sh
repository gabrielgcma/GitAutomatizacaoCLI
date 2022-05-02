#!/bin/bash

function criar() {
    source .env
    # quando este bash for executado, ele chamará o arquivo criar.py que, por sua vez, executará a função criar definida dentro do arquivo python:
    python3 create.py $1
    cd $CAMINHO$1
    git init
    git remote add origin https://github.com/$USUARIO/$1.git
    touch README.md
    git add .
    git commit -m "Primeiro commit"
    git push -u origin master
    # opcional: abrir instância do VSCode para começar o projeto:
    # code . 
}
