.. _troubleshooting-electrique:

*****************************************
⚡ Problèmes Électriques — Tests et Usage
*****************************************

Problèmes d’Alimentation et Tensions
====================================

.. _fusible-grille:

Fusible Saute Immédiatement
---------------------------

.. danger::
 **Un fusible qui fond a fait son travail** : il a coupé une surintensité causée par un défaut (court-circuit, varistance qui conduit, erreur de câblage).

 **NE PAS** remplacer le fusible sans avoir trouvé et corrigé ce défaut : le nouveau fusible fondrait à son tour, et un fusible remplacé par un calibre plus fort ou ponté expose à un incendie.

**Symptôme :** Fusible·s grille(nt) à la mise sous tension

Causes Possibles
~~~~~~~~~~~~~~~~

.. admonition:: Diagnostics court-circuit

   #. ☐ **Erreur de câblage**

      - 400 V entre la borne N et une borne de phase, par exemple une phase raccordée sur la borne N en triphasé
      - Les protections GM1–GM3, montées entre chaque phase et le neutre, conduisent alors et font fondre les fusibles

   #. ☐ **Pont de soudure sur pistes haute tension**

      - Inspecter visuellement avec une loupe
      - Zone 230 V particulièrement critique

   #. ☐ **Condensateur en court-circuit**

      - C1 (condensateur film secteur, entre L1 et N) défectueux
      - Rare mais possible

   #. ☐ **Module PS1 (MPC10-5) défectueux**

      - Peut être en court-circuit si défaut fabrication
      - Ou endommagé par soudure trop chaude

   #. ☐ **Varistance claquée**

      - RV0–RV3 ou GM1–GM3 (tous traversants), souvent après une surtension ou une erreur de câblage

   Les transformateurs :term:`ZMPT101K` (TR1, TR2, TR3) ne sont pas en cause : chacun est alimenté à travers 6 résistances de 20 kΩ en série (environ 2 mA). Même en court-circuit, ils ne peuvent pas faire fondre un fusible de 1 A.

.. note::
   Seuls les composants traversants que vous avez soudés se vérifient et se remplacent. Pour un composant :term:`CMS` défectueux, contactez le support : certains peuvent être réparés.

Procédure de Diagnostic
~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
 Débrancher l’alimentation et attendre 5 minutes avant ces tests !

 Les condensateurs peuvent rester chargés.

#. **Mesurer la résistance entre phase et neutre**, routeur débranché du secteur, fusibles en place

    - Multimètre en mode Ohm (Ω)
    - Mesurer entre les bornes **N** et **L1** du connecteur secteur PWR1 (et entre N et L2, N et L3 en triphasé)
    - Valeur attendue : **> 1 kΩ**
    - Si **< 100 Ω** → Court-circuit présent

#. **Vérifier chaque fusible** (continuité) : FS0 sur le neutre, FS1 à FS3 sur L1 à L3

#. **Inspection visuelle minutieuse**

    - Loupe recommandée
    - Chercher :

      - Traces de brûlure
      - Soudures touchant plusieurs pistes
      - Composants noircis
      - Fils dénudés touchant boîtier métallique

#. **Test par élimination**

    - Dessouder un côté des composants traversants de la chaîne secteur (PS1, C1, GM1–GM3, varistances RV0–RV3), un à la fois
    - Remesurer la résistance après chacun
    - Si le court-circuit disparaît → le dernier composant dessoudé est défectueux
    - Si le court-circuit persiste → problème sur le PCB

#. **Remplacement fusible**

    - Utiliser un fusible identique à celui d’origine (FS0–FS3) : même calibre et même type, marqués sur le fusible (de 0,75 à 1,25 A selon l’approvisionnement)
    - ⚠️ Jamais de fusible plus fort !

Tensions Incorrectes aux Points de Test
---------------------------------------

**Symptôme :** Tensions mesurées différentes des valeurs attendues

Valeurs de Référence
~~~~~~~~~~~~~~~~~~~~

