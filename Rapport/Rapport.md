# Question 1

* 10
  * Temps: 00.02 secondes  
  ![Temps à 10](figures/q1_10.png)

* 1000
  * Temps: 00.15 secondes  
  ![Temps à 1000](figures/q1_1000.png)

* 100000
  * Temps: 35.90 secondes  
  ![Temps à 100000](figures/q1_100000.png)

* 1000000
  * Temps : 8:06.73 minutes
  ![Temps à 1000000](figures/q1_1000000.png)

# Question 2

* A(0) = 10
  * *t** = 7
* A(0) = 1000
  * *t** = 8
* A(0) = 100000
  * *t** = 8
* A(0) = 1000000
  * *t** = 7

Ainsi, *t* ne varie pas pour des réactions dont le nombre de molécules varie.
*t* est ainsi **constant** en nombre de molécules.

# Question 3

Le temps de calcul est **exponentiel**. Ainsi, il serai comparable au nombre de molécules d'*H2O* présents dans 1L d'eau.

# Question 4

Pour un nombre de molécules de 10⁵, voici une trace de la courbe.  

* k = 0.001  
  ![Temps à 0.01, k=0.001](figures/q4_100000_001.png)

* k = 0.002  
  ![Temps à 0.01, k=0.002](figures/q4_100000_002.png)

Nous remarquons que nous pouvons diviser par 2 le temps mis en oeuvre afin de d'arriver à A(0)/2, en multipliant la vitesse par 2.  
Ainsi, **la vitesse de réaction influe directement sur l'obtention du temps de "demi-vie de la réaction"**

# Question 5

* E = 10  
  ![E=10](figures/q5_100000_10.png)

* E = 1  
  ![E=1](figures/q5_100000_1.png)

* E = 0  
  ![E=0](figures/q5_100000_0.png)

Pour la dernière figure, le nombre de molécules pour les espèces *E* et *P* sont à 0.

# Question 6

Voici les temps associés aux simulations:

* 10
  * Temps: 00.01 seconde (**meilleur**)  
* 1000
  * Temps: 00.02 secondes (**meilleur**)
* 100000
  * Temps: 00.03 secondes (**meilleur**)
* 1000000
  * Temps : 00.17 secondes (**meilleur**)

Ainsi, COPASI détient une meilleure implémentation que le programme Python écrit.

# Question 7

Oui, il y a toujours une concordance avec *t* = 7.

# Question 8

Non plus, car le temps sera toujours exponentiel.  
Par contre, ce sera toujours mieux que d'utiliser mon programme Python...

# Question 9

Voici les comparaisons concernant les courbes entre la question 6 et la question 9:

* 10  
  ![Q6](figures/q6_10.png)  
  ![Q9](figures/q9_10.png)

* 1000  
  ![Q6](figures/q6_1000.png)  
  ![Q9](figures/q9_1000.png)

* 100000  
  ![Q6](figures/q6_100000.png)  
  ![Q9](figures/q9_100000.png)

* 10000000  
  ![Q6](figures/q6_10000000.png)  
  ![Q9](figures/q9_10000000.png)

* 10000000  
  ![Q6](figures/q6_100000000.png)  
  ![Q9](figures/q9_100000000.png)

On voit ainsi que la réaction a tendance a allé moins vite vers le 0 que pour la méthode directe.  
La différence entre les 2 méthodes est que le **tau-leaping** est une approximation de la méthode directe de Gillespie, prenant en compte des intervalles de temps plus grands que ceux calculés avec la méthode exacte, car approximé. Cela permet ainsi de consommer moins de temps à calculer les *tau*, et donc d'économiser du temps de calcul.

# Question 10

* k = 0.001  
  ![k=0.001](figures/q10_001.png)

* k = 0.002  
  ![k=0.002](figures/q10_002.png)

On pourra remarquer que, par rapport aux figures effectués dans l'exercice 4, les temps de demi-vie sont divisés par 2.  
Ainsi, le temps de demi-vie de la réaction avec k=0.001 est égal à celui de la réaction à k=0.002 pour l'exercice 4; et le temps de demi-vie de la réaction avec k=0.002 est égal à celui de la réaction à k=0.002, divisé par 2.

# Question 11

* k = 0.001  
  ![k=0.001](figures/q11_001.png)
  
* k = 0.002  
  ![k=0.002](figures/q11_002.png)

La différence entre cette simulation stochastique et celle effectuée avec ma propre implémentation est justement celle retrouvée avec la simulation effectuée en **question 10**.
