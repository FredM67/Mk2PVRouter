.. _logiciel-triphase:

=================================
Installation et tests — Triphasé
=================================

| Une fois le processeur installé, il serait judicieux de vérifier que l’alimentation électrique fonctionne toujours correctement.
| Si c’est le cas, nous pouvons exécuter un croquis (programme) pour vérifier si le processeur fonctionne correctement.

| Nous allons maintenant tester le bon fonctionnement des autres parties matérielles de la carte-mère.
| Cela permettra à la fois de s’assurer que le processeur est opérationnel et de vérifier que les autres composants sont correctement installés et/ou assemblés.

| Pour cette prochaine étape, un dispositif de programmation approprié doit être mis en place.

.. contents:: Sommaire
    :local:
    :depth: 1

.. include:: ../common/test-logiciel-requirements.inc.rst

Installation du Firmware
-------------------------

Firmware : ``Mk2_3phase_RFdatalog_temp`` — `PVRouter-3-phase <https://github.com/FredM67/PVRouter-3-phase>`_

Site du firmware (en anglais) : `fredm67.github.io/PVRouter-3-phase <https://fredm67.github.io/PVRouter-3-phase/>`_, avec la `documentation du code <https://fredm67.github.io/PVRouter-3-phase/doc/>`_ (Doxygen), pour qui veut lire ou modifier le firmware, et l’`historique de sa taille et de sa vitesse <https://fredm67.github.io/PVRouter-3-phase/bench/>`_.

**Étapes communes à toutes les versions** : :ref:`installation-logiciel`

.. include:: firmware-triphase.inc.rst

Test de la partie *mesures*
----------------------------

.. note::
   À partir de maintenant, une alimentation triphasée devra être fournie à la carte-mère.

Les transformateurs ZMPT101K (TR1, TR2, TR3) fournissent les signaux de mesure de tension CA sur chaque phase.
Cela peut être vérifié en exécutant un programme (croquis) qui affiche les mesures analogiques prises par le processeur Atmel (**IC1**).

Le programme est *RawSamplesTool_6chan.ino* : il se trouve dans le dossier ``dev/RawSamplesTool_6chan/`` du dépôt `PVRouter-3-phase <https://github.com/FredM67/PVRouter-3-phase>`_ et se téléverse seul, sans le firmware du routeur.

Après avoir téléversé ce croquis sur le processeur via l’Arduino IDE, la fenêtre série (icône en forme de loupe) doit être ouverte.
Après avoir terminé chaque exécution, le programme peut être redémarré à partir du clavier en saisissant le caractère « **g** », suivi de *Entrée*.

Le programme *RawSamplesTool_6chan* affiche les échantillons des trois tensions alternatives et de courant pour un ou plusieurs cycles secteur complets.
Si un courant important est mesuré ainsi que la tension, les résultats affichés sembleront plus intéressants.

Si aucun signal n’est disponible sur les ports **CT1-CT3**, les formes d’onde de ces canaux seront toutes des lignes droites.
Seuls les signaux de tension afficheront un aspect sinusoïdal.
Pour vérifier le fonctionnement des ports **CT1-CT3** pendant que le :term:`PCB` est testé sur le banc, un câblage adapté sera nécessaire.

Prochaines Étapes
-----------------

✅ Le firmware est maintenant installé et fonctionnel !

**Prochaines étapes :**

#. **Étalonnage** : Voir chapitre :ref:`etalonnage-triphase`

   L’étalonnage est **OBLIGATOIRE** en triphasé : le routeur additionne les trois phases, et une seule phase mal mesurée fausse la somme.

#. **Installation finale** : Connexion au réseau électrique (faire appel à un électricien qualifié)

#. **Configuration avancée** : Relais, sondes de température, double tarif, etc., avec le :ref:`configurateur <configurateur-triphase>`

.. warning::
   Ne pas connecter le routeur au réseau électrique domestique avant d’avoir :

   - [ ] Vérifié toutes les soudures (pas de pont, pas de soudure froide)
   - [ ] Lu le chapitre de sécurité
   - [ ] Fait appel à un électricien qualifié (fortement recommandé)

.. important::
   **FONCTIONNALITÉ** : L’étalonnage doit être effectué après l’installation électrique pour que le routeur mesure correctement et fonctionne de manière optimale. Le routeur peut être connecté sans étalonnage (pas de danger), mais ses mesures seront approximatives : à quelques pour cent près en général avec la carte universelle ; avec l’ancienne carte, les valeurs par défaut ne sont qu’un point de départ.

.. |br| raw:: html

  <br/>
