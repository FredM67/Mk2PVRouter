
.. _glossary:

=========
Glossaire
=========

Ce glossaire est divisé en deux sections :

1. **Termes de Base** : Pour les débutants, explications simples des concepts électriques et électroniques fondamentaux
2. **Termes Techniques** : Définitions spécialisées pour le Mk2PVRouter et l’électronique avancée

=====================================
Termes de Base pour Débutants
=====================================

.. glossary::
   :sorted:

   Tension (V)
     | La **tension électrique**, mesurée en **volts (V)**, représente la « pression » qui pousse les électrons à circuler dans un circuit.
     | En France, la tension domestique standard est de **230 V AC**.

     💡 **Analogie** : Comme la pression de l’eau dans un tuyau. Plus la pression est élevée, plus l’eau circule fort.

   Courant (A)
     | Le **courant électrique**, mesuré en **ampères (A)**, représente la quantité d’électrons qui circulent dans un conducteur.
     | Un appareil de 2 000 W sous 230 V consomme environ 8,7 A.

     💡 **Analogie** : Comme le débit d’eau dans un tuyau. Plus le débit est élevé, plus il y a d’eau qui passe.

   Puissance (W)
     | La **puissance électrique**, mesurée en **watts (W)**, représente l’énergie consommée ou produite par un appareil.
     | **Formule** : Puissance (W) = Tension (V) × Courant (A)
     | Exemple : Un chauffe-eau de 2 000 W sous 230 V consomme environ 8,7 A.

   Résistance (Ω)
     | Une **résistance**, mesurée en **ohms (Ω)**, est un composant qui limite le passage du courant électrique.
     | Plus la résistance est élevée, moins le courant passe.

     💡 **Analogie** : Comme un rétrécissement dans un tuyau qui limite le débit d’eau.

   Phase
     | Le fil **phase** (généralement rouge, noir ou marron) apporte le courant électrique depuis le réseau.
     | ⚠️ **DANGER** : Ce fil est sous tension de **230 V** et peut être **MORTEL** au contact.

   Neutre
     | Le fil **neutre** (généralement bleu) permet le retour du courant vers le réseau électrique.
     | Il est normalement proche de 0 V, mais peut devenir dangereux en cas de défaut.

   Terre
     | Le fil de **terre** (vert/jaune) est une protection de sécurité.
     | Il évacue les courants de fuite et protège contre l’électrocution en cas de défaut d’isolement.

   Monophasé
     | Système électrique avec **une seule phase** (230 V entre phase et neutre).
     | C’est le système standard pour la plupart des habitations françaises.
     | Compteur électrique monophasé : 2 fils (phase + neutre + terre).

   Triphasé
     | Système électrique avec **trois phases** (400 V entre phases, 230 V entre chaque phase et le neutre).
     | Utilisé pour les installations nécessitant beaucoup de puissance (grandes maisons, bâtiments professionnels).
     | Compteur électrique triphasé : 4 fils (3 phases + neutre + terre).

   Disjoncteur
     | Dispositif de **sécurité** qui coupe automatiquement le courant en cas de :
     | - **Surcharge** (trop d’appareils branchés)
     | - **Court-circuit** (contact direct entre phase et neutre)
     | Il se trouve dans le **tableau électrique** de l’habitation.

   Court-circuit
     | Contact direct entre la **phase** et le **neutre** (ou la terre) sans résistance intermédiaire.
     | Provoque un courant très élevé qui fait disjoncter le disjoncteur.
     | Peut causer un incendie si non protégé.

   Diode
     | Composant électronique **polarisé** (a un sens) qui laisse passer le courant dans **un seul sens**.
     | Repérage : Une **bande** indique la cathode (côté -).
     | ⚠️ **Important** : À installer dans le bon sens, sinon ne fonctionne pas.

   Condensateur
     | Composant qui **stocke temporairement** de l’énergie électrique.
     | Deux types :
     | - **Polarisés** (électrolytiques) : Ont un + et un -, à respecter impérativement
     | - **Non polarisés** (céramiques) : Peuvent être montés dans les deux sens

   LED (Diode électroluminescente)
     | Composant **polarisé** qui émet de la lumière quand le courant passe.
     | Repérage : La **patte longue** est le + (anode), la **patte courte** est le - (cathode).
     | ⚠️ **Important** : À installer dans le bon sens, sinon ne s’allume pas (et peut être endommagée).

   Triac
     | Composant électronique qui agit comme un **interrupteur rapide** pour contrôler la puissance envoyée à une charge.
     | Utilisé dans le Mk2PVRouter pour réguler la puissance envoyée au chauffe-eau.
     | Génère de la chaleur, d’où la nécessité d’un dissipateur thermique.

   Transformateur
     | Composant qui **convertit** une tension alternative en une autre tension alternative.
     | Dans le Mk2PVRouter : Les transformateurs ZMPT101K mesurent la tension secteur de façon isolée (230 V → signal basse tension).

   Circuit intégré (IC)
     | Une « puce » électronique contenant de nombreux composants miniaturisés.
     | Le **microcontrôleur ATmega328P** du Mk2PVRouter est un circuit intégré.
     | ⚠️ **Important** : Fragile, sensible à l’électricité statique et à la chaleur.

   Fusible
     | Dispositif de **protection** qui fond (se coupe) en cas de surintensité.
     | Une fois fondu, il doit être **remplacé** (contrairement au disjoncteur qui se réarme).
     | Dans le Mk2PVRouter : Protège contre les courts-circuits et les surcharges.

   Polarité
     | Le **sens** d’un composant électronique (+ et -).
     | Certains composants (diodes, LED, condensateurs électrolytiques) **doivent** être montés dans le bon sens.
     | ⚠️ **Danger** : Un composant polarisé monté à l’envers peut exploser ou ne pas fonctionner.

   Soudure
     | Technique pour **fixer et relier électriquement** des composants sur un circuit imprimé.
     | Utilise un **fer à souder** (300–350 °C) et de l’**étain** (alliage qui fond à ~200 °C).
     | Une bonne soudure est brillante et forme un cône régulier.

   Pont de soudure
     | **Erreur de soudure** : De l’étain relie accidentellement deux pistes ou broches qui ne doivent pas être connectées.
     | Provoque un **court-circuit**.
     | Se corrige en retirant l’excédent d’étain avec une tresse à dessouder.

   Piste
     | Chemin conducteur en cuivre sur un circuit imprimé (:term:`PCB`) qui relie les composants entre eux.
     | Équivalent des fils électriques, mais imprimés sur la carte.

   Isolant électrique
     | Matériau qui **ne conduit pas** l’électricité (plastique, céramique, mica, silicone).
     | Utilisé pour **séparer électriquement** deux éléments conducteurs tout en permettant le contact thermique.
     | Exemple : Feuille de mica entre le triac et le dissipateur.

   Dissipateur thermique
     | Pièce métallique (généralement en aluminium) qui **évacue la chaleur** des composants électroniques.
     | Fonctionne par **convection naturelle** (l’air chaud monte) ou forcée (ventilateur).
     | Le Mk2PVRouter utilise des dissipateurs pour les triacs (3 kW max par dissipateur).

   Multimètre
     | Appareil de **mesure** électrique permettant de mesurer :
     | - **Tension** (V) en mode voltmètre
     | - **Courant** (A) en mode ampèremètre
     | - **Résistance** (Ω) en mode ohmmètre
     | - **Continuité** (pour vérifier les connexions)

   Électrisation
     | **Choc électrique** subi par une personne exposée à une tension électrique.
     | La personne **survit** mais peut avoir des séquelles (brûlures, troubles cardiaques).
     | Différent de l’électrocution (qui est mortel).

   Électrocution
     | **Décès causé** par un choc électrique.
     | Peut survenir à partir de 50 V AC en milieu humide, 120 V AC en milieu sec.
     | ⚠️ **DANGER DE MORT** : Le 230 V domestique peut tuer instantanément.

   Firmware
     | **Programme informatique** stocké dans la mémoire du microcontrôleur.
     | C’est le « cerveau » du Mk2PVRouter qui gère les mesures et le contrôle des charges.
     | Se télécharge via l’Arduino IDE avec un câble USB-série (FTDI).

   Microcontrôleur
     | **Mini-ordinateur** sur une seule puce électronique.
     | Le Mk2PVRouter utilise un **ATmega328P** (le même que l’Arduino Uno).
     | Contient : Processeur, mémoire, entrées/sorties, convertisseurs analogique-numérique.

   Arduino
     | **Plateforme de développement** open-source pour programmer des microcontrôleurs facilement.
     | Le Mk2PVRouter utilise le **langage Arduino** (basé sur C++) et l’**Arduino IDE** pour la programmation.

   Étalonnage / Calibration
     | Procédure d’**ajustement précis** du routeur pour qu’il mesure correctement :
     | - La tension du réseau électrique (230 V)
     | - Le courant consommé/produit (A)
     | - La puissance (W)
     | Sans étalonnage, les mesures sont fausses et le routeur ne fonctionne pas correctement.

   Routeur solaire
     | Appareil qui **redirige automatiquement** l’excédent de production photovoltaïque vers des charges (chauffe-eau, radiateur) au lieu de l’injecter sur le réseau.
     | Le **Mk2PVRouter** est un routeur solaire.

   Autoconsommation
     | Principe qui consiste à **consommer sa propre production** d’électricité au lieu de la revendre ou de la perdre.
     | Objectif : Maximiser l’utilisation de l’énergie gratuite produite par les panneaux solaires.

   Excédent
     | **Surplus de production** d’électricité photovoltaïque non consommé instantanément par les appareils de la maison.
     | Sans routeur : Cet excédent est injecté sur le réseau (souvent non rémunéré).
     | Avec routeur : Cet excédent est utilisé pour chauffer l’eau ou autre charge.

   Charge
     | Appareil électrique qui **consomme de l’énergie**.
     | Dans le contexte du Mk2PVRouter : Chauffe-eau, radiateur électrique, plancher chauffant, etc.

   Délestage / Diversion
     | Action de **rediriger** l’excédent de production vers une charge au lieu de l’injecter sur le réseau.
     | Le Mk2PVRouter fait du délestage intelligent en temps réel.

   Burst-fire
     | **Mode de contrôle** de puissance par cycles complets de la sinusoïde 50 Hz.
     | Le triac s’allume pour un certain nombre de cycles puis s’éteint.
     | Avantage : Réduit les perturbations électromagnétiques par rapport au contrôle par angle de phase.

   NF C 15-100
     | **Norme électrique française** qui définit les règles d’installation des circuits électriques domestiques.
     | Obligatoire pour toute installation électrique en France.
     | Le Mk2PVRouter doit être installé conformément à cette norme.

   Consuel
     | Organisme français de **contrôle des installations** électriques.
     | Délivre une attestation de conformité obligatoire pour toute nouvelle installation ou modification importante.

   Tableau électrique
     | **Coffret** contenant les disjoncteurs et dispositifs de protection de l’installation électrique.
     | C’est là que se trouve le **disjoncteur général** permettant de couper toute l’installation.

