.. _carte-mere-presentation:

======================================
Présentation de la carte universelle
======================================

⏱️ **Temps de lecture** : 10-15 minutes

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Choix de la configuration effectué (voir :ref:`choix-configuration`)

Vue d'ensemble
--------------

La carte **3phaseDiverter** (rév. 6.0) est la carte principale universelle du Mk2 PV Router. Elle remplace les anciennes cartes monophasée et triphasée séparées par une carte unique capable de gérer les quatre configurations supportées :

- **Monophasé** : une phase, un neutre (230 V)
- **Triphasé avec neutre** : trois phases + neutre (400 V / 230 V)
- **Triphasé sans neutre** : trois phases sans neutre (400 V)
- **Split-phase** : deux phases à 180° (120 V / 240 V, réseau nord-américain)

La sélection de la configuration se fait uniquement par les :term:`cavaliers de soudure <Cavalier de soudure>` et le choix des connecteurs — tous les composants CMS sont identiques quelle que soit la configuration.

Caractéristiques principales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Microcontrôleur **ATmega328P** (16 MHz, DIP-28)
- Jusqu'à 3 capteurs de tension (:term:`ZMPT101K`, rapport 1000:1000)
- Jusqu'à 3 connecteurs de transformateur de courant (:term:`CT` 1–CT3)
- Module radio **RFM69CW** (bande ISM 433/868 MHz) avec connecteur :term:`SMA`
- Alimentation AC-DC intégrée (**RAC05E-05SKT**, 5 V / 3 W)
- Régulateur :term:`LDO` **AP2112K-3.3** (5 V → 3,3 V, 600 mA)
- Protection parafoudre multiniveau (:term:`GDT`, fusibles, :term:`MOV`, self de mode commun)
- Buffer de la référence interne 1,1 V (AREF) par amplificateur opérationnel **LMV321A**
- Connecteurs d'extension : **TRIG_EXT**, **UART_EXT**, **FTDI**, **OLED**
- Compatible avec le module d'extension :term:`mk2Wifi`

Images de la carte
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Face avant (assemblée)
     - Face arrière
   * - .. figure:: ../img/mainboard-front.png
          :alt: Carte universelle — face avant assemblée

     - .. figure:: ../img/mainboard-back.png
          :alt: Carte universelle — face arrière

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Composants :term:`CMS` uniquement
     - Circuit imprimé nu
   * - .. figure:: ../img/mainboard-smd.png
          :alt: Carte universelle — composants CMS

     - .. figure:: ../img/mainboard-bare.png
          :alt: Carte universelle — PCB nu

Connecteurs
-----------

.. list-table::
   :header-rows: 1
   :widths: 15 25 20 40

   * - Réf
     - Valeur
     - Boîtier
     - Description
   * - PWR1
     - Conn_01x05_PWR
     - Phoenix Contact MSTBV 2,5
     - Entrée secteur (1×5, pas 5,08 mm). En monophasé, un connecteur 3 voies est fourni.
   * - TRIG_EXT
     - Conn_01x06
     - Barrette mâle 1×06 2,54 mm
     - Connecteur déclenchement/GPIO
   * - UART_EXT
     - Conn_01x06
     - Barrette mâle 1×06 2,54 mm
     - Connecteur UART + DS18B20
   * - FTDI
     - Conn_01x06
     - Molex SL 1×06 2,54 mm
     - Connecteur programmation/débogage
   * - OLED
     - Conn_01x04
     - Molex SL 1×04 2,54 mm
     - Connecteur écran I2C (monophasé uniquement)
   * - CN1
     - BU-SMA-V
     - :term:`SMA` vertical
     - Connecteur antenne :term:`RF` 50 Ω
   * - CT1
     - Conn_01x02
     - Molex SL 1×02 2,54 mm
     - Entrée :term:`CT` L1
   * - CT2
     - Conn_01x02
     - Molex SL 1×02 2,54 mm
     - Entrée :term:`CT` L2 (triphasé uniquement)
   * - CT3
     - Conn_01x02
     - Molex SL 1×02 2,54 mm
     - Entrée :term:`CT` L3 (triphasé uniquement)

Brochage des connecteurs
-------------------------

PWR1 — Entrée secteur (1×5 Phoenix Contact)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - Terre
   * - 2
     - Neutre
   * - 3
     - L1
   * - 4
     - L2
   * - 5
     - L3

En monophasé, un connecteur 3 voies est fourni (Terre, Neutre, L1).

