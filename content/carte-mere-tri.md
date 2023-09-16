(carte-mere-tri)=

# Carte-mère triphasée

Plusieurs versions du PCB peuvent exister.

Bien qu'elles fonctionnent toutes de la même manière, chaque version offre plus de flexibilité que la précédente ainsi que quelques améliorations mineures, essentiellement des aspects pratiques (facilité d'accès des entrées/sorties de l’Arduino, ...).

## Soudure des composants

### Résistances

Ces composants n'ont pas de sens et sont très peu sensibles à l'électricité statique.

Les valeurs des résistances sont indiquées sur le schéma de circuit et sont répétées ici pour plus de commodité :
(veuillez lire les notes ci-dessous qui concernent ces valeurs de composants)

- **R1** = **47&nbsp;k&Omega;**. Cela fournit le *pull-up* pour la ligne de réinitialisation du processeur.
- **R2-R4** = **100&nbsp;&Omega;** ou **180&nbsp;&Omega;**. **R2-R5** réduisent la taille du signal AC de chaque transformateur.
- **R5-R7** = **1&nbsp;k&Omega;**. Elles réduisent la taille du signal AC de chaque transformateur.
- **R8-R10** = **120&nbsp;&Omega;** ou **150&nbsp;&Omega;** en général. Il s'agit des résistances de charge (ou *burden*) de chaque capteur de courant *grille*, qui utilisent **CT1-CT3**.
- **R11-R12** = **10&nbsp;k&Omega;**. Ensemble, elles fournissent une tension de référence pour les capteurs d'entrée.
- **R19-R21** = **1&nbsp;k&Omega;**. Elles réduisent la taille du signal AC de chaque transformateur.
- **R22** = **1&nbsp;M&Omega;**. Cela fournit le *pull-up* pour la ligne de réinitialisation du processeur.

`````{note}
Comme mentionné en haut de la page Notes techniques, des valeurs inférieures pour **R2-R4** et **R5-R7** sont désormais utilisées pour augmenter la charge sur le transformateur.
Cela peut l'empêcher d'entrer en saturation, ce qui déformerait la forme d'onde de sortie.  
**R2-R4** = **100&nbsp;&Omega;** convient pour un fonctionnement en **3,3&nbsp;V**.  
Pour une meilleure utilisation de la plage d'entrée de l'ADC, **R2-R4** doit être augmenté à **180&nbsp;&Omega;** pour un fonctionnement en **5&nbsp;V**.

La valeur pour **R8-R10** a été initialement spécifiée comme étant **150&nbsp;&Omega;**.

Lorsque le processeur fonctionne à **3,3&nbsp;V**, cela donne une plage de fonctionnement d'environ **4&nbsp;kW**. En réduisant ces valeurs à **120&nbsp;&Omega;**, la plage est augmentée à **~5&nbsp;kW**.

Pour un système **5&nbsp;V**, la valeur originale de **150&nbsp;&Omega;** donne une plage de fonctionnement d'environ **6&nbsp;kW**.

Ces valeurs de résistance de charge s'appliquent lorsque le processeur fonctionne à **3,3&nbsp;V**. S'il fonctionne à **5&nbsp;V**, ces plages sont augmentées d'environ **50&nbsp;%**.

Ces puissances s'entendent sur chaque phase.

````{exercise} Un peu de mathématiques
Voici les 3 formules qui vous permettront de calculer une inconnue à partir des 2 autres données connues.

> Calcul de la résistance de burden en fonction de l'intensité efficace maximale :
> ```{math}
> burden\_resistor = {system\_voltage * ct\_turns \over 2 * \sqrt{2} * I_{RMS}}
> ```

> Calcul de l'intensité efficace maximale en fonction de la résistance de burden :
> ```{math}
> I_{RMS} = {system\_voltage * ct\_turns \over 2 * \sqrt{2} * burden\_resistor }
> ```

> Calcul du nombre de tours de capteur en fonction de la résistance de burden et de l'intensité efficace maximale :
> ```{math}
> ct\_turns = {2 * \sqrt{2} * I_{RMS} \over system\_voltage * burden\_resistor}
> ```


Dans notre cas précis, nous avons : {math}`ct\_turns = 2000`

**{math}`I_{RMS}`** correspond à l'intensité efficace.  
Pour un appareil purement résistif (chauffe-eau, ...), nous avons {math}`P_{RMS} = V_{RMS} * I_{RMS}`.  

Exemple pour un chauffe-eau de 3000&nbsp;W, nous aurons donc 
```{math}
I_{RMS} = {P_{RMS} \over V_{RMS}} = {3000 \over 230} = 13 A.
```
````

`````

