.. _bibliotheques-monophase:

Bibliothèques pour l’Arduino IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avec l’Arduino IDE, installer ces bibliothèques par le Gestionnaire de bibliothèques (menu : **Outils → Gérer les bibliothèques...**) :

- **OneWire** par Jim Studt et al. (version 2.3.7 ou supérieure)
- **RFM69** par Felix Rusu, LowPowerLab (version 1.5.3 ou supérieure)
- **U8g2** par Oliver Kraus (version 2.36.5 ou supérieure)
- **SPI** : incluse avec l’Arduino IDE

Elles sont toutes nécessaires, même sans sonde de température, sans module RF ni afficheur OLED : le code inutilisé est éliminé à la compilation. Avec PlatformIO, tout vient de `platformio.ini` : rien à installer. Voir le `Readme du firmware <https://github.com/FredM67/PVRouter-1-phase/blob/dev/Mk2_1phase_RFdatalog_temp/Readme.md#bibliothèques-requises-pour-larduino-ide>`_.


Étape 1 : Téléchargement du Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ouvrir le navigateur : https://github.com/FredM67/PVRouter-1-phase
#. Choisir la branche `dev` dans le menu des branches, au-dessus de la liste des fichiers
#. Cliquer sur le bouton vert **« Code »** → **« Download ZIP »**
#. Enregistrer le fichier `PVRouter-1-phase-dev.zip`
#. Extraire le contenu dans un dossier de votre choix (exemple : `Documents/Arduino/`)
#. Le firmware se trouve dans : `PVRouter-1-phase-dev/Mk2_1phase_RFdatalog_temp/`

Structure du Firmware
"""""""""""""""""""""

Après extraction, vous devriez avoir :

.. code-block:: text

   Mk2_1phase_RFdatalog_temp/
   ├── Mk2_1phase_RFdatalog_temp.ino  (fichier principal)
   ├── config.h                     (configuration utilisateur)
   ├── config_system.h              (fréquence du réseau, seuils d’export)
   ├── config_rf.h                  (liaison radio, si elle est utilisée)
   ├── calibration.h                (paramètres d’étalonnage)
   ├── dualtariff.h
   ├── processing.cpp
   ├── utils_temp.h
   └── ... (autres fichiers)

.. important::
   Les réglages courants sont dans deux fichiers :

   - **config.h** — Configuration générale (carte-mère, afficheur, sorties, relais, sondes…)
   - **calibration.h** — Paramètres d’étalonnage (à remplir après l’étalonnage)

   `config_system.h` (fréquence du réseau, export requis, période d’envoi des données, 30 s au plus) et `config_rf.h` (liaison radio) ne changent que dans des cas particuliers. Le :ref:`configurateur <configurateur-monophase>` écrit les trois fichiers `config.h`, `config_system.h` et `config_rf.h`.


Étape 2 : Configuration du Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::
   Le :ref:`configurateur <configurateur-monophase>` écrit ``config.h`` (et, avec le module mk2Wifi, le YAML ESPHome) à partir d’une description de votre installation, en vérifiant vos choix. Il suffit ensuite de remplacer les fichiers et de garder votre ``calibration.h``.

Ouverture du Projet
"""""""""""""""""""

#. Lancer Arduino IDE
#. Menu : **Fichier → Ouvrir**
#. Naviguer vers le dossier du firmware
#. Ouvrir le fichier `Mk2_1phase_RFdatalog_temp.ino`
#. Arduino IDE ouvre plusieurs onglets (c’est normal)

.. note::
   Les autres fichiers (`.cpp`, `.h`) s’affichent automatiquement dans des onglets séparés.

Configuration dans `config.h`
"""""""""""""""""""""""""""""

Cliquer sur l’onglet **`config.h`** pour le modifier. Il décrit l’installation avec des réglages, dont voici les principaux ; le détail de chacun est dans le `Readme du firmware <https://github.com/FredM67/PVRouter-1-phase/blob/dev/Mk2_1phase_RFdatalog_temp/Readme.md>`_.

Carte-mère
##########

Selon votre carte-mère :

.. code-block:: cpp

   // Carte Mk2 de Robin Emley, afficheur 7 segments
   inline constexpr PcbVersion PCB_VERSION{ PcbVersion::OLD_SEG };

   // Seconde ancienne carte monophasée, afficheur OLED
   inline constexpr PcbVersion PCB_VERSION{ PcbVersion::OLD_OLED };

   // Carte universelle (rév. 6.0 et suivantes)
   inline constexpr PcbVersion PCB_VERSION{ PcbVersion::NEW };

.. warning::
   Chaque carte a ses entrées analogiques, et la carte universelle utilise la référence interne 1,1 V de l’ATmega328P : un mauvais choix donne des mesures fausses. Après un changement, refaire l’étalonnage.

Le `config.h` fourni avec le firmware est réglé pour la carte universelle (`PcbVersion::NEW`).

Format de Sortie Série
######################

Le `config.h` fourni est en mode `IoT`, pour le module mk2Wifi. Pour les premiers tests au moniteur série, passer en mode lisible par un humain :

.. code-block:: cpp

   inline constexpr SerialOutputType SERIAL_OUTPUT_TYPE = SerialOutputType::HumanReadable;

Options disponibles :

