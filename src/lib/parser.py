from lib.gillespie import GSystem
from lib.reaction import Reaction
import re
import sys

def parse_fichier(nom_fichier):
    """
    Fonction permettant de parser un fichier, donné en entrée, afin de pouvoir obtenir un système chimique donné par un utilisateur
    nom_fichier : Le nom du fichier contenant le système chimique
    """
    int_to_especes = {}
    especes = {}
    reactions = []
    with open(nom_fichier) as fichier:
        for instruction in fichier:
            instruction = instruction.strip()
            mots = instruction.split(' ')
            if mots[0] == "ESP":
                for i in range(1, len(mots)):
                    especes[mots[i]] = 0
                    int_to_especes[i-1] = mots[i]
            elif mots[0] == "NBR":
                for i in range(1, len(mots)):
                    especes[int_to_especes[i - 1]] = int(mots[i])
            elif mots[0] == "REAC":
                entree = parse_demi_reaction(mots[2])
                sortie = parse_demi_reaction(mots[3])
                nv_reaction = Reaction(entree, sortie, float(mots[1]))
                reactions.append(nv_reaction)
            else:
                print(mots[0])
                sys.exit()
    return GSystem(especes, reactions)

def parse_demi_reaction(demi_reaction):
    """
    Fonction permettant de parser une demi-réaction, c'est-à-dire les réactifs ou les produits
    demi_reaction : Une chaîne de caractères (sans espace), caractérisant la demi-réaction
    """
    especes_ret = {}
    especes = demi_reaction.split('+')
    for espece in especes:
        r = parse_espece(espece)
        especes_ret[r[1]] = int(r[0])
    return especes_ret

def parse_espece(espece):
    """
    Fonction permettant de splitter une chaîne de caractères selon : (nb_espece, espece)
    """
    r = re.match(r"([0-9]+)([A-Z]+)", espece)
    if r:
        return r.groups()
    else:
        r = re.match(r"([A-Z]+)", espece)
        return (1, r.group(1))
