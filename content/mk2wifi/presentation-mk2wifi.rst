.. _presentation-mk2wifi:

=======================
Module mk2Wifi
=======================

⏱️ **Temps de lecture** : 5-10 minutes

Vue d'ensemble
--------------

La carte :term:`mk2Wifi` est un module d'extension qui ajoute une connectivité sans fil au Mk2 PV Router. Elle est basée sur un module **ESP32-C3-MINI-1** (:term:`ESP32-C3`, RISC-V simple cœur) et offre :

- **WiFi** 802.11 b/g/n (2,4 GHz)
- **Bluetooth LE 5**
- Connecteur **USB-C** pour le chargement initial du firmware (mises à jour suivantes via :term:`OTA`)
- Écran **OLED** optionnel via I2C (connecteur Molex SL)
- Cinq sorties GPIO de déclenchement/commande (**D5–D9**) vers la carte principale
- Passthrough du capteur de température 1-Wire **DS18B20**
- Liaison série **UART** avec la carte principale

Le module se branche directement sur la carte principale via les connecteurs **TRIG_EXT** et **UART_EXT**, et est alimenté en +5 V par celle-ci.

.. note::
   Le module mk2Wifi est **entièrement assemblé en usine** (composants :term:`CMS`). Aucune soudure n'est nécessaire.

Images de la carte
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Face avant (assemblée)
     - Face arrière
   * - .. figure:: ../img/mk2wifi-front.png
          :alt: Module mk2Wifi — face avant assemblée

     - .. figure:: ../img/mk2wifi-back.png
          :alt: Module mk2Wifi — face arrière

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Composants :term:`CMS` uniquement
     - Circuit imprimé nu
   * - .. figure:: ../img/mk2wifi-smd.png
          :alt: Module mk2Wifi — composants CMS

     - .. figure:: ../img/mk2wifi-bare.png
          :alt: Module mk2Wifi — PCB nu

Connecteurs
-----------

.. list-table::
   :header-rows: 1
   :widths: 15 25 20 40

   * - Réf
     - Valeur
     - Boîtier
     - Description
   * - TRIG_EXT
     - Conn_01x06
     - Barrette femelle 1×06 2,54 mm
     - Connecteur déclenchement/GPIO (s'enfiche sur la carte principale)
   * - UART_EXT
     - Conn_01x06
     - Barrette femelle 1×06 2,54 mm
     - Connecteur UART + DS18B20 (s'enfiche sur la carte principale)
   * - OLED
     - Conn_01x04
     - Molex SL 1×04 2,54 mm
     - Connecteur écran OLED I2C
   * - USB-C
     - USB_C_Receptacle
     - CSP-USC16-TR
     - Connecteur USB Type-C (programmation initiale)

Alimentation
------------

En fonctionnement normal, le **+5 V** est fourni par la carte principale via le connecteur UART_EXT (broche 3). Le régulateur :term:`LDO` AP2112K-3.3 (U2) convertit cette tension en +3,3 V pour l'ESP32-C3 et l'écran OLED, avec un courant maximal de 600 mA.

Le connecteur USB-C peut également fournir du +5 V lors de la programmation initiale, lorsque la carte n'est pas connectée à la carte principale.

.. danger::
   **Ne pas connecter l'USB-C lorsque la carte mk2Wifi est branchée sur la carte principale.**

   Les deux alimentations +5 V (USB et carte principale) ne sont pas isolées et les connecter simultanément peut endommager la carte ou l'hôte USB.

D1 est une LED témoin d'alimentation, allumée en permanence lorsque le +3,3 V est présent.

Intégration avec la carte principale
--------------------------------------

La mk2Wifi se branche sur les connecteurs **TRIG_EXT** et **UART_EXT** de la carte principale :

- La mk2Wifi utilise des **barrettes femelles** ; la carte principale utilise des **barrettes mâles**
- L'alimentation +5 V est fournie par la carte principale via UART_EXT broche 3
- L'UART (TX/RX) assure la communication série avec l'ATmega328P
- Le signal DS18B20 est acheminé pour la mesure de température 1-Wire
- Les signaux GPIO D5–D9 fournissent les sorties de déclenchement/commande
- Le bus I2C (SCL/SDA) est **local à la mk2Wifi uniquement** — il relie l'ESP32-C3 à l'écran OLED et n'est pas routé vers la carte principale

.. note::
   La gestion du capteur DS18B20 est sélectionnée par le cavalier **TEMP** sur la carte principale (voir :ref:`cavaliers`). En position 3–centre, c'est l'ESP32-C3 de la mk2Wifi qui gère le capteur.

.. |br| raw:: html

  <br/>
