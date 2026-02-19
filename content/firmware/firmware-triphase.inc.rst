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
   ├── calibration.h                (paramètres d'étalonnage)
   ├── dualtarif.h
   ├── processing.cpp
   ├── temperature.cpp
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
#. Ouvrir le fichier `Mk2_3phase_RFdatalog_temp.ino`
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


Configuration des Sorties Triac
###############################

Définir le nombre de sorties et leurs broches :

.. code-block:: cpp

   // Exemple : 2 sorties triac
   inline constexpr uint8_t NO_OF_DUMPLOADS{ 2 };

   inline constexpr IoPinMapping physicalPin_dump_load[NO_OF_DUMPLOADS]{
     { 5, DivertorConfig(NORMAL) },    // Sortie 1 sur broche D5
     { 4, DivertorConfig(NORMAL) },    // Sortie 2 sur broche D4
   };

Ordre de Démarrage
##################

Définir la priorité des charges :

.. code-block:: cpp

   inline constexpr uint8_t dumpLoad_startup_sequence[NO_OF_DUMPLOADS]{ 0, 1 };

Signification : Démarrer d’abord la sortie 0, puis la sortie 1.

Sondes de Température (Optionnel)
#################################

Si vous utilisez des sondes DS18B20, décommenter la ligne :

.. code-block:: cpp

   #define TEMP_ENABLED

Et configurer les adresses des sondes :

.. code-block:: cpp

   inline constexpr DeviceAddress sensor_list[3]
   {
     { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x01 },  // Sonde 1
     { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x02 },  // Sonde 2
     { 0x28, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x03 },  // Sonde 3
   };

.. note::
   Les adresses des sondes seront trouvées lors du premier lancement (voir Moniteur Série).

Configuration dans `calibration.h`
""""""""""""""""""""""""""""""""""

Ce fichier contient les paramètres d’étalonnage.

.. warning::
   Ne modifiez **PAS** ce fichier maintenant — les valeurs seront déterminées lors de l’étalonnage
   (voir chapitre :ref:`etalonnage`).

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

Prochaines Étapes
^^^^^^^^^^^^^^^^^

✅ Le firmware est maintenant installé et fonctionnel !

**Prochaines étapes :**

#. **Étalonnage** : Voir chapitre :ref:`etalonnage`

   L’étalonnage est **OBLIGATOIRE** pour que le routeur fonctionne correctement.

#. **Installation finale** : Connexion au réseau électrique (faire appel à un électricien qualifié)

#. **Configuration avancée** : Relais, sondes de température, double tarif, etc.

.. danger::
   Ne pas connecter le routeur au réseau électrique domestique avant d’avoir :

   - [ ] Vérifié toutes les soudures (pas de pont, pas de soudure froide)
   - [ ] Lu le chapitre de sécurité
   - [ ] Fait appel à un électricien qualifié (fortement recommandé)

.. important::
   **FONCTIONNALITÉ** : L’étalonnage doit être effectué après l’installation électrique pour que le routeur mesure correctement et fonctionne de manière optimale. Le routeur peut être connecté sans étalonnage (pas de danger), mais ne fonctionnera pas correctement.

