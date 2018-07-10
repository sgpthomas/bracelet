import itertools
from collections import Counter
import numpy as np

try:
    while True:
        pre = 2 * (input("Enter a bracelet: ") + " ")
        bracelet = [int(x) for x in pre.split()]
        L = len(bracelet) / 2

        veclist = []

        for i in range(int(L)):
            v_i = []
            for letter in range(int(L)):
                dist = 0
                beep = True

                while beep:
                    if bracelet[i + dist] == letter:
                        if dist > (L/2):
                            dist = L-dist
                        v_i.append(dist)
                        beep = False
                    else:
                        dist += 1

            veclist.append(v_i)

        vec_list = sorted(veclist)
        # for i, v in enumerate(vec_list):
        #     print("v_{}: {}".format(i, v))

        matrix = np.array(vec_list)
        print(matrix)
        det = np.linalg.det(matrix)
        print("Det: {}".format(det))
except EOFError:
    print("Exiting")
except KeyboardInterrupt:
    print("Exiting")
