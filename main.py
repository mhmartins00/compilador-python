# COMPILADORES - ETAPA 1
# NOMES: DOUGLAS MOELLER, MURILLO MARTINS
import sys
sys.path.append("../..")
import ply.lex as lex
import ply.yacc as yacc

#################### ANALISADOR LEXICO ####################
reserved = {
    'char'   : 'CHAR',
    'int'    : 'INT',
    'float'  : 'FLOAT',
    'if'     : 'IF',
    'else'   : 'ELSE',
    'switch' : 'SWITCH',
    'case'   : 'CASE',
    'break'  : 'BREAK',
    'default': 'DEFAULT',
    'while'  : 'WHILE',
    'for'    : 'FOR'
}

tokens = ['IDEN', 'NUM', 'ADEL', 'VIRGULA', 'PONTOVIRGULA', 'DOISPONTOS', 'EPAREN', 'DPAREN', 'ECHAVE', 'DCHAVE', 'ECOLCH', 'DCOLCH', 'IGUAL', 'DIFERENTE', 'MENORIGUAL', 'MAIORIGUAL', 'MENOR', 'MAIOR', 'MAIS', 'MENOS', 'MULTIPLICA', 'DIVIDE', 'MAISMAIS', 'MENOSMENOS', 'RECEBE', 'MAISIGUAL', 'MENOSIGUAL', 'MULTIGUAL', 'DIVIDEIGUAL']+ list(reserved.values())

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
t_ECOLCH        = r'\['
t_DCOLCH        = r'\]'

# Operadores Relacionais 
t_IGUAL         = r'=='
t_DIFERENTE		= r'!='
t_MENORIGUAL	= r'<='
t_MAIORIGUAL	= r'>='
t_MENOR			= r'<'
t_MAIOR			= r'>'