.. list-table:: Tensions normales
 :widths: 30 35 35
 :header-rows: 1

 * - Point de Test
   - Valeur Attendue
   - Tolérance
 * - TP3 « VCC » (+3,3 V)
   - 3,3 V
   - ±0,1 V (3,2–3,4 V)
 * - TP4 « +5V »
   - 5,0 V
   - ±0,2 V (4,8–5,2 V)
 * - VREF (point de test V_REF, firmware lancé)
   - 1,1 V
   - ±0,1 V (1,0–1,2 V)
 * - Entrées ADC A0–A3, et A4–A5 en triphasé si les cavaliers SDA et SCL sont soudés en position 1–centre (repos, firmware lancé)
   - 0,55 V (VREF/2)
   - ±0,05 V (0,50–0,60 V)

Diagnostic par Tension
~~~~~~~~~~~~~~~~~~~~~~

**+3,3 V (TP3) trop faible (< 3,2 V) :**

- Module PS1 (MPC10-5) défectueux, mal orienté ou mal soudé
- Court-circuit partiel consommant trop de courant

**+3,3 V (TP3) trop élevée (> 3,4 V) :**

- ⚠️ **DANGER** pour le module RFM69CW et l’ATmega328P, alimentés par ce rail (cavalier V sel. dans sa position d’usine)
- Régulateur U1 défectueux ou court-circuité
- **COUPER L’ALIMENTATION IMMÉDIATEMENT**

**+5 V (TP4) trop élevée (> 5,2 V) :**

- Module PS1 (MPC10-5) défectueux
- **COUPER L’ALIMENTATION**

**VREF ou entrées ADC à 0 V :**

- Normal tant que le firmware ne tourne pas : c’est lui qui active la référence interne 1,1 V de l’ATmega328P (AREF), que l’amplificateur LMV321A recopie sur VREF. Mesurez VREF et les entrées :term:`ADC` seulement après avoir inséré l’ATmega328P **et** téléversé le firmware.

**Entrées ADC loin de 0,55 V (firmware lancé, VREF correcte) :**

- Pont de soudure dans la zone analogique
- CT branché qui n’est pas à sortie tension 333 mV (un CT à sortie courant sans résistance de :term:`burden <Burden>`)
- Résistance de burden (soudée dans les trous traversants des empreintes des diodes CMS D13 / D23 / D33 ; R18 / R28 / R38 sur le schéma) de mauvaise valeur (solution de dépannage avec un CT à sortie courant, voir :ref:`types-de-capteurs-de-courant-supportes`)

Problèmes d’Étalonnage et Mesures
=================================

Mesures de Puissance Incohérentes
---------------------------------

**Symptôme :** Le routeur affiche des valeurs fantaisistes (très éloignées réalité)

