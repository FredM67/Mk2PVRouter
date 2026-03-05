.. _assemblage-carte-mere:

==========================================
Assemblage de la carte-mère universelle
==========================================

⏱️ **Temps estimé** : 45 min–1 heure (débutant), 20–30 minutes (expérimenté)

🔧 **Niveau de difficulté** : Intermédiaire

⚠️ **Niveau de risque** : Faible (composants basse tension uniquement)

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Configuration choisie (voir :ref:`choix-configuration`)
   | ☐ Chapitre :ref:`carte-mere-presentation` lu
   | ☐ Fer à souder et consommables prêts
   | ☐ Temps disponible (1,5–2 heures pour débutant)
   | ☐ Espace de travail propre et organisé

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

.. warning::
   **NE PAS insérer l'ATmega328P dans le support à ce stade !**

   Le microcontrôleur sera inséré après les tests électriques.

#. Repérez l'**encoche** sur le support et alignez-la avec le repère sur le :term:`PCB`
#. Positionnez le support et maintenez-le avec du ruban adhésif
#. Soudez une broche en diagonale, vérifiez l'alignement
#. Soudez la broche opposée en diagonale
#. Soudez toutes les broches restantes

.. todo:: Photo à fournir — support IC1 soudé, encoche alignée avec le repère PCB.

.. hint::
   Pour s'assurer que le support :term:`DIL` est bien plaqué contre le :term:`PCB`, commencez par souder une seule broche, puis vérifiez l'alignement avant de poursuivre.

Quartz X1
~~~~~~~~~

Le quartz 16 MHz (boîtier HC-49).

#. Soudez le quartz **X1** — composant non polarisé, les deux sens sont possibles

.. todo:: Photo à fournir — quartz X1 soudé.

.. note::
   Les condensateurs de charge C7 et C8 sont des composants :term:`CMS` déjà soudés en usine.

Condensateur électrolytique C3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le condensateur de filtrage 120 µF.

.. warning::
   Ce composant est **polarisé**. La bande blanche (signes −) indique le côté négatif. Respectez impérativement la polarité indiquée sur le :term:`PCB`.

#. Identifiez la polarité : la **bande blanche** sur le condensateur correspond au côté **négatif** (−)
#. Insérez le condensateur en respectant la polarité
#. Soudez les deux pattes

.. todo:: Photo à fournir — condensateur C3 soudé, bande blanche (−) visible et alignée avec le repère PCB.

Connecteur SMA (antenne RF) — optionnel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur :term:`SMA` femelle vertical pour l'antenne du module RFM69CW. Ce connecteur n'est nécessaire que si le module :term:`RF` est utilisé.

#. Positionnez le connecteur SMA sur le :term:`PCB`
#. Soudez les pattes de fixation mécanique (masse) en premier
#. Soudez la broche signal centrale

.. todo:: Photo à fournir — connecteur SMA soudé (pattes de masse + broche signal).

Module RF (RFM69CW) — optionnel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le module radio RFM69CW permet la communication sans fil (bande ISM 433/868 MHz).

.. warning::
   Le module RFM69CW est **très sensible aux décharges électrostatiques** (ESD). Avant de le manipuler :

   - Touchez une surface métallique reliée à la terre pour vous décharger
   - Évitez de toucher les composants ou les broches du module
   - Travaillez de préférence sur un tapis antistatique

.. warning::
   Avant de souder le module, vérifiez que le cavalier **V sel.** est en position **3–centre (3,3 V)**. Le module RFM69CW fonctionne en 3,3 V — une alimentation en 5 V le **détruirait immédiatement**.

#. Positionnez le module RFM69CW sur son emplacement
#. **Vérifiez l'alignement** : chaque broche du module doit correspondre exactement à sa pastille sur le :term:`PCB`. Reportez-vous à la sérigraphie pour l'orientation correcte.
#. Soudez une broche d'angle, vérifiez l'alignement, puis soudez les broches restantes

.. todo:: Photo à fournir — module RFM69CW soudé et aligné sur son emplacement.

