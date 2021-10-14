import ply.yacc as yacc

from Lexer import tokens
from Lexer import analyze_lexical

# Result variable that will store the resulting tree
result = []

# Code should start with START: and end with END
def p_code(p):
    '''
    code : body
    '''


# A line body can be either an instruction or a label
def p_body(p):
    '''
    body : instruction
         | label
    '''
    p[0] = (p[1])


# A label is of lexical type LABEL
def p_label(p):
    '''
    label : LABEL body
          | empty
    '''

    if p[1] != '$':
        p[0] = (p[1])
        result.append(p[0])
    else:
        p[0] = p[1]


# Instruction can be of four types
def p_instruction(p):
    '''
    instruction : spe_instr
                | ari_instr
                | reg_instr
                | mem_instr
                | bra_instr
    '''
    p[0] = p[1]


# Arithmetical instruction structure
def p_ari_instr(p):
    '''
    ari_instr : ari_instr_name REG COMMA REG COMMA REG SEMICOLON body
              | ari_instr_name REG COMMA REG COMMA IMM SEMICOLON body
              | empty
    '''
    if p[1] != '$':
        p[0] = (p[1], p[2], p[4], p[6])
        result.append(p[0])
    else:
        p[0] = p[1]


# Register instruction structure
def p_reg_instr(p):
    '''
    reg_instr : reg_instr_name REG COMMA REG SEMICOLON body
              | reg_instr_name REG COMMA IMM SEMICOLON body
              | empty
    '''
    p[0] = (p[1], p[2], p[4])
    result.append(p[0])


# Memory instruction structure
def p_mem_instr(p):
    '''
    mem_instr : mem_instr_name REG COMMA REG SEMICOLON body
              | mem_instr_name REG COMMA IMM SEMICOLON body
              | empty
    '''
    p[0] = (p[1], p[2], p[4])
    result.append(p[0])


# Branch instruction structure
def p_bra_instr(p):
    '''
    bra_instr : bra_instr_name LABEL SEMICOLON body
              | empty
    '''
    p[0] = (p[1], p[2])
    result.append(p[0])


# Special instructions
def p_spe_instr(p):
    '''
    spe_instr : STLL SEMICOLON body
              | empty
    '''
    p[0] = (p[1], '-')
    result.append(p[0])


# Arithmetic instruction names
def p_ari_instr_name(p):
    '''
    ari_instr_name : ADD
                   | ADDI
                   | SUB
                   | SUBI
                   | MUL
                   | MULI
    '''
    p[0] = p[1]


# Register instruction names
def p_reg_instr_name(p):
    '''
    reg_instr_name : MOVI
                   | CMP
                   | CMPI

    '''
    p[0] = p[1]


# Memory instruction names
def p_mem_instr_name(p):
    '''
    mem_instr_name : STR
                   | STRI
                   | LD
    '''
    p[0] = p[1]


# Branch instruction names
def p_bra_instr_name(p):
    '''
    bra_instr_name : BGT
                   | BGTE
                   | BE
                   | B
                   | BRGT
                   | BRGTE
                   | BRE
                   | BR
    '''
    p[0] = p[1]


# Empty terminal
def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'


# Error case
def p_error(p):
    print("Syntax Error!")
    print("info: " + str(p))
    print("line:  " + str(p.lineno))


# Analyze the syntax of a string with above rules
def analyze_syntax(string):
    print("Analyzing syntax...")
    parser = yacc.yacc()
    parser.parse(string)

    return result[::-1]