Vérifications CT (Current Transformer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Liste de contrôle — CT

 #. ☐ **CT dans le bon sens ?**

    - Flèche sur CT pointant **vers la maison** (depuis le compteur), comme dans :ref:`installation-finale-connexions`
    - Le contrôle qui fait foi : puissance **positive** quand la maison consomme (import), négative quand elle injecte
    - ⚠️ Si inversé : valeurs négatives ou erronées

 #. ☐ **CT sur la bonne phase ?**

    - Version mono : CT sur phase principale
    - Version tri : CT sur chacune des 3 phases

 #. ☐ **CT bien fermé ?**

    - Le noyau magnétique doit être complètement fermé
    - Pas d’espace/jeu
    - Clip bien enclenché

 #. ☐ **CT sur UN SEUL câble ?**

    - Ne jamais entourer phase + neutre ensemble
    - Annulerait la mesure (courant total = 0)

 #. ☐ **Connexion CT sur PCB correcte ?**

    - Connecteur Molex du CT bien enfoncé sur la carte-mère
    - Pas de faux contact

Vérifications Électroniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Composants de mesure

 #. ☐ **Résistances de burden correctes ?** (uniquement en dépannage, CT à sortie courant)

    - Trous traversants des empreintes des diodes CMS D13 / D23 / D33 (R18 / R28 / R38 sur le schéma), un par CT
    - Uniquement nécessaires avec des CT à sortie courant (ex. : SCT-013-000)
    - Pas nécessaires avec des CT à sortie tension (burden intégré)
    - Valeur calculée selon le CT — voir :ref:`carte-mere-presentation`

 #. ☐ **Pas de pont de soudure autour ADC ?**

    - Zone très sensible
    - Vérifier à la loupe

Valeurs de Référence
~~~~~~~~~~~~~~~~~~~~

**Test de cohérence :** après étalonnage, comparez la puissance affichée par le routeur à une mesure de référence (wattmètre, compteur) avec une charge résistive connue. Un écart de l’ordre de 20 % ou plus indique un problème matériel.

**Causes possibles d’un tel écart :**

- CT défectueux (rare mais possible)
- Burden résistances mauvaise valeur
- Problème ADC du microcontrôleur
- Interférences électromagnétiques (câble CT trop long/près moteur)

Étalonnage ne Converge Pas
--------------------------

**Symptôme :** Impossible d’obtenir valeurs correctes malgré ajustements

**Causes possibles :**

#. **Charge de référence instable**

   - Utiliser une résistance pure (radiateur, chauffe-eau)
   - Pas de charge à découpage (ordinateur, LED)
   - Puissance stable pendant la mesure

#. **Mesure de référence inexacte**

   - Utiliser un appareil de référence fiable (wattmètre, compteur)

#. **Interférences**

   - Variateurs de vitesse moteur
   - Plaques à induction
   - Équipements RF à proximité

**Procédure recommandée :**

#. Couper TOUS les autres appareils
#. Utiliser une charge purement résistive 1 500–2000 W
#. Laisser stabiliser 5 minutes
#. Mesurer avec un instrument calibré
#. Ajuster calibration
#. Vérifier avec une autre charge différente

Problèmes LED et Signalisation
==============================

LED ne s’Allume Jamais
----------------------

**Symptôme :** LED témoin ne s’allume pas malgré routage actif

Vérifications de Base
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Diagnostic LED

 #. ☐ **LED bien soudée ?**

    - Soudures brillantes ?
    - Contact avec pastilles ?

 #. ☐ **LED dans le bon sens ?**

    - Patte longue = Anode (+)
    - Patte courte = Cathode (-)
    - Repère plat sur LED = côté cathode (-)
    - ⚠️ Si inversée : ne s’allumera JAMAIS

 #. ☐ **Résistance série LED présente ?**

    - 1 kΩ (R1 de la carte indicateur)
    - Protège la LED
    - Si absente : LED peut griller

 #. ☐ **Carte sortie triac fonctionne ?**

    - Tester le routage avec une charge
    - Si charge activée mais pas LED → Problème LED/résistance
    - Si charge pas activée → Problème triac (voir section suivante)

Test de la LED
~~~~~~~~~~~~~~

**Test avec pile 9 V et résistance 1 kΩ** (une pile de 3 V n’allume pas une LED bleue ou blanche) :

#. Dessouder LED du PCB
#. Connecter :

   - **+** pile → **Résistance 1 kΩ** → **Anode LED** (patte longue)
   - **-** pile → **Cathode LED** (patte courte)

#. LED doit s’allumer

   - Si oui : LED OK, problème sur PCB
   - Si non : LED grillée, remplacer

LED Toujours Allumée
--------------------

**Symptôme :** LED reste allumée en permanence même sans excédent

**Causes possibles :**

La LED suit le signal de commande de la carte-mère : sur l’étage de sortie, elle est branchée en parallèle de l’entrée de l’:term:`optocoupleur <Optocoupleur>` (connecteurs J2 et J3). Un triac ou un optocoupleur en court-circuit ne l’allume donc pas.

#. **Problème firmware**

   - Entrée de marche forcée active (``OVERRIDE_PIN_PRESENT``), marche forcée programmée en heures creuses (``DUAL_TARIFF``) ou commande depuis Home Assistant via le module mk2Wifi
   - Au démarrage, le moniteur série indique les fonctions présentes : lignes « Override feature is present », « Dual-tariff capability is present »

.. note::
   Si la charge chauffe en permanence alors que la LED est **éteinte**, cherchez côté puissance : triac en court-circuit (mesurez MT1-MT2 hors tension), ou contacteur heures creuses câblé en parallèle de l’étage de sortie et resté fermé.

LED Clignote Bizarrement
------------------------

**Symptôme :** Comportement LED inattendu

.. list-table:: Diagnostic comportement LED
 :widths: 40 30 30
 :header-rows: 1

 * - Comportement
   - Signification
   - Action
 * - Éteinte en permanence
   - Pas d’excédent OU routeur non fonctionnel
   - Vérifier la production solaire et le moniteur série
 * - Allumée en permanence
   - Sortie commandée à pleine puissance
   - Normal avec un fort excédent ; le thermostat peut couper la charge sans éteindre la LED
 * - Allumée la plupart du temps
   - Beaucoup d’excédent routé
   - Normal en pleine production
 * - Allumée une petite partie du temps
   - Peu d’excédent routé
   - Normal début/fin journée

🔥 Problèmes de Routage — Charge ne Chauffe Pas
===============================================

Routeur Fonctionne mais Charge Pas Alimentée
--------------------------------------------

**Symptôme :** LEDs actives, routeur semble fonctionner, mais charge froide

Vérifications Triac
~~~~~~~~~~~~~~~~~~~

.. danger::
 Manipulation haute tension ! Couper le disjoncteur avant intervention.

.. admonition:: Diagnostic étage de puissance

 #. ☐ **Triac bien vissé sur le dissipateur ?**

    - Bon contact thermique (isolant, pâte), **sans** contact électrique
    - Pas de jeu mécanique

 #. ☐ **Isolant électrique présent ?**

    - Mica ou silicone entre triac et dissipateur
    - Évite court-circuit (dissipateur relié terre)

 #. ☐ **Vis triac bien serrée ?**

    - Couple serrage important pour contact thermique
    - Pas trop serré (risque fissure boîtier triac)

 #. ☐ **Pâte thermique appliquée ?**

    - Mince couche uniforme
    - Améliore transfert thermique

 #. ☐ **Câblage haute puissance correct ?**

    - **Phase** sur les deux broches **extérieures** du connecteur de puissance : entrée depuis le disjoncteur de la charge, sortie vers la charge
    - Broche **centrale** inutilisée
    - **Neutre** relié directement à la charge : il ne passe **jamais** par l’étage de sortie (un neutre sur ce connecteur met le triac en court-circuit entre phase et neutre)
    - Vis bornier bien serrées
    - Voir :ref:`raccordement-etages-sortie`

Test du Triac
~~~~~~~~~~~~~

**Mesure à froid (hors tension) :**

#. Couper l’alimentation
#. Multimètre en mode Ohm (Ω)
#. Mesurer la résistance MT1-MT2 :

   - Doit être **> 1 MΩ** (quasi ouvert)
   - Si < 100 Ω → Triac en court-circuit (détruit)

**Test fonctionnel (sous tension) :**

.. danger::
 Manipulations haute tension ! Compétences électriques requises.

#. Connecter voltmètre aux bornes charge
#. Mettre routeur sous tension avec excédent
#. Observer tension :

   - Doit être ~230 V RMS quand LED active
   - Doit être ~0 V quand LED éteinte
   - Si toujours 0 V → Triac ne conduit pas
   - Si toujours 230 V → Triac bloqué ON (défectueux)

**Signal de commande (côté basse tension uniquement) :**

.. danger::
   Ne mesurez **jamais** sur la gâchette (gate) du :term:`triac <Triac>` ni sur aucun point du côté puissance de l’étage de sortie : ils sont au potentiel du secteur. La masse d’un oscilloscope est reliée à la terre ; la brancher à cet endroit provoque un court-circuit, et la sonde devient dangereuse au toucher.

#. Multimètre en mode tension continue (V⎓) sur le connecteur Molex de commande, **côté carte-mère** : pointe noire sur la broche 1 (GND), pointe rouge sur la broche 2 (signal)
#. En fonctionnement :

   - ~0 V quand la charge doit être coupée
   - ~3,3 V quand la charge doit être alimentée à pleine puissance
   - Valeur intermédiaire et fluctuante en régime partiel (le multimètre affiche la moyenne des commutations)
   - Signal présent mais charge jamais alimentée → étage de sortie (optocoupleur, triac) ou câblage de puissance
   - Jamais de signal → sortie de la carte-mère, configuration du firmware (broche) ou câble Molex

Vérifications Charge
~~~~~~~~~~~~~~~~~~~~

**Chauffe-eau :**

- ☐ Thermostat non déclenché ? (température max atteinte)
- ☐ Thermostat pas coupé manuellement ?
- ☐ Résistance chauffe-eau fonctionnelle ?

  - Tester résistance : doit être ~25–30 Ω pour 2 000 W
  - Si infinie → Résistance coupée/brûlée

**Radiateur électrique :**

- ☐ Interrupteur radiateur allumé ?
- ☐ Thermostat radiateur pas en position MIN ?

**Test charge indépendamment :**

#. Couper le disjoncteur de la charge
#. Déconnecter la charge de l’étage de sortie
#. Mesurer sa résistance (voir ci-dessus) ; ne branchez pas un chauffe-eau sur une prise improvisée
#. Si la résistance est infinie → Problème charge, pas routeur

Triac Surchauffe
----------------

**Symptôme :** Dissipateur très chaud (>60 °C au toucher)

.. warning::
 Surchauffe = risque de destruction du triac et incendie !

**Causes possibles :**

#. **Puissance de la charge trop élevée**

   - Les dissipateurs fournis sont dimensionnés pour un **maximum de 3 kW**
   - Vérifier que la charge connectée ne dépasse pas cette limite
   - Exemples :

     - ✅ Chauffe-eau 2 000–3000 W : OK
     - ✅ Radiateur électrique 2 000 W : OK
     - ❌ Charge >3 kW : Dépasse les spécifications !

#. **Dissipateur mal orienté**

   - ⚠️ **IMPORTANT** : Le dissipateur **DOIT être en position verticale**
   - Permet la convection naturelle de l’air
   - Si horizontal : refroidissement insuffisant → surchauffe

   .. note::
      Les dissipateurs sont vissés sur l’**extérieur** du boîtier.
      Aucun trou de ventilation n’est nécessaire dans le boîtier.

#. **Contact thermique insuffisant**

   - Pâte thermique absente/mal appliquée
   - Vissage insuffisant
   - Surface du dissipateur pas plane
   - Isolant électrique (mica/silicone) mal positionné

**Solutions :**

- Vérifier que la charge ≤ 3 kW (mesurer avec pince ampèremétrique)
- **S’assurer que le dissipateur est vertical**
- Améliorer le contact thermique (pâte, serrage correct)
- Si charge >3 kW : répartir la puissance sur plusieurs étages de sortie, uniquement si la charge a plusieurs résistances, chacune sur son propre étage (jamais deux triacs en parallèle sur une même résistance), ou réduire la puissance de la charge


💻 Problèmes de Communication RF
================================

Module RF ne Répond Pas
-----------------------

**Symptôme :** Pas de communication radio (si module RF installé)

.. note::
 Cette section concerne uniquement les kits avec module RF optionnel.

Vérifications Matérielles
~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Diagnostic module RF

 #. ☐ **Module RF bien soudé/enfiché ?**

    - Toutes broches en contact ?
    - Orientation correcte ?

 #. ☐ **Cavaliers IRQ et NSS soudés ?**

    - Les cavaliers à souder JP3 « IRQ » (vers D2) et JP41 « NSS » (vers D10) sont ouverts par défaut : soudez-les pour relier le module RF (voir :ref:`cavaliers`)

 #. ☐ **Antenne connectée ?**

    - Antenne 433 ou 868 MHz (selon le module) vissée sur le connecteur SMA **CN1** de la carte-mère

 #. ☐ **Firmware compilé avec RF activé ?**

    - Le module radio est utilisé si ``RF_LOGGING_PRESENT`` vaut ``true`` dans ``config.h``, ou si des charges distantes sont déclarées (``Load::remote()``)
    - La fréquence (``FREQUENCY`` dans ``config_rf.h``) doit correspondre au module, et ``NETWORK_ID`` être le même sur tous les appareils
    - Recompiler et téléverser si nécessaire

 #. ☐ **Messages RF dans Moniteur Série ?**

    - Au démarrage : « RF capability IS present, Freq = 868 MHz » (ou 433 MHz), puis « RF module initialized »
    - Si « RF module initialization FAILED » → module absent, non alimenté ou mal soudé ; le firmware retente l’initialisation à chaque période de datalog

Dépannage Communication
~~~~~~~~~~~~~~~~~~~~~~~

**Problèmes fréquents :**

- Carte passée en 5 V (cavalier V sel.) : aucun module RF ne peut y fonctionner. Une carte équipée d’un module RF reste en 3,3 V, position d’usine de V sel. ; ce point est vérifié à la commande
- Interférences (éloigner de charges puissance)

