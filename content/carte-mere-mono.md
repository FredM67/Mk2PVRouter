(carte-mere-mono)=

# Carte-mère monophasée

Plusieurs versions du PCB peuvent exister.

Bien qu'elles fonctionnent toutes de la même manière, chaque version offre plus de flexibilité que la précédente ainsi que quelques améliorations mineures, essentiellement des aspects pratiques (facilité d'accès des entrées/sorties de l’Arduino, ...).

## Soudure des résistances

Ces composants n'ont pas de sens et sont très peu sensibles à l'électricité statique.

Les valeurs des résistances sont indiquées sur le schéma de circuit et sont répétées ici pour plus de commodité :
(veuillez lire les notes ci-dessous qui concernent ces valeurs de composants)

- **R1** = **47&nbsp;k&Omega;**. Cela fournit le "pull-up" pour la ligne de réinitialisation du processeur.
- **R2** = **10&nbsp;k&Omega;**. Avec R3, cela fournit une tension de référence pour les capteurs d'entrée.
- **R3** = **10&nbsp;k&Omega;**. Avec R2, cela fournit une tension de référence pour les capteurs d'entrée.
- **R4** = **100&nbsp;&Omega;** ou **180&nbsp;&Omega;**. R4 et R5 réduisent la taille du signal AC du transformateur.
- **R5** = **1&nbsp;k&Omega;**. R4 et R5 réduisent la taille du signal AC du transformateur.
- **R6** = **120&nbsp;&Omega;** ou **150&nbsp;&Omega;**. Il s'agit de la résistance de charge du capteur de courant *grille*, qui utilise CT1.
- **R7** = **120&nbsp;&Omega;** ou **150&nbsp;&Omega;**. Il s'agit de la résistance de charge pour le capteur de courant *détourné*, qui utilise CT2.
- **R8** = **1&nbsp;k&Omega;**. Cette résistance est en série avec CT1 pour protéger le processeur des signaux importants.

```{note}
Comme mentionné en haut de la page Notes techniques, des valeurs inférieures pour R4 et R5 sont désormais utilisées pour augmenter la charge sur le transformateur. Cela peut l'empêcher d'entrer en saturation, ce qui déformerait la forme d'onde de sortie. R4 = 100&nbsp;&Omega; convient pour un fonctionnement en **3,3&nbsp;V**. Pour une meilleure utilisation de la plage d'entrée de l'ADC, R4 doit être augmenté à 180&nbsp;&Omega; pour un fonctionnement en **5&nbsp;V**.

La valeur pour R6 et R7 a été initialement spécifiée comme étant **150&nbsp;&Omega;**. Lorsque le processeur fonctionne à **3,3&nbsp;V**, cela donne une plage de fonctionnement d'environ **4&nbsp;kW**. En réduisant ces valeurs à **120&nbsp;&Omega;**, l'autonomie est augmentée à **~5&nbsp;kW**. Pour un système **5&nbsp;V**, la valeur originale de **150&nbsp;&Omega;** donne une plage de fonctionnement d'environ **6&nbsp;kW**.

Si un enregistrement de données dans toute la maison est nécessaire, la plage de travail du capteur « grille » peut être augmentée en réduisant la valeur de R6. Il faut toutefois reconnaître que la sensibilité du système de mesure sera réduite d’autant.
- **R6** = **56&nbsp;&Omega;** permettra des mesures jusqu'à **~10&nbsp;kW**
- **R6** = **47&nbsp;&Omega;** permettra des mesures jusqu'à **~12&nbsp;kW**
- **R6** = **39&nbsp;&Omega;** permettra des mesures jusqu'à **~14&nbsp;kW**.

Ces valeurs de résistance de charge s'appliquent lorsque le processeur fonctionne à **3,3&nbsp;V**. S'il fonctionne à **5&nbsp;V**, ces plages sont augmentées d'environ **50&nbsp;%**.

R11 - R18 sont les résistances série pour l'affichage à 4 chiffres. Si la carte doit fonctionner à **3,3&nbsp;V**, ces huit résistances doivent être de **220&nbsp;&Omega;**. En cas de fonctionnement en **5&nbsp;V**, cette valeur doit être augmentée à 470&nbsp;&Omega; pour maintenir un niveau de luminosité similaire.
```

## Soudure des diodes

Ensuite, les diodes peuvent être ajoutées.

Celles-ci offrent un certain degré de protection au processeur lorsque des courants élevés traversent les CTs.

```{warning}
Ces composants sont polarisés.
Ils doivent être placés selon le repérage sur la couche sérigraphiée.
```

## Support circuits intégrés

Ensuite, on installe généralement les supports pour les circuits intégrés.

Si l'option *pin-saving hardware* est utilisée, quatre circuits intégrés seront nécessaires (IC1 - IC4) ; sinon il n'y en aura que deux (IC1 & IC2).
Cette distinction est expliquée plus en détail ultérieurement.

Chaque support a une encoche à une extrémité. Celle-ci doit être alignée avec la marque correspondante sur la couche sérigraphiée, comme indiqué ici.

Avec le support convenablement soutenue par le bas (on peut aussi utilisé un morceau d'adhésif), les deux broches situées dans les coins opposés peuvent être soudées en place.
Si un réalignement du composant est nécessaire, il doit être effectué avant que les broches restantes ne soient fixées.

L'affichage à 4 chiffres peut être contrôlé de deux manières.
Si le module RF n'est pas requis et que ces broches IO ne sont pas nécessaires à d'autres fins, un ensemble complet de broches IO sur le processeur peut être dédié au pilotage de l'affichage.
Cette configuration nécessite l'ajout de quatorze ponts comme indiqué dans la couche sérigraphiée. La planche de la photo suivante est assemblée de cette manière :

Les 14 ponts sont représentés ici :
- 5 ponts à IC3 ;
- 1 pont à IC4 ;
- 5 ponts en J1-5 ;
- 1 pont en R24 ;
- 1 pont en R25 ;
- 1 pont en R26 ;

Si l'installation RF est requise (ou si l'une de ces broches IO est nécessaire à toute autre fin), l'écran peut être utilisé à l'aide de l'option *pin-saving hardware*.
Pour cette disposition, les supports pour IC3 et IC4 doivent être installés comme indiqué ci-dessous.

Ici, l'un des PCB d'origine est présenté avec uniquement ces supports en place, pour IC3 et IC4.

```{note}
Lorsque l'option *pin-saving hardware* est utilisée, aucune liaison filaire ne doit être installée au niveau du connecteur J1-J5.
```

Étant donné que cette carte est assemblée avec l'option *pin-saving hardware*, des supports d'embase ont été installés aux quatre emplacements de circuits intégrés.

```{note}
Les deux circuits intégrés qui composent l'option *pin-saving hardware* ont tous deux été initialement spécifiés à partir de la série 74HC.

Malheureusement, le 74HC4543 pour IC3 n'est plus disponible sous forme DIL. Lorsqu'elle fonctionne à 3,3&nbsp;V, le composant CMOS de remplacement n'est pas en mesure de fonctionner correctement.

Ainsi, chaque fois que l'option *pin-saving hardware* doit être utilisée, le processeur doit fonctionner à 5&nbsp;V.
```

