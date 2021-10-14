import ply.lex as lex

# Tokens
tokens = [
    'COMMA',
    'SEMICOLON',
    'REG',
    'IMM',
    'LABEL',
]

# Reserved tokens in language
reserved = {
    'STLL': 'STLL',
    'ADD': 'ADD',
    'ADDI': 'ADDI',
    'SUB': 'SUB',
    'SUBI': 'SUBI',
    'MUL': 'MUL',
    'MULI': 'MULI',
    'MOVI': 'MOVI',
    'CMP': 'CMP',
    'CMPI': 'CMPI',
    'STR': 'STR',
    'STRI': 'STRI',
    'LD': 'LD',
    'BGT': 'BGT',
    'BGTE': 'BGTE',
    'BE': 'BE',
    'B': 'B',
    'BRGT': 'BRGT',
    'BRGTE': 'BRGTE',
    'BRE': 'BRE',
    'BR': 'BR',
}

tokens = tokens + list(reserved.values())

# Token initialization

# Ignore spaces
t_ignore = ' \t'

# Delimiters
t_COMMA = r','
t_SEMICOLON = r';'


# Register token
def t_REG(t):
    r'[R][0-9]+'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
    return t


# Label token
def t_LABEL(t):
    r'[a-zA-Z_][a-zA-Z0-9_#@]*'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
    return t


# Immediate value token
def t_IMM(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Moves parser 1 line when '\n' is detected
def t_new_line(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error token
def t_error(t):
    print("Illegal character! '%s'" % t.value[0])
    t.lexer.skip(1)


# Create lexical analysis using ply
def analyze_lexical(string):
    result = []
    analyzer = lex.lex()
    analyzer.input(string)

    while True:
        tok = analyzer.token()
        if not tok:
            break
        result.append(tok)

    return result
