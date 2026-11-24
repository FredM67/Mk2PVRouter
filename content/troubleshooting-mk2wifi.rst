.. _troubleshooting-mk2wifi:

======================================
📡 Problèmes du Module mk2Wifi
======================================

.. note::
   Les premières sections de cette page concernent uniquement les kits équipés du module d’extension :term:`mk2Wifi` (ESP32-C6). Les sections « Obtenir de l’aide », « Annexe — Outils de diagnostic essentiels » et « Conclusion » valent pour tout le routeur.

Le module ne s’allume pas
-------------------------

**Symptôme :** LED D1 du module éteinte lorsque la carte principale est sous tension

.. admonition:: Liste de contrôle — Alimentation mk2Wifi

   #. ☐ **Carte principale sous tension ?**

      - La mk2Wifi est alimentée en +5 V par la carte principale via UART_EXT broche 3
      - Vérifier que la carte principale fonctionne normalement

   #. ☐ **Module dans le bon sens ?**

      - Les connecteurs TRIG_EXT et UART_EXT ne possèdent **pas de détrompeur**
      - Le module peut être branché à l’envers
      - Vérifier visuellement l’alignement des sérigraphies

      .. warning::
         Un branchement inversé peut endommager le module et/ou la carte principale.

   #. ☐ **Connecteurs bien enfoncés ?**

      - Le module doit être fermement en contact sur les **deux** connecteurs (TRIG_EXT et UART_EXT)
      - Pas de broche tordue ou décalée

   #. ☐ **Cavalier V sel. en position 3,3 V ?**

      - V sel. ne coupe pas l’alimentation du module : son régulateur est alimenté par le +5 V de UART_EXT broche 3
      - Mais en position 5 V, les lignes UART et D5–D9 arrivent en 5 V sur l’ESP32-C6, qui peut avoir été endommagé : remettre V sel. en position 3,3 V avant tout nouvel essai
      - Voir :ref:`cavaliers`

Programmation USB-C impossible
------------------------------

**Symptôme :** L’ESP32-C6 n’est pas détecté par l’ordinateur via USB-C

.. admonition:: Liste de contrôle — Connexion USB-C

   #. ☐ **Module débranché de la carte principale ?**

      - Le module **doit** être déconnecté de la carte principale pendant la programmation USB-C
      - Les deux alimentations +5 V (USB et carte principale) ne sont pas isolées

   #. ☐ **Mode téléchargement activé ?**

      - Maintenir le bouton **Boot** (SW1) enfoncé pendant la mise sous tension (branchement du câble USB-C)
      - Relâcher le bouton après la connexion
      - Sans cette manipulation, le module démarre en mode normal (pas en mode programmation)

   #. ☐ **Câble USB-C avec données ?**

      - Certains câbles USB-C ne servent **qu’à la charge** (pas de fils de données)
      - Essayer un autre câble connu pour transférer des données

   #. ☐ **Port USB fonctionnel ?**

      - Essayer un autre port USB (préférer un port direct, pas un hub)

   #. ☐ **Pilotes USB-série ?**

      - L’ESP32-C6 dispose d’un contrôleur **USB-série/JTAG intégré** — aucun pilote externe normalement nécessaire
      - Windows : vérifier dans le Gestionnaire de périphériques qu’un nouveau port COM apparaît
      - Linux : ``dmesg | grep tty`` doit montrer un nouveau périphérique

Pas de communication avec la carte principale
---------------------------------------------

**Symptôme :** Module alimenté (LED D1 allumée) mais aucune donnée reçue de la carte principale

