import ply.yacc as yacc

# Do not remove this import. PLY uses it to read tokens
from Lexer import tokens

# Result variable that will store the resulting tree
result = []

# Default code definition
def p_code(p):
    '''
    code : body
    '''


# A line body can be either an instruction or a label
def p_body(p):
    '''
    body : instruction body
         | label body
    '''
    p[0] = (p[1])


def p_empty(p):
    '''
    body :
    '''


# A label is of lexical type LABEL
def p_label(p):
    '''
    label : LABEL
    '''

    if p[1] != '$':
        p[0] = (p[1])
        result.append(p[0])
    else:
        p[0] = p[1]


# Instruction can be of five types
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
    ari_instr : ari_instr_name REG COMMA REG COMMA REG
              | ari_instr_name REG COMMA REG COMMA IMM
    '''
    if p[1] != '$':
        p[0] = (p[1], p[2], p[4], p[6])
        result.append(p[0])
    else:
        p[0] = p[1]


# Register instruction structure
def p_reg_instr(p):
    '''
    reg_instr : reg_instr_name REG COMMA REG
              | reg_instr_name REG COMMA IMM
    '''
    p[0] = (p[1], p[2], p[4])
    result.append(p[0])


# Memory instruction structure
def p_mem_instr(p):
    '''
    mem_instr : mem_instr_name REG COMMA REG
              | mem_instr_name REG COMMA IMM
    '''
    p[0] = (p[1], p[2], p[4])
    result.append(p[0])


# Branch instruction structure
def p_bra_instr(p):
    '''
    bra_instr : bra_instr_name LABEL
              | bra_ret_instr_name REG
    '''
    p[0] = (p[1], p[2])
    result.append(p[0])


# Special instructions
def p_spe_instr(p):
    '''
    spe_instr : STLL
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
    reg_instr_name : MOV
                   | MOVI
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
                   | BEQ
                   | B
    '''
    p[0] = p[1]


# Branch return instruction names
def p_bra_ret_instr_name(p):
    '''
    bra_ret_instr_name : BRGT
                       | BRGTE
                       | BREQ
                       | BR
    '''
    p[0] = p[1]


# Error case
def p_error(p):
    print("Syntax Error!")
    print("linea: " + str(p.lineno) + ' token: ' + str(p))


# Analyze the syntax of a string with above rules
def analyze_syntax(string):
    print("Analyzing syntax...")
    parser = yacc.yacc()
    parser.parse(string)

    return result[::-1]
