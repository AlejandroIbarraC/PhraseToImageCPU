# Available registers
registers = {
    'R0': '0000',
    'R1': '0001',
    'R2': '0010',
    'R3': '0011',
    'R4': '0100',
    'R5': '0101',
    'R6': '0110',
    'R7': '0111',
    'R8': '1000',
    'R9': '1001',
    'R10': '1010',
    'R11': '1011',
    'R12': '1100',
    'R13': '1101',
    'R14': '1110',
    'R15': '1111'
}

# Arithmetic type instructions
ari_instrs = {
    'ADD': int('00010', 2),
    'ADDI': int('00011', 2),
    'SUB': int('00100', 2),
    'SUBI': int('00101', 2),
    'MUL': int('00110', 2),
    'MULI': int('00111', 2)
}

# Register type instructions
reg_instrs = {
    'MOV': int('01000', 2),
    'MOVI': int('01001', 2),
    'CMP': int('01010', 2),
    'CMPI': int('01011', 2)
}

# Memory type instructions
mem_instrs = {
    'STR': int('01100', 2),
    'STRI': int('01101', 2),
    'LD': int('01110', 2)
}

# Branch type instructions
bra_instrs = {
    'BGT': int('10001', 2),
    'BGTE': int('10011', 2),
    'BEQ': int('10101', 2),
    'B': int('10111', 2),
    'BRGT': int('10000', 2),
    'BRGTE': int('10010', 2),
    'BREQ': int('10100', 2),
    'BR': int('10110', 2)
}

# Special type instructions
spe_instrs = {
    'STLL': int('00000', 2)
}