.. admonition:: Liste de contrôle — Communication UART

   #. ☐ **Module dans le bon sens ?**

      - Un branchement inversé empêche la communication
      - Vérifier l’alignement des sérigraphies TRIG_EXT et UART_EXT

   #. ☐ **Routeur en sortie série IoT ?**

      - Dans le ``config.h`` du routeur : ``SERIAL_OUTPUT_TYPE = SerialOutputType::IoT`` (9600 bauds, 7E1), le seul mode que le module comprend. À remettre si vous êtes passé en mode lisible pour les premiers tests
      - Dans le YAML ESPHome, le bloc ``uart`` doit correspondre : ``tx_pin: GPIO16``, ``rx_pin: GPIO17``, ``baud_rate: 9600``, ``parity: EVEN``, ``data_bits: 7``, ``stop_bits: 1``. Le configurateur ne l’écrit que si la sortie du routeur est IoT : régénérez le YAML après tout changement du ``config.h``
      - Au démarrage, le routeur affiche sa configuration à 9600 bauds 8N1 ; les trames qui suivent sont en 7E1. Un moniteur série réglé en 8N1 affiche donc des caractères incohérents après le démarrage

   #. ☐ **Barrettes bien soudées ?**

      - Vérifier les soudures sur les barrettes du module mk2Wifi
      - Vérifier les soudures des connecteurs TRIG_EXT et UART_EXT sur la carte principale
      - Soudure froide = contact intermittent

Connexion WiFi impossible
-------------------------

**Symptôme :** Le module ne se connecte pas au réseau WiFi

**Vérifications :**

#. **Réseau en 2,4 GHz ?**

   - L’ESP32-C6 supporte **uniquement le 2,4 GHz** (802.11 b/g/n/ax)
   - Les réseaux 5 GHz ne sont **pas visibles** par le module
   - Si votre box utilise un SSID unique pour 2,4 et 5 GHz, essayez de séparer les bandes

#. **Identifiants corrects ?**

   - Vérifier le SSID et le mot de passe dans la configuration du firmware (avec le YAML du configurateur : ``wifi_ssid`` et ``wifi_password`` dans ``secrets.yaml``)
   - Attention aux majuscules/minuscules et aux caractères spéciaux
   - Avec le YAML du configurateur, un module qui ne trouve pas le réseau ouvre son point d’accès de secours (nom commençant par le nom convivial de l’appareil, mot de passe ``wifi_fallback_password``) : s’y connecter pour saisir le bon réseau

#. **Signal suffisant ?**

   - Le module est souvent installé dans un boîtier métallique (tableau électrique)
   - Le métal atténue fortement le signal WiFi
   - Rapprocher le point d’accès ou utiliser un répéteur WiFi

#. **Firmware WiFi configuré ?**

   - Vérifier que le firmware chargé inclut la configuration WiFi
   - Un firmware vierge ne se connecte à aucun réseau

La mise à jour OTA échoue
-------------------------

**Symptôme :** La mise à jour sans fil échoue ou le module ne redémarre pas

**Causes possibles :**

#. **Module et ordinateur pas sur le même réseau**

   - Les deux doivent être sur le même réseau local (même sous-réseau)

#. **Connexion WiFi instable**

   - Une coupure pendant la mise à jour peut corrompre le firmware
   - Rapprocher le module du point d’accès pendant la mise à jour

#. **Espace mémoire insuffisant**

   - Le firmware est trop volumineux pour la partition OTA
   - Désactiver les fonctionnalités non nécessaires et recompiler

**Si le module ne répond plus après un OTA raté :**

- Revenir à la programmation par **USB-C**, routeur hors tension et **module débranché de la carte principale** (voir procédure initiale dans :ref:`installation-mk2wifi`) : ne jamais brancher le câble USB-C sur le module tant qu’il est enfiché sur la carte principale
- Maintenir le bouton **Boot** (SW1) enfoncé pour entrer en mode téléchargement

Écran OLED vide ou incorrect
----------------------------

**Symptôme :** L’écran OLED branché sur le connecteur mk2Wifi n’affiche rien ou des caractères incohérents

