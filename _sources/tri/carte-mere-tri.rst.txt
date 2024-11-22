.. _carte-mere-tri:

Carte-mère triphasée
====================

Plusieurs versions du :term:`PCB` peuvent exister.

Bien qu’elles fonctionnent toutes de la même manière, chaque nouvelle version offre plus de flexibilité que la précédente ainsi que quelques améliorations mineures, essentiellement des aspects pratiques (facilité d’accès des entrées/sorties de l’Arduino…).

.. hint::
   | Après chaque étape, il conviendra de vérifier les soudures effectuées (l’utilisation d’une loupe facilitera la vérification).
   | Ensuite, on pourra couper **à ras** toutes les pattes qui dépassent avec une petite pince coupante afin de faire place nette pour l’étape suivante.

.. contents:: Sommaire
   :local:
   :depth: 1
   
-------------

Soudure des composants
----------------------

Résistances
~~~~~~~~~~~

Ces composants n’ont pas de sens et sont très peu sensibles à l’électricité statique.

Les valeurs des résistances sont indiquées sur le schéma de circuit et sont répétées ici pour plus de commodité :
(veuillez lire les notes ci-dessous qui concernent ces valeurs de composants)

* **R1** = **47 kΩ**. Cela fournit le :term:`pull-up` pour la ligne de réinitialisation du processeur.
* **R2-R4** = **100 Ω** ou **180 Ω**. Elles réduisent la taille du signal :term:`AC` de chaque transformateur.
* **R5-R7** = **1 kΩ**. Elles réduisent la taille du signal :term:`AC` de chaque transformateur.
* **R8-R10** = **120 Ω** ou **150 Ω** en général. Il s’agit des résistances de charge (ou :term:`burden`) de chaque capteur de courant *grille*, qui utilisent :term:`CT`\1 - :term:`CT`\3.
* **R11-R12** = **10 kΩ**. Ensemble, elles fournissent une tension de référence pour les capteurs d’entrée.
* **R19-R21** = **1 kΩ**. Elles sont chacune en série avec un :term:`CT` pour protéger le processeur des signaux importants.
* **R22** = **1 MΩ**. Cela fournit le :term:`pull-up` pour la ligne de réinitialisation du processeur.

.. note::

   Des valeurs inférieures pour **R2-R4** et **R5-R7** sont désormais utilisées pour augmenter la charge sur le transformateur.
   Cela peut l’empêcher d’entrer en saturation, ce qui déformerait la forme d’onde de sortie. |br|
   **R2-R4** = **100 Ω** convient pour un fonctionnement en **3,3 V**. |br|
   Pour une meilleure utilisation de la plage d’entrée de l’:term:`ADC`, **R2-R4** doit être augmenté à **180 Ω** pour un fonctionnement en **5 V**.
   
   La valeur pour **R8-R10** a été initialement spécifiée comme étant **150 Ω**.
   
   Lorsque le processeur fonctionne à **3,3 V**, cela donne une plage de fonctionnement d’environ **4 kW**. En réduisant ces valeurs à **120 Ω**, la plage est augmentée à **~5 kW**.
   
   Pour un système **5 V**, la valeur originale de **150 Ω** donne une plage de fonctionnement d’environ **6 kW**.
   
   Ces valeurs de résistance de charge s’appliquent lorsque le processeur fonctionne à **3,3 V**. S’il fonctionne à **5 V**, ces plages sont augmentées d’environ **50 %**.
   
   Ces puissances s’entendent sur chaque phase.
   
   .. include:: ../common/burden-calc.inc.rst

Diodes
~~~~~~

Ensuite, les diodes peuvent être ajoutées.

Celles-ci offrent un certain degré de protection au processeur lorsque des courants élevés traversent les CTs.

.. attention::

   Les diodes sont polarisées. |br|
   Elles doivent être placées selon le repérage sur la couche sérigraphiée.

Supports circuits intégrés
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensuite, on installe généralement les supports pour les circuits intégrés.

.. attention::
   Chaque support a une encoche à une extrémité. Celle-ci doit être alignée avec la marque correspondante sur la couche sérigraphiée, comme indiqué ici.

Avec le support convenablement soutenu par le bas (on peut aussi utiliser un morceau d’adhésif), les deux broches situées dans les coins opposés peuvent être soudées en place. |br|
Si un réalignement du composant est nécessaire, il doit être effectué **avant** que les broches restantes ne soient fixées.

Condensateurs céramiques et oscillateur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ces composants ne sont pas polarisés.

Les condensateurs céramiques sont en général orange, et ont la forme d’une goutte d’eau, par opposition aux condensateurs électrolytiques polarisés de forme cylindriques et bleus ou noirs.

