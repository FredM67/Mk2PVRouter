.. _installation-mk2wifi:

================================
Installation du module mk2Wifi
================================

⏱️ **Temps estimé** : 30–45 minutes

🔧 **Niveau de difficulté** : Débutant

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Chapitre :ref:`presentation-mk2wifi` lu
   | ☐ Carte principale assemblée et testée
   | ☐ Cavalier TEMP configuré selon votre choix (voir :ref:`cavaliers`)
   | ☐ Routeur programmé avec ``SERIAL_OUTPUT_TYPE = SerialOutputType::IoT`` dans ``config.h`` (9600 bauds, 7E1), le mode par défaut : à remettre si vous êtes passé en mode lisible pour les premiers tests
   | ☐ Câble USB-C disponible
   | ☐ Ordinateur avec port USB

Soudure des barrettes
---------------------

Le module mk2Wifi est livré avec ses composants :term:`CMS` assemblés. Les deux **barrettes femelles** TRIG_EXT et UART_EXT (1×06, 2,54 mm) doivent être soudées par l’utilisateur ; la carte principale porte les barrettes mâles correspondantes.

#. Insérez chaque barrette femelle **par la face arrière** du module (face sans composants, où sont sérigraphiés les cadres TRIG_EXT et UART_EXT) ; les soudures se font côté composants. Une barrette soudée sur la mauvaise face obligerait à brancher le module à l’envers
#. Soudez une broche, vérifiez que la barrette est perpendiculaire au :term:`PCB`
#. Soudez les broches restantes

.. todo:: Photo à fournir — barrettes TRIG_EXT et UART_EXT soudées et perpendiculaires au PCB.

Installation physique
---------------------

Si le module n’est pas encore programmé, faites d’abord la :ref:`programmation initiale <installation-mk2wifi-programmation>`, qui se fait module débranché de la carte principale.

.. warning::
   **COUPER L’ALIMENTATION SECTEUR** avant toute manipulation.

   Le routeur doit être **hors tension** pour brancher ou débrancher le module mk2Wifi.

.. warning::
   Avant de brancher le module, vérifiez que le cavalier **V sel.** de la carte principale est dans sa position d’usine **1–centre (3,3 V)**. Les broches GPIO de l’ESP32-C6 ne tolèrent que 3,3 V — une tension de 5 V sur ces lignes **endommagerait le module** (voir :ref:`cavaliers`).

#. **Vérifiez l’orientation** : composants du module vers le haut (barrettes femelles dessous), TRIG_EXT du module sur TRIG_EXT de la carte principale et UART_EXT sur UART_EXT, la broche 1 (GND, pastille carrée) de chaque barrette du module en face de la broche 1 (GND) du connecteur de la carte principale. Le module ne doit pas être retourné.

#. **Enfoncez le module** fermement mais sans forcer sur les deux connecteurs de la carte principale (TRIG_EXT et UART_EXT)

#. **Vérifiez** que le module est bien en contact sur toute la longueur des deux connecteurs

.. warning::
   Le module peut être branché à l’envers — les connecteurs ne possèdent pas de détrompeur. Vérifiez visuellement l’orientation et l’alignement avant d’enfoncer le module. Un branchement inversé peut endommager le module et/ou la carte principale.

.. _installation-mk2wifi-programmation:

Programmation initiale (USB-C)
-------------------------------

Le premier chargement du firmware se fait obligatoirement via le connecteur USB-C. Les mises à jour suivantes pourront se faire via :term:`OTA` (WiFi).

.. warning::
   **Ne pas connecter l’USB-C lorsque la carte mk2Wifi est branchée sur la carte principale.**

   Débranchez le module de la carte principale avant de connecter le câble USB-C.

.. tip::
   Pour le routeur triphasé, le :ref:`configurateur <configurateur-triphase>` génère le YAML ESPHome du module, cohérent avec le ``config.h`` du routeur, et indique les ponts de soudure à fermer. Pour le routeur monophasé, ce YAML n’est pas encore généré (voir :ref:`configurateur-monophase`) ; le `Gist de référence <https://gist.github.com/FredM67/986e1cb0fc020fa6324ccc151006af99>`_ peut servir de point de départ.

Procédure
~~~~~~~~~

#. **Coupez l’alimentation secteur du routeur**, puis **débranchez le module** de la carte principale (si connecté)

#. **Connectez le câble USB-C** entre le module et votre ordinateur

