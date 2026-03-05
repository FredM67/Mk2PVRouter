.. _installation-mk2wifi:

================================
Installation du module mk2Wifi
================================

⏱️ **Temps estimé** : 30–45 minutes

🔧 **Niveau de difficulté** : Débutant

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Chapitre :ref:`presentation-mk2wifi` lu
   | ☐ Carte principale assemblée et testée
   | ☐ Cavalier TEMP configuré selon votre choix (voir :ref:`cavaliers`)
   | ☐ Câble USB-C disponible
   | ☐ Ordinateur avec port USB

Soudure des barrettes
---------------------

Le module mk2Wifi est livré entièrement assemblé (composants :term:`CMS`). Seules les deux **barrettes** (TRIG_EXT et UART_EXT, 1×06, 2,54 mm) doivent être soudées par l’utilisateur — mâles ou femelles, selon le choix fait sur la carte principale.

#. Positionnez chaque barrette dans son emplacement
#. Soudez une broche, vérifiez que la barrette est perpendiculaire au :term:`PCB`
#. Soudez les broches restantes

.. todo:: Photo à fournir — barrettes TRIG_EXT et UART_EXT soudées et perpendiculaires au PCB.

Installation physique
---------------------

.. danger::
   **COUPER L’ALIMENTATION SECTEUR** avant toute manipulation.

   Le routeur doit être **hors tension** pour brancher ou débrancher le module mk2Wifi.

.. warning::
   Avant de brancher le module, vérifiez que le cavalier **V sel.** de la carte principale est en position **3–centre (3,3 V)**. Les broches GPIO de l’ESP32-C3 ne tolèrent que 3,3 V — une tension de 5 V sur ces lignes **endommagerait le module** (voir :ref:`cavaliers`).

#. **Vérifiez l’orientation** : Les connecteurs TRIG_EXT et UART_EXT du module doivent s’aligner avec ceux de la carte principale. Le module ne doit pas être retourné.

#. **Enfoncez le module** fermement mais sans forcer sur les deux connecteurs de la carte principale (TRIG_EXT et UART_EXT)

#. **Vérifiez** que le module est bien en contact sur toute la longueur des deux connecteurs

.. warning::
   Le module peut être branché à l’envers — les connecteurs ne possèdent pas de détrompeur. Vérifiez visuellement l’orientation et l’alignement avant d’enfoncer le module. Un branchement inversé peut endommager le module et/ou la carte principale.

Programmation initiale (USB-C)
-------------------------------

Le premier chargement du firmware se fait obligatoirement via le connecteur USB-C. Les mises à jour suivantes pourront se faire via :term:`OTA` (WiFi).

.. warning::
   **Ne pas connecter l’USB-C lorsque la carte mk2Wifi est branchée sur la carte principale.**

   Débranchez le module de la carte principale avant de connecter le câble USB-C.

Procédure
~~~~~~~~~

#. **Débranchez le module** de la carte principale (si connecté)

#. **Connectez le câble USB-C** entre le module et votre ordinateur

#. **Passez en mode téléchargement** : Maintenez le **bouton-poussoir** enfoncé (GPIO9 à l’état bas) pendant la mise sous tension, puis relâchez

   .. tip::
      Il s’agit du petit bouton-poussoir situé sur la carte. Si le module est déjà alimenté par USB, débranchez et rebranchez le câble USB-C tout en maintenant le bouton enfoncé.

#. **L’ESP32-C3** dispose d’un contrôleur USB-série/JTAG intégré — aucun programmateur externe n’est nécessaire

#. **Chargez le firmware** à l’aide de votre outil de développement préféré (Arduino IDE, PlatformIO, esptool, etc.)

#. **Après le chargement**, débranchez le câble USB-C

#. **Rebranchez le module** sur la carte principale

Mises à jour OTA
-----------------

Après le premier chargement par USB-C, les mises à jour du firmware peuvent se faire **sans fil** via WiFi (:term:`OTA`).

#. Assurez-vous que le module mk2Wifi est connecté à votre réseau WiFi

#. Lancez la mise à jour OTA depuis votre outil de développement

#. Le module redémarre automatiquement après la mise à jour

.. note::
   La connexion USB-C n’est nécessaire que pour le **premier chargement** du firmware. Toutes les mises à jour suivantes se font via OTA.

Écran OLED (optionnel)
-----------------------

Le module mk2Wifi dispose d’un connecteur **OLED** (Molex SL 1×4) pour un écran I2C.

.. note::
   Le bus I2C de l’écran OLED est **local au module mk2Wifi**. Il n’est pas partagé avec la carte principale. Cela signifie que l’écran OLED du mk2Wifi est **indépendant** du connecteur OLED de la carte principale.

   En mode triphasé, l’écran OLED de la carte principale n’est pas disponible (broches A4/A5 utilisées pour la mesure). L’écran OLED via le mk2Wifi est alors la seule option d’affichage.

Vérification
------------

.. admonition:: ✅ Point de Contrôle — Module mk2Wifi

   Après l’installation, vérifiez :

   | ☐ Module correctement enfoncé sur les deux connecteurs (TRIG_EXT et UART_EXT)
   | ☐ LED témoin **D1** allumée lorsque la carte principale est sous tension
   | ☐ Firmware chargé avec succès (premier chargement via USB-C)
   | ☐ Communication série fonctionnelle (données visibles sur le moniteur série)
   | ☐ Connexion WiFi établie (si le firmware WiFi est configuré)

.. |br| raw:: html

  <br/>