### Diodes

Ensuite, les diodes peuvent être ajoutées.

Celles-ci offrent un certain degré de protection au processeur lorsque des courants élevés traversent les CTs.

```{warning}
Ces composants sont polarisés.  
Ils doivent être placés selon le repérage sur la couche sérigraphiée.
```

### Supports circuits intégrés

Ensuite, on installe généralement les supports pour les circuits intégrés.

```{warning}
Chaque support a une encoche à une extrémité. Celle-ci doit être alignée avec la marque correspondante sur la couche sérigraphiée, comme indiqué ici.
```

Avec le support convenablement soutenu par le bas (on peut aussi utiliser un morceau d'adhésif), les deux broches situées dans les coins opposés peuvent être soudées en place.
Si un réalignement du composant est nécessaire, il doit être effectué avant que les broches restantes ne soient fixées.

### Condensateurs céramiques et oscillateur

Ces composants ne sont pas polarisés.

Les condensateurs céramiques sont en général orange, et ont la forme d'une goutte d'eau, par opposition aux condensateurs électrolytiques polarisés de forme cylindriques et bleus ou noirs.

```{note}
Parmi le jeu de condensateurs céramiques, deux d'entre eux sont plus petits que les autres.

Il s'agit des deux condensateurs associés à l'oscillateur, leur valeur est de **22&nbsp;pF** et sont référencés **C10** et **C11**.

**C4** et **C6-C9** sont des condensateurs céramiques de **100&nbsp;nF**, généralement marqués *104*.
```

```{note}
L'oscillateur ainsi que ses deux condensateurs associés peuvent être soudés légèrement au-dessus du PCB.  
Ce n'est pas nécessaire pour le bon fonctionnement.  
Pour se faire, on pourra utiliser une allumette le temps d'effectuer la soudure.
```

### Ponts redresseur ou ponts de diodes

Le rôle de ce composant est de redressé le courant alternatif fourni par le transformateur.  
C'est la première étape nécessaire pour obtenir une alimentation en courant continu.

Sur la figure ci-après, la courbe du haut correspond à la tension fournie par le transformateur.  
La courbe du bas est la tension fournie par le redresseur.

```{figure} img/Redresseur_monophase.png
:alt: Redressement double alternance monophasé
:align: center
:scale: 50%

Redressement double alternance monophasé
```

Sur la version triphasée de ce routeur, ils sont au nombre de trois, un par phase.  

```{note}
Il aurait été possible de réaliser un redresseur double alternance triphasé. Ce type de redresseur ne nécessite que six diodes.
Il y a cependant deux inconvénients :
- un tel composant est relativement cher, plus de 3x de prix d'un redresseur standard.
- la tension moyenne résultante est plus de 2 fois la tension moyenne de chaque entrée. Cela engendre un surcroît de "*travail*" du régulateur de tension qui chauffera bien plus.
```

```{warning}
Ces composants sont polarisés.  
Il faudra bien veiller à faire correspondre le marquage sur le boîtier avec celui de la couche sérigraphiée.
```

La broche la plus longue correspond au **+**.

Comme pour l'oscillateur, il est courant de les souder légèrement au dessus du PCB.

### Connecteurs SIL/Molex

Les connecteurs Molex sont *polarisés*, ils possèdent un détrompeur.  
Physiquement, ce sont des composants passifs, mais étant donné qu'ils serviront à la connection d'autres composants ou modules polarisés, il est important de les souder selon le marquage sur la couche sérigraphiée.

Les connecteurs SIL, ou *pin header*, peuvent être soudés dans n'importe quel sens.

### Inductance

Ce composant n'est pas polarisé. Il est référencé **L1**, à proximité de l'**ATmega328-P**.

### Condensateurs électrolytiques

Les deux condensateurs électrolytiques, **C1** et **C2**, sont polarisés et doivent donc être installés dans le bon sens.
La broche **-ve** est indiquée par une bande proéminente, en général blanche, sur toute la longueur du composant.

L'autre broche est la **+ve**, qui doit aller dans le trou marqué **+** sur la couche sérigraphiée.

```{warning}
Bien qu’ils se ressemblent assez, il est important que ces deux condensateurs soient installés aux bons endroits.

Le plus grand condensateur (**C1** = **100&nbsp;μF**) est le plus proche du bord du PCB.  
Le plus petit (**C2** = **10&nbsp;μF**) est le plus proche de **VR1**.

Si ces deux composants sont inversés, les symptômes qui en résultent peuvent être difficiles à diagnostiquer.
```

### Ponts de neutre

Pour un raccordement triphasé **avec** neutre, il est possible de ponter le neutre entre chacune des 3 sous-alimentions.  
Les deux ponts sont référencés "**N**", entre les transformateurs.   
De cette façon, il ne sera pas nécessaire d'introduire un fil de neutre dans chaque connecteur secteur, un seul suffira.

```{warning}
Pour un raccordement triphasé **sans** neutre, essentiellement le 3&nbsp;*&nbsp;230&nbsp;V en **Belgique**, il ne faudra pas souder ces ponts.
```

### Connecteurs secteur et porte-fusible

Les connecteurs secteur (**PWR1-PWR3**) et les porte-fusible (**FS1-FS3**) peuvent maintenant être installés.  
En raison des pistes du plan masse, les broches référencées **PE** sur chacun des connecteurs nécessitera plus de chaleur que les autres broches.
Ces borniers doivent être orientés correctement pour permettre un accès facile au câblage.  
Il est très facile de se tromper de sens !

Si cela se produit, le plastique peut être soigneusement coupé avec un couteau et chaque broche extraite séparément.

Les porte-fusible, accompagnés de leur fusible de **100&nbsp;mA**, sont simples à mettre en place.

### Régulateur de tension

Le régulateur de tension (**VR1**) doit être monté avec son ailette métallique éloignée du transformateur comme indiqué sur la sérigraphie.  
Selon l'application, le **VR1** sera une version 3,3&nbsp;V ou 5&nbsp;V.  
5&nbsp;V est nécessaire chaque fois que l'option *pin-saving hardware* est utilisée.

Souder les broches du **VR1** nécessitera probablement plus de chaleur.
Pour réduire la quantité de métal à chauffer, il est possible de prédécouper ces broches à la longueur requise.

### Transformateurs

Les derniers composants à installer sont les transformateurs. Il s'agit généralement d'un appareil double **6&nbsp;V** comme indiqué sur la couche sérigraphiée.  
Chacun des transformateurs de **6&nbsp;V** peut prendre en charge un régulateur de tension de **3,3&nbsp;V** ou de **5&nbsp;V**.

```{important}
Lors du montage de ces composants, il ne doit y avoir aucun espace entre la base du transformateur et le PCB.
```

## Tests électriques

Une fois les transformateurs en place, la carte est maintenant prête pour les tests électriques.  

C'est le bon moment pour vérifier que tous les joints soudés sont en bon état et que toutes les éclaboussures de soudure ont été éliminées.

### Test de chaque sous-alimentation

Avant d'installer les circuits intégrés, le fonctionnement de l'alimentation doit être vérifié.

```{danger}
**Alerte de sécurité**
Pour poursuivre cette séquence de construction, un accès à la tension secteur **230&nbsp;V** est requis.

Veuillez ne pas passer à cette étape suivante à moins que vous soyez compétent pour le faire.
```

Nous effectuerons les tests suivants en alimentant le routeur via chacun des connecteurs secteur, l'un après l'autre.  
Ainsi, si une tension est incorrecte, il sera plus facile d'identifier la partie du circuit qui est défectueuse.

Si tout a été correctement assemblé, la sortie de l’alimentation devrait être d’environ 3,3&nbsp;Volts... ou 5&nbsp;V si un régulateur de tension 5&nbsp;V a été installé.

Cette tension peut être facilement vérifiée au niveau du point de test **Test VCC**, ainsi que **Test GND**, comme indiqué ici.

À l'exception du transformateur, qui peut sembler légèrement chaud après plusieurs minutes, aucun des composants de la carte ne doit présenter d'augmentation notable de la température.

### Insertion du LM358 et test de Vref

Avec la tension correcte en place, les circuits intégrés peuvent maintenant être installés, après avoir coupé l'alimentation.

Le premier d’entre eux est LM358.  
Il s'agit d'un amplificateur opérationnel qui fournit une tension de référence intermédiaire pour les capteurs de tension et de courant.

Avec les packs Dual-in-Line, les broches devront peut-être être légèrement pliées vers l'intérieur pour s'insérer dans l'embase.
Cela peut être fait en *faisant rouler* doucement la puce de chaque côté, tour à tour.

Pour minimiser les risques de dommages électriques, cette opération doit être effectuée sur une surface protectrice telle qu'un sac antistatique.

Avec les broches bien alignées, le circuit intégré peut être délicatement placé sur son connecteur, comme indiqué ici.

```{warning}
Les circuits intégrés doivent être installés dans le bon sens. Le point sur la puce doit être aligné avec l'encoche de l'image sérigraphiée.
```

Une fois que tout a été soigneusement vérifié, la puce peut être enfoncée fermement.

Avec **LM358** en place et la carte alimentée à nouveau, la référence de tension peut être mesurée.  
**Vref** doit être environ la moitié de la tension d'alimentation. Ici, nous testons une carte **3,3&nbsp;V**.

Cette tension est accessible via le point de test **Test Vref** juste en dessous du **LM358**.

### Insertion du processeur principal

Le processeur principal, **ATmega328-P**, est installé de la même manière que pour **LM358**, toujours après avoir couper l'alimentation.
Avec autant de broches, il est très facile pour l’une d’entre elles de se plier en dessous.

```{warning}
Si ce circuit intégré est dans le mauvais sens lors de la mise sous tension, il ne fonctionnera probablement plus jamais !
```

## Test logiciel

Une fois le processeur en place, il peut être judicieux de vérifier que l'alimentation électrique est toujours correcte.  
En supposant que ce soit le cas, exécutons un croquis (programme) pour déterminer si le processeur fonctionne.

Pour cette prochaine étape, un dispositif de programmation adapté devra être mis en place.  
Des détails sur la configuration de l'environnement de développement intégré (IDE) Arduino peuvent être trouvés en haut de cette page.  
Un programmateur USB vers UART devra être branché sur le connecteur **FTDI** du PCB comme indiqué ci-dessous.  
L'autre extrémité du programmateur doit être connectée via un câble USB approprié à l'installation de programmation (PC ou équivalent).

La broche à une extrémité du connecteur à 6 voies du programmateur sera étiquetée **Gnd**. Cette broche doit correspondre au marquage **0&nbsp;V** sur le PCB.

Ici, le programmeur FTDI est utilisé. Notez qu'il doit être monté dans l'autre sens.
La broche **Gnd** doit toujours être la plus proche du bord de la carte

Pour éviter de tordre le connecteur du programmateur, on peut fabriquer un simple câble d'extension comme indiqué ici.
Seules quatre des lignes sont réellement utilisées (données **Tx** & **Rx**, masse et réinitialisation).  
Aucune des lignes d'alimentations électriques n'est utilisée par cette carte.

Le fil noir est destiné à la connexion **GND** (ou **0&nbsp;V**).

```{note}
La carte FTDI ne permet pas d'alimenter la carte-mère.

Le routeur devra toujours être alimenté par sa propre alimentation.
```

### Test de la partie *mesures*

```{note}
À partir de maintenant, une alimentation triphasée devra être fournie à la carte-mère.
```

Chaque transformateur a deux sorties : l'une pour l'alimentation CC, l'autre pour le capteur de tension CA qui devrait déjà fonctionner.  
Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (ATmega328-P).

Le programme, qui se trouve également sur la page Téléchargements, est : RawSamplesTool_6chan.ino

Après avoir téléchargé ce croquis sur le processeur via l'IDE Arduino, la fenêtre série (icône en forme de loupe) doit être ouverte.  
Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère "**g**", suivi de *Entrée*.

Le programme *RawSamplesTool_6chan* affiche les échantillons des trois tensions alternatives et de courant pour un ou plusieurs cycles secteur complets.  
Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3&nbsp;kW avec le CT branché sur CT2.  
Lorsque le CT a été déplacé vers le port **CT1**, la sortie résultante semblait presque identique, mais avec les caractères "**1**" et "**2**" inversés.

RSResults_V_and_I2.txt

Si aucun signal n'est disponible sur les ports **CT1-CT3**, les formes d'onde de ces canaux seront toutes deux des lignes droites.  
Seuls les signaux de tension afficheront un aspect sinusoïdal.  
Pour vérifier le fonctionnement des ports **CT1-CT3** pendant que le PCB est testé sur le banc, un câblage adapté sera nécessaire.

### Test des sorties
