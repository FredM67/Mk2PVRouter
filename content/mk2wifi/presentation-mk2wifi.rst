.. _presentation-mk2wifi:

=======================
Module mk2Wifi
=======================

⏱️ **Temps de lecture** : 5–10 minutes

Vue d’ensemble
--------------

Le module :term:`mk2Wifi` est un module d’extension qui ajoute une connectivité sans fil au Mk2 PV Router. Il est basé sur un module **ESP32-C6-MINI-1** (:term:`ESP32-C6`, RISC-V simple cœur) et offre :

- **WiFi 6** 802.11 b/g/n/ax (2,4 GHz)
- **Bluetooth LE 5**
- **Zigbee** et **Thread** (802.15.4)
- Connecteur **USB-C** pour le chargement initial du firmware (mises à jour suivantes via :term:`OTA`)
- Écran **OLED** optionnel via I2C (connecteur Molex SL)
- Cinq sorties GPIO de déclenchement/commande (**D5–D9**) vers la carte principale
- Quatre GPIO supplémentaires (**GPIO19–GPIO22**) sur un connecteur MISC
- Passthrough du capteur de température 1-Wire **DS18B20**
- Liaison série **UART** avec la carte principale

Le module se branche directement sur la carte principale via les connecteurs **TRIG_EXT** et **UART_EXT**, et est alimenté en +5 V par celle-ci.

.. note::
   Les composants :term:`CMS` du module mk2Wifi sont **assemblés en usine**. Seuls les **deux connecteurs à broches** (pin headers) doivent être soudés par l’utilisateur pour relier le module à la carte-mère.

Images de la carte
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Face avant (assemblée)
     - Face arrière
   * - .. figure:: ../img/mk2wifi-front.png
          :alt: Module mk2Wifi — face avant assemblée
          :class: clickable-img

     - .. figure:: ../img/mk2wifi-back.png
          :alt: Module mk2Wifi — face arrière
          :class: clickable-img

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Composants :term:`CMS` uniquement
     - Circuit imprimé nu
   * - .. figure:: ../img/mk2wifi-smd.png
          :alt: Module mk2Wifi — composants CMS
          :class: clickable-img

     - .. figure:: ../img/mk2wifi-bare.png
          :class: clickable-img
          :alt: Module mk2Wifi — PCB nu

Connecteurs
-----------

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Réf
     - Boîtier
     - Description
   * - TRIG_EXT
     - Barrette femelle 1×06 2,54 mm
     - Connecteur déclenchement/GPIO (s’enfiche sur la carte principale)
   * - UART_EXT
     - Barrette femelle 1×06 2,54 mm
     - Connecteur UART + DS18B20 (s’enfiche sur la carte principale)
   * - OLED
     - Molex SL 1×04 2,54 mm
     - Connecteur écran OLED I2C
   * - USB-C
     - CSP-USC16-TR
     - Connecteur USB Type-C (programmation initiale)
   * - MISC
     - Barrette mâle 1×05 2,54 mm
     - GPIO supplémentaires (GPIO19–GPIO22)

Connecteur MISC
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - GPIO19
   * - 3
     - GPIO20
   * - 4
     - GPIO21
   * - 5
     - GPIO22

Ces 4 GPIO sont directement connectés à l’ESP32-C6 sans résistance série. Ils peuvent être utilisés pour des capteurs, E/S ou interfaces de communication supplémentaires.

Cavaliers de soudure (D5–D9)
-------------------------------

Le module mk2Wifi dispose de **5 cavaliers de soudure** qui permettent de déconnecter individuellement chaque signal GPIO entre le module et la carte principale. Par défaut, les cavaliers sont **ouverts** (signaux déconnectés).

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Cavalier
     - Fonction
   * - D5
     - GPIO 5 (TRIG_EXT broche 5)
   * - D6
     - GPIO 6 (TRIG_EXT broche 4)
   * - D7
     - GPIO 7 (TRIG_EXT broche 3)
   * - D8
     - GPIO 8 (TRIG_EXT broche 2)
   * - D9
     - GPIO 9 (TRIG_EXT broche 6)

Pour utiliser une sortie de déclenchement, le cavalier correspondant doit être **fermé** (goutte de soudure entre les deux pastilles). Cela permet de n’activer que les sorties réellement utilisées et de libérer les autres broches pour d’autres usages sur la carte principale.

.. tip::
   Si vous utilisez toutes les sorties D5–D9, fermez les 5 cavaliers. Si vous n’utilisez que certaines sorties, ne fermez que les cavaliers correspondants.

Alimentation
------------

En fonctionnement normal, le **+5 V** est fourni par la carte principale via le connecteur UART_EXT (broche 3). Le régulateur :term:`LDO` AP2112K-3.3 (U2) convertit cette tension en +3,3 V pour l’ESP32-C6 et l’écran OLED, avec un courant maximal de 600 mA.

Le connecteur USB-C peut également fournir du +5 V lors de la programmation initiale, lorsque la carte n’est pas connectée à la carte principale.

.. warning::
   **Ne pas connecter l’USB-C lorsque le module mk2Wifi est branché sur la carte principale.**

   Les deux alimentations +5 V (USB et carte principale) ne sont pas isolées et les connecter simultanément peut endommager la carte ou l’hôte USB.

La LED témoin **D1** est allumée en permanence lorsque le +3,3 V est présent.

Intégration avec la carte principale
--------------------------------------

Le module mk2Wifi se branche sur les connecteurs **TRIG_EXT** et **UART_EXT** de la carte principale :

- L’une des deux cartes utilise des **barrettes mâles**, l’autre des **barrettes femelles** (au choix de l’utilisateur)
- L’alimentation +5 V est fournie par la carte principale via UART_EXT broche 3
- L’UART (TX/RX) assure la communication série avec l’ATmega328P
- Le signal DS18B20 est acheminé pour la mesure de température 1-Wire
- Les signaux GPIO D5–D9 fournissent les sorties de déclenchement/commande
- Le bus I2C (SCL/SDA) est **local au module mk2Wifi uniquement** — il relie l’ESP32-C6 à l’écran OLED et n’est pas routé vers la carte principale

.. note::
   La gestion du capteur DS18B20 est sélectionnée par le cavalier **TEMP** sur la carte principale (voir :ref:`cavaliers`). En position 3–centre, c’est l’ESP32-C6 du mk2Wifi qui gère le capteur.

.. |br| raw:: html

  <br/>
