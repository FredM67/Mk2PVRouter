.. _cavaliers:

=================================
Configuration des cavaliers
=================================

⏱️ **Temps estimé** : 15–20 minutes

🔧 **Niveau de difficulté** : Débutant

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Configuration choisie (voir :ref:`choix-configuration`)
   | ☐ Assemblage de la carte terminé (voir :ref:`assemblage-carte-mere`)

Les :term:`cavaliers de soudure <Cavalier de soudure>` permettent de configurer le comportement de la carte universelle. Ils sont configurés en déposant une goutte de soudure entre deux pastilles adjacentes.

.. warning::
   La configuration des cavaliers doit être effectuée **avant** le premier test électrique. Une mauvaise configuration peut entraîner des mesures erronées ou un dysfonctionnement.

Vue d’ensemble
--------------

.. list-table::
   :header-rows: 1
   :widths: 12 12 76

   * - Cavalier
     - Pôles
     - Fonction
   * - V sel.
     - 3
     - Alimentation ATmega328P : 3–centre = 3,3 V (défaut), 1–centre = 5 V
   * - SDA
     - 3
     - Mesure tension L3 / I2C : 1–centre = tension L3, 3–centre = I2C SDA (OLED)
   * - SCL
     - 3
     - Mesure courant L3 / I2C : 1–centre = courant L3, 3–centre = I2C SCL (OLED)
   * - IRQ
     - 2
     - Module RF : relie l’IRQ du RFM69 à D2 de l’ATmega328P (face arrière)
   * - NSS
     - 2
     - Module RF : relie le NSS (chip select) du RFM69 à D10 de l’ATmega328P (face avant)
   * - TEMP
     - 3
     - Capteur DS18B20 : non soudé (pas de capteur), 1–centre (routeur), 3–centre (mk2Wifi)
   * - GND_LINK
     - 2
     - Pont entre Earth (terre de protection) et GND (masse basse tension) — cavalier fil 0,75 mm²
   * - +5V Rail
     - 2
     - Rail +5 V sorties : fermé = +5 V actif sur les connecteurs 1×03 (pour relais), ouvert = déconnecté (défaut)

Description détaillée
---------------------

V sel. — Alimentation ATmega328P
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles sérigraphié **V sel.** sur le :term:`PCB`. Il sélectionne la tension d’alimentation du microcontrôleur.

- **Position 3–centre** (défaut) : L’ATmega328P est alimenté en 3,3 V via le régulateur :term:`LDO` U1 (AP7361C-33E)
- **Position 1–centre** : L’ATmega328P est alimenté directement en 5 V depuis le module PS1 (MPC10-5)

.. warning::
   Si le module RF (RFM69CW) et/ou la carte :term:`mk2Wifi` sont utilisés, ce cavalier **doit impérativement** être en position **3–centre (3,3 V)**. Ces modules fonctionnent en 3,3 V — une alimentation en 5 V les **détruirait immédiatement**.

.. important::
   Après avoir soudé le cavalier en position **3–centre (3,3 V)**, vérifiez au multimètre (mode continuité) qu’il n’y a **pas de court-circuit** entre la pastille centrale et la pastille **1 (5 V)**. Un pont de soudure accidentel entre les deux côtés relierait le 5 V directement au 3,3 V, ce qui **détruirait le régulateur LDO, le module RF et/ou la carte mk2Wifi**.

SDA — Mesure tension L3 / I2C SDA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui sélectionne entre la mesure de tension de la phase L3 et le bus I2C.

- **Position 1–centre** : Mesure de tension de la phase L3 (via le :term:`ZMPT101K` TR3).
- **Position 3–centre** : Bus I2C (signal SDA). Permet l’utilisation de l’écran OLED.

SCL — Mesure courant L3 / I2C SCL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui sélectionne entre la mesure de courant de la phase L3 et le bus I2C.

- **Position 1–centre** : Mesure de courant de la phase L3 (via le connecteur CT3).
- **Position 3–centre** : Bus I2C (signal SCL). Permet l’utilisation de l’écran OLED.

.. note::
   SDA et SCL fonctionnent en paire :

   - **Triphasé** : les deux en position **1–centre** (mesure L3)
   - **Monophasé ou split-phase** : les deux en position **3–centre** (I2C pour écran OLED)

Cavaliers module RF — IRQ et NSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si le module radio RFM69CW est présent, **deux cavaliers de soudure** doivent être fermés :