.. note::
   Parmi le jeu de condensateurs céramiques, deux d’entre eux sont plus petits que les autres.

   Il s’agit des deux condensateurs associés à l’oscillateur, leur valeur est de **22 pF** et sont référencés **C10** et **C11**.

   **C4** et **C6-C9** sont des condensateurs céramiques de **100 nF**, généralement marqués *104*.

.. note::
   L’oscillateur ainsi que ses deux condensateurs associés peuvent être soudés légèrement au-dessus du :term:`PCB`. |br|
   Ce n’est pas nécessaire pour le bon fonctionnement. |br|
   Pour ce faire, on pourra utiliser une allumette le temps d’effectuer la soudure.

Ponts redresseurs ou ponts de diodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le rôle de ce composant est de redresser le courant alternatif fourni par le transformateur. |br|
C’est la première étape nécessaire pour obtenir une alimentation en courant continu.

Sur la figure ci-après, la courbe du haut correspond à la tension fournie par le transformateur. |br|
La courbe du bas est la tension fournie par le redresseur.

.. figure:: ../img/Redresseur-monophase.png
   :alt: Redressement double alternance monophasé
   :align: center
   :scale: 50%

   Redressement double alternance monophasé

Sur la version triphasée de ce routeur, ils sont au nombre de trois, un par phase. |br|

.. note::
   Il aurait été possible de réaliser un redresseur double alternance triphasé. Ce type de redresseur ne nécessite que six diodes.
   Il y a cependant deux inconvénients :
   * un tel composant est relativement cher, plus de 3x de prix d’un redresseur standard.
   * la tension moyenne résultante est plus de 2 fois la tension moyenne de chaque entrée. Cela engendre un surcroît de "*travail*" du régulateur de tension qui chauffera bien plus.

.. attention::
   Les ponts redresseurs sont polarisés. |br|
   Il faudra bien veiller à faire correspondre le marquage sur le boîtier avec celui de la couche sérigraphiée.

La broche la plus longue correspond au **+**.

Comme pour l’oscillateur, il est courant de les souder légèrement au-dessus du :term:`PCB`.

.. tip::
   On pourra "recycler" 2 des pattes coupées pour réaliser les :ref:`ponts-de-neutre`.

Connecteurs SIL/Molex
~~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex sont *polarisés*, ils possèdent un détrompeur. |br|
Physiquement, ce sont des composants passifs, mais étant donné qu’ils serviront à la connexion d’autres composants ou modules polarisés, il est important de les souder selon le marquage sur la couche sérigraphiée.

Les connecteurs SIL, ou *pin header*, peuvent être soudés dans n’importe quel sens.

Ils seront plus ou moins nombreux selon la configuration :

* 3 connecteurs à **2 pôles** pour les pinces ampèremétriques, référencés :term:`CT`\1 - :term:`CT`\3
* 1 connecteur à **2 pôles** pour le bouton *reset*, référencé **Reset**
* 1 connecteur à **6 pôles** pour le connecteur :term:`FTDI`, référencé **FTDI**
* 1 connecteur à **2 pôles** par sortie, référencé parmi **D3-D13**.

Inductance
~~~~~~~~~~

Ce composant n’est pas polarisé. Il est référencé **L1**, à proximité de l’**ATmega328-P**.

Condensateurs électrolytiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les deux condensateurs électrolytiques, **C1** et **C2**, sont polarisés et doivent donc être installés dans le bon sens.
La broche **-ve** est indiquée par une bande proéminente, en général blanche, sur toute la longueur du composant.

L’autre broche est la **+ve**, qui doit aller dans le trou marqué **+** sur la couche sérigraphiée.

.. attention::
   Bien qu’ils se ressemblent assez, il est important que ces deux condensateurs soient installés aux bons endroits.

   Le plus grand condensateur (**C1** = **100 μF**) est le plus proche du bord du :term:`PCB`. |br|
   Le plus petit (**C2** = **10 μF**) est le plus proche de **VR1**.

   Si ces deux composants sont inversés, les symptômes qui en résultent peuvent être difficiles à diagnostiquer.

.. _ponts-de-neutre:

Ponts de neutre
~~~~~~~~~~~~~~~

Pour un raccordement triphasé **avec** neutre (en France et la plupart des pays européens), il est possible de ponter le neutre entre chacune des 3 sous-alimentations. |br|
Les deux ponts sont référencés "**N**", entre les transformateurs. |br|
De cette façon, il ne sera pas nécessaire d’introduire un fil de neutre dans chaque connecteur secteur, un seul suffira.

.. warning::
   Pour un raccordement triphasé **sans** neutre, essentiellement le **3 * 230 V** en **Belgique**, il ne faudra pas souder ces ponts.

.. hint::
   Pour réaliser ces ponts, on pourra utiliser le reliquat des pattes coupées de l’inductance.

