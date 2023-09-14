(carte-mere-mono)=

# Carte-mère monophasée

Plusieurs versions du PCB peuvent exister.

Bien qu'elles fonctionnent toutes de la même manière, chaque version offre plus de flexibilité que la précédente ainsi que quelques améliorations mineures, essentiellement des aspects pratiques (facilité d'accès des entrées/sorties de l’Arduino, ...).

## Soudure des composants

### Soudure des résistances

Ces composants n'ont pas de sens et sont très peu sensibles à l'électricité statique.

Les valeurs des résistances sont indiquées sur le schéma de circuit et sont répétées ici pour plus de commodité :
(veuillez lire les notes ci-dessous qui concernent ces valeurs de composants)

- **R1** = **47&nbsp;k&Omega;**. Cela fournit le "pull-up" pour la ligne de réinitialisation du processeur.
- **R2** = **10&nbsp;k&Omega;**. Avec R3, cela fournit une tension de référence pour les capteurs d'entrée.
- **R3** = **10&nbsp;k&Omega;**. Avec R2, cela fournit une tension de référence pour les capteurs d'entrée.
- **R4** = **100&nbsp;&Omega;** ou **180&nbsp;&Omega;**. R4 et R5 réduisent la taille du signal AC du transformateur.
- **R5** = **1&nbsp;k&Omega;**. R4 et R5 réduisent la taille du signal AC du transformateur.
- **R6** = **120&nbsp;&Omega;** ou **150&nbsp;&Omega;**. Il s'agit de la résistance de charge (ou *burden*) du capteur de courant *grille*, qui utilise CT1.
- **R7** = **120&nbsp;&Omega;** ou **150&nbsp;&Omega;**. Il s'agit de la résistance de charge pour le capteur de courant *détourné*, qui utilise CT2.
- **R8** = **1&nbsp;k&Omega;**. Cette résistance est en série avec CT1 pour protéger le processeur des signaux importants.

```{note}
Comme mentionné en haut de la page Notes techniques, des valeurs inférieures pour R4 et R5 sont désormais utilisées pour augmenter la charge sur le transformateur. Cela peut l'empêcher d'entrer en saturation, ce qui déformerait la forme d'onde de sortie.  
R4 = **100&nbsp;&Omega;** convient pour un fonctionnement en **3,3&nbsp;V**.  
Pour une meilleure utilisation de la plage d'entrée de l'ADC, R4 doit être augmenté à **180&nbsp;&Omega;** pour un fonctionnement en **5&nbsp;V**.

La valeur pour R6 et R7 a été initialement spécifiée comme étant **150&nbsp;&Omega;**.

Lorsque le processeur fonctionne à **3,3&nbsp;V**, cela donne une plage de fonctionnement d'environ **4&nbsp;kW**. En réduisant ces valeurs à **120&nbsp;&Omega;**, l'autonomie est augmentée à **~5&nbsp;kW**.

Pour un système **5&nbsp;V**, la valeur originale de **150&nbsp;&Omega;** donne une plage de fonctionnement d'environ **6&nbsp;kW**.

Si un enregistrement de données dans toute la maison est nécessaire, la plage de travail du capteur « grille » peut être augmentée en réduisant la valeur de R6. Il faut toutefois reconnaître que la sensibilité du système de mesure sera réduite d’autant.
- **R6** = **56&nbsp;&Omega;** permettra des mesures jusqu'à **~10&nbsp;kW**
- **R6** = **47&nbsp;&Omega;** permettra des mesures jusqu'à **~12&nbsp;kW**
- **R6** = **39&nbsp;&Omega;** permettra des mesures jusqu'à **~14&nbsp;kW**.

Ces valeurs de résistance de charge s'appliquent lorsque le processeur fonctionne à **3,3&nbsp;V**. S'il fonctionne à **5&nbsp;V**, ces plages sont augmentées d'environ **50&nbsp;%**.

**R11 - R18** sont les résistances série pour l'affichage à 4 chiffres.  
Si la carte doit fonctionner à **3,3&nbsp;V**, ces huit résistances doivent être de **220&nbsp;&Omega;**.  
En cas de fonctionnement en **5&nbsp;V**, cette valeur doit être augmentée à 470&nbsp;&Omega; pour maintenir un niveau de luminosité similaire.
```

