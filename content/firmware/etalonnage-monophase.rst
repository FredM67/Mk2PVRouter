.. _etalonnage-monophase:

======================
Étalonnage — Monophasé
======================

⏱️ **Temps estimé** : 45 min–1 heure

🔧 **Niveau de difficulté** : Intermédiaire

⚠️ **Niveau de risque** : Élevé (manipulation 230 V sous tension)

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Tests électriques effectués (voir :ref:`tests-electriques`)
   | ☐ Firmware installé et fonctionnel (voir :ref:`logiciel-monophase`)
   | ☐ Routeur alimenté par le secteur
   | ☐ Multimètre ou wattmètre disponible
   | ☐ Accès au compteur d'électricité

.. contents:: Sommaire
    :local:
    :depth: 2

.. include:: ../common/etalonnage-intro.inc.rst

:term:`CT` *grille/réseau*
--------------------------

Lors de l'étalonnage d'un nouvel ensemble de matériel, la première étape consiste à étalonner le canal **CT1**. À cette fin, le matériel en cours de test doit exécuter le programme ``cal_CT1_v_meter.ino``, qui est disponible sur la page de téléchargements.

Le taux du flux d'impulsions pour le matériel en cours de test peut être ajusté en modifiant la valeur de ``powerCal_grid``. Lorsque les deux flux d'impulsions sont synchronisés, l'étalonnage correct a été atteint.

Pour chaque unité d'énergie mesurée au point de connexion au réseau via **CT1**, une impulsion sera générée au port de sortie. |br|
Le taux des impulsions peut être modifié en changeant la valeur de ``powerCal_grid``. Un flux d'impulsions similaire sera visible au compteur.

Pour avancer un flux d'impulsions par rapport à l'autre, un second chemin pour le courant devra passer à travers **CT1**. |br|
La puissance consommée par n'importe quel petit appareil fera l'affaire — un seul de ses cœurs actifs doit passer à travers **CT1** — et le courant peut circuler dans les deux sens. |br|
Lorsque l'appareil est éteint, le fil supplémentaire n'aura aucun effet sur les performances du :term:`CT`, car aucun courant ne le traverse.

Lorsque la valeur correcte a été trouvée pour ``powerCal_grid``, cette même valeur peut être utilisée avec n'importe quel croquis de routeur Mk2PVRouter qui doit être exécuté sur le **même matériel**.


.. admonition:: ✅ Point de Contrôle — Étalonnage CT Grille

   Avant de passer à l'étalonnage du :term:`CT` diversion, vérifiez :

   | ☐ **Programme cal_CT1_v_meter.ino** téléversé et fonctionnel
   | ☐ **Valeur powerCal_grid trouvée** et notée (à conserver précieusement)
   | ☐ Flux d'impulsions synchronisé avec le compteur
   | ☐ Test de vérification effectué (appareil de puissance connue)
   | ☐ Valeur stable et reproductible

:term:`CT` *diversion*
-----------------------

Ayant obtenu la valeur correcte pour ``powerCal_grid``, le canal *grid* peut ensuite être utilisé pour étalonner le canal *diverted power* qui utilise **CT2**. |br|
À cette fin, le matériel en cours de test doit exécuter le programme ``cal_CT2_v_CT1.ino``, qui est disponible sur la page de téléchargements. |br|
Le paramètre ``powerCal_grid`` doit être réglé à la valeur correcte comme déterminé précédemment dans la première partie de ce processus.

Les deux **CTs** devraient être montés autour du même fil porteur de courant. Si **CT2** a été intégré dans un système complet, le commutateur de marche forcée peut être utilisé pour forcer le courant à travers ce câblage. |br|
Le canal **CT2** d'une carte autonome peut être étalonné en utilisant simplement un câble d'extension modifié qui fonctionne entre n'importe quelle prise de courant pratique et un appareil approprié.

Lorsque la valeur correcte a été trouvée pour ``powerCal_diverted``, cette même valeur peut être utilisée avec n'importe quel croquis de routeur Mk2PVRouter qui doit être exécuté sur le **même matériel**.


.. admonition:: ✅ Point de Contrôle — Étalonnage Monophasé Complet

   Avant de passer à l'installation finale, vérifiez :

   | ☐ **Programme cal_CT2_v_CT1.ino** téléversé avec powerCal_grid correct
   | ☐ **Valeur powerCal_diverted trouvée** et notée
   | ☐ Deux :term:`CT`\s montés autour du même fil donnent mesures identiques
   | ☐ Documentation des valeurs : powerCal_grid et powerCal_diverted conservées
   | ☐ **:term:`CT`\s marqués** (CT1 = grille, CT2 = diversion)

.. |br| raw:: html

  <br/>
