from lib.gillespie import GSystem
from lib.parser import parse_fichier
from lib.reaction import Reaction

import math
import random
import sys

def fact(n, m):

    if n <= m:
        return m
    else:
        return n * fact(n-1, m)

def calcul_hi_ai(nb_especes, reactions):

    h_a = []
    for reaction in reactions:
        hi_ai = reaction.vitesse
        for espece in reaction.entree:
            hi_ai = hi_ai * (fact(nb_especes[espece], (nb_especes[espece] - reaction.entree[espece] + 1)) / fact(reaction.entree[espece],1))
        h_a.append(hi_ai)
    return h_a

def main(fichier, temps):

    # Système de Gillespie parsé
    gsystem = parse_fichier(fichier)
    temps = float(temps)

    c_temps = 0

    tau = 10

    of = open(fichier+"_output", 'w')

    a_esp = ""
    for esp in gsystem.especes:
        a_esp += esp + ", "
    a_esp = a_esp[:-2]
    a_esp += "\n"
    a_esp = "tau, " + a_esp

    of.write(a_esp)

    while c_temps < temps:

        print("Temps: {0}".format(c_temps))

        #Calcul de hi_ai et de sum_hi_ai
        hi_ai = calcul_hi_ai(gsystem.especes, gsystem.reactions)
        sum_hi_ai = sum(hi_ai)

        print(sum_hi_ai)

        if sum_hi_ai == 0:
            sys.exit()

        hi_ai_sorted = sorted(hi_ai, reverse=True)

        hi_ai_sorted_to_normal = []
        for h_a in hi_ai_sorted:
            hi_ai_sorted_to_normal.append(hi_ai.index(h_a))

        #Calcul du random, concernant la réaction
        rand_choix_reaction = random.uniform(0, sum_hi_ai)

        print("Random : {0} / {1}".format(rand_choix_reaction, sum_hi_ai))

        c_h_a = (0, 0)

        reaction = None

        # Choix de la réaction
        for h_a in hi_ai_sorted:
            c_h_a = (c_h_a[0], c_h_a[1] + h_a)
            #print(gsystem.reactions[hi_ai_sorted_to_normal[c_h_a[0]]])
            if rand_choix_reaction < c_h_a[1] and not reaction:
                print("\t REACTION {0}".format(hi_ai_sorted_to_normal[c_h_a[0]]))
                reaction = gsystem.reactions[hi_ai_sorted_to_normal[c_h_a[0]]]
            else:
                c_h_a = (c_h_a[0] + 1, c_h_a[1])

        print("\t {0} -> {1}".format(reaction.entree, reaction.sortie))

        tau = (1 / sum_hi_ai) * math.log(1/random.random())

        print("\t tau : {0}".format(tau))

        c_temps = c_temps + tau

        # Modification des entrées et des sorties
        for entree in reaction.entree:
            print("\t entree : {0} / {1} -> {2}".format(entree, gsystem.especes[entree], gsystem.especes[entree] - reaction.entree[entree]))
            gsystem.especes[entree] = gsystem.especes[entree] - reaction.entree[entree]

        for sortie in reaction.sortie:
            print("\t sortie : {0} / {1} -> {2}".format(sortie, gsystem.especes[sortie], gsystem.especes[sortie] + reaction.sortie[sortie]))
            gsystem.especes[sortie] = gsystem.especes[sortie] + reaction.sortie[sortie]

        # Écriture du résultat dans le fichier CSV
        a_esp = str(c_temps) + ", "
        for esp in gsystem.especes:
            a_esp += str(gsystem.especes[esp]) + ", "
        a_esp = a_esp[:-2]
        a_esp += "\n"

        of.write(a_esp)

        input()

    of.close()

if __name__ == '__main__':

    main(sys.argv[1], sys.argv[2])
