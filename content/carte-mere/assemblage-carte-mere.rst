.. _assemblage-carte-mere:

==========================================
Assemblage de la carte-mère universelle
==========================================

⏱️ **Temps estimé** : 1,5-2 heures (débutant), 45 min-1 heure (expérimenté)

🔧 **Niveau de difficulté** : Intermédiaire

⚠️ **Niveau de risque** : Faible (composants basse tension uniquement)

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Configuration choisie (voir :ref:`choix-configuration`)
   | ☐ Chapitre :ref:`carte-mere-presentation` lu
   | ☐ Fer à souder et consommables prêts
   | ☐ Temps disponible (1,5-2 heures pour débutant)
   | ☐ Espace de travail propre et organisé

.. contents:: Sommaire
   :local:
   :depth: 1

Introduction
------------

La carte universelle 3phaseDiverter est livrée avec tous les composants :term:`CMS` (montés en surface) déjà soudés en usine. Vous n'avez qu'à souder les composants **traversants** (through-hole).

Le nombre de composants à souder dépend de votre configuration (monophasé, triphasé, etc.). Consultez le tableau dans le chapitre :ref:`choix-configuration` pour la liste complète.

.. tip::
   Avant de commencer, lisez la section :ref:`introduction` pour les recommandations générales de soudure et l'identification des composants polarisés.

.. include:: ../common/qualite-soudures.inc.rst

Composants communs (toutes configurations)
-------------------------------------------

Ces composants doivent être soudés quelle que soit la configuration choisie.

Support IC1 (ATmega328P)
~~~~~~~~~~~~~~~~~~~~~~~~~

Le support :term:`DIL` 28 broches pour le microcontrôleur ATmega328P.

.. danger::
   **NE PAS insérer l'ATmega328P dans le support à ce stade !**

   Le microcontrôleur sera inséré après les tests électriques.

#. Repérez l'**encoche** sur le support et alignez-la avec le repère sur le :term:`PCB`
#. Positionnez le support et maintenez-le avec du ruban adhésif
#. Soudez une broche en diagonale, vérifiez l'alignement
#. Soudez la broche opposée en diagonale
#. Soudez toutes les broches restantes

.. hint::
   Pour s'assurer que le support :term:`DIL` est bien plaqué contre le :term:`PCB`, commencez par souder une seule broche, puis vérifiez l'alignement avant de poursuivre.

Quartz X1 et condensateurs C7, C8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le quartz 16 MHz (boîtier HC-49) et ses deux condensateurs de charge 22 pF.

#. Soudez le quartz **X1** — composant non polarisé, les deux sens sont possibles
#. Soudez les condensateurs **C7** et **C8** (22 pF) — non polarisés

Condensateur électrolytique C3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le condensateur de filtrage 120 µF.

.. warning::
   Ce composant est **polarisé**. La bande blanche (signes −) indique le côté négatif. Respectez impérativement la polarité indiquée sur le :term:`PCB`.

#. Identifiez la polarité : la **bande blanche** sur le condensateur correspond au côté **négatif** (−)
#. Insérez le condensateur en respectant la polarité
#. Soudez les deux pattes

