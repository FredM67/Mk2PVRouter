.. _cavaliers:

=================================
Configuration des cavaliers
=================================

⏱️ **Temps estimé** : 15-20 minutes

🔧 **Niveau de difficulté** : Débutant

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

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
   * - JP0
     - 3
     - Alimentation ATmega328P : 3,3 V (défaut) ou 5 V
   * - JP1
     - 3
     - Broche A4 : mesure tension L3 (A4') ou I2C SDA
   * - JP2
     - 3
     - Broche A5 : mesure courant L3 (A5') ou I2C SCL
   * - JP3
     - 2
     - Configuration de déclenchement
   * - JP4
     - 3
     - DS18B20 géré par le routeur (D3) ou par le module :term:`mk2Wifi` (« TEMP »)
   * - GND_LINK
     - 2
     - Pont entre GND et AGND (cavalier fil 0,75 mm²)

Description détaillée
---------------------

JP0 — Alimentation ATmega328P
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui sélectionne la tension d'alimentation du microcontrôleur.

- **Position 3,3 V** (défaut) : L'ATmega328P est alimenté en 3,3 V via le régulateur :term:`LDO` AP2112K-3.3
- **Position 5 V** : L'ATmega328P est alimenté directement en 5 V depuis le module RAC05E

.. important::
   La position **3,3 V est recommandée** pour tous les cas d'utilisation normaux. La position 5 V n'est utile que dans des cas spécifiques (alimentation externe 5 V).

JP1 — Sélection broche A4
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui configure la broche analogique A4 de l'ATmega328P.

- **Position I2C SDA** : La broche A4 est connectée au bus I2C (signal SDA). Permet l'utilisation de l'écran OLED.
- **Position A4'** : La broche A4 est connectée au circuit de mesure de tension de la phase L3 (via le :term:`ZMPT101K` TR3).

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Configuration
     - Position JP1
     - Raison
   * - Monophasé
     - I2C SDA
     - Écran OLED disponible, pas de phase L3
   * - Triphasé
     - A4' (tension L3)
     - Mesure tension L3 nécessaire
   * - Split-phase
     - I2C SDA
     - Pas de phase L3

JP2 — Sélection broche A5
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui configure la broche analogique A5 de l'ATmega328P.

- **Position I2C SCL** : La broche A5 est connectée au bus I2C (signal SCL). Permet l'utilisation de l'écran OLED.
- **Position A5'** : La broche A5 est connectée au circuit de mesure de courant de la phase L3 (via le connecteur CT3).

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Configuration
     - Position JP2
     - Raison
   * - Monophasé
     - I2C SCL
     - Écran OLED disponible, pas de CT3
   * - Triphasé
     - A5' (courant L3)
     - Mesure courant L3 nécessaire
   * - Split-phase
     - I2C SCL
     - Pas de CT3

.. note::
   JP1 et JP2 fonctionnent en paire. En mode triphasé, les deux doivent être en position mesure (A4'/A5'). En mode monophasé ou split-phase, les deux doivent être en position I2C (SDA/SCL).

JP3 — Configuration de déclenchement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 2 pôles pour la configuration du mode de déclenchement des sorties.

JP4 — Capteur de température DS18B20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier à 3 pôles qui sélectionne quel microcontrôleur gère le capteur de température 1-Wire DS18B20.

- **Position routeur (D3)** : Le signal DS18B20 est acheminé vers la broche D3 de l'ATmega328P. Le firmware du routeur gère directement le capteur.
- **Position mk2Wifi (TEMP)** : Le signal DS18B20 est acheminé vers le module d'extension :term:`mk2Wifi` via le connecteur UART_EXT (broche 2). L'ESP32-C3 gère le capteur.

.. tip::
   Si vous n'utilisez pas le module mk2Wifi, laissez JP4 en position **routeur (D3)**.
   Si vous utilisez le module mk2Wifi et souhaitez que celui-ci gère la température (pour transmission WiFi par exemple), placez JP4 en position **mk2Wifi (TEMP)**.

La résistance de pull-up nécessaire pour le bus 1-Wire est intégrée sur la carte (R6, 4,7 kΩ).

GND_LINK — Pont GND–AGND
~~~~~~~~~~~~~~~~~~~~~~~~~

Cavalier fil qui relie la masse numérique (GND) à la masse analogique (AGND).

.. important::
   Ce cavalier **doit toujours être fermé** en fonctionnement normal. Il est réalisé avec un fil de 0,75 mm² soudé entre les deux pastilles.

   Sans ce pont, les circuits analogiques (mesure de tension et de courant) n'ont pas de référence de masse et ne fonctionnent pas.

Procédure de soudure des cavaliers
------------------------------------

.. warning::
   Travaillez **hors tension**. Les cavaliers sont configurés une seule fois et ne sont pas prévus pour être modifiés fréquemment.

#. **Identifiez le cavalier** sur la carte à l'aide des repères sérigraphiés (JP0, JP1, JP2, JP3, JP4, GND_LINK)

#. **Pour les cavaliers 3 pôles** (JP0, JP1, JP2, JP4) : Déposez une goutte de soudure entre la pastille centrale et la pastille correspondant à la position souhaitée

#. **Pour les cavaliers 2 pôles** (JP3, GND_LINK) : Déposez une goutte de soudure entre les deux pastilles

#. **Pour GND_LINK** : Soudez un fil de cuivre de 0,75 mm² entre les deux pastilles (la distance est trop grande pour un simple pont de soudure)

#. **Vérifiez** au multimètre (mode continuité) que le cavalier est bien fermé entre les bonnes pastilles

.. admonition:: ✅ Point de Contrôle — Cavaliers

   Avant de continuer, vérifiez :

   | ☐ JP0 configuré en position 3,3 V (sauf cas particulier)
   | ☐ JP1 configuré selon votre configuration (I2C SDA ou A4')
   | ☐ JP2 configuré selon votre configuration (I2C SCL ou A5')
   | ☐ JP4 configuré selon votre choix (routeur ou mk2Wifi)
   | ☐ GND_LINK fermé (fil soudé)
   | ☐ Continuité vérifiée au multimètre pour chaque cavalier

.. |br| raw:: html

  <br/>