- `HumanReadable` : Affichage facile à lire (recommandé pour débuter)
- `IoT` : Format compact pour le module mk2Wifi et Home Assistant (9600 bauds, 7E1)
- `JSON` : Format JSON pour intégration domotique

.. important::
   Avec le module mk2Wifi, **repassez en mode** `IoT` après les premiers tests, puis recompilez et téléversez : le module ne comprend que ce mode.

Sonde 2 (CT2) et Afficheur
##########################

La sonde CT2 mesure l’énergie routée : faire passer par elle les fils de toutes les sorties locales (triacs et relais). Si aucune sonde n’est montée :

.. code-block:: cpp

   inline constexpr bool DIVERTED_CT_PRESENT{ false };

L’afficheur se règle avec `TYPE_OF_DISPLAY` :

- `NONE` : Pas d’affichage
- `SEG` : Afficheur 7 segments (carte `OLD_SEG`)
- `SEG_HW` : Afficheur 7 segments avec ses circuits d’économie de broches
- `OLED` : Afficheur OLED (cartes `OLD_OLED` et `NEW`)

Configuration des Sorties Triac
###############################

Définir le nombre de sorties et la broche de chacune :

.. code-block:: cpp

   // Exemple : 2 sorties triac
   inline constexpr uint8_t NO_OF_DUMPLOADS{ 2 };

   inline constexpr uint8_t physicalLoadPin[NO_OF_DUMPLOADS]{
     Load::local(5),  // Sortie 1 sur la broche D5
     Load::local(6)   // Sortie 2 sur la broche D6
   };

.. note::
   Le `config.h` fourni a une seule sortie, un triac sur D5. Pour en ajouter, changer ensemble `NO_OF_DUMPLOADS`, `physicalLoadPin` et `loadPrioritiesAtStartup`. Une charge pilotée par radio par une unité distante s’écrit `Load::remote(1)` (unité 1, de 1 à 3) au lieu de `Load::local(…)`.

Ordre de Démarrage
##################

Définir la priorité des charges :

.. code-block:: cpp

   inline constexpr uint8_t loadPrioritiesAtStartup[NO_OF_DUMPLOADS]{ 0, 1 };

Signification : les priorités désignent les sorties par leur rang dans `physicalLoadPin`, à partir de 0 : `{ 0, 1 }` démarre d’abord la sortie 1 (D5), puis la sortie 2 (D6).

Relais, Sondes de Température, Double Tarif, Radio (Optionnel)
##############################################################

Ces fonctions s’activent chacune par un réglage de `config.h`, puis se détaillent dans ``config.h``, dans la section de chaque fonction :

- **Relais** (`RELAY_DIVERSION`, `relays`) : relais tout-ou-rien pilotés par le surplus.
- **Sondes de température** (`TEMP_SENSOR_PRESENT`, `temperatureSensing`) : sondes DS18B20, dont il faut indiquer les adresses (le mode étalonnage les liste au démarrage). Collez une étiquette avec l’adresse sur le câble de chaque sonde.
- **Double tarif** (`DUAL_TARIFF`, `dualTariffPin`, `scheduledBoosts`, `iTemperatureThreshold`) : heures creuses et boosts programmés, avec un seuil de température.
- **Radio** (`RF_LOGGING_PRESENT`, `config_rf.h`) : journalisation et charges distantes par module RFM69.

Configuration dans `calibration.h`
""""""""""""""""""""""""""""""""""

Ce fichier contient les paramètres d’étalonnage, avec un jeu de valeurs par carte-mère : le routeur utilise celui de `PCB_VERSION`.

.. code-block:: cpp

   // Anciennes cartes
   inline constexpr float f_powerCalOldBoard{ 0.05000F };
   inline constexpr float f_powerCalDivertedOldBoard{ 0.05000F };
   inline constexpr float f_voltageCalOldBoard{ 0.805653F };
   // Carte universelle
   inline constexpr float f_ctRating{ 50.0F };
   inline constexpr float f_ctRatingDiverted{ 50.0F };
   inline constexpr float f_powerCalPerAmp{ 0.00286405F };
   inline constexpr float f_voltageCalNewBoard{ 0.888065256F };

**Carte universelle** : `f_ctRating` et `f_ctRatingDiverted` sont les calibres (courant nominal) des sondes CT1 et CT2, en ampères. Si vos sondes ne sont pas des 50 A / 333 mV, indiquez dès maintenant leur calibre : avec une sonde à sortie courant et une résistance de charge R (par exemple YHDC SCT-013-000), le calibre vaut 666 / R, soit 30,3 avec 22 Ω.

.. warning::
   Ne modifiez **PAS** les autres valeurs maintenant — elles seront déterminées lors de l’étalonnage
   (voir chapitre :ref:`etalonnage-monophase`).

Les paramètres par défaut permettent de tester le routeur.


Étape 3 : Connexion et Programmation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Préparation
"""""""""""

.. note::

   L’adaptateur FTDI ne peut **PAS** alimenter le routeur seul !

   Le routeur doit être alimenté par sa propre alimentation 230 V.

.. include:: ../common/connexion-ftdi.inc.rst


.. include:: ../common/configuration-arduino-ide.inc.rst

.. include:: ../common/compilation-televerement.inc.rst

.. include:: ../common/resolution-problemes-upload.inc.rst

.. include:: ../common/moniteur-serie.inc.rst
