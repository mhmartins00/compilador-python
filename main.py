import sys
sys.path.append("../..")
import ply.lex as lex
import ply.yacc as yacc

#################### ANALISADOR LEXICO ####################
reserved = {
    'char'  : 'CHAR',
    'int'   : 'INT',
    'float' : 'FLOAT'
}

tokens = ['IDEN', 'VIRGULA', 'PONTOVIRGULA']+ list(reserved.values())

# caraceres ignorados [nova linha, espaco em branco, tab]
t_ignore = '\n \t'

# expressao regular para tokens simples
t_VIRGULA = r','
t_PONTOVIRGULA = r';'

'''
t_CHAR      = r'char'
t_INT       = r'int'
t_FLOAT     = r'float'
'''

# expressao rewgular para identificadores
def t_IDEN(t) :
    r'[_a-zA-Z]+[a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#################### ANALISADOR SINTATICO E REGRAS ####################
# criamos as regras bem especificas para facilitar a manutencao e o desenvolvimento futuro

def p_fim_instrucao(p):
    'fim : PONTOVIRGULA'

def p_defincao_tipo(t):
    '''tipo : CHAR
            | INT
            | FLOAT
    '''
    t[0]=t[1]

def p_variavel(t):
    'variavel : IDEN'
    t[0]=t[1]

# inicio
def p_programa(t):
    'programa : declaracao_var'
    t[0]=t[1]

# para listas de declaracao [int a; int b;]
def p_declaracao_var(t):
    '''declaracao_var : tipo sequencia_var fim
                      | tipo sequencia_var fim declaracao_var
    ''' 
    t[0]=t[1]

# sequencia [a,b,c]
def p_sequencia_var(t):
    '''sequencia_var : variavel
                     | variavel VIRGULA sequencia_var
    '''
    t[0]=t[1]

def p_error(t):
    print('Erro ao compilar!')
    print('Caractere ilegal: %s' % t.value)
    # raise TypeError('parser error: %s' % t.value)

# definicao para o start das regras
parser = yacc.yacc(start='programa')

#################### INICIO DO PROGRAMA COM LEITURA DE ARQUIVO ####################

print("#---------------------------#")
print("|   Compilador DCM / MHG    |")
print("|                           |")
print("| *Digite o nome do arquivo |")
print("| * no comando              |")
print("#---------------------------#\n")

# com leitura de arquivo direto no comando pelo terminal
# ex: "python main.py comp.txt"
if len(sys.argv) < 2:
    print ("Executar : python main.py comp.txt")
    raise SystemExit
elif len(sys.argv) == 2:
        filename = sys.argv[1]
else:
    print ("Opcao invalida '%s'" % sys.argv[1])
    raise SystemExit

arquive = open(filename).read()

parser.parse(arquive)
print ("Compilador finalizado...\n")