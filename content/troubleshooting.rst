.. _troubleshooting:

*******************
Guide de Dépannage
*******************

Ce chapitre vous aide à diagnostiquer et résoudre les problèmes courants rencontrés lors de l’assemblage et de l’utilisation du Mk2PVRouter.

.. important::
 **Avant de commencer le dépannage :**

 - Toujours **couper l’alimentation** au disjoncteur avant toute intervention
 - Vérifier l’absence de tension avec un testeur
 - Prendre des photos avant de modifier quoi que ce soit
 - Noter tous les symptômes observés

.. contents:: Sections du guide de dépannage
 :local:
 :depth: 2

==========================================
📋 Composants selon la configuration
==========================================

Ce guide couvre la carte universelle **3phaseDiverter** du Mk2PVRouter.

.. list-table:: Composants selon la version
 :widths: 40 30 30
 :header-rows: 1

 * - Composant
   - Monophasé
   - Triphasé
 * - Fusibles
   - FS0, FS1
   - FS0, FS1, FS2, FS3
 * - Transformateurs
   - TR1
   - TR1, TR2, TR3
 * - Modules de protection
   - GM1
   - GM1, GM2, GM3
 * - Alimentation 5 V, régulateur 3,3 V
   - PS1 (MPC10-5), U1 (AP7361C-33E)
   - PS1 (MPC10-5, commun), U1 (AP7361C-33E)
 * - Capteurs de courant (CT)
   - 1 CT (réseau) + 1 CT facultatif (énergie routée, CT2)
   - 3 CT (un par phase)
 * - Sorties triac
   - 1 ou plusieurs (selon modèle)
   - 1 ou plusieurs (selon modèle)
 * - Sorties relais
   - 0 ou plusieurs (selon modèle)
   - 0 ou plusieurs (selon modèle)

.. note::
 Dans ce guide, les instructions utilisent la notation :

 - **Mono :** composants pour version monophasée
 - **Tri :** composants pour version triphasée

======================================
🔌 Problèmes Après Soudure de la Carte
======================================

La Carte ne s’Allume Pas
========================

**Symptôme :** Pas de tension aux points de test, aucun signe de vie

Vérifications de Base
---------------------

Effectuez ces vérifications dans l’ordre :

.. admonition:: Liste de contrôle — Alimentation

 #. ☐ L’alimentation secteur est-elle branchée ?
 #. ☐ Le disjoncteur est-il enclenché ?
 #. ☐ **Fusibles intacts ?**

    - Mono : FS0, FS1
    - Tri : FS0, FS1, FS2, FS3
    - Vérifier avec multimètre en mode continuité
    - Un fusible grillé indique un court-circuit

 #. ☐ Tension au point Test VCC = 3,3 V ou 5 V ?

    - Multimètre en mode tension continue (DC)
    - Mesurer entre VCC et GND
    - Si pas de tension → Problème alimentation

Si Pas de Tension au Test VCC
-----------------------------

.. warning::
 **COUPER L’ALIMENTATION** avant toute vérification de composants !

Vérifier les composants d’alimentation :

.. admonition:: Composants à vérifier

 #. ☐ **Module PS1 (MPC10-5)** dans le bon sens ?

    - Vérifier l’orientation selon le schéma
    - Vérifier que le point ou l’encoche du module correspond au repère sur le PCB

 #. ☐ **Chaîne d’alimentation bien soudée ?**

    - Connecteur PWR1, fusibles (Mono : FS0, FS1 ; Tri : FS0 à FS3), module PS1, diode D1 (SMBJ7.0A), régulateur U1
    - Soudures brillantes et lisses (pas ternes) ?

.. include:: common/qualite-soudures.inc.rst

Pont de Soudure (Court-Circuit)
-------------------------------

**Symptôme :** Deux pistes ou broches reliées par erreur

.. todo:: Ajouter photo de pont de soudure (img/pont-de-soudure.png)

**Détection :**

- Inspection visuelle avec une loupe
- Multimètre en mode continuité entre broches qui ne devraient pas être connectées

**Solution — Retrait avec tresse à dessouder :**

#. Placer tresse à dessouder sur le pont
#. Appliquer fer à souder sur la tresse
#. La soudure est absorbée par capillarité
#. Répéter si nécessaire avec section propre de tresse

**Alternative — Retrait avec pompe à dessouder :**

#. Chauffer le pont avec fer à souder
#. Approcher la pompe
#. Activer la pompe (aspiration)
#. Nettoyer et recommencer si nécessaire

