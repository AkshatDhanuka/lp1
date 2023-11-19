def process_pass1():
    count_pp, count_kp, mdtp, kptp, macro_count = 0, 0, 1, 1, 0
    mnt, pntab, kpdt, ic, mdt = "", "", "", "", ""
    next_macro, is_start = False, False

    with open("input.txt", "r") as file:
        for lines in file:
            if 'START' in lines or is_start:
                ic += lines
                is_start = True
            else:
                word = lines.replace("&", "").replace(",", "").split()

                if next_macro:
                    count_kp, count_pp = 0, 0
                    macro_name = word[0]
                    pntab += f"{macro_name}\t"

                    for i in range(1, len(word)):
                        if '=' in word[i]:
                            count_kp += 1
                            parameter_name, given_name = word[i].split("=")     
                            pntab += f"{parameter_name}\t"
                            kpdt += f"{parameter_name}\t{given_name}\n"
                        else:
                            pntab += f"{word[i]}\t"
                            count_pp += 1

                    pntab += "\n"
                    mnt += f"{macro_name}\t{count_pp}\t{count_kp}\t{mdtp}\t{kptp}\n"
                    kptp += count_kp
                    next_macro = False

                elif word[0] == 'MACRO':
                    macro_count += 1
                    next_macro = True

                else:
                    string = f"{word[0]}\t"
                    parameters = pntab.split('\n')[macro_count-1].split()

                    for i in range(1, len(word)):
                        if '=' in word[i]:
                            string += f"{word[i]}\t"
                        else:
                            index = parameters.index(word[i])
                            string += f"(P,{index})\t"

                    mdtp += 1
                    string += "\n"
                    mdt += string

    print("*"*8 + "MDT" + "*"*8)
    print(mdt)
    print("*"*8 + "MNT" + "*"*8)
    print(mnt)
    print("*"*8 + "PNTAB" + "*"*8)
    print(pntab)
    print("*"*8 + "KPDT" + "*"*8)
    print(kpdt)
    print("*"*8 + "IC" + "*"*8)
    print(ic)


process_pass1()
