# COMPILADORES - ETAPA 1
# NOMES: DOUGLAS MOELLER, MURILLO MARTINS
import sys
sys.path.append("../..")
import ply.lex as lex
import ply.yacc as yacc

#################### ANALISADOR LEXICO ####################
reserved = {
    'char'  : 'CHAR',
    'int'   : 'INT',
    'float' : 'FLOAT',
    'if'    : 'IF',
    'else'  : 'ELSE',
    'switch': 'SWITCH',
    'case'  : 'CASE',
    'default': 'DEFAULT'
}

tokens = ['IDEN', 'NUM', 'VIRGULA', 'PONTOVIRGULA', 'DOISPONTOS', 'EPAREN', 'DPAREN', 'ECHAVE', 'DCHAVE', 'IGUAL', 'DIFERENTE', 'MENORIGUAL', 'MAIORIGUAL', 'MENOR', 'MAIOR', 'MAIS', 'MENOS', 'MULTIPLICA', 'DIVIDE', 'MAISMAIS', 'MENOSMENOS', 'RECEBE', 'MAISIGUAL', 'MENOSIGUAL', 'MULTIGUAL', 'DIVIDEIGUAL']+ list(reserved.values())

# caraceres ignorados [nova linha, espaco em branco, tab]
t_ignore = '\n \t'

# expressao regular para tokens simples
t_VIRGULA       = r','
t_PONTOVIRGULA  = r';'
t_DOISPONTOS    = r':'
t_EPAREN        = r'\('
t_DPAREN        = r'\)'
t_ECHAVE        = r'\{'
t_DCHAVE        = r'\}'

# Operadores Relacionais 
t_IGUAL         = r'=='
t_DIFERENTE		= r'!='
t_MENORIGUAL	= r'<='
t_MAIORIGUAL	= r'>='
t_MENOR			= r'<'
t_MAIOR			= r'>'

# Operadores Matemáticos
t_MAIS   		= r'\+'
t_MENOS			= r'-'
t_MULTIPLICA	= r'\*'
t_DIVIDE		= r'/'
t_MAISMAIS		= r'\++'
t_MENOSMENOS	= r'/--'

# Operadores de atribuição
t_RECEBE		= r'='
t_MAISIGUAL		= r'\+='
t_MENOSIGUAL	= r'-='
t_MULTIGUAL 	= r'\*='
t_DIVIDEIGUAL	= r'/='

'''
t_CHAR      = r'char'
t_INT       = r'int'
t_FLOAT     = r'float'
t_IF        = r'if'
t_ELSE      = r'else'
t_SWITCH    = r'switch'
t_CASE      = r'case'
t_DEFAULT   = r'default'
'''

# expressao rewgular para identificadores
def t_IDEN(t) :
    r'[_a-zA-Z]+[a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_NUM(t) :
    r'[0-9]+([.]{1}[0-9])*'
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
    '''programa : sequencia_codigo
    '''
    t[0]=t[1]

def p_sequencia_codigo(t):
    '''sequencia_codigo : codigo sequencia_codigo
                        | codigo
    '''
    t[0]=t[1]

def p_codigo(t):
    '''codigo : declaracao_var
              | declaracao_if
    '''
    t[0]=t[1]

# para listas de declaracao [int a; int b;]
def p_declaracao_var(t):
    '''declaracao_var : tipo sequencia_var fim
                      | tipo sequencia_var fim declaracao_var
                      | declaracao_if
    ''' 
    t[0]=t[1]

def p_declaracao_if(t):
    '''declaracao_if : IF EPAREN IDEN DPAREN ECHAVE IDEN DCHAVE
                    | IF EPAREN IDEN DPAREN ECHAVE IDEN DCHAVE ELSE ECHAVE IDEN DCHAVE
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