def read_files():
    mnt = {
        'M1': [2, 2, 1, 1],
        'M2': [2, 2, 6, 3]
    }

    pntab = {
        'M1': ['X', 'Y', 'A', 'B'],
        'M2': ['P', 'Q', 'U', 'V']
    }

    kpdt = {
        'A': 'AREG',
        'B': '',
        'U': 'CREG',
        'V': 'DREG'
    }

    return mnt, pntab, kpdt


def process():
    mnt, pntab, kpdt = read_files()
    aptab = {}
    current_macro = 0
    output = ""

    with open("intermediate.txt", "r") as ic_file, open("mdt.txt", "r") as mdt_file:
        for line in ic_file:
            words = line.replace(",", "").replace("&", "").split()

            if words[0] not in mnt.keys():
                output += line
            else:
                current_macro += 1
                aptab = {}
                mnt_values = mnt[words[0]]
                pp = mnt_values[0]
                kp = mnt_values[1]

                for i in range(1, pp + 1):
                    aptab[i] = words[i]

                for i in range(pp + 1, pp + kp + 1):
                    if words[i].partition("=")[2] == '':
                        aptab[i] = kpdt[words[i].partition('=')[0]]
                    else:
                        aptab[i] = words[i].partition("=")[2]

                for mdt_line in mdt_file:
                    mdt_words = mdt_line.split()

                    if mdt_words[0] != 'MEND':
                        output += mdt_words[0] + "\t"

                        for i in range(1, len(mdt_words)):
                            if mdt_words[i].find('=') == -1:
                                parameter_index = int(mdt_words[i][3])
                                output += aptab[parameter_index] + "\t"
                            else:
                                output += mdt_words[i] + "\t"

                        output += "\n"
                    else:
                        break

    print(output)


read_files()
process()
