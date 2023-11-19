def pass1():
    count_pp, count_kp, mdtp, kptp, macro_count = 0, 0, 1, 1, 0
    mdt, mnt, kpdt, ic, pntab = "", "", "", "", ""
    next_macro, is_start = False, False

    with open("imp.txt", "r") as file:
        for lines in file:
            if "START" in lines or is_start:
                ic += lines
                is_start = True
            else:
                word = lines.replace("&", "").replace(",", "").split()

                if next_macro:
                    count_kp, count_pp = 0
                    macro_name = word[0]
                    pntab += f"{macro_name}\t"
                    next_macro = False

                    for i in range(1, len(word)):
                        if "=" in word[i]:
                            count_kp += 1
                            var_name, given_name = word[i].split('=')
                            pntab += f"{var_name}\t"
                            kpdt += f"{var_name}\t{given_name}\n"
                        else:
                            count_pp += 1
                            pntab += f"{word[i]}\t"

                    pntab += "\n"
                    mnt += f"{macro_name}\t{count_pp}\t{count_kp}\t{mdtp}\t{kptp}\n"
                    kptp += count_kp
                
                elif word[0] == "MACRO":
                    next_macro = True
                    macro_count += 1
                
                else:
                    string = f"{word[i]}\t"
                    parameters = pntab.split('\n')[macro_count-1].split()

                    for i in range(1, len(word)):
                        if "=" in word:
                            string += f"{word[i]}\t"
                        else:
                            index = parameters.index(word[i])
                            string += f"(P,{index})\t"

                    mdtp += 1
                    string += "\n"
                    mdt += string
    # Print All the tables

pass1()