.. tip::
   Un petit morceau de ruban adhésif double face entre le module et le PCB permet de le maintenir en place pendant la soudure.

.. note::
   N'oubliez pas de fermer les cavaliers **IRQ** (face arrière) et **NSS** (face avant, près du module RF) pour activer le module RF (voir :ref:`cavaliers`).

Cavalier fil GND_LINK
~~~~~~~~~~~~~~~~~~~~~~

Ce cavalier relie la **terre de protection** (Earth, provenant du réseau électrique) à la **masse basse tension** (GND) du circuit.

#. Coupez un morceau de fil de cuivre de **0,75 mm²** à la longueur nécessaire
#. Insérez le fil entre les deux pastilles GND_LINK
#. Soudez les deux extrémités

.. todo:: Photo à fournir — cavalier fil GND_LINK soudé entre les deux pastilles.

.. note::
   Lorsque GND_LINK est **ouvert**, le circuit basse tension est entièrement isolé de la terre grâce à l'isolation galvanique du module d'alimentation RAC05E. Lorsqu'il est **fermé**, la masse basse tension est référencée à la terre de protection.

   La configuration recommandée dépend de votre installation. En cas de doute, laissez le cavalier **ouvert** — il pourra toujours être soudé ultérieurement.

Connecteurs signaux
~~~~~~~~~~~~~~~~~~~~

Soudez les connecteurs suivants :

#. **FTDI** (Molex SL 1×06) — Connecteur programmation/débogage
#. **OLED** (Molex SL 1×04) — Connecteur écran I2C
#. **TRIG_EXT** (barrette mâle 1×06) — Connecteur déclenchement/GPIO
#. **UART_EXT** (barrette mâle 1×06) — Connecteur UART + DS18B20

.. todo:: Photo à fournir — connecteurs signaux soudés et perpendiculaires au PCB.

.. hint::
   Pour aligner correctement les connecteurs :

   - Soudez une seule broche
   - Vérifiez que le connecteur est perpendiculaire au :term:`PCB`
   - Corrigez si nécessaire en chauffant la soudure
   - Soudez les broches restantes

Connecteurs sorties numériques (D2–D13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chaque sortie numérique dispose de deux emplacements Molex SL : un 2 broches (GND, I/O) et un 3 broches (GND, I/O, VCC). Soudez uniquement les connecteurs correspondant aux sorties utilisées dans votre configuration.

.. todo:: Photo à fournir — connecteurs Molex 1×02 et 1×03 soudés sur les sorties numériques.

.. note::
   Les connecteurs fournis dépendent de la configuration commandée. Inutile de souder des connecteurs sur des sorties non utilisées.

   - **D2\*, D10\*–D13\*** : réservées au module RF (si soudé)
   - **D5–D9** : réservées au module :term:`mk2Wifi` (si présent)
   - Les sorties non réservées sont librement utilisables

Cavaliers de soudure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configurez les cavaliers selon votre configuration. Consultez le chapitre :ref:`cavaliers` pour les détails.

.. admonition:: ✅ Point de Contrôle — Composants Communs

   Avant de continuer, vérifiez :

   | ☐ Support IC1 correctement orienté (encoche alignée)
   | ☐ Quartz X1 soudé
   | ☐ Condensateur C3 soudé avec la **bonne polarité**
   | ☐ Connecteur SMA soudé solidement (si module RF utilisé)
   | ☐ Module RFM69CW soudé et V sel. en 3,3 V (si module RF utilisé)
   | ☐ GND_LINK configuré (ouvert ou fermé selon votre installation)
   | ☐ Tous les connecteurs signaux soudés et perpendiculaires
   | ☐ Cavaliers configurés selon votre configuration (voir :ref:`cavaliers`)
   | ☐ Toutes les soudures propres et brillantes
   | ☐ Pas de pont de soudure

Étape suivante
--------------

Poursuivez avec les composants spécifiques à votre configuration :

- **Monophasé ou split-phase** → :ref:`assemblage-monophase`
- **Triphasé** (avec ou sans neutre) → :ref:`assemblage-triphase`

.. |br| raw:: html

  <br/>