.. admonition:: Liste de contrôle — OLED mk2Wifi

   #. ☐ **Écran branché sur le bon connecteur ?**

      - L’écran doit être branché sur le connecteur **OLED du mk2Wifi**, pas sur celui de la carte principale
      - Le bus I2C du mk2Wifi est **indépendant** de celui de la carte principale

   #. ☐ **Type d’écran compatible ?**

      - Vérifier le contrôleur : SSD1306 ou SH1106
      - L’adresse I2C doit correspondre (typiquement 0x3C ou 0x3D)
      - Vérifier la configuration dans le firmware

   #. ☐ **Brochage correct ?**

      - Ordre des broches : GND, VCC, SCL, SDA
      - VCC = 3,3 V : choisir un écran qui fonctionne en 3,3 V
      - Certains écrans ont un brochage différent — vérifier avant de brancher

Capteur DS18B20 — pas de température
------------------------------------

**Symptôme :** La température n’est pas mesurée malgré un capteur DS18B20 branché

.. admonition:: Liste de contrôle — DS18B20

   #. ☐ **Cavalier TEMP en bonne position ?**

      - En position **3–centre** : le DS18B20 est géré par le mk2Wifi (ESP32-C6). La mesure de température doit alors être désactivée dans le ``config.h`` du routeur (``TEMP_SENSOR_PRESENT`` à ``false``) et le bus déclaré dans le YAML (``one_wire`` sur GPIO23, écrit par le configurateur)
      - En position **1–centre** : le DS18B20 est géré par la carte principale (ATmega328P, broche D3)
      - Voir :ref:`cavaliers`

   #. ☐ **Capteur correctement branché ?**

      - Vérifier la polarité (GND, DATA, VCC)
      - Un branchement inversé peut endommager le capteur

   #. ☐ **Résistance de pull-up présente ?**

      - Le bus 1-Wire nécessite une résistance de pull-up de 4,7 kΩ
      - Elle est déjà sur la carte principale (R6, vers le 3,3 V) : n’en ajoutez pas sur le câble

Obtenir de l’aide
-----------------

Si aucune solution ne fonctionne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ressources communautaires
^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Communauté Facebook :** https://www.facebook.com/groups/3571488193062570

   - Moteur de recherche (problème déjà résolu ?)
   - Poster nouveau sujet avec détails

#. **Email support :** mk2pvrouter.france@gmail.com

   - Temps réponse : 2–5 jours ouvrés

#. **GitHub Issues :**

   - Bugs du firmware : https://github.com/FredM67/PVRouter-3-phase/issues (triphasé) ou https://github.com/FredM67/PVRouter-1-phase/issues (monophasé)
   - Erreurs ou suggestions pour la documentation : https://github.com/FredM67/Mk2PVRouter/issues

Informations à fournir
^^^^^^^^^^^^^^^^^^^^^^

.. important::
 **📞 Pour obtenir une aide efficace, inclure :**

 ☐ **Description détaillée problème**

 - Symptômes observés
 - Quand ça se produit
 - Qu’avez-vous déjà essayé ?

 ☐ **Photos haute résolution**

 - Dessus carte (composants)
 - Dessous carte (soudures)
 - Zones suspectes en gros plan

 ☐ **Mesures électriques**

 - Tensions aux points de test
 - Résistances composants suspects

 ☐ **Messages d’erreur complets**

 - Copier-coller depuis Moniteur Série Arduino IDE
 - Ou capture d’écran

 ☐ **Informations configuration**

 - Version firmware (voir Moniteur Série au démarrage)
 - Configuration (mono/tri, nombre sorties)
 - Système 3,3 V ou 5 V ?

📸 Photos utiles — exemples
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Photo dessus (composants) :**

- Vue d’ensemble carte complète
- Netteté suffisante pour lire références composants
- Éclairage uniforme sans reflets

**Photo dessous (soudures) :**

- Macro sur soudures suspectes
- Toutes soudures visibles (pas de zones d’ombre)
- Angle permettant voir qualité (brillant/terne)

