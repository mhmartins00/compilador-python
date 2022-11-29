## Introdução Compilador Python

Este projeto é um compilador escrito em python.

Clone este repositorio git em seu computador

 > git clone https://github.com/mhmartins00/compilador-python.git

 > git checkout main

 > git checkout -b feature/sua_Nova_Feature

## Configuration

Crie um ambiente virtual
 > python -m venv .env

Ative este ambiente virtual
 > .env/Scripts/activate

## Installation

Instale as dependencias
 > pip install -r requirements.txt

Depois rode o seguinte comando para compilar o arquivo comp.txt
 > python main.py comp.txt 


-----------------
Duvidas:

- A declaração das variáveis somente no inicio do programa ou também pode ser depois de comandos (dentro de blocos ou outros locais)?
-ok--ex: TANTO FAZ
int a;

if(a>b){
    int c;
    a = c;
}

int d;


- Comando de atribuição somente dentro do bloco de IF e SWITCH, ou pode estar fora?
--ex: SÓ DENTRO
int a;

a = 2;

if(a>b){
    int c;
    a = c;
}

d = 3;

- Podem existir multiplos comandos dentro de blocos?
--ex: PODE TER
int a, b;

if(a>b){
    a = b;
    b = a;
}

- Comando IF pode estar com bloco de <comandos> vazio?
--ex: COM COMANDOS
int a, b;
--char a[10] fazer

if(a>b){}