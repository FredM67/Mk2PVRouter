Installation de U8g2
^^^^^^^^^^^^^^^^^^^^

.. note::
   Cette bibliothèque est **uniquement nécessaire pour les PCB monophasés** équipés d’un affichage.
   Les versions triphasées n’utilisent pas cette bibliothèque.

Cette bibliothèque gère l’affichage sur écran.

#. Dans le Gestionnaire de bibliothèques d’Arduino IDE
#. Dans le champ de recherche, taper : `U8g2`
#. Trouver **« U8g2 »** par oliver
#. Cliquer sur **« Installer »**


Étape 1 : Téléchargement du Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ouvrir le navigateur : https://github.com/FredM67/PVRouter-1-phase
#. Cliquer sur le bouton vert **« Code »** → **« Download ZIP »**
#. Enregistrer le fichier `PVRouter-1-phase-main.zip`
#. Extraire le contenu dans un dossier de votre choix (exemple : `Documents/Arduino/`)
#. Le firmware se trouve dans : `PVRouter-1-phase-main/Mk2_fasterControl_Full/`

Structure du Firmware
"""""""""""""""""""""

Après extraction, vous devriez avoir :

.. code-block:: text

   Mk2_fasterControl_Full/
   ├── Mk2_fasterControl_Full.ino  (fichier principal)
   ├── config.h                     (configuration utilisateur)
   ├── config_system.h              (fréquence du réseau, seuils d’export)
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

Ouverture du Projet
"""""""""""""""""""

#. Lancer Arduino IDE
#. Menu : **Fichier → Ouvrir**
#. Naviguer vers le dossier du firmware
#. Ouvrir le fichier `Mk2_fasterControl_Full.ino`
#. Arduino IDE ouvre plusieurs onglets (c’est normal)

.. note::
   Les autres fichiers (`.cpp`, `.h`) s’affichent automatiquement dans des onglets séparés.

Configuration dans `config.h`
"""""""""""""""""""""""""""""

Cliquer sur l’onglet **`config.h`** pour le modifier.

Version du PCB
##############

Selon la version de votre PCB :

.. code-block:: cpp

   // Ancienne version de PCB (avant 2023)
   inline constexpr bool OLD_PCB{ true };

   // Nouvelle version de PCB (2023+)
   inline constexpr bool OLD_PCB{ false };

.. tip::
   Si vous avez reçu votre kit après 2 023, mettez `false`.

Format de Sortie Série
######################

Pour débuter, laisser le mode lisible par un humain :

.. code-block:: cpp

   inline constexpr SerialOutputType SERIAL_OUTPUT_TYPE = SerialOutputType::HumanReadable;

Options disponibles :

- `HumanReadable` : Affichage facile à lire (recommandé pour débuter)
- `IoT` : Format compact pour IoT
- `JSON` : Format JSON pour intégration domotique

Type d’Affichage
################

Si vous n’avez pas d’afficheur :

.. code-block:: cpp

   inline constexpr DisplayType TYPE_OF_DISPLAY{ DisplayType::NONE };

Options disponibles :

- `NONE` : Pas d’affichage
- `SEG` : Afficheur 7 segments (logiciel)
- `SEG_HW` : Afficheur 7 segments (matériel)

Configuration des Sorties Triac
###############################

Définir le nombre de sorties et la broche de chacune :

.. code-block:: cpp

   // Exemple : 2 sorties triac
   inline constexpr uint8_t NO_OF_DUMPLOADS{ 2 };

   inline constexpr uint8_t physicalLoadPin[NO_OF_DUMPLOADS]{ 4, 3 };  // Sortie 1 sur D4, sortie 2 sur D3

.. note::
   Par défaut, D3 est la broche de marche forcée (`forcePin`) : pour l’utiliser comme sortie, mettre `forcePin` sur une autre broche libre, ou bien `forcePin` à `0xff` et `OVERRIDE_PIN_PRESENT` à `false`. Avec l’afficheur 7 segments, peu de broches restent libres (voir les commentaires de `config.h`).

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

Puis indiquer la broche du bus *OneWire* (une broche libre, avec une résistance de *pull-up*) et les adresses des sondes :

.. code-block:: cpp

   inline constexpr TemperatureSensing temperatureSensing{ 2,
                                                           { { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x01 },     // Sonde 1
                                                             { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x02 } } };  // Sonde 2

.. note::
   Le firmware ne recherche pas les sondes : relevez leurs adresses avec un programme de scan *OneWire* (exemples de l’Arduino IDE ou sur Internet). Collez une étiquette avec l’adresse sur le câble de chaque sonde.

Configuration dans `calibration.h`
""""""""""""""""""""""""""""""""""

Ce fichier contient les paramètres d’étalonnage.

.. warning::
   Ne modifiez **PAS** ce fichier maintenant — les valeurs seront déterminées lors de l’étalonnage
   (voir chapitre :ref:`etalonnage-monophase`).

Les paramètres par défaut permettent de tester le routeur.


Étape 3 : Connexion et Programmation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Préparation
"""""""""""

.. note::

   L’adaptateur FTDI ne peut **PAS** alimenter le routeur seul !
   
   Le routeur doit être alimenté par sa propre alimentation 230 V.

.. include:: ../common/connexion-ftdi.inc.rst


.. include:: ../common/configuration-arduino-ide.inc.rst

.. include:: ../common/compilation-televerement.inc.rst

.. include:: ../common/resolution-problemes-upload.inc.rst

.. include:: ../common/moniteur-serie.inc.rst