# Operadores Matemáticos
t_MAIS  		= r'\+'
t_MENOS			= r'-'
t_MULTIPLICA	= r'\*'
t_DIVIDE		= r'/'
t_MAISMAIS		= r'\+\+'
t_MENOSMENOS	= r'--'

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
t_BREAK'    = r'break',
t_DEFAULT   = r'default'
t_WHILE     = r'while'
t_FOR       = r'for'
'''

# expressao regular para identificadores
def t_IDEN(t) :
    r'[_a-zA-Z]+[a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

# expressao regular para numeros int ou float
def t_NUM(t) :
    r'[\d]+(\.[\d]+)?'
    return t

# expressao regular para SOMENTE numeros int
def t_ADEL(t) :
    r'[0-9]+$'
    return t

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#################### ANALISADOR SINTATICO E REGRAS ####################
# criamos as regras bem especificas para facilitar a manutencao e o desenvolvimento futuro

def p_fim_instrucao(p):
    'fim : PONTOVIRGULA'

def p_num(t):
    'num : NUM'
    t[0]=t[1]

def p_adel(t):
    'adel : ADEL'
    t[0]=t[1]
    
def p_defincao_tipo(t):
    '''tipo : INT
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
              | declaracao_switch
              | declaracao_while
              | declaracao_for
    '''
    t[0]=t[1]

def p_condicao(t):
    '''condicao : expressao_relacional
    '''
    t[0]=t[1]

def p_comandos(t):
    '''comandos : atribuicao comandos
                | atribuicao
    '''
    t[0]=t[1]

def p_expressao_relacional(t):
    '''expressao_relacional : var_ou_num MAIOR var_ou_num
                            | var_ou_num MENOR var_ou_num
                            | var_ou_num MAIORIGUAL var_ou_num
                            | var_ou_num MENORIGUAL var_ou_num
                            | var_ou_num IGUAL var_ou_num
                            | var_ou_num DIFERENTE var_ou_num
    '''
    t[0]=t[1]

def p_expressao_matematica(t):
    '''expressao_matematica : var_ou_num
                            | var_ou_num operacao_matematica expressao_matematica
    '''
    t[0]=t[1]

def p_operacao_matematica(t):
    '''operacao_matematica : MENOS
                           | MAIS
                           | MULTIPLICA
                           | DIVIDE
    '''
    t[0]=t[1]

def p_var_ou_num(t):
    '''var_ou_num : variavel
                  | num

    '''
    t[0]=t[1]

def p_operador_atribuicao(t):
    '''operador_atribuicao : RECEBE 
                           | MAISIGUAL
                           | MENOSIGUAL
                           | MULTIGUAL
                           | DIVIDEIGUAL
    '''
    t[0]=t[1]

def p_atribuicao(t):
    '''atribuicao : variavel operador_atribuicao expressao_matematica fim
                  | variavel operador_atribuicao var_ou_num fim
                  | variavel MAISMAIS fim
                  | variavel MENOSMENOS fim
    '''
    t[0]=t[1]

def p_encremento_ou_decremento_for(t):
    '''encremento_ou_decremento_for : variavel operador_atribuicao expressao_matematica
                                    | variavel operador_atribuicao var_ou_num
                                    | variavel MAISMAIS
                                    | variavel MENOSMENOS
    '''
    t[0]=t[1]

# para listas de declaracao [int a; int b;]
def p_declaracao_var(t):
    '''declaracao_var : tipo sequencia_var fim
                      | tipo sequencia_var fim declaracao_var
                      | declaracao_char
    ''' 
    t[0]=t[1]

# sequencia [a,b,c]
def p_sequencia_var(t):
    '''sequencia_var : variavel
                     | variavel VIRGULA sequencia_var
    '''
    t[0]=t[1]

# para declaracao char [char a; char b[1];]
def p_declaracao_char(t):
    '''declaracao_char : CHAR sequencia_char fim
                       | CHAR sequencia_char fim declaracao_var
    ''' 
    t[0]=t[1]

# sequencia char [char a; char a[1], b, c[2];]
def p_sequencia_char(t):
    '''sequencia_char : variavel
                      | variavel VIRGULA sequencia_char
                      | variavel ECOLCH adel DCOLCH
                      | variavel ECOLCH adel DCOLCH VIRGULA sequencia_char
    '''
    t[0]=t[1]

def p_declaracao_if(t):
    '''declaracao_if : IF EPAREN condicao DPAREN ECHAVE comandos DCHAVE
                     | IF EPAREN condicao DPAREN ECHAVE comandos DCHAVE ELSE ECHAVE comandos DCHAVE
    ''' 
    t[0]=t[1]

# switch (variavel) { declaracao_case }
def p_declaracao_switch(t): 
    '''declaracao_switch : SWITCH EPAREN variavel DPAREN ECHAVE declaracao_case DCHAVE
                         | SWITCH EPAREN variavel DPAREN ECHAVE declaracao_case declaracao_default DCHAVE
    ''' 
    t[0]=t[1]

def p_declaracao_while(t):
    '''declaracao_while : WHILE EPAREN condicao DPAREN ECHAVE comandos DCHAVE
    ''' 
    t[0]=t[1]

# for(parametros_for){<comandos>}
def p_declaracao_for(t):
    '''declaracao_for : FOR EPAREN parametros_for DPAREN ECHAVE comandos DCHAVE
    ''' 
    t[0]=t[1]
# ini_variável; condição; incremento/decremento
def p_parametros_for(t):
    '''parametros_for : atribuicao condicao fim encremento_ou_decremento_for
    ''' 
    t[0]=t[1]

# sequencia_case { comandos break; }
def p_declaracao_case(t): 
    '''declaracao_case : sequencia_case ECHAVE comandos BREAK fim DCHAVE declaracao_case
                       | sequencia_case ECHAVE comandos BREAK fim DCHAVE
    ''' 
    t[0]=t[1]

# para sequencia de cases [case id: case id: case id:]
def p_sequencia_case(t): 
    '''sequencia_case : CASE var_ou_num DOISPONTOS sequencia_case
                      | CASE var_ou_num DOISPONTOS 
    ''' 
    t[0]=t[1]

# default: { comandos }
def p_declaracao_default(t): 
    '''declaracao_default : DEFAULT DOISPONTOS ECHAVE comandos DCHAVE
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