**IRQ** (face arrière)

Cavalier à 2 pôles sérigraphié **IRQ** sur la face arrière du :term:`PCB`. Il relie la broche d’interruption (IRQ) du module RFM69 à la broche D2 (INT0) de l’ATmega328P.

**NSS** (face avant)

Cavalier à 2 pôles sérigraphié **NSS**, situé près du coin inférieur droit du module RF. Il relie la broche de sélection (chip select, NSS) du module RFM69 à la broche D10 (SPI SS) de l’ATmega328P.

Pour chaque cavalier :

- **Fermé** : obligatoire si le module RFM69CW est présent sur la carte
- **Ouvert** : le module RF n’est pas utilisé

TEMP — Capteur de température DS18B20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles sérigraphié **TEMP** sur le :term:`PCB`. Il configure l’acheminement du signal du capteur de température 1-Wire DS18B20.

- **Non soudé** : Aucun capteur DS18B20 utilisé. La broche D3 de l’ATmega328P reste disponible comme entrée/sortie numérique standard.
- **Position 1–centre** : Le capteur DS18B20 est géré par le **routeur** (ATmega328P, broche D3).
- **Position 3–centre** : Le capteur DS18B20 est géré par le module **mk2Wifi** (ESP32-C3, via le connecteur UART_EXT).

La résistance de pull-up nécessaire pour le bus 1-Wire est intégrée sur la carte (R6, 4,7 kΩ).

GND_LINK — Pont Earth–GND
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier fil qui relie la **terre de protection** (Earth, provenant du réseau électrique) à la **masse basse tension** (GND) du circuit. Il est réalisé avec un fil de 0,75 mm² soudé entre les deux pastilles.

Lorsque GND_LINK est **ouvert**, le circuit basse tension est entièrement isolé de la terre grâce à l’isolation galvanique du module d’alimentation MPC10-5. Lorsqu’il est **fermé**, la masse basse tension est référencée à la terre de protection.

.. note::
   La configuration recommandée dépend de votre installation. En cas de doute, laissez le cavalier **ouvert** — il pourra toujours être soudé ultérieurement.

« +5V Rail » — Rail +5 V sorties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 2 pôles situé en **haut à droite** de la carte. Il active le **rail +5 V** qui alimente la broche VCC des connecteurs 1×03 des sorties numériques (D2–D13).

- **Fermé** : le rail +5 V est actif — obligatoire si des **cartes de sortie relais** sont utilisées (le relais a besoin du +5 V pour sa bobine)
- **Ouvert** (défaut) : le rail +5 V est déconnecté des connecteurs de sortie

.. warning::
   Ne fermez ce cavalier que si vous utilisez des cartes de sortie relais. Les cartes de sortie :term:`triac` n’ont pas besoin de cette alimentation.

La LED témoin **+5V** (en haut à gauche de la carte) s’allume lorsque ce rail est actif.

Procédure de soudure des cavaliers
------------------------------------

.. warning::
   Travaillez **hors tension**. L’opération est réversible (à l’aide d’une tresse à dessouder), mais des modifications répétées risquent d’altérer les pistes en cuivre.

#. **Identifiez le cavalier** sur la carte à l’aide des repères sérigraphiés (V sel., SDA, SCL, IRQ, NSS, TEMP)

#. **Pour les cavaliers 3 pôles** (V sel., SDA, SCL, TEMP) : Déposez une goutte de soudure entre la pastille centrale et la pastille correspondant à la position souhaitée

#. **Pour les cavaliers 2 pôles** (IRQ, NSS, +5V Rail) : Déposez une goutte de soudure entre les deux pastilles

#. **Vérifiez** au multimètre (mode continuité) que le cavalier est bien fermé entre les bonnes pastilles

.. admonition:: ✅ Point de Contrôle — Cavaliers

   Avant de continuer, vérifiez :

   | ☐ V sel. configuré en position 3,3 V (sauf cas particulier)
   | ☐ SDA configuré selon votre configuration (tension L3 ou I2C SDA)
   | ☐ SCL configuré selon votre configuration (courant L3 ou I2C SCL)
   | ☐ TEMP configuré selon votre choix (non soudé, routeur ou mk2Wifi)
   | ☐ « +5V Rail » fermé si des cartes de sortie relais sont utilisées
   | ☐ Continuité vérifiée au multimètre pour chaque cavalier

.. |br| raw:: html

  <br/>
