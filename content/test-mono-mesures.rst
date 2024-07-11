.. _test-mono-mesures:

Test de la partie *mesures*
"""""""""""""""""""""""""""

| Le transformateur a deux sorties : l'une pour l'alimentation CC, l'autre pour le capteur de tension CA qui devrait déjà fonctionner.
| Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (**IC1**).

Le programme, qui se trouve également sur la page Téléchargements, est : *RawSamplesTool_2chan.ino*

| Après avoir téléchargé ce croquis sur le processeur via l'Arduino IDE, la fenêtre série (icône en forme de loupe) doit être ouverte.
| Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère "**g**", suivi de *Entrée*.

| Le programme *RawSamplesTool_2chan* affiche les échantillons de tension alternative et de courant pour un ou plusieurs cycles secteur complets.
| Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

| Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3 kW avec le :term:`CT` branché sur **CT2**.
| Lorsque le :term:`CT` a été déplacé vers le port :term:`CT`\1, la sortie résultante semblait presque identique, mais avec les caractères "**1**" et "**2**" inversés.

RSResults_V_and_I2.txt

| Si aucun signal n'est disponible sur les ports **CT1** et **CT2**, les formes d'onde de ces canaux seront toutes deux des lignes droites.
| Seul le signal de tension affichera un aspect sinusoïdal.
| Pour vérifier le fonctionnement des ports **CT1** et **CT2** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.
