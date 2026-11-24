.. _logiciel-monophase:

==================================
Installation et tests — Monophasé
==================================

| Une fois le processeur installé, il serait judicieux de vérifier que l'alimentation électrique fonctionne toujours correctement.
| Si c'est le cas, nous pouvons exécuter un croquis (programme) pour vérifier si le processeur fonctionne correctement.

| Nous allons maintenant tester le bon fonctionnement des autres parties matérielles de la carte-mère.
| Cela permettra à la fois de s'assurer que le processeur est opérationnel et de vérifier que les autres composants sont correctement installés et/ou assemblés.

| Pour cette prochaine étape, un dispositif de programmation approprié doit être mis en place.

.. contents:: Sommaire
    :local:
    :depth: 1

.. include:: ../common/test-logiciel-requirements.inc.rst

Installation du Firmware
-------------------------

Firmware : ``Mk2_1phase_RFdatalog_temp`` — `PVRouter-1-phase <https://github.com/FredM67/PVRouter-1-phase>`_

Documentation du code : `Doxygen <https://fredm67.github.io/PVRouter-1-phase/doc/>`_ (en anglais), pour qui veut lire ou modifier le firmware.

.. include:: ../common/ancien-firmware-monophase.inc.rst

**Étapes communes à toutes les versions** : :ref:`installation-logiciel`

.. include:: firmware-monophase.inc.rst

Test de la partie *mesures*
----------------------------

| Le transformateur ZMPT101K (TR1) fournit le signal de mesure de tension CA.
| Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (**IC1**).

Le programme est *RawSamplesTool_2chan.ino* : il se trouve dans le dossier ``dev/RawSamplesTool_2chan/`` du dépôt `PVRouter-1-phase <https://github.com/FredM67/PVRouter-1-phase>`_ et se téléverse seul, sans le firmware du routeur.

.. note::
   Le programme lit la tension sur A3, **CT1** sur A5 et **CT2** sur A4, les entrées de la carte Mk2 de Robin Emley (`OLD_SEG`). Sur les autres cartes (tension A0, **CT1** A1, **CT2** A3), changer les trois numéros de broche en tête du programme.

| Après avoir téléchargé ce croquis sur le processeur via l'Arduino IDE, la fenêtre série (icône en forme de loupe) doit être ouverte.
| Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère « **g** », suivi de *Entrée*.

| Le programme *RawSamplesTool_2chan* affiche les échantillons de tension alternative et de courant pour un ou plusieurs cycles secteur complets.
| Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

| Voici quelques résultats capturés lors de la mesure du courant consommé par une charge de 3 kW avec le :term:`CT` branché sur **CT2**.
| Lorsque le :term:`CT` a été déplacé vers le port :term:`CT`\1, la sortie résultante semblait presque identique, mais avec les caractères « **1** » et « **2** » inversés.

``RSResults_V_and_I2.txt``

| Si aucun signal n'est disponible sur les ports **CT1** et **CT2**, les formes d'onde de ces canaux seront toutes deux des lignes droites.
| Seul le signal de tension affichera un aspect sinusoïdal.
| Pour vérifier le fonctionnement des ports **CT1** et **CT2** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.

Prochaines Étapes
------------------

✅ Le firmware est maintenant installé et fonctionnel !

**Prochaines étapes :**

#. **Étalonnage** : Voir chapitre :ref:`etalonnage-monophase`

   L’étalonnage est recommandé : il donne des valeurs réalistes, et il devient nécessaire dès que des relais routent le surplus, car leurs seuils sont en watts.

#. **Installation finale** : Connexion au réseau électrique (faire appel à un électricien qualifié)

#. **Configuration avancée** : Relais, sondes de température, double tarif, etc., avec le :ref:`configurateur <configurateur-monophase>`

.. warning::
   Ne pas connecter le routeur au réseau électrique domestique avant d’avoir :

   - [ ] Vérifié toutes les soudures (pas de pont, pas de soudure froide)
   - [ ] Lu le chapitre de sécurité
   - [ ] Fait appel à un électricien qualifié (fortement recommandé)

.. important::
   **FONCTIONNALITÉ** : L’étalonnage se fait après l’installation électrique. Le routeur peut être connecté sans étalonnage (pas de danger), mais ses mesures seront approximatives.

.. |br| raw:: html

  <br/>
