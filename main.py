"""TP complejidad nros sociales"""

from utils import sum_divs1 as s

# def main():
#    """encontrar perfectos hasta lim"""
#    lim = 1000
#    space = [True] * 3 * lim  # hasta q nro habria q guardar?
#    for i in range(lim):
#        sequence = [i]
#        tries = 0
#        holder = i
#        while tries < 30:
#            tries += 1
#            res = s(holder)
#            if res > 2 * i:
#                print(i)
#            if space[res]:  # nro no explorado
#                if res in sequence:
#                    subseq_start = sequence.index(res)
#                    social_nbrs = sequence[subseq_start:]
#                    for nbr in sequence:
#                        space[nbr] = False
#                    print(f"sequence of length {len(social_nbrs)}: {social_nbrs}")
#                    break
#                else:
#                    sequence.append(res)
#                    holder = res
#            else:  # nro q no es social o q si es social
#                for elem in sequence:
#                    space[elem] = False
#                break
#        if tries == 30:
#            print("30 reps")
#            for elem in sequence:
#                space[elem] = False

# with open("output.txt", "w") as file:
#    for i in range(lim):
#        if perfs[i]:
#            file.write(str(i) + "\n")


def main():
    """encontrar perfectos hasta lim"""
    lim = 100_000
    space_set = {0}  # hasta q nro habria q guardar?
    for i in range(lim):
        sequence = [i]
        tries = 0
        holder = i
        while tries < 30:
            tries += 1
            res = s(holder)
            if res not in space_set:  # nro no explorado
                if res in sequence:
                    if res == 1:
                        break
                    subseq_start = sequence.index(res)
                    social_nbrs = sequence[subseq_start:]
                    for nbr in sequence:
                        space_set.add(nbr)
                    print(f"sequence of length {len(social_nbrs)}: {social_nbrs}")
                    break
                else:
                    sequence.append(res)
                    holder = res
            else:  # nro q no es social o q si es social
                for elem in sequence:
                    space_set.add(elem)
                break
        if tries == 30:
            print(f"30 reps for i == {i}")
            for elem in sequence:
                space_set.add(elem)


main()
