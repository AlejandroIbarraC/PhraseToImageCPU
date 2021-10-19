import Lang

from Lexer import analyze_lexical
from Syntaxer import analyze_syntax

# Variables for compilation
bra_labels = {}

hex_instr = []
bin_instr = []

# Useful constants
four_0s = '0000'
fifteen_0s = '000000000000000'
nineteen_0s = '0000000000000000000'


# Compile a block of code using the Spasm language lexemes and syntax
def compile_code(code):
    # Lexical and syntax analysis
    analyze_lexical(code)

    result_tree = analyze_syntax(code)
    result_tree.reverse()

    print("Result tree:")
    print(result_tree)

    # Get all labels and their line position in code
    p_dir = 0
    for ele in result_tree:
        if isinstance(ele, tuple):
            p_dir += 1
        else:
            if ele[0] == '_':
                bra_labels.update({ele: hex(p_dir)})

    print("Branch labels:")
    print(bra_labels)

    # Convert each instruction using language definition in binary form
    tree_to_bin(result_tree)

    print(bin_instr)
    # Convert binary instructions to hex
    bin_to_hex()

    print(hex_instr)

    # Write on file
    write_instr()


# Convert each instruction using language definition in binary form
def tree_to_bin(tree):
    p_dir = 0
    hex_dir_list = []
    instr_list = []
    for ele in tree:
        if isinstance(ele, tuple):
            hex_dir = hex(p_dir)
            hex_dir_list.append(hex_dir)

            instr_list.append(ele)
            analyze_instr(ele, hex_dir)
            p_dir += 1



# Convert binary instructions to hex
def bin_to_hex():
    i = 0
    for instr in bin_instr:
        if len(instr) != 32:
            print("Not 32: " + instr + " " + str(i))
        i += 1

        bin_code = int(instr, 2)
        hex_code = hex(bin_code)
        hex_code_len = len(hex_code)

        if hex_code_len != 10:
            hex_code = hex_code[2:]

            # Append 0s to fill hex length as 10
            while hex_code_len < 10:
                hex_code = "0" + hex_code
                hex_code_len += 1

            # Add '0x' to represent hex codes
            hex_code = '0x' + hex_code

        # Append new hex instruction in list
        hex_instr.append(hex_code)


# Writes instructions in hex form on an output txt file
def write_instr():
    with open("./output.txt", "w") as file:
        for instr in hex_instr:
            file.write("%s\n" % instr[2:])


# Analyze instructions and convert to corresponding op code for processor
def analyze_instr(instr, p_dir):
    print("ANALYZING")
    print("instruction: " + str(instr) + " on line " + str(int(p_dir, 16)))

    bin_res = ''
    instr_str = instr[0]
    # Detect in which category the instruction label falls
    if instr_str in Lang.ari_instrs:
        bin_res = analyze_instr_ari(instr)
    elif instr_str in Lang.reg_instrs:
        bin_res = analyze_instr_reg(instr)
    elif instr_str in Lang.mem_instrs:
        bin_res = analyze_instr_mem(instr)
    elif instr_str in Lang.bra_instrs:
        bin_res = analyze_instr_bra(instr, p_dir)
    elif instr_str in Lang.spe_instrs:
        bin_res = analyze_instr_spe(instr)
    else:
        print("Instruction " + instr + " unrecognized")

    # Append binary result of instruction to list
    bin_instr.append(bin_res)


# Analyzes arithmetical instructions and adds 32 bit binary number to list
def analyze_instr_ari(instr):
    bin_code = ''
    bin_code += str(format(Lang.ari_instrs.get(instr[0]), '#010b'))[5:]

    print("op code for " + instr[0] + " is " + bin_code)

    if isinstance(instr[3], int):
        # Arithmetical instruction is REG REG IMM
        # Get data
        imm = shift_num(str(format(instr[3], '#00010b'))[2:], 19)

        print("imm is " + imm)

        r1 = Lang.registers.get(str(instr[1]))
        r2 = Lang.registers.get(str(instr[2]))

        print("registers are " + r1 + " " + r2)

        # Append data
        bin_code += r1
        bin_code += imm
        bin_code += r2
    else:
        # Arithmetical instruction is REG REG REG
        # Get data
        r1 = Lang.registers.get(str(instr[1]))
        r2 = Lang.registers.get(str(instr[2]))
        r3 = Lang.registers.get(str(instr[3]))

        print("registers are " + r1 + " " + r2 + " " + r3)

        # Append data
        bin_code += r1
        bin_code += r3
        bin_code += fifteen_0s
        bin_code += r2

    print("binary: " + bin_code)
    print("length: " + str(len(bin_code)))

    return bin_code


