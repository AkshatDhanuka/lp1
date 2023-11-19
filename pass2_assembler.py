def read_files(symtab_path, littab_path)
    symtab = []
    littab = []

    with open(symtab_path, r) as file
        for line in file
            word = line.split()
            symtab.append(int(word[2][-1]))

    with open(littab_path, r) as file
        for line in file
            word = line.split()
            littab.append(int(word[2][-1]))

    return symtab, littab

def literal_or_symbol(word, symtab, littab)
    index = int(word[3-1])
    return littab[index - 1] if 'L' in word else symtab[index]

def process(input_path, symtab, littab)
    with open(input_path, r) as file
        for line in file
            word = line.replace(n, ).strip().split()

            if 'AD' in word[0] or 'DL,02' in word[0]
                print()
            elif 'DL,01' in word[0]
                print(f00t0t{word[1][3-1]})
            elif 'IS,00' in word[0]
                print(00t0t000)
            elif 'IS,10' in word[0]
                code = literal_or_symbol(word[1], symtab, littab)
                print(f10t0t{code})
            elif 'IS' in word[0]
                code1 = word[0][46]
                code2 = word[1][1]
                code3 = literal_or_symbol(word[2], symtab, littab)
                print(f{code1}t{code2}t{code3})
            else
                print()

symtab_path = homerohandoshi21DevelopmentLP1Assemblerpass2Symtab.txt
littab_path = homerohandoshi21DevelopmentLP1Assemblerpass2Littab.txt
input_path = homerohandoshi21DevelopmentLP1Assemblerpass2input.txt

symtab, littab = read_files(symtab_path, littab_path)
process(input_path, symtab, littab)