#. **Passez en mode téléchargement** : Maintenez le bouton **Boot** (SW1) enfoncé (GPIO9 à l’état bas) pendant la mise sous tension, puis relâchez

   .. tip::
      Il s’agit du petit bouton-poussoir marqué « Boot » sur la carte. Si le module est déjà alimenté par USB, débranchez et rebranchez le câble USB-C tout en maintenant le bouton enfoncé.

#. **Chargez le firmware** : pour ESPHome, voir :ref:`installation-mk2wifi-esphome` ci-dessous

#. **Après le chargement**, débranchez le câble USB-C

#. **Routeur hors tension**, rebranchez le module sur la carte principale

.. note::
   L’ESP32-C6 dispose d’un contrôleur USB-série/JTAG intégré : aucun programmateur externe n’est nécessaire.

.. _installation-mk2wifi-esphome:

ESPHome et Home Assistant
~~~~~~~~~~~~~~~~~~~~~~~~~

Le YAML généré par le configurateur se charge dans ESPHome (tableau de bord ou ligne de commande) :

- il demande **ESPHome 2026.10.0 ou plus récent** (``min_version``), première version qui intègre le composant ``mk2pvrouter`` ;
- les mots de passe et clés n’y figurent pas : ils sont lus dans un fichier ``secrets.yaml``, qui doit définir ``wifi_ssid``, ``wifi_password``, ``wifi_fallback_password``, ``api_encryption_key``, ``esphome_ota_password``, ``esphome_web_server_username`` et ``esphome_web_server_password`` ;
- la **première installation** se fait par le câble USB-C, module débranché de la carte principale (procédure ci-dessus) : dans le tableau de bord ESPHome, « Install », puis « Plug into this computer » (ou ESPHome Web depuis le navigateur) ; les suivantes se font **sans fil** (:term:`OTA`, voir plus bas) ;
- une fois le module sur le réseau WiFi, Home Assistant le détecte (intégration ESPHome) : ajoutez-le en saisissant la clé ``api_encryption_key`` ; la connexion passe par l’API native d’ESPHome, chiffrée avec cette clé ;
- si le module ne trouve pas le réseau WiFi, il ouvre son propre point d’accès de secours, dont le nom commence par le nom convivial de l’appareil (mot de passe ``wifi_fallback_password``), qui permet de saisir le bon réseau ;
- le journal série d’ESPHome est désactivé (``baud_rate: 0``) : l’UART sert à la liaison avec le routeur. Les journaux se consultent par WiFi.

.. important::
   Le module ne comprend que la sortie série ``IoT`` du routeur (9600 bauds, 7E1) : vérifiez ``SERIAL_OUTPUT_TYPE`` dans le ``config.h`` du routeur.

Mises à jour OTA
-----------------

Après le premier chargement par USB-C, les mises à jour du firmware peuvent se faire **sans fil** via WiFi (:term:`OTA`).

#. Assurez-vous que le module mk2Wifi est connecté à votre réseau WiFi

#. Lancez la mise à jour OTA depuis votre outil de développement (avec ESPHome, installation sans fil protégée par le mot de passe ``esphome_ota_password``)

#. Le module redémarre automatiquement après la mise à jour

.. note::
   La connexion USB-C n’est nécessaire que pour le **premier chargement** du firmware. Toutes les mises à jour suivantes se font via OTA.

Écran OLED (optionnel)
-----------------------

Le module mk2Wifi dispose d’un connecteur **OLED** (Molex SL 1×4) pour un écran I2C.

.. note::
   Le bus I2C de l’écran OLED est **local au module mk2Wifi**. Il n’est pas partagé avec la carte principale. Cela signifie que l’écran OLED du mk2Wifi est **indépendant** du connecteur OLED de la carte principale.

   En mode triphasé, l’écran OLED de la carte principale n’est pas disponible (broches A4/A5 utilisées pour la mesure). L’écran OLED via le mk2Wifi est alors la seule option d’affichage.

   Le YAML généré par le configurateur déclare le bus I2C (``bus_oled``) mais ne pilote pas l’écran : le composant ``display`` est à ajouter vous-même.

Vérification
------------

.. admonition:: ✅ Point de Contrôle — Module mk2Wifi

   Après l’installation, vérifiez :

   | ☐ Module correctement enfoncé sur les deux connecteurs (TRIG_EXT et UART_EXT)
   | ☐ LED témoin **D1** allumée lorsque la carte principale est sous tension
   | ☐ Firmware chargé avec succès (premier chargement via USB-C)
   | ☐ Mesures du routeur (puissance instantanée…) mises à jour dans Home Assistant ou dans les journaux ESPHome (par WiFi)
   | ☐ Connexion WiFi établie (si le firmware WiFi est configuré)

.. |br| raw:: html

  <br/>