**Photos contexte :**

- Installation dans boîtier
- Câblage complet
- Connexions CT
- Étiquettes équipements

Avant de poster
^^^^^^^^^^^^^^^

**Checklist pré-demande :**

- ☐ J’ai lu toute la section pertinente du guide dépannage
- ☐ J’ai vérifié tous les points de la liste de contrôle
- ☐ J’ai cherché le problème sur forum (peut-être déjà résolu)
- ☐ J’ai préparé photos/mesures/infos nécessaires
- ☐ J’ai relu pour clarté et complétude

.. tip::
 Plus votre demande est précise et documentée, plus rapide sera la résolution !

🛠️ Annexe — Outils de diagnostic essentiels
--------------------------------------------

Multimètre — utilisation de base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mode Tension Continue (V⎓ ou VDC) :**

- Mesurer VCC et les tensions d’alimentation
- Sonde noire sur GND, rouge sur point à mesurer
- Calibres : 20 V pour 3,3 V/5 V, 200 V pour >12 V

**Mode Tension Alternative (V~ ou VAC) :**

- Mesurer 230 V secteur
- ⚠️ Danger haute tension !
- Calibre minimum : 750 V

**Mode Résistance (Ω) :**

- Mesurer les résistances, tester la continuité
- ⚠️ Toujours hors tension !
- Calibres : 200 Ω, 2 kΩ, 20 kΩ, 200 kΩ

**Mode Continuité (♪) :**

- Tester connexions, détecter court-circuits
- Bip si résistance <50 Ω
- Idéal pour vérifier soudures, tracer pistes

Loupe ou microscope USB
~~~~~~~~~~~~~~~~~~~~~~~

**Utilité :**

- Inspecter qualité soudures
- Détecter ponts microscopiques
- Vérifier l’orientation des composants CMS

**Recommandation :**

- Loupe ×5 à ×10 minimum
- Microscope USB 200× pour inspection détaillée
- Éclairage LED intégré essentiel

Oscilloscope (optionnel)
~~~~~~~~~~~~~~~~~~~~~~~~

**Pour diagnostics avancés :**

- Visualiser le signal de commande des étages de sortie, **côté basse tension uniquement** (connecteur Molex de la carte-mère) ; jamais sur la gâchette du triac ni côté puissance : la masse de l’oscilloscope est reliée à la terre
- Vérifier oscillateur ATmega328P
- Analyser les formes d’onde de l’ADC

**Alternative économique :**

- Oscilloscope USB 20 MHz (50–100€)
- Suffisant pour diagnostics DIY

Pince ampèremétrique
~~~~~~~~~~~~~~~~~~~~

**Utilité :**

- Mesurer courant sans couper câble
- Vérifier puissance réelle charge
- Indispensable pour étalonnage

**Spécifications minimum :**

- Plage : 0–20 A AC
- Précision : ±3 %
- Lecture True RMS recommandée

Conclusion
----------

Ce guide de dépannage couvre les problèmes les plus fréquents rencontrés lors de l’assemblage et de l’utilisation du Mk2PVRouter.

.. important::
 **Règles d’or du dépannage :**

 #. Toujours couper l’alimentation avant intervention
 #. Procéder méthodiquement (listes de contrôle)
 #. Prendre photos AVANT toute modification
 #. Au moindre doute : demander de l’aide plutôt que forcer
 #. Un composant coûte moins cher qu’un routeur détruit !

**En cas de doute sérieux :**

- Ne pas prendre de risques avec 230 V
- Faire appel à un électricien qualifié
- Votre sécurité prime sur tout le reste

.. tip::
 💡 **Prévention > Réparation**

 - Vérifier 3 fois avant de souder
 - Tester progressivement (pas tout d’un coup)
 - Noter les modifications (traçabilité)
 - Prendre des pauses (fatigue = erreurs)

Bon courage dans votre dépannage ! 🔧

