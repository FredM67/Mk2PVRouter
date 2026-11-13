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

Le `config.h` fourni avec le firmware est réglé pour la carte universelle (`PcbVersion::NEW`) : avec l’ancienne carte, mettre `PcbVersion::OLD`.

Format de Sortie Série
######################

Le `config.h` fourni est en mode `IoT`, pour le module mk2Wifi. Pour les premiers tests au moniteur série, passer en mode lisible par un humain :

.. code-block:: cpp

   inline constexpr SerialOutputType SERIAL_OUTPUT_TYPE = SerialOutputType::HumanReadable;

Options disponibles :

- `HumanReadable` : Affichage facile à lire (recommandé pour débuter)
- `IoT` : Format compact pour le module mk2Wifi et Home Assistant (9600 bauds, 7E1)
- `JSON` : Format JSON pour intégration domotique

.. note::
   Dans tous les modes, le routeur affiche sa configuration au démarrage, pour vérifier avec quels réglages il tourne. En mode `IoT`, il le fait à 9600 bauds 8N1 (le réglage par défaut du moniteur série), puis passe en 7E1 : les caractères illisibles qui suivent dans le moniteur série sont normaux. En mode `JSON`, ces lignes précèdent la première ligne JSON. Les messages d’état en cours de fonctionnement (relais, rotation des priorités, heures creuses…) ne s’affichent qu’en mode `HumanReadable`.


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

Ce fichier contient les paramètres d’étalonnage, avec un jeu de valeurs par carte-mère : le routeur utilise celui de `PCB_VERSION`.

.. code-block:: cpp

   // Ancienne carte
   inline constexpr float f_powerCalOldBoard[NO_OF_PHASES]{ 0.05000F, 0.05000F, 0.05000F };
   inline constexpr float f_voltageCalOldBoard[NO_OF_PHASES]{ 0.8151F, 0.8184F, 0.8195F };
   // Carte universelle
   inline constexpr float f_ctRating[NO_OF_PHASES]{ 50.0F, 50.0F, 50.0F };
   inline constexpr float f_powerCalPerAmp[NO_OF_PHASES]{ 0.00286405F, 0.00286405F, 0.00286405F };
   inline constexpr float f_voltageCalNewBoard[NO_OF_PHASES]{ 0.888065256F, 0.888065256F, 0.888065256F };

**Carte universelle** : `f_ctRating` est le calibre (courant nominal) de la sonde de chaque phase, en ampères. Si vos sondes ne sont pas des 50 A / 333 mV, indiquez dès maintenant leur calibre : avec une sonde à sortie courant et une résistance de charge R (par exemple YHDC SCT-013-000), le calibre vaut 666 / R, soit 30,3 avec 22 Ω. Avec les valeurs par défaut, le routeur est en général précis à quelques pour cent sans étalonnage.

**Ancienne carte** : si votre routeur était déjà étalonné avec une version précédente du firmware, recopiez vos anciennes valeurs de `f_powerCal` et `f_voltageCal` dans `f_powerCalOldBoard` et `f_voltageCalOldBoard`.

.. warning::
   Ne modifiez **PAS** les autres valeurs maintenant — elles seront déterminées lors de l’étalonnage
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

