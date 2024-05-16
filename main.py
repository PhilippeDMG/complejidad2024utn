"""TP complejidad nros sociales"""

from numerosPrimos import my_set
from utils import sum_divs1 as s
from decorators import delta_time

@delta_time("GRUPO G8")
def sociables(n):
    """encontrar perfectos hasta lim"""
    lim = 100_000
    space_set = my_set
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
            print(f"30 iterations for i == {i}")
            # for elem in sequence:
            #     space_set.add(elem)
    return lista

if __name__ =="__main__":
        print(multiperfecto(DATOS))
