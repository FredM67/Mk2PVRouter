.. _test-logiciel:

.. toctree::
   :hidden:
   
   carte-mono-test-afficheur
   test-mono-mesures

Tests logiciel
^^^^^^^^^^^^^^

| Une fois le processeur installé, il serait judicieux de vérifier que l'alimentation électrique fonctionne toujours correctement.
| Si c'est le cas, nous pouvons exécuter un croquis (programme) pour vérifier si le processeur fonctionne correctement.

| Pour cette prochaine étape, un dispositif de programmation approprié doit être mis en place.
| Vous trouverez des détails sur la configuration de l'Environnement de Développement Intégré (IDE) Arduino en haut de cette page.
| Un programmateur USB vers UART doit être connecté au connecteur :term:`FTDI` du :term:`PCB` comme indiqué ci-dessous.
| L'autre extrémité du programmateur doit être connectée à l'ordinateur de programmation (PC ou équivalent) via un câble USB approprié.

La broche à une extrémité du connecteur à 6 voies du programmateur sera étiquetée **Gnd**. Cette broche doit correspondre au marquage **0 V** sur le :term:`PCB`.

| Ici, nous utilisons le programmateur :term:`FTDI`. Notez qu'il doit être monté dans le sens inverse.
| La broche **Gnd** doit toujours être la plus proche du bord de la carte.

| Pour éviter de tordre le connecteur du programmateur, vous pouvez fabriquer un simple câble d'extension comme indiqué ici.
| Seules quatre des lignes sont réellement utilisées (données **Tx** & **Rx**, masse et réinitialisation).
| Aucune des lignes d'alimentation électrique n'est utilisée par cette carte.

Le fil noir est destiné à la connexion **GND** (ou **0 V**).

.. note::
   La carte FTDI ne peut pas alimenter la carte-mère.

   Le routeur doit toujours être alimenté par sa propre source d'alimentation.

.. include:: carte-mono-test-afficheur.rst
   
.. include:: test-mono-mesures.rst