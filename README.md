#SV - Projet 3

#Auteur

Carette Antonin
antonin.carette@etudiant.univ-lille1.fr

#Langage de programmation

Python, version 3.4

#Utilisation

```
cd src/
python3.4 main.py <mon_fichier_test.txt> <la_durée_voulue>
```

#Exemple

```
cd src/
python3.4 main.py ../tests/test_0.txt 1
```

#Fichier de sortie

**Le fichier de sortie (en CSV), contenant les résultats des réactions au temps voulu, est sous la forme *<mon_fichier_test.txt_output>*, présent dans *src*.**  
Deux scripts *gnuplot* est disponible pour tracer les courbes associés aux fichiers test *test_0.txt* et *test_1.txt*.  
Les scripts sont disponibles sous la forme : ```plot_test_0.txt``` et ```plot_test_1.txt```.

**Pour utiliser chacun de ces scripts, il est nécessaire de faire une sortie des *test_0.txt* et *test_1.txt*, et d'expliquer quel est l'ordre des espèces chimiques dans le fichier de sortie!**

La commande suivante affichera ainsi le graphe associé aux résultats de chacun des fichiers : ```gnuplot plot_test_0.txt```.
