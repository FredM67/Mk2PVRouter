.. _installation-logiciel:

==========================================
Installation du Logiciel et du Firmware
==========================================

Ce chapitre détaille l'installation complète de l'environnement de développement Arduino et la programmation du firmware du Mk2PVRouter.

⏱️ **Temps estimé :**
   - Débutant : 2-3 heures
   - Expérimenté : 1-2 heures

.. contents:: Sommaire de l’installation
   :local:
   :depth: 2

===================================
Étape 1 : Installation Arduino IDE
===================================

L’Arduino IDE est le logiciel qui permet de programmer le routeur.

Windows
~~~~~~~

Téléchargement
^^^^^^^^^^^^^^

#. Ouvrir le navigateur web : https://www.arduino.cc/en/software
#. Cliquer sur **« Windows Win 10 and newer »** (fichier `.exe` ou `.zip`)
#. ⚠️ **NE PAS** télécharger la version **« Windows app »** (incompatibilités connues)
#. Attendre la fin du téléchargement (~200 MB)

Installation
^^^^^^^^^^^^

#. Double-cliquer sur le fichier téléchargé (`arduino-ide-xxxx.exe`)
#. Accepter la licence
#. **IMPORTANT :** Cocher **« Install USB drivers »** et tous les composants
#. Choisir le répertoire d’installation (laisser par défaut : `C:\\Program Files\\Arduino`)
#. Cliquer sur **« Install »**
#. Attendre la fin de l’installation (5-10 minutes)
#. Laisser l’installateur créer les raccourcis sur le bureau

.. note::
   Si Windows affiche un avertissement de sécurité, cliquer sur **« Exécuter quand même »**.
   Le logiciel Arduino est sûr et largement utilisé.

macOS
~~~~~

Téléchargement
^^^^^^^^^^^^^^

#. Ouvrir le navigateur web : https://www.arduino.cc/en/software
#. Cliquer sur **« macOS »** (fichier `.dmg`)
#. Attendre la fin du téléchargement

Installation
^^^^^^^^^^^^

#. Ouvrir le fichier `.dmg` téléchargé
#. Glisser l’icône Arduino dans le dossier **Applications**
#. Attendre la copie des fichiers
#. Éjecter l’image disque

.. note::
   Au premier lancement, macOS peut demander l’autorisation d’ouvrir l’application.
   Cliquer sur **« Ouvrir »** dans la fenêtre de sécurité.

Linux (Ubuntu/Debian)
~~~~~~~~~~~~~~~~~~~~~

Méthode recommandée : AppImage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ouvrir le navigateur web : https://www.arduino.cc/en/software
#. Télécharger la version **« Linux AppImage »**
#. Ouvrir un terminal
#. Rendre le fichier exécutable :

   .. code-block:: bash

      cd ~/Téléchargements
      chmod +x arduino-ide-*-linux-x64.AppImage
      ./arduino-ide-*-linux-x64.AppImage

Alternative : Installation via le gestionnaire de paquets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo apt update
   sudo apt install arduino

.. warning::
   La version des dépôts peut être ancienne. Privilégier l’AppImage pour avoir la dernière version.

===================================
Étape 2 : Installation Pilotes FTDI
===================================

Les pilotes FTDI sont **OBLIGATOIRES** pour communiquer avec le routeur via le programmateur USB.

.. danger::
   Sans ces pilotes, l’ordinateur ne détectera pas le routeur !

Windows
~~~~~~~

#. Ouvrir le navigateur : https://ftdichip.com/drivers/vcp-drivers/
#. Cliquer sur **« Windows »** dans la colonne **« Available Drivers »**
#. Télécharger la dernière version (fichier `.exe`)
#. Exécuter le fichier téléchargé en tant qu’administrateur (clic droit → **« Exécuter en tant qu’administrateur »**)
#. Suivre l’assistant d’installation
#. **Redémarrer l’ordinateur** après l’installation

Vérification
^^^^^^^^^^^^

#. Connecter l’adaptateur FTDI à un port USB
#. Ouvrir le **Gestionnaire de périphériques** (Win + X → Gestionnaire de périphériques)
#. Développer **« Ports (COM et LPT) »**
#. Vérifier la présence de **« USB Serial Port (COMx) »** où x est un numéro
#. **Noter le numéro COMx** (exemple : COM3, COM4)

macOS
~~~~~

Les pilotes FTDI sont généralement inclus dans macOS moderne.

Vérification
^^^^^^^^^^^^

#. Connecter l’adaptateur FTDI à un port USB
#. Ouvrir un terminal
#. Taper la commande :

   .. code-block:: bash

      ls /dev/tty.*

#. Rechercher une ligne contenant `tty.usbserial` (exemple : `/dev/tty.usbserial-A50285BI`)

