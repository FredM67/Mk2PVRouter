.. _choix-configuration:

=========================
Choix de la configuration
=========================

⏱️ **Temps de lecture** : 5–10 minutes

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Connaissance de votre type de raccordement électrique (monophasé ou triphasé)

La carte universelle 3phaseDiverter supporte trois configurations. Cette page vous aide à déterminer celle qui correspond à votre installation.

Quel est votre type de raccordement ?
--------------------------------------

.. admonition:: À retenir

   Peu importe l’installation de production d’électricité (monophasée, biphasée, triphasée), le routeur **DOIT** correspondre au type de raccordement au réseau électrique (Enedis ou régie locale).

   **Exemple** : Si votre raccordement au réseau est triphasé, vous devez utiliser un routeur triphasé, même si votre production est monophasée.

Guide de décision
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Configuration
     - Raccordement réseau
     - Neutre disponible ?
     - Cas d’usage typique
   * - **Monophasé**
     - 1 phase + neutre
     - Oui
     - Majorité des foyers en France et en Europe (230 V)
   * - **Triphasé avec neutre**
     - 3 phases + neutre
     - Oui
     - Foyers avec abonnement triphasé, souvent au-delà de 12 kVA (400 V / 230 V)
   * - **Triphasé 3 × 230 V sans neutre**
     - 3 phases, 230 V entre phases
     - Non
     - Certains foyers en Belgique et en Norvège, anciennes installations rurales

Comment identifier votre raccordement ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Vérifiez la plaque signalétique de votre compteur électrique.** Un pictogramme de câblage indique le nombre de conducteurs traversant le compteur :

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Symbole
     - Type
     - Ce que montre le pictogramme
   * - ``1~`` ou ``1P+N``
     - Monophasé
     - **2 fils** passant dans le compteur (phase + neutre)
   * - ``3~+N`` ou ``3P+N``
     - Triphasé avec neutre
     - **4 fils** passant dans le compteur (3 phases + neutre)
   * - ``3~`` ou ``3P``
     - Triphasé 3 × 230 V sans neutre
     - **3 fils** passant dans le compteur (3 phases, pas de neutre)

.. tip::
   Sur un compteur Linky, le type de raccordement est aussi affiché sur l’écran (« MONO » ou « TRI »).

**En cas de doute**, consultez votre contrat d’électricité ou contactez votre fournisseur d’énergie.

Différences par configuration
------------------------------

Composants traversants à souder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La carte universelle est livrée avec tous les composants :term:`CMS` déjà soudés en usine, sauf les éclateurs GDT optionnels. Seuls les composants traversants (through-hole) et, si vous les montez, ces éclateurs doivent être soudés par l’utilisateur. Les composants à souder varient selon la configuration choisie :

.. list-table::
   :header-rows: 1
   :widths: 40 20 20 20

   * - Composant
     - Mono
     - Tri+N
     - Tri-N
   * - Support IC1 (ATmega328P DIP-28)
     - ✔
     - ✔
     - ✔
   * - Quartz X1
     - ✔
     - ✔
     - ✔
   * - Condensateur film C1 (1 µF 310 VAC)
     - ✔
     - ✔
     - ✔
   * - Self de mode commun FL1
     - ✔
     - ✔
     - ✔
   * - Module d’alimentation PS1 (MPC10-5)
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`SMA` (antenne RF, optionnel)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Module RF (RFM69CW, optionnel)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Connecteurs signaux (FTDI, RESET ; TRIG_EXT et UART_EXT pour le mk2Wifi, recommandés dans tous les cas)
     - ✔
     - ✔
     - ✔
   * - Connecteur OLED (écran, optionnel)
     - (opt.)
     - –
     - –
   * - Connecteurs des sorties numériques D2–D13
     - selon les sorties utilisées
     - selon les sorties utilisées
     - selon les sorties utilisées
   * - Connecteurs DS18B20 (sondes de température, optionnel)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Fusibles FS0, FS1
     - ✔
     - ✔
     - ✔
   * - Fusible FS2
     -
     - ✔
     - ✔
   * - Fusible FS3
     -
     - ✔
     -
   * - Module protection GM1
     - ✔
     - ✔
     - ✔
   * - Module protection GM2
     -
     - ✔
     - ✔
   * - Module protection GM3
     -
     - ✔
     -
   * - Transformateur :term:`ZMPT101K` TR1
     - ✔
     - ✔
     - ✔
   * - Transformateur :term:`ZMPT101K` TR2
     -
     - ✔
     - ✔
   * - Transformateur :term:`ZMPT101K` TR3
     -
     - ✔
     -
   * - Connecteur :term:`CT` CT1
     - ✔
     - ✔
     - ✔
   * - Connecteur :term:`CT` CT2 (optionnel en mono pour mesure diversion)
     - (opt.)
     - ✔
     - ✔
   * - Connecteur :term:`CT` CT3
     -
     - ✔
     -
   * - Résistances de :term:`burden <Burden>` (CT à sortie courant, dépannage)
     - (opt.) D13, D23
     - (opt.) D13, D23, D33
     - (opt.) D13, D23
   * - Paires varistance + éclateur RV0 + GDT0, RV1 + GDT1 (protection optionnelle, toujours **par paire**)
     - (opt.)
     - (opt.)
     - (opt.)
   * - Paire RV2 + GDT2 (protection optionnelle, toujours **par paire**)
     -
     - (opt.)
     - (opt.)
   * - Paire RV3 + GDT3 (protection optionnelle, toujours **par paire**)
     -
     - (opt.)
     -
   * - Connecteur secteur
     - 3 voies
     - 5 voies
     - 5 voies

Configuration des cavaliers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les cavaliers de soudure (V sel., SDA, SCL, IRQ, NSS, TEMP, +5V Rail) et le cavalier fil GND_LINK doivent être configurés selon la configuration choisie. Consultez le chapitre :ref:`cavaliers` pour les détails.

Résumé rapide :

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Cavalier
     - Mono
     - Tri+N
     - Tri-N
   * - V sel.
     - 1–centre (3,3 V, d’usine)
     - 1–centre (3,3 V, d’usine)
     - 1–centre (3,3 V, d’usine)
   * - SDA
     - 3–centre (I2C SDA)
     - 1–centre (tension L3)
     - 1–centre (tension L3)
   * - SCL
     - 3–centre (I2C SCL)
     - 1–centre (courant L3)
     - 1–centre (courant L3)
   * - IRQ, NSS
     - Fermés si module RF
     - Fermés si module RF
     - Fermés si module RF
   * - TEMP
     - Voir :ref:`cavaliers`
     - Voir :ref:`cavaliers`
     - Voir :ref:`cavaliers`
   * - +5V Rail
     - Fermé si cartes relais
     - Fermé si cartes relais
     - Fermé si cartes relais
   * - GND_LINK
     - Voir :ref:`cavaliers`
     - Voir :ref:`cavaliers`
     - Voir :ref:`cavaliers`
   * - OLED disponible
     - Oui
     - Non
     - Non

Firmware
~~~~~~~~

Le firmware à utiliser dépend de la configuration :

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Configuration
     - Firmware
     - Dépôt
   * - Monophasé
     - PVRouter-1-phase
     - ``Mk2_1phase_RFdatalog_temp``
   * - Triphasé avec neutre
     - PVRouter-3-phase
     - ``Mk2_3phase_RFdatalog_temp``
   * - Triphasé 3 × 230 V sans neutre
     - PVRouter-3-phase
     - ``Mk2_3phase_RFdatalog_temp``

.. |br| raw:: html

  <br/>
