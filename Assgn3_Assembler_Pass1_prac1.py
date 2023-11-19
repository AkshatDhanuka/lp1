OPTAB = {
    "STOP": "(IS,00)",
    "ADD": "(IS,01)",
    "SUB": "(IS,02)",
    "MUL": "(IS,03)",
    "MOVER": "(IS,04)",
    "MOVEM": "(IS,05)",
    "COMP": "(IS,06)",
    "BC": "(IS,07)",
    "DIV": "(IS,08)",
    "READ": "(IS,09)",
    "PRINT": "(IS,10)",
}

REG = {
    "AREG": "(1)",
    "BREG": "(2)",
    "CREG": "(3)",
    "DREG": "(4)",
}

CC = {
    "LT": "(1)",
    "LE": "(2)",
    "EQ": "(3)",
    "GT": "(4)",
    "GE": "(5)",
    "ANY": "(6)"
}

symtab = []
lc = 0
literaltab = []
litIndex = 0
poolTab = [0]
poolIndex = 0


def updateSymtab(pair):
    global symtab
    for i in range(len(symtab)):
        if symtab[i][0] == pair[0]:
            symtab[i][1] = pair[1]
            break
    else:
        symtab.append(pair)


def getSymtabLC(symbol):
    global symtab
    for i in range(len(symtab)):
        if symtab[i][0] == symbol:
            return symtab[i][1]
    else:
        return -1


def getSymtabPos(symbol):
    global symtab
    for i in range(len(symtab)):
        if symtab[i][0] == symbol:
            return i
    else:
        return -1


def process():
    global lc, litIndex, poolIndex, symtab, literaltab, poolTab

    with open("/home/rohandoshi21/Development/LP1/Assembler/Simple.txt", "r") as file:
        data = file.readlines()
        i = 0

        while i < len(data):
            line = data[i]
            word = line.rstrip('\n').split('\t')

            if word[0]:  # A label is present
                pair = [word[0], lc]
                updateSymtab(pair)

            if word[1] == 'START':
                lc = int(word[2])
                print(f"(AD,01)\t(C,{lc})")

            if word[1] == 'DC':
                lc += 1
                constant = word[2][1:-1]
                print(f"(DL,01)\t(C,{constant})")

            if word[1] == 'LTORG':
                j = poolIndex
                while j < litIndex:
                    literaltab[j][1] = lc
                    lc += 1
                    value = int(literaltab[j][0].lstrip("='").rstrip("'"))
                    print(f"(DL,01)\t(C,{value})")
                    j += 1
                poolTab.append(litIndex)
                poolIndex = litIndex

            if word[1] == 'DS':
                constant = int(word[2])
                lc += constant
                print(f"(DL,02)\t(C,{constant})")

            if word[1] == 'ORIGIN':
                lc = int(word[2])
                print(f"(AD,03)\t(C,{lc})")

            if word[1] == 'EQU':
                Equation = word[2].split('+')
                index = getSymtabLC(Equation[0]) + int(Equation[1])
                updateSymtab([word[0], index])
                index_print = getSymtabPos(Equation[0])
                print(f"(AD,04) (S,{index_print})+{Equation[1]}")

            if OPTAB.get(word[1]) is not None:
                code = OPTAB.get(word[1]) + "\t"
                j = 2
                while j < len(word):
                    if REG.get(word[j]) is not None:
                        code += REG.get(word[j]) + "\t"
                    elif CC.get(word[j]) is not None:
                        code += CC.get(word[j]) + "\t"
                    elif '=' in word[j]:
                        literaltab.append([word[j], -1])
                        word[j] = word[j].lstrip("='").rstrip("'")
                        litIndex += 1
                        code += f"(L,{litIndex})"
                    else:
                        if getSymtabLC(word[j]) == -1:
                            pair = [word[j], -1]
                            updateSymtab(pair)
                        const = getSymtabPos(word[j])
                        code += f"(S,{const})"
                    j += 1
                lc += 1
                print(code)

            if word[1] == 'END':
                j = poolIndex
                while j < litIndex:
                    literaltab[j][1] = lc
                    lc += 1
                    value = int(literaltab[j][0].lstrip("='").rstrip("'"))
                    print(f"(DL,01)\t(C,{value})")
                    j += 1
                poolTab.append(litIndex)
                poolIndex = litIndex
                print('(AD, 02)')

            i += 1

        print("Symtab: ")
        print(symtab)

        print("Littab: ")
        print(literaltab)

        print("Pooltab :")
        print(poolTab)

        file.close()

    with open("/home/rohandoshi21/Development/LP1/Assembler/Symtab.txt", "w") as file:
        for x in range(len(symtab)):
            file.write(f"{x}\t{symtab[x]}\n")

    with open("/home/rohandoshi21/Development/LP1/Assembler/Littab.txt", "w") as file:
        for x in range(len(literaltab)):
            file.write(f"{x}\t{literaltab[x]}\n")

    with open("/home/rohandoshi21/Development/LP1/Assembler/Pooltab.txt", "w") as file:
        for x in range(len(poolTab)):
            file.write(f"{x}\t{poolTab[x]}\n")


process()