Connecteurs secteur et porte-fusible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les connecteurs secteur (**PWR1-PWR3**) et les porte-fusible (**FS1-FS3**) peuvent maintenant être installés. |br|
En raison des pistes du plan masse, les broches référencées **PE** sur chacun des connecteurs nécessitera plus de chaleur que les autres broches.
Ces borniers doivent être orientés correctement pour permettre un accès facile au câblage. |br|
Il est très facile de se tromper de sens !

Les porte-fusible, accompagnés de leur fusible de **100 mA**, sont simples à mettre en place.

Régulateur de tension
~~~~~~~~~~~~~~~~~~~~~

Le régulateur de tension (**VR1**) doit être installé de manière à ce que son ailette métallique soit éloignée du transformateur, comme indiqué sur la sérigraphie. |br|
En fonction de l’application, le **VR1** sera une version **3,3 V** ou **5 V**.

La soudure des broches du **VR1** nécessitera probablement une température plus élevée. |br|
Pour réduire la quantité de métal à chauffer, il est possible de couper préalablement ces broches à la longueur requise.

Transformateurs
~~~~~~~~~~~~~~~

Les derniers composants à installer sont les transformateurs. Ce sont des transformateurs doubles de **6 V**, comme indiqué sur la couche sérigraphiée.
Ces transformateurs de **6 V** peuvent alimenter un régulateur de tension de **3,3 V** ou de **5 V**.

.. important::
   Lors du montage de ces composants, il ne doit y avoir aucun espace entre la base du transformateur et la carte de circuit imprimé :term:`PCB`.

-------------

Tests électriques
-----------------

Une fois les transformateurs en place, la carte est maintenant prête pour les tests électriques. |br|

C’est le bon moment pour vérifier que tous les joints soudés sont en bon état et que toutes les éclaboussures de soudure ont été éliminées.

Test de chaque sous-alimentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avant d’installer les circuits intégrés, le fonctionnement de l’alimentation doit être vérifié.

.. danger::
   **Alerte de sécurité**

   Pour poursuivre cette séquence de construction, un accès à la tension secteur **230 V** est requis.

   Veuillez ne pas passer à cette étape suivante à moins que vous soyez compétent pour le faire.

Nous effectuerons les tests suivants en alimentant le routeur via chacun des connecteurs secteur, l’un après l’autre. |br|
Ainsi, si une tension est incorrecte, il sera plus facile d’identifier la partie du circuit qui est défectueuse.

Si tout a été correctement assemblé, la sortie de l’alimentation devrait être d’environ **3,3 V**… ou **5 V** si un régulateur de tension **5 V** a été installé.

Cette tension peut être facilement vérifiée au niveau du point de test **Test VCC**, ainsi que **Test GND**, comme indiqué ici.

.. hint::
   N’oubliez pas de mettre votre multimètre sur la position *courant continu*, :term:`DC`, symbole **⎓** !

À l’exception du transformateur, qui peut sembler légèrement chaud après plusieurs minutes, aucun des composants de la carte ne doit présenter d’augmentation notable de la température.

Insertion du LM358 et test de Vref
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avec la tension correcte en place, les circuits intégrés peuvent maintenant être installés, après avoir coupé l’alimentation.

Le premier d’entre eux est LM358. |br|
Il s’agit d’un amplificateur opérationnel qui fournit une tension de référence intermédiaire pour les capteurs de tension et de courant.

Avec les packs Dual-in-Line, les broches devront peut-être être légèrement pliées vers l’intérieur pour s’insérer dans l’embase.
Cela peut être fait en *faisant rouler* doucement la puce de chaque côté, tour à tour.

Pour minimiser les risques de dommages électriques, cette opération doit être effectuée sur une surface protectrice telle qu’un sac antistatique.

Avec les broches bien alignées, le circuit intégré peut être délicatement placé sur son connecteur, comme indiqué ici.

.. warning::
   Les circuits intégrés doivent être installés dans le bon sens. Le point sur la puce doit être aligné avec l’encoche de l’image sérigraphiée.

Une fois que tout a été soigneusement vérifié, la puce peut être enfoncée fermement.

Avec **LM358** en place et la carte alimentée à nouveau, la référence de tension peut être mesurée. |br|
**Vref** doit être environ la moitié de la tension d’alimentation. Ici, nous testons une carte **3,3 V**.

Cette tension est accessible via le point de test **Test Vref** juste en dessous du **LM358**.

Insertion du processeur principal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le processeur principal, **ATmega328-P**, est installé de la même manière que pour **LM358**, toujours après avoir coupé l’alimentation.
Avec autant de broches, il est très facile pour l’une d’entre elles de se plier en dessous.

.. caution::
   Si ce circuit intégré est dans le mauvais sens lors de la mise sous tension, il ne fonctionnera probablement plus jamais !

.. |br| raw:: html

  <br/>