### Soudure des diodes

Ensuite, les diodes peuvent être ajoutées.

Celles-ci offrent un certain degré de protection au processeur lorsque des courants élevés traversent les CTs.

```{warning}
Ces composants sont polarisés.

Ils doivent être placés selon le repérage sur la couche sérigraphiée.
```

### Support circuits intégrés

Ensuite, on installe généralement les supports pour les circuits intégrés.

Si l'option *pin-saving hardware* est utilisée, quatre circuits intégrés seront nécessaires (**IC1 - IC4**) ; sinon il n'y en aura que deux (**IC1** & **IC2**).
Cette distinction est expliquée plus en détail ultérieurement.

```{warning}
Chaque support a une encoche à une extrémité. Celle-ci doit être alignée avec la marque correspondante sur la couche sérigraphiée, comme indiqué ici.
```

Avec le support convenablement soutenu par le bas (on peut aussi utiliser un morceau d'adhésif), les deux broches situées dans les coins opposés peuvent être soudées en place.
Si un réalignement du composant est nécessaire, il doit être effectué avant que les broches restantes ne soient fixées.

L'affichage à 4 chiffres peut être contrôlé de deux manières.
Si le module RF n'est pas requis et que ces broches IO ne sont pas nécessaires à d'autres fins, un ensemble complet de broches IO sur le processeur peut être dédié au pilotage de l'affichage.
Cette configuration nécessite l'ajout de quatorze ponts comme indiqué dans la couche sérigraphiée. La planche de la photo suivante est assemblée de cette manière :

Les 14 ponts sont représentés ici :
- 5 ponts à **IC3** ;
- 1 pont à **IC4** ;
- 5 ponts en **J1-5** ;
- 1 pont en **R24** ;
- 1 pont en **R25** ;
- 1 pont en **R26** ;

Si le module RF est requis (ou si l'une de ces broches IO est nécessaire à toute autre fin), l'écran peut être utilisé à l'aide de l'option *pin-saving hardware*.
Pour cette disposition, les supports pour **IC3** et **IC4** doivent être installés comme indiqué ci-dessous.

Ici, l'un des PCB d'origine est présenté avec uniquement ces supports en place, pour **IC3** et **IC4**.

```{note}
Lorsque l'option *pin-saving hardware* est utilisée, aucune liaison filaire ne doit être installée au niveau du connecteur **J1-J5**.
```

Étant donné que cette carte est assemblée avec l'option *pin-saving hardware*, des supports d'embase ont été installés aux quatre emplacements de circuits intégrés.

```{note}
Les deux circuits intégrés qui composent l'option *pin-saving hardware* ont tous deux été initialement spécifiés à partir de la série **74HC**.

Malheureusement, le **74HC4543** pour **IC3** n'est plus disponible sous forme DIL. Lorsqu'elle fonctionne à **3,3&nbsp;V**, le composant CMOS de remplacement n'est pas en mesure de fonctionner correctement.

Ainsi, chaque fois que l'option *pin-saving hardware* doit être utilisée, le processeur doit fonctionner à **5&nbsp;V**.
```

### Condensateurs céramiques et oscillateur

Ces composants ne sont pas polarisés.

Les condensateurs céramiques sont en général orange, et ont la forme d'une goutte d'eau, par opposition aux condensateurs électrolytiques polarisés de forme cylindriques et bleus ou noirs.

```{note}
Parmi le jeu de condensateurs céramiques, deux d'entre eux sont plus petits que les autres.

Il s'agit des deux condensateurs associés à l'oscillateur, leur valeur est de **22&nbsp;pF** et sont référencés **C6** et **C7**.

**C3**, **C4** et **C5** sont des condensateurs céramiques de **100&nbsp;nF**, généralement marqués *104*.
```

```{note}
L'oscillateur ainsi que ses deux condensateurs associés peuvent être soudés légèrement au-dessus du PCB.  
Ce n'est pas nécessaire pour le bon fonctionnement.  
Pour se faire, on pourra utiliser une allumette le temps d'effectuer la soudure.
```

### Pont redresseur ou pont de diodes

Le rôle de ce composant est de redressé le courant alternatif fourni par le transformateur.  
C'est la première étape nécessaire pour obtenir une alimentation en courant continu.

Sur la figure ci-après, la courbe du haut correspond à la tension fournie par le transformateur.  
La courbe du bas est la tension fournie par le redresseur.

```{figure} img/Redresseur_monophase.png
:alt: Redressement double alternance
:align: center
:scale: 50%

Redressement double alternance
```

```{warning}
Ce composant est polarisé.  
Il faudra bien veiller à faire correspondre le marquage sur le boîtier avec celui de la couche sérigraphiée.
```

La broche la plus longue correspond au *+*.

Comme pour l'oscillateur, il est courant de le souder légèrement au dessus du PCB.

### Connecteurs SIL/Molex/Embase 14 broches

Les connecteurs Molex ainsi que l'embase 14 broches sont "polarisés", ils possèdent un détrompeur.  
Physiquement, ce sont des composants passifs, mais étant donné qu'ils serviront à la connection d'autres composants polarisés, il est important de les souder selon le marquage sur la couche sérigraphiée.

Les connecteurs SIL, ou *pin header*, peuvent être soudés dans n'importe quel sens.

### Condensateurs électrolytiques

Les deux condensateurs électrolytiques, **C1** et **C2**, sont polarisés et doivent donc être installés dans le bon sens.
La broche -ve est indiquée par une bande proéminente, en général blanche, sur toute la longueur du composant.

L'autre broche est la +ve, qui doit aller dans le trou marqué '+' sur la couche sérigraphiée.

```{warning}
Bien qu’ils se ressemblent assez, il est important que ces deux condensateurs soient installés aux bons endroits.

Le plus grand condensateur (**C1** = **100&nbsp;μF**) est le plus proche du pont redresseur.  
Le plus petit (**C2** = **10&nbsp;μF**) est le plus proche de **IC2**.

Si ces deux composants sont inversés, les symptômes qui en résultent peuvent être difficiles à diagnostiquer.
```

### Connecteurs secteur et fusible

Les connecteurs secteur (**TB1** & **TB2**) et le porte-fusible (**FS1**) peuvent maintenant être installés.  
En raison des pistes du plan masse, la broche centrale de **TB1** nécessitera plus de chaleur que les autres broches.
Ces borniers doivent être orientés correctement pour permettre un accès facile au câblage.  
Il est trop facile de se tromper de sens !

Si cela se produit, le plastique peut être soigneusement coupé avec un couteau et chaque broche extraite séparément.

Le porte-fusible, accompagné de son fusible de **100&nbsp;mA**, est simple à mettre en place.

### Régulateur de tension

Le régulateur de tension (**VR1**) doit être monté avec son ailette métallique éloignée du transformateur comme indiqué sur la sérigraphie.  
Selon l'application, le **VR1** sera une version 3,3&nbsp;V ou 5&nbsp;V.  
5&nbsp;V est nécessaire chaque fois que l'option *pin-saving hardware* est utilisée.

Souder les broches du **VR1** nécessitera probablement plus de chaleur.
Pour réduire la quantité de métal à chauffer, il est possible de prédécouper ces broches à la longueur requise.

### Transformateur

Le dernier composant à installer est le transformateur. Il s'agit généralement d'un appareil double **6&nbsp;V** comme indiqué sur la couche sérigraphiée.  
Un transformateur de **6&nbsp;V** peut prendre en charge un régulateur de tension de **3,3&nbsp;V** ou de **5&nbsp;V**.

```{important}
Lors du montage de ce composant, il ne doit y avoir aucun espace entre la base du transformateur et le PCB.
```

## Test

Une fois le transformateur en place, la carte est maintenant prête pour les tests électriques.  

C'est le bon moment pour vérifier que tous les joints soudés sont en bon état et que toutes les éclaboussures de soudure ont été éliminées.

Avant d'installer les circuits intégrés, le fonctionnement de l'alimentation doit être vérifié.

```{danger}
**Alerte de sécurité**
Pour poursuivre cette séquence de construction, un accès à la tension secteur **230&nbsp;V** est requis.

Veuillez ne pas passer à cette étape suivante à moins que vous soyez compétent pour le faire.
```