Si Tension Correcte mais Pas de Fonctionnement
----------------------------------------------

.. admonition:: Vérifications microcontrôleur

 #. ☐ **ATmega328P** bien inséré dans le support ?

    - Toutes les pattes dans les trous ?
    - Pas de patte pliée sous le boîtier ?

 #. ☐ **ATmega328P** dans le bon sens ?

    - ⚠️ **CRITIQUE** : Encoche alignée avec marquage PCB ?
    - Si inversé → **Puce détruite à la mise sous tension !**
    - Vérifier 3 fois avant d’alimenter

 #. ☐ **Firmware programmé ?**

    - Voir la section :ref:`logiciel-monophase` ou :ref:`logiciel-triphase`
    - ATmega328P vierge ne fait rien

Causes Fréquentes — Résumé
--------------------------

.. list-table::
 :widths: 30 40 30
 :header-rows: 1

 * - Symptôme
   - Cause Probable
   - Solution
 * - Aucune tension VCC
   - Fusible grillé
   - Trouver le court-circuit, remplacer le fusible
 * - Tension VCC faible (<3 V)
   - Régulateur U1 ou module PS1 défectueux
   - Vérifier l’orientation, remplacer
 * - Tension OK, rien ne fonctionne
   - ATmega328P mal inséré/inversé
   - Vérifier l’orientation, réinsérer
 * - Soudures ternes
   - Soudure froide
   - Refaire les soudures avec plus de chaleur

======================================
Problèmes de Programmation du Firmware
======================================

Le Firmware ne se Téléverse Pas
===============================

**Symptôme :** Erreur dans Arduino IDE lors du téléversement

.. code-block:: text

 avrdude: stk500_recv(): programmer is not responding
 avrdude: stk500_getsync() attempt 1 of 10: not in sync

Vérifications de la Connexion FTDI
----------------------------------

.. admonition:: Liste de contrôle — Connexion FTDI

 #. ☐ **Câblage FTDI correct ?**

    - **GND** (fil noir du câble FTDI) → broche 1 (**GND**, repère « GND> ») du connecteur FTDI (J0)
    - **TX** de l’adaptateur (fil orange) → broche 4 (**RX** de l’ATmega328P)
    - **RX** de l’adaptateur (fil jaune) → broche 5 (**TX** de l’ATmega328P)
    - **DTR** (fil vert, RTS, sur le câble FTDI) → broche 6 (**DTR**) : reset automatique, indispensable
    - VCC (fil rouge) : non utilisé, le laisser libre (la broche 3 n’est reliée à rien sur la carte)

 #. ☐ **ATmega328P bien inséré ?**

    - Toutes les pattes dans le support ?
    - Orientation correcte (encoche) ?

 #. ☐ **Routeur alimenté en 230 V ?**

    - Le FTDI ne fournit **PAS** de courant
    - Alimentation secteur obligatoire

 #. ☐ **Bon port COM sélectionné dans Arduino IDE ?**

    - Menu : Outils → Port → COMX
    - Essayer chaque port disponible

 #. ☐ **Pilotes FTDI installés ?**

    - Télécharger les pilotes sur ftdichip.com
    - Windows : Gestionnaire de périphériques doit montrer « USB Serial Port »
    - Linux : ``dmesg | grep tty`` doit montrer nouveau périphérique

Problèmes Port USB Windows
--------------------------

**Symptôme :** Port COM n’apparaît pas dans Arduino IDE

**Solutions :**

#. **Vérifier Gestionnaire de périphériques**

   - Ouvrir : Panneau de configuration → Gestionnaire de périphériques
   - Chercher : « Ports (COM et LPT) »
   - Doit afficher : « USB Serial Port (COMx) »
   - Si point d’exclamation jaune → Pilote problématique

#. **Réinstaller les pilotes FTDI**

   - Désinstaller pilote actuel (clic droit → Désinstaller)
   - Débrancher FTDI
   - Redémarrer ordinateur
   - Rebrancher FTDI
   - Windows devrait installer automatiquement

#. **Essayer autre port USB**

   - Certains ports USB peuvent avoir problèmes
   - Préférer ports USB directs (pas hub)

Problèmes Arduino IDE
---------------------

.. admonition:: Configuration Arduino IDE

 #. ☐ **Type de carte correct ?**

    - Menu : Outils → Type de carte → **Arduino Uno**
    - Pas Arduino Nano, pas Mega

 #. ☐ **Processeur correct ?** (si option disponible)

    - ATmega328P

 #. ☐ **Port libre ?**

    - Aucun autre programme (terminal, moniteur série d’un autre logiciel) ne doit occuper le port pendant le téléversement