Si aucun périphérique n’apparaît
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Télécharger les pilotes sur https://ftdichip.com/drivers/vcp-drivers/
#. Choisir la version macOS
#. Installer le fichier `.dmg`
#. Redémarrer le Mac

Linux
~~~~~

Les pilotes FTDI sont généralement inclus dans le noyau Linux.

Vérification
^^^^^^^^^^^^

.. code-block:: bash

   lsusb

Rechercher une ligne contenant « FTDI » ou « Future Technology Devices ».

Si le pilote n’est pas chargé
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo modprobe ftdi_sio

Ajouter l’utilisateur au groupe dialout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   sudo reboot

.. note::
   Le redémarrage est nécessaire pour que les changements prennent effet.

================================================
Étape 3 : Configuration Arduino IDE pour C++17
================================================

.. danger::
   **ÉTAPE CRITIQUE** — Le firmware nécessite le support C++17.

   Sans cette modification, la compilation échouera avec des erreurs incompréhensibles !

Le firmware du Mk2PVRouter utilise des fonctionnalités modernes du C++ (C++17) qui ne sont pas activées par défaut dans Arduino IDE.

Localisation du fichier `platform.txt`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier à modifier se trouve à différents emplacements selon le système d’exploitation :

Windows
^^^^^^^

Deux emplacements possibles :

#. `C:\\Program Files (x86)\\Arduino\\hardware\\arduino\\avr\\platform.txt`
#. `%LOCALAPPDATA%\\Arduino15\\packages\\arduino\\hardware\\avr\\x.y.z\\platform.txt`

   (remplacer `x.y.z` par la version installée, exemple : `1.8.6`)

macOS
^^^^^

`/Users/[nom_utilisateur]/Library/Arduino15/packages/arduino/hardware/avr/1.8.6/platform.txt`

.. note::
   Le dossier `Library` peut être caché. Pour y accéder :

   #. Dans le Finder, menu **« Aller »** → maintenir **Option** → cliquer sur **« Bibliothèque »**

   Ou taper dans le terminal :

   .. code-block:: bash

      open ~/Library/Arduino15/packages/arduino/hardware/avr/

Linux
^^^^^

`~/.arduino15/packages/arduino/hardware/avr/1.8.6/platform.txt`

Modification du fichier
~~~~~~~~~~~~~~~~~~~~~~~

#. Faire une **copie de sauvegarde** du fichier `platform.txt` (exemple : `platform.txt.bak`)

   .. code-block:: bash

      # Linux/macOS
      cp platform.txt platform.txt.bak

#. Ouvrir le fichier `platform.txt` avec un éditeur de texte (Notepad++, nano, gedit, etc.)

#. Rechercher la ligne contenant :

   .. code-block:: text

      "-std=gnu++11"

#. Remplacer par :

   .. code-block:: text

      "-std=gnu++17"

#. **Sauvegarder** le fichier

#. **Redémarrer Arduino IDE** pour que le changement soit pris en compte

.. tip::
   Si vous ne trouvez pas le fichier, ouvrez Arduino IDE, allez dans **Fichier → Préférences**,
   et regardez l’emplacement du **« Dossier de Sketchbook »**. Le fichier `platform.txt` est
   généralement dans un sous-dossier relatif à cet emplacement.

Vérification
~~~~~~~~~~~~

La modification sera validée lors de la compilation du firmware (étape 7).

========================================
Étape 4 : Installation des Bibliothèques
========================================

Le firmware nécessite plusieurs bibliothèques externes.

Ouvrir le Gestionnaire de bibliothèques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Lancer Arduino IDE
#. Menu : **Outils → Gérer les bibliothèques...**
#. Une fenêtre « Gestionnaire de bibliothèques » s’ouvre

Installation de ArduinoJson
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Dans le champ de recherche, taper : `ArduinoJson`
#. Trouver la bibliothèque **« ArduinoJson »** par Benoit Blanchon
#. ⚠️ **IMPORTANT** : Installer la version **6.x** (PAS la version 7 !)

   - Version 6.21.5 recommandée
   - La version 7 est **incompatible** avec l’ATmega328P

#. Cliquer sur **« Installer »**

.. danger::
   Ne pas installer ArduinoJson version 7.x — elle ne fonctionnera pas sur l’ATmega328P !

Installation de OneWire
~~~~~~~~~~~~~~~~~~~~~~~

Cette bibliothèque gère les sondes de température (optionnelles).

#. Dans le champ de recherche, taper : `OneWire`
#. Trouver **« OneWire »** par Paul Stoffregen
#. ⚠️ Installer la version **2.3.7 ou supérieure**
#. Cliquer sur **« Installer »**

Vérification
~~~~~~~~~~~~

#. Menu : **Croquis → Inclure une bibliothèque**
#. Vérifier la présence de : **ArduinoJson**, **OneWire**

.. tip::
   Si les bibliothèques n’apparaissent pas, redémarrer Arduino IDE.

