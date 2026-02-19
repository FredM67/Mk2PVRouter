.. _cavaliers:

=================================
Configuration des cavaliers
=================================

⏱️ **Temps estimé** : 15-20 minutes

🔧 **Niveau de difficulté** : Débutant

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Configuration choisie (voir :ref:`choix-configuration`)
   | ☐ Assemblage de la carte terminé (voir :ref:`assemblage-carte-mere`)

Les :term:`cavaliers de soudure <Cavalier de soudure>` permettent de configurer le comportement de la carte universelle. Ils sont configurés en déposant une goutte de soudure entre deux pastilles adjacentes.

.. warning::
   La configuration des cavaliers doit être effectuée **avant** le premier test électrique. Une mauvaise configuration peut entraîner des mesures erronées ou un dysfonctionnement.

Vue d'ensemble
--------------

.. list-table::
   :header-rows: 1
   :widths: 12 12 76

   * - Cavalier
     - Pôles
     - Fonction
   * - V sel.
     - 3
     - Alimentation ATmega328P : 3–centre = 3,3 V (défaut), 1–centre = 5 V
   * - JP1
     - 3
     - Broche A4 : mesure tension L3 (A4') ou I2C SDA
   * - JP2
     - 3
     - Broche A5 : mesure courant L3 (A5') ou I2C SCL
   * - JP3
     - 2
     - Activation du module RF (RFM69) : relie l'IRQ du module à D2 de l'ATmega328P
   * - TEMP
     - 3
     - Capteur DS18B20 : non soudé (pas de capteur), 1–centre (routeur), 3–centre (mk2Wifi)
   * - GND_LINK
     - 2
     - Pont entre Earth (terre de protection) et GND (masse basse tension) — cavalier fil 0,75 mm²

Description détaillée
---------------------

V sel. — Alimentation ATmega328P
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles sérigraphié **V sel.** sur le :term:`PCB`. Il sélectionne la tension d'alimentation du microcontrôleur.

- **Position 3–centre** (défaut) : L'ATmega328P est alimenté en 3,3 V via le régulateur :term:`LDO` U1 (AP2112K-3.3)
- **Position 1–centre** : L'ATmega328P est alimenté directement en 5 V depuis le module PS1 (RAC05E)

.. danger::
   Si le module RF (RFM69CW) et/ou la carte :term:`mk2Wifi` sont utilisés, ce cavalier **doit impérativement** être en position **3–centre (3,3 V)**. Ces modules fonctionnent en 3,3 V — une alimentation en 5 V les **détruirait immédiatement**.

JP1 — Sélection broche A4
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui configure la broche analogique A4 de l'ATmega328P.

- **Position 1–centre** : La broche A4 est connectée au circuit de mesure de tension de la phase L3 (via le :term:`ZMPT101K` TR3).
- **Position 3–centre** : La broche A4 est connectée au bus I2C (signal SDA). Permet l'utilisation de l'écran OLED.

JP2 — Sélection broche A5
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui configure la broche analogique A5 de l'ATmega328P.

- **Position 1–centre** : La broche A5 est connectée au circuit de mesure de courant de la phase L3 (via le connecteur CT3).
- **Position 3–centre** : La broche A5 est connectée au bus I2C (signal SCL). Permet l'utilisation de l'écran OLED.

.. note::
   JP1 et JP2 fonctionnent en paire :

   - **Triphasé** : les deux en position **1–centre** (mesure L3)
   - **Monophasé ou split-phase** : les deux en position **3–centre** (I2C pour écran OLED)

JP3 — Module RF (RFM69)
~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 2 pôles situé sur la **face arrière** du :term:`PCB`. Il relie la broche IRQ du module radio RFM69 à la broche D2 (INT0) de l'ATmega328P.

- **Fermé** : Le module RF est activé — obligatoire si le module RFM69CW est présent sur la carte
- **Ouvert** : Le module RF n'est pas utilisé

TEMP — Capteur de température DS18B20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles sérigraphié **TEMP** sur le :term:`PCB`. Il configure l'acheminement du signal du capteur de température 1-Wire DS18B20.

- **Non soudé** : Aucun capteur DS18B20 utilisé. La broche D3 de l'ATmega328P reste disponible comme entrée/sortie numérique standard.
- **Position 1–centre** : Le capteur DS18B20 est géré par le **routeur** (ATmega328P, broche D3).
- **Position 3–centre** : Le capteur DS18B20 est géré par le module **mk2Wifi** (ESP32-C3, via le connecteur UART_EXT).

La résistance de pull-up nécessaire pour le bus 1-Wire est intégrée sur la carte (R6, 4,7 kΩ).

GND_LINK — Pont Earth–GND
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier fil qui relie la **terre de protection** (Earth, provenant du réseau électrique) à la **masse basse tension** (GND) du circuit. Il est réalisé avec un fil de 0,75 mm² soudé entre les deux pastilles.

Lorsque GND_LINK est **ouvert**, le circuit basse tension est entièrement isolé de la terre grâce à l'isolation galvanique du module d'alimentation RAC05E. Lorsqu'il est **fermé**, la masse basse tension est référencée à la terre de protection.

.. note::
   La configuration recommandée dépend de votre installation. En cas de doute, laissez le cavalier **ouvert** — il pourra toujours être soudé ultérieurement.

Procédure de soudure des cavaliers
------------------------------------

.. warning::
   Travaillez **hors tension**. L'opération est réversible (à l'aide d'une tresse à dessouder), mais des modifications répétées risquent d'altérer les pistes en cuivre.

#. **Identifiez le cavalier** sur la carte à l'aide des repères sérigraphiés (V sel., JP1, JP2, JP3, TEMP)

#. **Pour les cavaliers 3 pôles** (V sel., JP1, JP2, TEMP) : Déposez une goutte de soudure entre la pastille centrale et la pastille correspondant à la position souhaitée

#. **Pour les cavaliers 2 pôles** (JP3) : Déposez une goutte de soudure entre les deux pastilles

#. **Vérifiez** au multimètre (mode continuité) que le cavalier est bien fermé entre les bonnes pastilles

.. admonition:: ✅ Point de Contrôle — Cavaliers

   Avant de continuer, vérifiez :

   | ☐ V sel. configuré en position 3,3 V (sauf cas particulier)
   | ☐ JP1 configuré selon votre configuration (I2C SDA ou A4')
   | ☐ JP2 configuré selon votre configuration (I2C SCL ou A5')
   | ☐ TEMP configuré selon votre choix (non soudé, routeur ou mk2Wifi)
   | ☐ Continuité vérifiée au multimètre pour chaque cavalier

.. |br| raw:: html

  <br/>
