Étape 5 : Téléchargement du Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Ouvrir le navigateur : https://github.com/FredM67/PVRouter-1-phase
#. Cliquer sur le bouton vert **« Code »** → **« Download ZIP »**
#. Enregistrer le fichier `PVRouter-1-phase-main.zip`
#. Extraire le contenu dans un dossier de votre choix (exemple : `Documents/Arduino/`)
#. Le firmware se trouve dans : `PVRouter-1-phase-main/Mk2_fasterControl_Full/`

Structure du Firmware
~~~~~~~~~~~~~~~~~~~~~

Après extraction, vous devriez avoir :

.. code-block:: text

   Mk2_fasterControl_Full/
   ├── Mk2_fasterControl_Full.ino  (fichier principal)
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


Étape 6 : Configuration du Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ouverture du Projet
~~~~~~~~~~~~~~~~~~~

#. Lancer Arduino IDE
#. Menu : **Fichier → Ouvrir**
#. Naviguer vers le dossier du firmware
#. Ouvrir le fichier `.ino` :

   - Mono : `Mk2_fasterControl_Full.ino`
   - Tri : `Mk2_3phase_RFdatalog_temp.ino`

#. Arduino IDE ouvre plusieurs onglets (c’est normal)

.. note::
   Les autres fichiers (`.cpp`, `.h`) s’affichent automatiquement dans des onglets séparés.

Configuration dans `config.h`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cliquer sur l’onglet **`config.h`** pour le modifier.

Version du PCB
^^^^^^^^^^^^^^

Selon la version de votre PCB :

.. code-block:: cpp

   // Ancienne version de PCB (avant 2023)
   inline constexpr bool OLD_PCB{ true };

   // Nouvelle version de PCB (2023+)
   inline constexpr bool OLD_PCB{ false };

.. tip::
   Si vous avez reçu votre kit après 2023, mettez `false`.

Format de Sortie Série
^^^^^^^^^^^^^^^^^^^^^^

Pour débuter, laisser le mode lisible par un humain :

.. code-block:: cpp

   inline constexpr SerialOutputType SERIAL_OUTPUT_TYPE = SerialOutputType::HumanReadable;

Options disponibles :

- `HumanReadable` : Affichage facile à lire (recommandé pour débuter)
- `IoT` : Format compact pour IoT
- `JSON` : Format JSON pour intégration domotique

Type d’Affichage
^^^^^^^^^^^^^^^^

Si vous n’avez pas d’afficheur :

.. code-block:: cpp

   inline constexpr DisplayType TYPE_OF_DISPLAY{ DisplayType::NONE };

Options disponibles :

- `NONE` : Pas d’affichage
- `SEG` : Afficheur 7 segments (logiciel)
- `SEG_HW` : Afficheur 7 segments (matériel)

Configuration des Sorties Triac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Définir le nombre de sorties et leurs broches :

.. code-block:: cpp

   // Exemple : 2 sorties triac
   inline constexpr uint8_t NO_OF_DUMPLOADS{ 2 };

   inline constexpr IoPinMapping physicalPin_dump_load[NO_OF_DUMPLOADS]{
     { 5, DivertorConfig(NORMAL) },    // Sortie 1 sur broche D5
     { 4, DivertorConfig(NORMAL) },    // Sortie 2 sur broche D4
   };

Ordre de Démarrage
^^^^^^^^^^^^^^^^^^

Définir la priorité des charges :

.. code-block:: cpp

   inline constexpr uint8_t dumpLoad_startup_sequence[NO_OF_DUMPLOADS]{ 0, 1 };

Signification : Démarrer d’abord la sortie 0, puis la sortie 1.

Sondes de Température (Optionnel)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce fichier contient les paramètres d’étalonnage.

.. warning::
   Ne modifiez **PAS** ce fichier maintenant — les valeurs seront déterminées lors de l’étalonnage
   (voir chapitre :ref:`etalonnage-mono` ou :ref:`etalonnage-tri`).

Les paramètres par défaut permettent de tester le routeur.


Étape 7 : Connexion et Programmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Préparation
~~~~~~~~~~~

.. danger::
   **ORDRE IMPORTANT** :

   #. D’abord, alimenter le routeur avec sa propre alimentation 230 V
   #. Ensuite, connecter l’adaptateur FTDI

   L’adaptateur FTDI ne peut **PAS** alimenter le routeur seul !

Connexion du Routeur
~~~~~~~~~~~~~~~~~~~~

