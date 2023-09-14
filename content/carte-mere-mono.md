(carte-mere-mono)=

# Carte-mère monophasée

Plusieurs versions du PCB peuvent exister.

Bien qu'elles fonctionnent toutes de la même manière, chaque version offre plus de flexibilité que la précédente ainsi que quelques améliorations mineures, essentiellement des aspects pratiques (facilité d'accès des entrées/sorties de l’Arduino, ...).

## Soudure des résistances

Ces composants n'ont pas de sens et sont très peu sensibles à l'électricité statique.

Les valeurs des résistances sont indiquées sur le schéma de circuit et sont répétées ici pour plus de commodité :
(veuillez lire les notes ci-dessous qui concernent ces valeurs de composants)

- R1 = 47 k&Omega;. Cela fournit le "pull-up" pour la ligne de réinitialisation du processeur.
- R2 = 10 k&Omega;. Avec R3, cela fournit une tension de référence pour les capteurs d'entrée.
- R3 = 10 k&Omega;. Avec R2, cela fournit une tension de référence pour les capteurs d'entrée.
- R4 = 100 &Omega; ou 180 &Omega;. R4 et R5 réduisent la taille du signal AC du transformateur.
- R5 = 1 k&Omega;. R4 et R5 réduisent la taille du signal AC du transformateur.
- R6 = 120 &Omega; ou 150 &Omega;. Il s'agit de la résistance de charge du capteur de courant *grille*, qui utilise CT1.
- R7 = 120 &Omega; ou 150 &Omega;. Il s'agit de la résistance de charge pour le capteur de courant *détourné*, qui utilise CT2.
- R8 = 1 k&Omega;. Cette résistance est en série avec CT1 pour protéger le processeur des signaux importants.

```{note}
Comme mentionné en haut de la page Notes techniques, des valeurs inférieures pour R4 et R5 sont désormais utilisées pour augmenter la charge sur le transformateur. Cela peut l'empêcher d'entrer en saturation, ce qui déformerait la forme d'onde de sortie. R4 = 100 &Omega; convient pour un fonctionnement en 3,3V. Pour une meilleure utilisation de la plage d'entrée de l'ADC, R4 doit être augmenté à 180 &Omega; pour un fonctionnement en 5V.

La valeur pour R6 et R7 a été initialement spécifiée comme étant 150 &Omega;. Lorsque le processeur fonctionne à 3,3V, cela donne une plage de fonctionnement d'environ 4 kW. En réduisant ces valeurs à 120R, l'autonomie est augmentée à ~5 kW. Pour un système 5V, la valeur originale de 150 &Omega; donne une plage de fonctionnement d'environ 6 kW.

Si un enregistrement de données dans toute la maison est nécessaire, la plage de travail du capteur « grille » peut être augmentée en réduisant la valeur de R6. Il faut toutefois reconnaître que la sensibilité du système de mesure sera réduite d’autant.

R6 = 56 &Omega; permettra des mesures jusqu'à ~10 kW
R6 = 47 &Omega; permettra des mesures jusqu'à ~12 kW
R6 = 39 &Omega; permettra des mesures jusqu'à ~14 kW.

Ces valeurs de résistance de charge s'appliquent lorsque le processeur fonctionne à 3,3V. S'il fonctionne à 5V, ces plages sont augmentées d'environ 50 %.

R11 - R18 sont les résistances série pour l'affichage à 4 chiffres. Si la carte doit fonctionner à 3,3V, ces huit résistances doivent être de 220 &Omega;. En cas de fonctionnement en 5V, cette valeur doit être augmentée à 470 &Omega; pour maintenir un niveau de luminosité similaire.
```

## Soudure des diodes
