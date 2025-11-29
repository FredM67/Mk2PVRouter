.. _installation-logiciel:


Installation du Logiciel
========================

Ce chapitre détaille l’installation complète de l’environnement de développement Arduino et la programmation du firmware du Mk2PVRouter.

⏱️ **Temps estimé :**
   - Débutant : 2-3 heures
   - Expérimenté : 1-2 heures

.. contents:: Sommaire de l’installation
   :local:
   :depth: 2

.. _install-etape1-ftdi:


Étape 1 : Installation Pilotes FTDI
===================================

Les pilotes FTDI sont **OBLIGATOIRES** pour communiquer avec le routeur via le programmateur USB.

.. danger::
   Sans ces pilotes, l'ordinateur ne détectera pas le routeur !

.. _ftdi-windows:

Windows
-------

#. Ouvrir le navigateur : https://ftdichip.com/drivers/vcp-drivers/
#. Cliquer sur **« Windows »** dans la colonne **« Available Drivers »**
#. Télécharger la dernière version (fichier `.exe`)
#. Exécuter le fichier téléchargé en tant qu’administrateur (clic droit → **« Exécuter en tant qu’administrateur »**)
#. Suivre l’assistant d’installation
#. **Redémarrer l'ordinateur** après l'installation

.. _ftdi-windows-verif:

Vérification
~~~~~~~~~~~~

#. Connecter l'adaptateur FTDI à un port USB
#. Ouvrir le **Gestionnaire de périphériques** (Win + X → Gestionnaire de périphériques)
#. Développer **« Ports (COM et LPT) »**
#. Vérifier la présence de **« USB Serial Port (COMx) »** où x est un numéro
#. **Noter le numéro COMx** (exemple : COM3, COM4)

.. _ftdi-macos:

macOS
-----

Les pilotes FTDI sont généralement inclus dans macOS moderne.

.. _ftdi-macos-verif:

Vérification
~~~~~~~~~~~~

#. Connecter l’adaptateur FTDI à un port USB
#. Ouvrir un terminal
#. Taper la commande :

   .. code-block:: bash

      ls /dev/tty.*

#. Rechercher une ligne contenant `tty.usbserial` (exemple : `/dev/tty.usbserial-A50285BI`)

Si aucun périphérique n’apparaît
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Télécharger les pilotes sur https://ftdichip.com/drivers/vcp-drivers/
#. Choisir la version macOS
#. Installer le fichier `.dmg`
#. Redémarrer le Mac

.. _ftdi-linux:

Linux
-----

Les pilotes FTDI sont généralement inclus dans le noyau Linux.

.. _ftdi-linux-verif:

Vérification
~~~~~~~~~~~~

.. code-block:: bash

   lsusb

Rechercher une ligne contenant « FTDI » ou « Future Technology Devices ».

Si le pilote n’est pas chargé
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo modprobe ftdi_sio

Ajouter l’utilisateur au groupe dialout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   sudo reboot

.. note::
   Le redémarrage est nécessaire pour que les changements prennent effet.


Étape 2 : Choix de l’Environnement de Développement
===================================================

Vous avez deux options pour programmer le Mk2PVRouter :

**Option A : Arduino IDE** (recommandé pour les débutants)
   - Configuration manuelle nécessaire (C++17, bibliothèques)
   - Suivre les sous-sections de l'**Option A** ci-dessous

**Option B : PlatformIO** (recommandé pour les utilisateurs avancés)
   - Support C++17 natif (pas de configuration manuelle)
   - Suivre les sous-sections de l'**Option B**' ci-dessous

.. important::
   **Choisissez UNE SEULE option** : soit Arduino IDE, soit PlatformIO.



.. _install-arduino:

.. include:: common/installation-arduino-ide.inc.rst



.. _install-platformio:


.. include:: common/installation-platformio.inc.rst