#. ⚠️ **Couper l’alimentation secteur** du routeur (disjoncteur)
#. Brancher l’adaptateur FTDI sur le routeur :

   +----------------+---------------------+------------------------+
   | Broche FTDI    | Broche PCB          | Couleur câble (FTDI)   |
   +================+=====================+========================+
   | GND            | 0 V (ou GND)        | Noir                   |
   +----------------+---------------------+------------------------+
   | TX (Transmit)  | RX (Receive)        | Vert ou Orange         |
   +----------------+---------------------+------------------------+
   | RX (Receive)   | TX (Transmit)       | Blanc ou Jaune         |
   +----------------+---------------------+------------------------+
   | VCC            | **NE PAS CONNECTER**| Rouge (laisser libre)  |
   +----------------+---------------------+------------------------+

.. danger::
   ⚠️ **NE PAS** connecter le fil VCC (rouge) de l’adaptateur FTDI au routeur !

   Cela peut endommager l’adaptateur FTDI ou le routeur.

#. Vérifier le cavalier ou switch de l’adaptateur FTDI :

   - Position **3.3 V** si routeur en 3.3 V
   - Position **5 V** si routeur en 5 V

#. Connecter l’adaptateur FTDI à l’ordinateur (port USB)

#. **Mettre le routeur sous tension** (réenclencher le disjoncteur)

Configuration Arduino IDE
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Menu : **Outils → Type de carte → Arduino AVR Boards → Arduino Uno**

#. Menu : **Outils → Port → COMx** (Windows) ou `/dev/tty.usbserial-xxx` (Mac/Linux)

   - Choisir le port correspondant à l’adaptateur FTDI
   - Si plusieurs ports : essayer chacun jusqu'à ce que ça fonctionne

#. Menu : **Outils → Programmateur → AVRISP mkII** (ou laisser par défaut)

Compilation et Téléversement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Checklist avant téléversement

   - [ ] Modifications sauvegardées dans `config.h`
   - [ ] Routeur alimenté (230 V)
   - [ ] Adaptateur FTDI connecté (USB + PCB)
   - [ ] Bon port COM sélectionné
   - [ ] Type de carte = Arduino Uno

#. Cliquer sur le bouton **« Vérifier »** (✓) pour compiler

   - Attendre la compilation (1-2 minutes la première fois)
   - Vérifier qu’il n’y a **aucune erreur**

#. Si la compilation réussit, cliquer sur **« Téléverser »** (→)

   - La LED **TX** sur l’adaptateur FTDI clignote
   - La LED **RX** sur le routeur clignote
   - Attendre le message **« Téléversement terminé »**

.. tip::
   Si la compilation échoue avec des erreurs sur `std::array` ou `constexpr`,
   c’est que le fichier `platform.txt` n’a pas été correctement modifié (voir Étape 3).

Résolution des Problèmes
~~~~~~~~~~~~~~~~~~~~~~~~

Erreur : `avrdude: stk500_recv(): programmer is not responding`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

#. Mauvais port COM sélectionné → Essayer un autre port
#. Routeur non alimenté → Vérifier l’alimentation 230 V
#. Câblage FTDI incorrect → Vérifier TX ↔ RX inversés
#. ATmega328 mal inséré → Vérifier l’orientation et l’insertion complète

Erreur : `error: 'constexpr' does not name a type`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le fichier `platform.txt` n’a pas été modifié correctement.

**Solution :** Reprendre l’Étape 3.

Port COM n’apparaît pas
^^^^^^^^^^^^^^^^^^^^^^^

#. Vérifier que les pilotes FTDI sont installés (Étape 2)
#. Débrancher/rebrancher l’adaptateur FTDI
#. Redémarrer l’ordinateur


Étape 8 : Vérification du Fonctionnement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ouverture du Moniteur Série
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Menu : **Outils → Moniteur série**
#. Configurer en bas à droite :

   - **Vitesse (baud rate)** : `9600`
   - **Fin de ligne** : `Retour chariot et Nouvelle ligne` (NL & CR)

Messages Attendus
~~~~~~~~~~~~~~~~~

Si tout fonctionne, vous devriez voir des messages s’afficher :

.. code-block:: text

   Mk2PVRouter v3.x
   Initialisation...
   CT1: 0 W
   CT2: 0 W  (si triphasé)
   CT3: 0 W  (si triphasé)
   Grid: 230 V
   Load 1: OFF
   Load 2: OFF

.. note::
   Les valeurs exactes dépendent de votre installation et de l’étalonnage.

