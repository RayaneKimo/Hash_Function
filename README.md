# Hash_Function
![image](https://user-images.githubusercontent.com/85368764/201329418-7835d670-2280-4275-ab59-eb10a9be09c5.png)

# Principe :
- Il existe 3 intervalles possibles pour nos valeurs de sortie [A-Z] , [0,9], [a-z] qui sont équivalent aux codes ASCII suivant : [48-57], [65,90], [97,122]
- Pour introduire le principe qu'un petit changement en entrée engendre un énorme changement en sortie , on fait le produit au début du HASH tous les codes ASCII > 0  de mon message ( c'est comme si on est entrain de calculer une métrique,  si on ajoute , modifie ou supprime un caractère n'importe où sur notre chaîne , ce produit va être affecté )
- Ensuite on fait 18 itérations (pour créer un hash de longueur fixe ),tel que chaque itération est responsable de calculer le résultat d'un seul bloc du hash, en essayant à chaque fois trouver une valeur dans un des 3 intervalles [48-57], [65,90], [97,122], tel que :
   * Si ASCII < 58 Alors on normalise dans [48, 58]  ( son hash est un chiffre)
   * Si ASCII dans ]58, 91] alors on normalise dans [65, 91]   ( son hash est une Majuscule )
   * Si ASCII dans ]91, 122] alors on normalise dans [97, 122] ( son hash est une Minuscu )