# Analyzes register type instructions and adds 32 bit binary number to list
def analyze_instr_reg(instr):
    bin_code = ''
    bin_code += str(format(Lang.reg_instrs.get(instr[0]), '#010b'))[5:]

    print("op code for " + instr[0] + " is " + bin_code)

    if isinstance(instr[2], int):
        # Register instruction is REG IMM
        # Get data
        imm = shift_num(str(bin(instr[2]))[2:], 23)
        r1 = Lang.registers.get(str(instr[1]))

        print("imm is " + imm)
        print("reg is " + r1)

        # Append data
        bin_code += r1
        bin_code += imm
    else:
        # Register instruction is REG REG

        # Get data
        r1 = Lang.registers.get(str(instr[1]))
        r2 = Lang.registers.get(str(instr[2]))

        print("registers are " + r1 + " " + r2)

        # Append data
        bin_code += r1
        bin_code += r2
        bin_code += nineteen_0s

    print("binary: " + bin_code)
    print("length: " + str(len(bin_code)))

    return bin_code


# Analyzes memory instructions and adds 32 bit binary number to list
def analyze_instr_mem(instr):
    bin_code = ''
    bin_code += str(format(Lang.mem_instrs.get(instr[0]), '#010b'))[5:]

    print("op code for " + instr[0] + " is " + bin_code)

    if isinstance(instr[2], int):
        # Get data
        imm = shift_num(str(bin(instr[2]))[2:], 23)
        r1 = Lang.registers.get(str(instr[1]))

        print("imm is " + imm)
        print("r1 is " + r1)

        # Append data
        bin_code += r1
        bin_code += imm
    else:
        # Get data
        r1 = Lang.registers.get(str(instr[1]))
        r2 = Lang.registers.get(str(instr[2]))

        print("r1 is " + r1)
        print("r2 is " + r2)

        # Append data
        bin_code += r1
        bin_code += r2
        bin_code += nineteen_0s

    print("binary: " + bin_code)
    print("length: " + str(len(bin_code)))

    return bin_code


# Analyzes branch instructions and adds 32 bit binary number to list
def analyze_instr_bra(instr, p_dir):
    bin_code = ''

    bra_op_code = str(format(Lang.bra_instrs.get(instr[0]), '#010b'))[5:]
    print("op code for " + instr[0] + " is " + bra_op_code)

    target = str(instr[1])

    if target.startswith('_'):
        # Target is a label
        # Verify that label exists
        if target in bra_labels:
            # Label exists
            bra_dir = bra_labels.get(instr[1])
            bra_lines = int(bra_dir, 16) - int(p_dir, 16)

            print("jump " + str(bra_lines) + ' lines')

            # Switch bit in position 2 for backwards jumps
            if bra_lines < 0:
                bra_op_code = list(bra_op_code)
                bra_op_code[1] = '1'
                bra_op_code = ''.join(bra_op_code)
                print("new op code is: " + bra_op_code)

            # Append op code
            bin_code += bra_op_code

            # Fill with 0s to complete 32 - 5 bits
            bra_lines = bin(abs(bra_lines))[2:]
            bra_lines = shift_num(bra_lines, 27)

            # Append data
            bin_code += bra_lines
        else:
            # Label doesn't exist
            print("target branch " + str(instr[1]) + " does not exist")
    else:
        # Branch return
        r1 = Lang.registers.get(str(instr[1]))
        print("r1 is " + r1)

        bin_code += bra_op_code
        bin_code += four_0s
        bin_code += r1
        bin_code += nineteen_0s

    print("binary: " + bin_code)
    print("length: " + str(len(bin_code)))

    return bin_code


# Analyzes special instructions and adds 32 bit binary number to list
def analyze_instr_spe(instr):
    bin_code = ''
    bin_code += str(format(Lang.spe_instrs.get(instr[0]), '#010b'))[5:]

    print("op code for " + instr[0] + " is " + bin_code)

    # Append data
    bin_code += nineteen_0s
    bin_code += four_0s
    bin_code += four_0s

    print("binary: " + bin_code)
    print("length: " + str(len(bin_code)))

    return bin_code


# Shifts a string number by adding 0s to its left
def shift_num(num, shift):
    num_len = len(num)

    if num_len < shift:
        while num_len < shift:
            num = '0' + num
            num_len += 1

    return num
