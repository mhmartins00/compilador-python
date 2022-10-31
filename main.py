
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'DECLARACAO',
)

t_ignore = ' \t'

# Definicao das funcoes com as expressoes regulares
def t_DECLARACAO( t ) :
    r'^(int|float|char)\s+([_a-zA-Z])+[a-zA-Z0-9]*([,]?\s[_a-zA-Z])*[;]{1}$'
    return t

def t_error( t ):
  t.lexer.skip( 1 )

lexer = lex.lex()

# Definição das funcoes para validacao de tokens
def p_declaracao( p ):
    'expr : DECLARACAO'
    p[0] = f'DECLARACAO VÁLIDA'

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

