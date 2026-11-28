.. _installation-logiciel:


Installation des Logiciels
==========================

Ce chapitre détaille l’installation de l’environnement de développement nécessaire pour programmer le Mk2PVRouter. Pour le téléchargement et la configuration du firmware, voir :ref:`logiciel-monophase` (monophasé) ou :ref:`logiciel-triphase` (triphasé).

Chaque firmware a aussi son site (en anglais), avec la documentation du code : `PVRouter-1-phase <https://fredm67.github.io/PVRouter-1-phase/>`_ (monophasé) et `PVRouter-3-phase <https://fredm67.github.io/PVRouter-3-phase/>`_ (triphasé).

⏱️ **Temps estimé :**

- Débutant : 2–3 heures
- Expérimenté : 1–2 heures

.. contents:: Sommaire de l’installation
   :local:
   :depth: 2

.. _install-etape1-ftdi:


Installation Pilotes FTDI
-------------------------

L’ordinateur a besoin du pilote de la puce de l’adaptateur USB-série. Cette section décrit le pilote des adaptateurs à puce FTDI ; un adaptateur à puce CH340 ou CP2102 demande le pilote de son propre fabricant.

.. important::
   Sans pilote, l’ordinateur ne voit pas l’adaptateur, donc pas le routeur !

.. _ftdi-windows:

🪟 Windows
~~~~~~~~~~

#. Ouvrir le navigateur : https://ftdichip.com/drivers/vcp-drivers/
#. Cliquer sur **« Windows »** dans la colonne **« Available Drivers »**
#. Télécharger la dernière version (fichier `.exe`)
#. Exécuter le fichier téléchargé en tant qu’administrateur (clic droit → **« Exécuter en tant qu’administrateur »**)
#. Suivre l’assistant d’installation
#. **Redémarrer l’ordinateur** après l’installation

.. _ftdi-windows-verif:

Vérification
^^^^^^^^^^^^

#. Connecter l’adaptateur FTDI à un port USB
#. Ouvrir le **Gestionnaire de périphériques** (Win + X → Gestionnaire de périphériques)
#. Développer **« Ports (COM et LPT) »**
#. Vérifier la présence de **« USB Serial Port (COMx) »** où x est un numéro
#. **Noter le numéro COMx** (exemple : COM3, COM4)

.. _ftdi-macos:

🍎 macOS
~~~~~~~~

Les pilotes FTDI sont généralement inclus dans macOS moderne.

.. _ftdi-macos-verif:

Vérification
^^^^^^^^^^^^

#. Connecter l’adaptateur FTDI à un port USB
#. Ouvrir un terminal
#. Taper la commande :

   .. code-block:: bash

      ls /dev/tty.*

#. Rechercher une ligne contenant `tty.usbserial` (exemple : `/dev/tty.usbserial-A50285BI`)

Si aucun périphérique n’apparaît
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Télécharger les pilotes sur https://ftdichip.com/drivers/vcp-drivers/
#. Choisir la version macOS
#. Installer le fichier `.dmg`
#. Redémarrer le Mac

.. _ftdi-linux:

🐧 Linux
~~~~~~~~

Les pilotes FTDI sont généralement inclus dans le noyau Linux.

.. _ftdi-linux-verif:

Vérification
^^^^^^^^^^^^

.. code-block:: bash

   lsusb

Rechercher une ligne contenant « FTDI » ou « Future Technology Devices ».

Si le pilote n’est pas chargé
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo modprobe ftdi_sio

Ajouter l’utilisateur au groupe dialout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   sudo reboot

.. note::
   Le redémarrage est nécessaire pour que les changements prennent effet.


Choix de l’Environnement de Développement
-----------------------------------------

Vous avez deux options pour programmer le Mk2PVRouter :

**Option A : Arduino IDE**

- La plus simple à prendre en main
- Configuration manuelle nécessaire (C++17, bibliothèques)
- Suivre les sous-sections de l’**Option A** ci-dessous

**Option B : PlatformIO** (recommandé)

- Support C++17 et bibliothèques sans configuration manuelle
- Suivre les sous-sections de l’**Option B** ci-dessous

.. note::
   Vous pouvez choisir l’une ou l’autre option, ou même installer les deux environnements si vous le souhaitez.



.. _install-arduino:

.. include:: common/installation-arduino-ide.inc.rst



.. _install-platformio:


.. include:: common/installation-platformio.inc.rst
