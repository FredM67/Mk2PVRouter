Option B : Installation avec PlatformIO
---------------------------------------

Présentation
~~~~~~~~~~~~

**PlatformIO** est un environnement de développement plus complet que l’Arduino IDE. C’est la méthode recommandée, avec Visual Studio Code ; l’Arduino IDE reste la plus simple à installer.

Avantages
~~~~~~~~~

- Gestion automatique des bibliothèques (OneWire, RFM69, et U8g2 pour le monophasé)
- Support C++17 natif (pas besoin de modifier `platform.txt`)
- Compilations plus rapides
- Meilleure intégration avec Git

.. important::
   Avec PlatformIO, **aucune configuration manuelle n’est nécessaire**.

   Vous n’avez **PAS** besoin de :

   - Configurer C++17 manuellement (voir ci-dessus)
   - Installer les bibliothèques manuellement (voir ci-dessus)

   Tout est géré automatiquement par PlatformIO !

Installation Visual Studio Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visual Studio Code est l’éditeur de code qui hébergera PlatformIO.

Windows
~~~~~~~

#. Ouvrir le navigateur web : https://code.visualstudio.com/
#. Cliquer sur **« Download for Windows »**
#. Double-cliquer sur le fichier téléchargé (`VSCodeSetup-xxx.exe`)
#. Accepter la licence
#. **Recommandé :** Cocher toutes les options additionnelles :

   - Ajouter à PATH
   - Créer une icône sur le bureau
   - Ajouter l’action « Ouvrir avec Code » au menu contextuel

#. Cliquer sur **« Installer »**
#. Attendre la fin de l’installation
#. Lancer VS Code

macOS
~~~~~

#. Ouvrir le navigateur web : https://code.visualstudio.com/
#. Cliquer sur **« Download for Mac »**
#. Ouvrir le fichier `.zip` téléchargé
#. Glisser **Visual Studio Code.app** dans le dossier **Applications**
#. Lancer VS Code depuis le dossier Applications

.. _platformio-vscode-linux:

Linux (Ubuntu/Debian)
~~~~~~~~~~~~~~~~~~~~~

Méthode 1 : Installation via le site officiel (recommandé)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Ouvrir le navigateur web : https://code.visualstudio.com/
#. Cliquer sur **« .deb »** (pour Ubuntu/Debian)
#. Installer le paquet téléchargé :

   .. code-block:: bash

      sudo dpkg -i code_*.deb
      sudo apt-get install -f

Méthode 2 : Installation via le gestionnaire de paquets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sudo apt update
   sudo apt install code

Installation PlatformIO IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO s’installe comme une extension dans Visual Studio Code.

Installation de l’Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Ouvrir **Visual Studio Code**
#. Cliquer sur l’icône **Extensions** dans la barre latérale gauche (ou Ctrl+Shift+X / Cmd+Shift+X)
#. Dans le champ de recherche, taper : `PlatformIO IDE`
#. Trouver l’extension **« PlatformIO IDE »** par PlatformIO
#. Cliquer sur **« Install »**
#. Attendre la fin de l’installation (peut prendre 2–5 minutes)
#. Une fois terminé, cliquer sur **« Reload »** pour redémarrer VS Code

.. note::
   Au premier lancement après installation, PlatformIO téléchargera des outils supplémentaires.
   Cela peut prendre quelques minutes. Soyez patient !

Vérification de l’Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Après le redémarrage de VS Code :

#. Une icône PlatformIO (alien/extraterrestre) devrait apparaître dans la barre latérale gauche
#. Cliquer sur cette icône ouvre le **PIO Home**
#. Si vous voyez le **PIO Home**, l’installation est réussie !

Ouverture du Projet
~~~~~~~~~~~~~~~~~~~

#. Dans **PIO Home**, cliquer sur **« Open Project »**
#. Naviguer vers le dossier du firmware :

   - Mono : `PVRouter-1-phase-dev/Mk2_1phase_RFdatalog_temp/`
   - Tri : `PVRouter-3-phase-dev/Mk2_3phase_RFdatalog_temp/`

#. PlatformIO détecte automatiquement le fichier `platformio.ini`
#. Le projet s’ouvre avec tous les fichiers visibles dans l’explorateur

Configuration du Projet
~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO télécharge **automatiquement** :

- Le compilateur AVR-GCC avec support C++17
- Les bibliothèques nécessaires (OneWire, RFM69, et U8g2 pour le monophasé)
- Les outils de programmation

.. note::
   Le premier téléchargement des dépendances peut prendre 5–10 minutes selon votre connexion Internet.
   PlatformIO affiche la progression dans le terminal intégré.

Compilation et Téléversement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connecter le routeur via l’adaptateur FTDI (voir *Connexion du Routeur* dans :ref:`logiciel-monophase` ou :ref:`logiciel-triphase`)
#. Dans la barre inférieure de VS Code, cliquer sur l’icône **« Upload »** (→)
#. PlatformIO compile automatiquement et téléverse le firmware
#. Surveiller le terminal pour les messages de progression
#. Pour le moniteur série, cliquer sur l’icône **« Serial Monitor »** (une prise) dans la barre inférieure : PlatformIO l’ouvre à 9600 bauds, sa vitesse par défaut, qui est celle du routeur

Sélection de la Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les deux firmwares contiennent les mêmes environnements préconfigurés :

- `env:basic` : le firmware du routeur, **environnement par défaut** : c’est celui à utiliser
- `env:basic_debug` : le même firmware compilé en mode débogage, pour les développeurs
- `env:native`, `env:uno_sim` : tests unitaires et simulateur, réservés au développement

Les options (sondes de température, module RF, relais…) ne dépendent pas de l’environnement : elles se règlent dans `config.h`.

Pour changer d’environnement :

#. Cliquer sur le sélecteur d’environnement dans la barre inférieure
#. Choisir la configuration désirée
#. Recompiler le projet

.. tip::
   PlatformIO évite les deux étapes manuelles de l’Arduino IDE, sources d’erreurs fréquentes : la modification de `platform.txt` et l’installation des bibliothèques.

.. _platformio-termine:

✅ **Configuration PlatformIO terminée !** Passez maintenant aux étapes spécifiques à votre version (:term:`monophasé <Monophasé>` ou :term:`triphasé <Triphasé>`).
