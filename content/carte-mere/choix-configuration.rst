.. _choix-configuration:

=========================
Choix de la configuration
=========================

⏱️ **Temps de lecture** : 5-10 minutes

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Connaissance de votre type de raccordement électrique (monophasé ou triphasé)

La carte universelle 3phaseDiverter supporte quatre configurations. Cette page vous aide à déterminer celle qui correspond à votre installation.

Quel est votre type de raccordement ?
--------------------------------------

.. admonition:: À retenir

   Peu importe l'installation de production d'électricité (monophasée, biphasée, triphasée), le routeur **DOIT** correspondre au type de raccordement au réseau électrique (Enedis ou régie locale).

   **Exemple** : Si votre raccordement au réseau est triphasé, vous devez utiliser un routeur triphasé, même si votre production est monophasée.

Guide de décision
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Configuration
     - Raccordement réseau
     - Neutre disponible ?
     - Cas d'usage typique
   * - **Monophasé**
     - 1 phase + neutre
     - Oui
     - Habitation standard en France (230 V)
   * - **Triphasé avec neutre**
     - 3 phases + neutre
     - Oui
     - Grande habitation, atelier, bâtiment professionnel en France (400 V / 230 V)
   * - **Triphasé sans neutre**
     - 3 phases (triangle)
     - Non
     - Installations industrielles, certains réseaux ruraux
   * - **Split-phase**
     - 2 phases à 180°
     - Oui
     - Réseau nord-américain (120 V / 240 V)

Comment identifier votre raccordement ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Vérifiez votre compteur électrique :**

- **Compteur monophasé** : 2 fils principaux (phase + neutre) + terre
- **Compteur triphasé** : 4 fils principaux (3 phases + neutre) + terre, ou 3 fils (3 phases sans neutre) + terre

**En cas de doute**, consultez votre contrat d'électricité ou contactez votre fournisseur d'énergie.

Différences par configuration
------------------------------

Composants traversants à souder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La carte universelle est livrée avec tous les composants :term:`CMS` déjà soudés en usine. Seuls les composants traversants (through-hole) doivent être soudés par l'utilisateur. Les composants à souder varient selon la configuration choisie :

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 15 15

   * - Composant
     - Mono
     - Tri+N
     - Tri-N
     - Split
   * - Support IC1 (ATmega328P DIP-28)
     - ✔
     - ✔
     - ✔
     - ✔
   * - Quartz X1 + condensateurs C7, C8
     - ✔
     - ✔
     - ✔
     - ✔
   * - Condensateur électrolytique C3
     - ✔
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`SMA` CN1 (antenne RF)
     - ✔
     - ✔
     - ✔
     - ✔
   * - Cavalier fil GND_LINK
     - ✔
     - ✔
     - ✔
     - ✔
   * - Connecteurs signaux (FTDI, OLED, TRIG_EXT, UART_EXT)
     - ✔
     - ✔
     - ✔
     - ✔
   * - Cavaliers JP0–JP4 (configuration)
     - ✔
     - ✔
     - ✔
     - ✔
   * - Fusibles FS0, FS1
     - ✔
     - ✔
     - ✔
     - ✔
   * - Fusibles FS2, FS3
     -
     - ✔
     - ✔
     - ✔
   * - Module protection GM1
     - ✔
     - ✔
     - ✔
     - ✔
   * - Modules protection GM2, GM3
     -
     - ✔
     - ✔
     - ✔
   * - Transformateur :term:`ZMPT101K` TR1
     - ✔
     - ✔
     - ✔
     - ✔
   * - Transformateurs :term:`ZMPT101K` TR2, TR3
     -
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`CT` CT1
     - ✔
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`CT` CT2 (optionnel en mono pour mesure diversion)
     - (opt.)
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`CT` CT3
     -
     - ✔
     - ✔
     -
   * - Varistances RV0, RV1 (protection optionnelle)
     - (opt.)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Varistances RV2, RV3 (protection optionnelle)
     -
     - (opt.)
     - (opt.)
     - (opt.)
   * - Éclateurs GDT0, GDT1 (protection optionnelle)
     - (opt.)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Éclateurs GDT2, GDT3 (protection optionnelle)
     -
     - (opt.)
     - (opt.)
     - (opt.)
   * - Connecteur PWR1
     - 3 voies
     - 5 voies
     - 5 voies
     - 5 voies

Configuration des cavaliers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les cavaliers de soudure JP0–JP4 et GND_LINK doivent être configurés selon la configuration choisie. Consultez le chapitre :ref:`cavaliers` pour les détails.

Résumé rapide :

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20

   * - Cavalier
     - Mono
     - Tri+N
     - Tri-N
     - Split
   * - JP0
     - 3,3 V
     - 3,3 V
     - 3,3 V
     - 3,3 V
   * - JP1
     - I2C SDA
     - A4' (tension L3)
     - A4' (tension L3)
     - I2C SDA
   * - JP2
     - I2C SCL
     - A5' (courant L3)
     - A5' (courant L3)
     - I2C SCL
   * - JP4
     - Au choix
     - Au choix
     - Au choix
     - Au choix
   * - GND_LINK
     - Fermé
     - Fermé
     - Fermé
     - Fermé
   * - OLED disponible
     - Oui
     - Non
     - Non
     - Oui

Firmware
~~~~~~~~

Le firmware à utiliser dépend de la configuration :

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Configuration
     - Firmware
     - Dépôt
   * - Monophasé
     - PVRouter-1-phase
     - ``Mk2_fasterControl_Full``
   * - Triphasé avec neutre
     - PVRouter-3-phase
     - ``Mk2_3phase_RFdatalog_temp``
   * - Triphasé sans neutre
     - PVRouter-3-phase
     - ``Mk2_3phase_RFdatalog_temp``
   * - Split-phase
     - PVRouter-1-phase
     - ``Mk2_fasterControl_Full``

.. |br| raw:: html

  <br/>
