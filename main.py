#  README
#  Para executar basta estar no mesmo diretório do arquivo main.py e digitar > python main.py.
# 1) número de telefone VARIAVEL = 00900000000 [obrigatorio o comeco com o 9]
# 2) placas de carro = xxx0000 | XXX000 [3 letras seguidas por 4 numeros]
# 3) TIPO = 123.456.789-01 [qualquer numero 11 digitos mas com mascara] 
# 4) números reais = 123.5555555 [de qualquer tamanho]
# 5) tags html = <qualquer_coisa INCLUSIVE com espaço = @>
# 6) URL de páginas = HTTP:// | http:// | HTTPS:// | https:// [qualquer coisa seguida]
# 7) palavras = aass ou AAAS ou asAD [sem numeros e simbolos mas com acentos]
# 8) cnpj = 12345678901234 [qualquer numero 14 digitos sem mascara]
# 9) identificadores ling. C = [ids do C int, float, etc...]

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TIPO',
    'VARIAVEL',
)

# REGEX PARA VALIDACOES
# t_VARIAVEL = r'^[0-9]{2}9[0-9]{8}$'
# t_TIPO = r'^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$'
# t_PLACA = r'^[a-zA-Z]{3}[0-9]{4}$'
# t_URL = r'^([hH][tT][tT][pP][sS]?[:][\\/]{2})+([a-zA-Z0-9 -_./:=&"%+?@\$!])+$'
# t_CNPJ = r'^[0-9]{14}$'
# t_PALAVRA_RESERVADA_C = r'^(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|printf)$'
# t_PALAVRA = r'^[a-zA-ZÀ-ÿ \s]+$'
# t_NUMERO_REAL = r'^[0-9]+.[0-9]+$'
# t_TAG_HTML =r'^<[a-zA-Z0-9 -_./:=&"%+?@\$! \s]+>$'

t_ignore = ' \t'

# Definicao das funcoes com as expressoes regulares
def t_TIPO( t ) :
    # r'\b(int|float|double|char)\s+(\w+)\s*\([^)]*\)\s*{
    r'^(int|float|char)\s+([_a-zA-Z])+;'
    return t

def t_error( t ):
  t.lexer.skip( 1 )

lexer = lex.lex()

# Definição das funcoes para validacao de tokens
def p_tipo( p ):
    'expr : TIPO'
    p[0] = f'TIPO VÁLIDO'

# def p_variavel( p ):
#     'expr : VARIAVEL'
#     p[0] = f'VARIAVEL VÁLIDO'

# def p_declaracao( p ):
#     'expr : TIPO VARIAVEL'
#     p[0] = f'DECLARACAO VALIDA'


def p_error( p ):
    print("Token inválido")

parser = yacc.yacc()

# Digitar tokens para validar no console
escape = ""
print("#---------------------------#")
print("|     Testes de tokens      |")
print("|                           |")
print("| *Para sair digite 's'     |")
print("#---------------------------#\n")
while escape != "s":
    token = input("Digite o token: ")
    res = parser.parse(token)
    print(f"Token = {res}")
    print("_________________________________________\n")
    escape = input("Parar? [s / n]: ")
    print("_________________________________________\n")