==============================
Termes Techniques Avancés
==============================

.. glossary::
   :sorted:

   Théorème de Blondel
     | Théorème fondamental de la mesure de puissance en régime polyphasé, énoncé par André Blondel en 1893.
     | Il stipule que pour mesurer la puissance totale d’un système à **N conducteurs**, il suffit de **N−1 wattmètres** (ou capteurs de courant).
     | Application au Mk2PVRouter : en triphasé sans neutre (3 fils), 2 CT suffisent (CT1 et CT2) — la puissance sur L3 est déduite mathématiquement.
     | Voir `l’article Wikipédia (en anglais) <https://en.wikipedia.org/wiki/Blondel%27s_theorem>`__.

   CMS
     | *Composant Monté en Surface* (ou SMD en anglais : *Surface-Mount Device*).
     | Composant électronique miniaturisé soudé directement sur la surface du circuit imprimé, sans traverser la carte.
     | Sur la carte universelle 3phaseDiverter, les composants CMS sont assemblés en usine.

   LDO
     | *Low Drop-Out regulator* ou régulateur linéaire à faible chute de tension.
     | Composant qui convertit une tension continue en une tension plus basse avec un minimum de pertes.
     | La carte principale utilise un **AP7361C-33E** (1 A) pour convertir 5 V en 3,3 V. Le module mk2Wifi utilise un **AP2112K-3.3** (600 mA).

   GDT
     | *Gas Discharge Tube* ou éclateur à gaz.
     | Composant de protection contre les surtensions qui s’amorce lorsqu’une tension transitoire dépasse son seuil.
     | Les GDT0–GDT3 sur la carte universelle forment la première ligne de défense parafoudre.

   MOV
     | *Metal Oxide Varistor* ou varistance à oxyde métallique.
     | Composant de protection qui écrête les surtensions en absorbant l’énergie excédentaire.
     | Les varistances RV0–RV3 et les modules GM1–GM3 protègent les circuits de mesure du Mk2PVRouter.

   TVS
     | *Transient Voltage Suppressor* ou suppresseur de surtension transitoire.
     | Diode spécialisée qui protège les circuits sensibles contre les surtensions rapides.
     | La carte universelle utilise des diodes TVS (DF2B7AE, CDSOD323-T03C) pour protéger les entrées :term:`ADC` de l’ATmega328P.

   SMA
     | *SubMiniature version A*.
     | Type de connecteur coaxial utilisé pour les connexions radiofréquences (:term:`RF`).
     | Le connecteur SMA de la carte universelle reçoit l’antenne du module RFM69CW.

   OTA
     | *Over-The-Air* ou mise à jour sans fil.
     | Technique permettant de mettre à jour le firmware d’un appareil via WiFi, sans connexion physique.
     | Le module mk2Wifi supporte les mises à jour OTA après le premier chargement par USB-C.

   ESPHome
     | Plateforme open-source de configuration et de gestion de microcontrôleurs ESP32/ESP8266 via des fichiers YAML.
     | Permet une intégration native avec **Home Assistant**. Le module mk2Wifi est principalement conçu pour fonctionner avec ESPHome.

   ESP32-C6
     | Microcontrôleur RISC-V simple cœur de la société Espressif, intégrant WiFi 6 (802.11ax), Bluetooth LE 5, Zigbee et Thread (802.15.4).
     | Le module **mk2Wifi** utilise un ESP32-C6-MINI-1 pour ajouter la connectivité sans fil au Mk2PVRouter.

   Split-phase
     | Système électrique nord-américain composé de deux phases à 180° fournissant 120 V entre chaque phase et le neutre, et 240 V entre les deux phases.
     | La carte universelle 3phaseDiverter supporte cette configuration.

   mk2Wifi
     | Module d’extension WiFi/BLE pour le Mk2PVRouter, basé sur un :term:`ESP32-C6`.
     | Se branche sur les connecteurs TRIG_EXT et UART_EXT de la carte principale.
     | Ajoute la connectivité sans fil, un écran OLED optionnel et la gestion du capteur de température DS18B20.

   Carte universelle
     | Carte principale **3phaseDiverter** (rév. 6.0) qui remplace les anciennes cartes monophasée et triphasée séparées.
     | Supporte 4 configurations : monophasé, triphasé avec neutre, triphasé sans neutre et split-phase.

   ZMPT101K
     | Transformateur de tension miniature (rapport 1000:1000) utilisé pour mesurer la tension secteur.
     | La carte universelle en utilise 1 (monophasé) à 3 (triphasé) pour la mesure de tension sur chaque phase.

   Cavalier de soudure
     | Pont conducteur réalisé en soudant deux pastilles adjacentes sur le :term:`PCB`.
     | Les cavaliers V sel., SDA, SCL, IRQ, NSS et TEMP sur la carte universelle permettent de configurer le mode de fonctionnement (monophasé/triphasé, alimentation, module RF, capteur de température).

   CT
     | *Current Transformer* ou dans notre cas **pince ampèremétrique**.
     | La pince ampèremétrique, aussi appelée capteur de courant sans contact, est un type d’ampèremètre permettant de mesurer l’intensité du courant électrique circulant dans un fil conducteur sans avoir à ouvrir le circuit pour y placer un ampèremètre classique.

     .. seealso::
        | `Wikipédia, Pince ampèremétrique <https://fr.wikipedia.org/wiki/Pince_amp%C3%A8rem%C3%A9trique>`_
        | `CT sensors - An Introduction <https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/introduction.html>`_

   PCB
     | *Printed Circuit Board* ou **circuit imprimé**.
     | Un circuit imprimé est un support, en général une plaque, permettant de maintenir et de relier électriquement un ensemble de composants électroniques entre eux, dans le but de réaliser un circuit électronique complexe. On le désigne aussi par le terme de carte électronique.

     .. seealso:: `Wikipédia, Circuit imprimé <https://fr.wikipedia.org/wiki/Circuit_imprim%C3%A9>`_

   Burden
     | Résistance de charge.
     | Si le capteur :term:`CT` est du type « sortie courant » tel que le YHDC SCT-013-000, le signal de courant doit être converti en signal de tension avec une résistance de charge.

     .. seealso:: `CT Sensors - Interfacing with an Arduino <https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/interface-with-arduino.html>`_

   ADC
     | *Analog Digital Converter* ou convertisseur analogique/numérique.
     | Il permet de convertir un signal analogique, par exemple une tension, en un signal numérique, par exemple une valeur entre 0 et 1 023.
     | Supposons que la plage de mesure aille de 0 à 5 V, alors, une tension d’entrée de 2,5 V correspondra à la valeur 511. Une tension de 5 V correspondra à une valeur de 1 023.

   AC
     | *Alternating Current* ou courant alternatif.
     | Courant électrique dont l’intensité et la direction varient périodiquement (50 Hz en France).

   DC
     | *Direct Current* ou courant continu.
     | Courant électrique dont l’intensité et la direction sont constantes dans le temps.

   Optocoupleur
     | Ou photocoupleur.
     | Un optocoupleur est un composant électronique qui permet de transférer un signal électrique entre deux parties d’un circuit tout en les isolant électriquement l’une de l’autre. Il est souvent utilisé pour contrôler un circuit de haute tension à partir d’un signal de basse tension, en assurant une isolation galvanique entre les deux.

     .. seealso:: `Wikipédia, Photocoupleur <https://fr.wikipedia.org/wiki/Photocoupleur>`_

   Pull-up
     | Résistance de rappel.
     | Une résistance de rappel permet de fixer une entrée numérique à un état *HIGH* ou *LOW* stable.
     | Elle permet aussi de réduire le bruit, d’éliminer les broches flottantes et surtout, d’établir deux états électriques clairs et distincts.

   DIL
      | *Dual In-line Package* ou boîtier double en ligne.
      | Un support DIL pour circuit intégré sert à plusieurs fins :
      |
      | 1. **Facilité de Remplacement** : Il permet de remplacer facilement un circuit intégré sans avoir à dessouder et ressouder le composant, ce qui est particulièrement utile en cas de défaillance ou de mise à jour.
      | 2. **Protection Contre la Chaleur** : Lors de la soudure, il protège le circuit intégré de la chaleur excessive qui pourrait l’endommager.
      | 3. **Réutilisabilité** : Il permet de réutiliser les circuits intégrés en les insérant et les retirant facilement du support.
      | 4. **Alignement Précis** : Il assure un alignement précis des broches du circuit intégré avec les pistes du circuit imprimé.
      |
      | En résumé, un support DIL facilite l’installation, le remplacement et la protection des circuits intégrés dans un montage électronique.

   SIL
      | *Single In-line Package* ou boîtier simple en ligne ou aussi *pin-header*.
      | Un support SIL pour circuit intégré est un support à une seule rangée de broches qui permet d’insérer et de retirer facilement un circuit intégré d’un circuit imprimé.
      | Il est utilisé pour les circuits intégrés ou modules à une seule rangée de broches.

   FTDI
      | *Future Technology Devices International*.
      | FTDI est une société spécialisée dans la conception de circuits intégrés et de modules de communication USB. Les modules FTDI sont largement utilisés pour la programmation et la communication avec des microcontrôleurs et des circuits intégrés via une interface USB.

      .. seealso:: `FTDI <https://www.ftdichip.com/>`_

   ATmega328P
      | Microcontrôleur 8 bits de la famille AVR d’Atmel (maintenant Microchip).
      | C’est le « cerveau » du Mk2PVRouter et de l’Arduino Uno.
      | Caractéristiques : 32 Ko de mémoire Flash, 2 Ko de RAM, 1 Ko d’EEPROM, 6 entrées analogiques, fonctionne à 16 MHz.

   EEPROM
      | *Electrically Erasable Programmable Read-Only Memory*.
      | Mémoire non volatile qui conserve les données même sans alimentation.
      | Le Mk2PVRouter y stocke les paramètres d’étalonnage.

   PWM
      | *Pulse Width Modulation* ou modulation de largeur d’impulsion.
      | Technique de contrôle de puissance en faisant varier le rapport cyclique d’un signal carré.
      | Le Mk2PVRouter n’utilise pas le PWM mais le burst-fire pour des raisons de compatibilité électromagnétique.

   RMS
      | *Root Mean Square* ou valeur efficace.
      | Valeur d’une tension ou d’un courant alternatif équivalente à celle d’un courant continu qui produirait la même puissance.
      | Exemple : 230 V AC RMS = tension efficace du réseau français.

   Zero-crossing
      | Détection du **passage par zéro** de la sinusoïde du réseau électrique.
      | Utilisé par le Mk2PVRouter pour synchroniser le contrôle des triacs et minimiser les perturbations.

   Phase-angle control
      | Contrôle de puissance en déclenchant le triac à un angle variable de la sinusoïde.
      | Non utilisé dans le Mk2PVRouter car génère beaucoup de perturbations électromagnétiques.

   RF
      | *Radio Frequency* ou radiofréquence.
      | Transmission de données sans fil par ondes radio.
      | Certaines versions du Mk2PVRouter supportent la transmission RF pour communiquer avec d’autres appareils.

   IoT
      | *Internet of Things* ou Internet des Objets.
      | Connexion d’objets physiques à Internet pour collecter et échanger des données.
      | Le Mk2PVRouter peut être configuré pour envoyer des données au format IoT.

   JSON
      | *JavaScript Object Notation*.
      | Format de données structuré, lisible par l’homme et facilement analysable par les machines.
      | Le Mk2PVRouter peut envoyer ses données au format JSON pour intégration domotique.

   Baud rate
      | Vitesse de communication série, mesurée en bits par seconde.
      | Le Mk2PVRouter utilise généralement 9 600 ou 115 200 bauds pour la communication avec l’ordinateur.
