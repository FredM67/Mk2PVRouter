.. _test-logiciel-tri:

Test logiciel
-------------

.. include:: test-logiciel.md
   :parser: myst_parser.sphinx_

Test de la partie *mesures*
---------------------------

.. note::
   À partir de maintenant, une alimentation triphasée devra être fournie à la carte-mère.

Chaque transformateur a deux sorties : l'une pour l'alimentation CC, l'autre pour le capteur de tension CA qui devrait déjà fonctionner.
Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (ATmega328-P).

Le programme, qui se trouve également sur la page Téléchargements, est : RawSamplesTool_6chan.ino

Après avoir téléchargé ce croquis sur le processeur via l'IDE Arduino, la fenêtre série (icône en forme de loupe) doit être ouverte.
Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère "**g**", suivi de *Entrée*.

Le programme *RawSamplesTool_6chan* affiche les échantillons des trois tensions alternatives et de courant pour un ou plusieurs cycles secteur complets.
Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3 kW avec le :term:`CT` branché sur :term:`CT`2.
Lorsque le :term:`CT` a été déplacé vers le port **:term:`CT`1**, la sortie résultante semblait presque identique, mais avec les caractères "**1**" et "**2**" inversés.

RSResults_V_and_I2.txt

Si aucun signal n'est disponible sur les ports **:term:`CT`1-:term:`CT`3**, les formes d'onde de ces canaux seront toutes deux des lignes droites.
Seuls les signaux de tension afficheront un aspect sinusoïdal.
Pour vérifier le fonctionnement des ports **:term:`CT`1-:term:`CT`3** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.