Si Aucun Message n’Apparaît
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Vérifier que le bon baud rate est sélectionné (9600 bauds)
#. Vérifier le câblage FTDI (TX ↔ RX)
#. Vérifier que le routeur est alimenté
#. Vérifier l’oscillateur 16 MHz et les condensateurs C6/C7

Adresses des Sondes de Température
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si vous avez activé `TEMP_ENABLED`, le moniteur série affichera les adresses détectées :

.. code-block:: text

   Temperature sensor 0 address: 28 AA BB CC DD EE FF 01
   Temperature sensor 1 address: 28 AA BB CC DD EE FF 02

Copier ces adresses dans `config.h` (section sondes de température).


Étape 9 : Prochaines Étapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

✅ Le firmware est maintenant installé et fonctionnel !

**Prochaines étapes :**

#. **Étalonnage** : Voir chapitre :ref:`etalonnage-mono` ou :ref:`etalonnage-tri`

   L’étalonnage est **OBLIGATOIRE** pour que le routeur fonctionne correctement.

#. **Installation finale** : Connexion au réseau électrique (faire appel à un électricien qualifié)

#. **Configuration avancée** : Relais, sondes de température, double tarif, etc.

.. danger::
   Ne pas connecter le routeur au réseau électrique domestique avant d’avoir :

   - [ ] Vérifié toutes les soudures (pas de pont, pas de soudure froide)
   - [ ] Lu le chapitre de sécurité
   - [ ] Fait appel à un électricien qualifié (fortement recommandé)

.. important::
   **FONCTIONNALITÉ** : L'étalonnage doit être effectué après l'installation électrique pour que le routeur mesure correctement et fonctionne de manière optimale. Le routeur peut être connecté sans étalonnage (pas de danger), mais ne fonctionnera pas correctement.


Annexe : Alternative PlatformIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour les Utilisateurs Avancés
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**PlatformIO** est un environnement de développement plus complet que l’Arduino IDE.

Avantages
^^^^^^^^^

- Gestion automatique des bibliothèques
- Support C++17 natif (pas besoin de modifier `platform.txt`)
- Compilations plus rapides
- Meilleure intégration avec Git
- Débogage avancé

Installation
^^^^^^^^^^^^

#. Installer **Visual Studio Code** : https://code.visualstudio.com/
#. Ouvrir VS Code
#. Aller dans l’onglet **Extensions** (Ctrl+Shift+X)
#. Rechercher **« PlatformIO IDE »**
#. Cliquer sur **« Installer »**
#. Redémarrer VS Code

Ouverture du Projet
^^^^^^^^^^^^^^^^^^^

#. Menu PlatformIO : **PIO Home → Open Project**
#. Sélectionner le dossier du firmware
#. PlatformIO détecte automatiquement le fichier `platformio.ini`

Compilation et Téléversement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Cliquer sur l’icône **« Upload »** (→) dans la barre inférieure
#. PlatformIO télécharge automatiquement les bibliothèques nécessaires
#. La compilation et le téléversement se font automatiquement

Sélection de la Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le firmware contient plusieurs environnements préconfigurés :

- `env:release` : Version normale
- `env:temperature` : Version avec support sondes de température
- `env:debug` : Version avec messages de débogage supplémentaires

Pour changer d’environnement :

#. Cliquer sur le sélecteur d’environnement (barre inférieure)
#. Choisir la configuration désirée

.. tip::
   PlatformIO est recommandé pour les utilisateurs avancés qui développent ou modifient le firmware.
   Pour un usage standard, Arduino IDE suffit amplement.


Support et Aide
~~~~~~~~~~~~~~~

En Cas de Problème
~~~~~~~~~~~~~~~~~~

#. Relire attentivement les étapes ci-dessus
#. Consulter le chapitre :ref:`troubleshooting` (section programmation)
#. Vérifier le forum GitHub Discussions : https://github.com/FredM67/PVRouter-1-phase/discussions

Pour Rapporter un Bug
~~~~~~~~~~~~~~~~~~~~~

GitHub Issues :

- Monophasé : https://github.com/FredM67/PVRouter-1-phase/issues
- Triphasé : https://github.com/FredM67/PVRouter-1-phase/issues

**Informations à fournir :**

- Version Arduino IDE
- Système d’exploitation (Windows/Mac/Linux)
- Version du firmware
- Message d’erreur complet (copier/coller du Moniteur Série)
- Photos de la carte (si problème matériel)
