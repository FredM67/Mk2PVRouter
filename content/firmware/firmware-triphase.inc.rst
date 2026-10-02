Étape 1 : Téléchargement du Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ouvrir le navigateur : https://github.com/FredM67/PVRouter-3-phase
#. Cliquer sur le bouton vert **« Code »** → **« Download ZIP »**
#. Enregistrer le fichier `PVRouter-3-phase-main.zip`
#. Extraire le contenu dans un dossier de votre choix (exemple : `Documents/Arduino/`)
#. Le firmware se trouve dans : `PVRouter-3-phase-main/Mk2_3phase_RFdatalog_temp/`

Structure du Firmware
"""""""""""""""""""""

Après extraction, vous devriez avoir :

.. code-block:: text

   Mk2_3phase_RFdatalog_temp/
   ├── Mk2_3phase_RFdatalog_temp.ino  (fichier principal)
   ├── config.h                     (configuration utilisateur)
   ├── config_system.h              (fréquence du réseau, période d’envoi des données)
   ├── config_rf.h                  (liaison radio, si elle est utilisée)
   ├── calibration.h                (paramètres d’étalonnage)
   ├── dualtariff.h
   ├── processing.cpp
   ├── utils_temp.h
   └── ... (autres fichiers)

.. important::
   Seuls deux fichiers doivent être modifiés par l’utilisateur :

   - **config.h** — Configuration générale (pins, type d’affichage, sorties)
   - **calibration.h** — Paramètres d’étalonnage (à remplir après l’étalonnage)


Étape 2 : Configuration du Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::
   Le :ref:`configurateur <configurateur-triphase>` écrit ``config.h`` (et, avec le module mk2Wifi, le YAML ESPHome) à partir d’une description de votre installation, en vérifiant vos choix. Il suffit ensuite de remplacer les fichiers et de garder votre ``calibration.h``.

Ouverture du Projet
"""""""""""""""""""

#. Lancer Arduino IDE
#. Menu : **Fichier → Ouvrir**
#. Naviguer vers le dossier du firmware
#. Ouvrir le fichier `Mk2_3phase_RFdatalog_temp.ino`
#. Arduino IDE ouvre plusieurs onglets (c’est normal)

.. note::
   Les autres fichiers (`.cpp`, `.h`) s’affichent automatiquement dans des onglets séparés.

Configuration dans `config.h`
"""""""""""""""""""""""""""""

Cliquer sur l’onglet **`config.h`** pour le modifier.

Carte-mère
##########

Selon votre carte-mère :

.. code-block:: cpp

   // Ancienne carte triphasée
   inline constexpr PcbVersion PCB_VERSION{ PcbVersion::OLD };

   // Carte universelle 3phaseDiverter (rév. 6.0 et suivantes)
   inline constexpr PcbVersion PCB_VERSION{ PcbVersion::NEW };

.. warning::
   Les deux cartes ne mesurent pas de la même façon : la carte universelle utilise la référence interne 1,1 V de l’ATmega328P, que le firmware n’active qu’avec `PcbVersion::NEW`. Un mauvais choix donne des mesures fausses. Après un changement, refaire l’étalonnage.

Format de Sortie Série
######################

Pour débuter, laisser le mode lisible par un humain :

.. code-block:: cpp

   inline constexpr SerialOutputType SERIAL_OUTPUT_TYPE = SerialOutputType::HumanReadable;

Options disponibles :

- `HumanReadable` : Affichage facile à lire (recommandé pour débuter)
- `IoT` : Format compact pour IoT
- `JSON` : Format JSON pour intégration domotique


Configuration des Sorties Triac
###############################

Définir le nombre de sorties et la broche de chacune :

.. code-block:: cpp

   // Exemple : 2 sorties triac
   inline constexpr uint8_t NO_OF_DUMPLOADS{ 2 };

   inline constexpr uint8_t physicalLoadPin[NO_OF_DUMPLOADS]{
     Load::local(5),  // Sortie 1 sur la broche D5
     Load::local(6)   // Sortie 2 sur la broche D6
   };

.. note::
   Une charge pilotée par radio par une unité distante s’écrit `Load::remote(1)` (unité 1, de 1 à 3) au lieu de `Load::local(…)`.

Ordre de Démarrage
##################

Définir la priorité des charges :

.. code-block:: cpp

   inline constexpr uint8_t loadPrioritiesAtStartup[NO_OF_DUMPLOADS]{ 0, 1 };

Signification : Démarrer d’abord la sortie 0, puis la sortie 1.

Sondes de Température (Optionnel)
#################################

Si vous utilisez des sondes DS18B20, activer la mesure :

.. code-block:: cpp

   inline constexpr bool TEMP_SENSOR_PRESENT{ true };

Puis indiquer la broche du bus *OneWire* (D3 par défaut, qui a déjà sa résistance de *pull-up*) et les adresses des sondes :

.. code-block:: cpp

   inline constexpr TemperatureSensing temperatureSensing{ 3,
                                                           { { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x01 },     // Sonde 1
                                                             { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x02 } } };  // Sonde 2

.. note::
   Le firmware ne recherche pas les sondes : relevez leurs adresses avec un programme de scan *OneWire* (exemples de l’Arduino IDE ou sur Internet). Collez une étiquette avec l’adresse sur le câble de chaque sonde.

Configuration dans `calibration.h`
""""""""""""""""""""""""""""""""""

Ce fichier contient les paramètres d’étalonnage.

.. warning::
   Ne modifiez **PAS** ce fichier maintenant — les valeurs seront déterminées lors de l’étalonnage
   (voir chapitre :ref:`etalonnage-triphase`).

Les paramètres par défaut permettent de tester le routeur.


Étape 3 : Connexion et Programmation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Préparation
"""""""""""

.. note::

   L’adaptateur FTDI ne peut **PAS** alimenter le routeur seul !
   
   Le routeur doit être alimenté par sa propre alimentation triphasée.

.. include:: ../common/connexion-ftdi.inc.rst


.. include:: ../common/configuration-arduino-ide.inc.rst

.. include:: ../common/compilation-televerement.inc.rst

.. include:: ../common/resolution-problemes-upload.inc.rst

.. include:: ../common/moniteur-serie.inc.rst