**Solutions supplémentaires :**

- Fermer et rouvrir Arduino IDE
- Débrancher/rebrancher FTDI
- Essayer sur autre ordinateur (test matériel vs logiciel)

Firmware se Téléverse mais Rien ne Fonctionne
=============================================

**Symptôme :** Téléversement réussi mais routeur inactif

Vérification via Moniteur Série
-------------------------------

#. **Ouvrir Moniteur Série**

   - Menu : Outils → Moniteur série
   - Ou raccourci : Ctrl+Maj+M

#. **Régler les paramètres en bas à droite :**

   - **Baud rate :** 9 600
   - **Fin de ligne :** sans importance (le routeur ne lit rien sur le port série)

#. **Redémarrer le routeur** : l’ouverture du moniteur série le redémarre (signal DTR). Sinon, fermer puis rouvrir le moniteur série, ou couper puis remettre l’alimentation. La carte elle-même n’a pas de bouton reset ; un bouton externe peut se brancher sur son connecteur J1 « RESET ».

#. **Vous devriez voir**, après 3 secondes, la configuration du routeur, terminée par ``----``, puis une ligne de mesures toutes les 5 secondes (par défaut). Extrait d’une capture réelle, en triphasé avec la sortie ``HumanReadable`` :

   .. code-block:: text

      ----------------------------------
      Sketch ID: Mk2_3phase_RFdatalog_temp
      From branch 'dev', commit 0d88595e
      ...
      Datalogging capability in Human-readable format
      ...
      ----
      308.52, P:-2, P1:0, P2:-1, P3:-1, V1:232.86, V2:232.88, V3:233.12, (minSampleSets/MC 32, #ofSampleSets 8011)

   En monophasé, la ligne de mesures donne ``P:``, ``V:`` et, avec la sonde CT2, ``diverted <W> W, <Wh> Wh``. Voir aussi *Messages Attendus* dans :ref:`logiciel-monophase` ou :ref:`logiciel-triphase`.

**Si pas de messages :**

.. admonition:: Diagnostics oscillateur

 Le microcontrôleur nécessite un oscillateur pour fonctionner.

 #. ☐ **Quartz/résonateur bien soudé ?**

    - Composant à 2 pattes près de l’ATmega328P
    - Soudures correctes ?

**Si la configuration est lisible, mais la suite illisible :**

- C’est normal avec le ``config.h`` fourni : ``SERIAL_OUTPUT_TYPE`` y est en ``IoT``. Le routeur affiche sa configuration à 9600 bauds 8N1, puis passe en 7E1 pour le module mk2Wifi.
- Pour lire les mesures au moniteur série, passer ``SERIAL_OUTPUT_TYPE`` à ``SerialOutputType::HumanReadable`` dans ``config.h`` et téléverser à nouveau.

**Si rien n’est lisible :**

- Vérifier que le baud rate = 9 600
- Si toujours illisible → Problème oscillateur (fréquence incorrecte : quartz X1 16 MHz, condensateurs C7/C8)

Erreur « Out of Memory » lors de la Compilation
===============================================

**Symptôme :**

.. code-block:: text

 Sketch too big; see https://support.arduino.cc/hc/en-us/articles/360013825179

**Cause :** Trop de fonctionnalités activées dans config.h

**Solution :**

#. Ouvrir onglet ``config.h`` dans Arduino IDE
#. Désactiver les fonctionnalités non nécessaires : mettre à ``false`` celles qui ne servent pas, parmi ``ENABLE_DEBUG``, ``RF_LOGGING_PRESENT``, ``RELAY_DIVERSION``, ``TEMP_SENSOR_PRESENT`` et ``DUAL_TARIFF``. Par exemple :

   .. code-block:: cpp

      inline constexpr bool ENABLE_DEBUG{ false };
      inline constexpr bool RF_LOGGING_PRESENT{ false };

   Ne pas mettre ces lignes en commentaire : le firmware ne compilerait plus. Une fonction désactivée doit aussi avoir sa broche à ``unused_pin`` (par exemple ``dualTariffPin``, ou la broche de ``temperatureSensing``), sinon la compilation le signale. Le configurateur (:ref:`monophasé <configurateur-monophase>`, :ref:`triphasé <configurateur-triphase>`) fait ces changements de façon cohérente.

#. Recompiler et téléverser