TRIG_EXT — Déclenchement/GPIO (1×6 barrette mâle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - D8
   * - 3
     - D7
   * - 4
     - D6
   * - 5
     - D5
   * - 6
     - D9

UART_EXT — UART + DS18B20 (1×6 barrette mâle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - DS18B20
   * - 3
     - +5 V
   * - 4
     - RX
   * - 5
     - TX
   * - 6
     - DTR

Les noms des signaux (TX, RX) sont du point de vue de la **carte principale** : TX transporte les données émises par l'ATmega328P, RX les données reçues.

FTDI — Programmation/débogage (1×6 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - CTS (NC)
   * - 3
     - VCC (NC)
   * - 4
     - TXO
   * - 5
     - RXI
   * - 6
     - DTR

Brochage compatible avec les adaptateurs FTDI standard. Le signal DTR permet l'auto-reset pour le téléversement via le bootloader Arduino.

OLED — Écran I2C (1×4 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - VCC
   * - 3
     - SCL
   * - 4
     - SDA

.. important::
   Le bus I2C est partagé sur les broches A4 (SDA) et A5 (SCL) de l'ATmega328P. En mode triphasé, ces broches sont affectées à la mesure de tension/courant L3 — l'écran OLED n'est alors **pas disponible**. Le choix est effectué par les cavaliers **JP1** et **JP2** (voir :ref:`cavaliers`).

CT1 / CT2 / CT3 — Transformateurs de courant (1×2 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - Signal CT
   * - 2
     - AGND

CT1 est utilisé en monophasé et en triphasé. CT2 et CT3 sont utilisés uniquement en triphasé.

Alimentation
------------

Chaîne d'alimentation
~~~~~~~~~~~~~~~~~~~~~~

Le secteur entre par le connecteur **PWR1** et traverse une chaîne de protection avant d'atteindre le module d'alimentation :

.. code-block:: text

   Secteur → GDT (éclateurs) → Fusibles (FS0–FS3) → Varistances (RV0–RV3, GM1–GM3)
          → Self de mode commun (FL1) → Condensateur film (C1)
          → PS1 (RAC05E-05SKT) : 230 VAC → 5 VDC, 3 W
          → D1 (SMBJ7.0A) : protection TVS côté 5 V
          → U1 (AP2112K-3.3) : 5 V → 3,3 V, 600 mA

Protection contre les surtensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La carte intègre plusieurs niveaux de protection contre les surtensions transitoires (foudre, commutations sur le réseau). Deux niveaux sont obligatoires, un troisième est optionnel.

**Niveau 1 — Modules de protection GM1–GM3** (obligatoire)

Chaque phase est protégée par un module combiné :term:`GDT`\+\ :term:`MOV`. Ces modules constituent la protection principale des circuits de mesure. GM1 protège la phase L1, GM2 la phase L2, GM3 la phase L3 (triphasé avec neutre uniquement).

**Niveau 2 — Fusibles FS0–FS3** (obligatoire)

Les fusibles protègent les circuits de mesure contre les surintensités. Ils sont dimensionnés pour couper en cas de court-circuit ou de défaut sur un transformateur :term:`ZMPT101K`.

**Niveau 3 — Varistances RV0–RV3 et éclateurs GDT0–GDT3** (optionnel)

Ce niveau de protection supplémentaire est recommandé pour les installations exposées aux surtensions (zones rurales, lignes aériennes, régions à forte activité orageuse). Les éclateurs :term:`GDT` constituent la première ligne de défense et dévient les surtensions les plus violentes. Les varistances :term:`MOV` écrêtent les surtensions résiduelles.

.. note::
   Les composants optionnels (RV0–RV3, GDT0–GDT3) ne sont pas fournis dans le kit de base. Ils peuvent être ajoutés ultérieurement sans modifier le reste du circuit.

Rails d'alimentation
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Rail
     - Tension
     - Usage
   * - +5 V
     - 5 V
     - Connecteurs UART_EXT et FTDI
   * - +3,3 V
     - 3,3 V
     - ATmega328P, module RFM69CW
   * - AVCC
     - 3,3 V (filtré)
     - Référence analogique ATmega328P, connecteur OLED
   * - GND
     - 0 V
     - Masse numérique
   * - AGND
     - 0 V
     - Masse analogique

Intégration du module mk2Wifi
------------------------------

La carte principale est conçue pour accueillir le module d'extension :term:`mk2Wifi` via les connecteurs TRIG_EXT et UART_EXT :

- La carte principale utilise des **barrettes mâles** ; la mk2Wifi utilise des **barrettes femelles**
- L'alimentation +5 V est fournie par la carte principale via UART_EXT broche 3
- L'UART (TX/RX) assure la communication série avec le module d'extension
- Le signal DS18B20 est acheminé via UART_EXT broche 2 pour la mesure de température 1-Wire
- Les signaux GPIO D5–D9 fournissent les sorties de déclenchement/commande via TRIG_EXT
- Le bus I2C (SCL/SDA) est **local au module mk2Wifi uniquement** — il n'est pas routé vers la carte principale

.. |br| raw:: html

  <br/>