Connecteur SMA CN1 (antenne RF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur :term:`SMA` femelle vertical pour l'antenne du module RFM69CW.

#. Positionnez le connecteur CN1 sur le :term:`PCB`
#. Soudez les pattes de fixation mécanique (masse) en premier
#. Soudez la broche signal centrale

Cavalier fil GND_LINK
~~~~~~~~~~~~~~~~~~~~~~

Ce cavalier relie la masse numérique (GND) à la masse analogique (AGND).

#. Coupez un morceau de fil de cuivre de **0,75 mm²** à la longueur nécessaire
#. Insérez le fil entre les deux pastilles GND_LINK
#. Soudez les deux extrémités

.. important::
   Ce cavalier est **obligatoire** pour le fonctionnement de la carte. Sans lui, les circuits analogiques n'ont pas de référence de masse.

Connecteurs signaux
~~~~~~~~~~~~~~~~~~~~

Soudez les connecteurs suivants :

#. **FTDI** (Molex SL 1×06) — Connecteur programmation/débogage
#. **OLED** (Molex SL 1×04) — Connecteur écran I2C
#. **TRIG_EXT** (barrette mâle 1×06) — Connecteur déclenchement/GPIO
#. **UART_EXT** (barrette mâle 1×06) — Connecteur UART + DS18B20

.. hint::
   Pour aligner correctement les connecteurs :

   - Soudez une seule broche
   - Vérifiez que le connecteur est perpendiculaire au :term:`PCB`
   - Corrigez si nécessaire en chauffant la soudure
   - Soudez les broches restantes

Cavaliers de soudure JP0–JP4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configurez les cavaliers selon votre configuration. Consultez le chapitre :ref:`cavaliers` pour les détails.

.. admonition:: ✅ Point de Contrôle — Composants Communs

   Avant de continuer, vérifiez :

   | ☐ Support IC1 correctement orienté (encoche alignée)
   | ☐ Quartz X1 et condensateurs C7, C8 soudés
   | ☐ Condensateur C3 soudé avec la **bonne polarité**
   | ☐ Connecteur SMA CN1 soudé solidement
   | ☐ GND_LINK fermé (fil soudé)
   | ☐ Tous les connecteurs signaux soudés et perpendiculaires
   | ☐ Cavaliers JP0–JP4 configurés selon votre configuration
   | ☐ Toutes les soudures propres et brillantes
   | ☐ Pas de pont de soudure

Composants monophasé
---------------------

En configuration monophasée, soudez les composants suivants en plus des composants communs.

Fusibles FS0, FS1
~~~~~~~~~~~~~~~~~~~

Les porte-fusibles pour la protection de la phase et du neutre (1 A × 250 V).

#. Soudez le porte-fusible **FS0** (neutre)
#. Soudez le porte-fusible **FS1** (phase L1)

Module de protection GM1
~~~~~~~~~~~~~~~~~~~~~~~~~

Le module varistance combinée GDT+MOV pour la protection de la phase L1.

#. Soudez le module **GM1**

Transformateur de tension TR1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le transformateur :term:`ZMPT101K` pour la mesure de tension de la phase L1.

#. Positionnez **TR1** sur le :term:`PCB`
#. Soudez les broches

Connecteur CT1
~~~~~~~~~~~~~~~

Le connecteur Molex SL 1×02 pour le transformateur de courant de la phase L1.

#. Soudez le connecteur **CT1**

Connecteur CT2 (optionnel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si vous souhaitez mesurer la puissance de diversion (puissance routée vers la charge), soudez le connecteur **CT2**.

Connecteur PWR1 (3 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 3 voies (Terre, Neutre, L1) pour l'entrée secteur.

#. Soudez le connecteur **PWR1** (3 voies)

Protection optionnelle (RV0, RV1, GDT0, GDT1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si fournis dans votre kit, soudez les composants de protection supplémentaires :

#. Varistances **RV0** et **RV1** (radial, 300 V)
#. Éclateurs à gaz **GDT0** et **GDT1**

.. admonition:: ✅ Point de Contrôle — Composants Monophasé

   Avant de continuer, vérifiez :

   | ☐ Fusibles FS0, FS1 soudés
   | ☐ Module GM1 soudé
   | ☐ Transformateur TR1 soudé
   | ☐ Connecteur CT1 soudé (+ CT2 si option diversion)
   | ☐ Connecteur PWR1 (3 voies) soudé
   | ☐ Protections optionnelles soudées (si fournies)
   | ☐ Toutes les soudures propres et brillantes

Composants triphasé
--------------------

En configuration triphasée (avec ou sans neutre), soudez les composants suivants en plus des composants communs.

Fusibles FS0–FS3
~~~~~~~~~~~~~~~~~

Les porte-fusibles pour la protection de toutes les phases et du neutre (1 A × 250 V).

#. Soudez les porte-fusibles **FS0** (neutre), **FS1** (L1), **FS2** (L2), **FS3** (L3)

Modules de protection GM1–GM3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les modules varistance combinées GDT+MOV pour la protection de chaque phase.

#. Soudez les modules **GM1**, **GM2**, **GM3**

Transformateurs de tension TR1–TR3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les transformateurs :term:`ZMPT101K` pour la mesure de tension de chaque phase.

#. Soudez **TR1** (L1), **TR2** (L2), **TR3** (L3)

Connecteurs CT1–CT3
~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex SL 1×02 pour les transformateurs de courant de chaque phase.

#. Soudez **CT1** (L1), **CT2** (L2), **CT3** (L3)

Connecteur PWR1 (5 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 5 voies (Terre, Neutre, L1, L2, L3) pour l'entrée secteur.

#. Soudez le connecteur **PWR1** (5 voies)

Protection optionnelle (RV0–RV3, GDT0–GDT3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si fournis dans votre kit, soudez les composants de protection supplémentaires :

#. Varistances **RV0**, **RV1**, **RV2**, **RV3** (radial, 300 V)
#. Éclateurs à gaz **GDT0**, **GDT1**, **GDT2**, **GDT3**

.. admonition:: ✅ Point de Contrôle — Composants Triphasé

   Avant de continuer, vérifiez :

   | ☐ Fusibles FS0–FS3 soudés
   | ☐ Modules GM1–GM3 soudés
   | ☐ Transformateurs TR1–TR3 soudés
   | ☐ Connecteurs CT1–CT3 soudés
   | ☐ Connecteur PWR1 (5 voies) soudé
   | ☐ Protections optionnelles soudées (si fournies)
   | ☐ Toutes les soudures propres et brillantes

Inspection finale
-----------------

Avant de passer aux tests électriques, effectuez une inspection minutieuse de toute la carte.

.. admonition:: ✅ Point de Contrôle Final — Assemblage Carte-Mère

   | ☐ **Toutes les soudures vérifiées** : brillantes, sans pont, sans soudure froide
   | ☐ **Pas de morceaux de pattes** coupées sur la carte
   | ☐ **Pas de flux de soudure** résiduel entre les pistes
   | ☐ **Support IC1 vide** (ATmega328P PAS encore inséré)
   | ☐ **Cavaliers configurés** selon votre configuration
   | ☐ **Composants polarisés** vérifiés (C3)
   | ☐ **Carte propre** et exempte de débris

Passez ensuite au chapitre :ref:`tests-electriques` pour vérifier le bon fonctionnement de la carte.

.. |br| raw:: html

  <br/>
