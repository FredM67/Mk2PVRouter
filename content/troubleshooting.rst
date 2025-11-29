.. _troubleshooting:

*********************
🔧 Guide de Dépannage
*********************

Ce chapitre vous aide à diagnostiquer et résoudre les problèmes courants rencontrés lors de l’assemblage et de l’utilisation du Mk2PVRouter.

.. important::
 **Avant de commencer le dépannage :**

 - Toujours **couper l’alimentation** au disjoncteur avant toute intervention
 - Vérifier l’absence de tension avec un testeur
 - Prendre des photos avant de modifier quoi que ce soit
 - Noter tous les symptômes observés

.. contents:: Sections du guide de dépannage
 :local:
 :depth: 2

==============================
📋 Différences Mono/Tri Phases
==============================

Ce guide couvre les versions **monophasée** et **triphasée** du Mk2PVRouter.

.. list-table:: Composants selon la version
 :widths: 40 30 30
 :header-rows: 1

 * - Composant
   - Monophasé
   - Triphasé
 * - Fusibles
   - FS1
   - FS1, FS2, FS3
 * - Transformateurs
   - TXFR1
   - TXFR1, TXFR2, TXFR3
 * - Ponts redresseurs
   - BR1
   - BR1, BR2, BR3
 * - Régulateur 3.3 V/5 V
   - VR1
   - VR1 (commun)
 * - Capteurs de courant (CT)
   - 1 CT (phase principale)
   - 3 CT (un par phase)
 * - Sorties triac
   - 1 ou plusieurs
   - 3 ou plus (selon modèle)

.. note::
 Dans ce guide, les instructions utilisent la notation :

 - **Mono :** composants pour version monophasée
 - **Tri :** composants pour version triphasée

======================================
🔌 Problèmes Après Soudure de la Carte
======================================

La Carte ne s’Allume Pas
========================

**Symptôme :** Pas de tension aux points de test, aucun signe de vie

Vérifications de Base
---------------------

Effectuez ces vérifications dans l’ordre :

.. admonition:: Liste de contrôle — Alimentation

 #. ☐ L’alimentation secteur est-elle branchée ?
 #. ☐ Le disjoncteur est-il enclenché ?
 #. ☐ **Fusibles intacts ?**

    - Mono : FS1
    - Tri : FS1, FS2, FS3
    - Vérifier avec multimètre en mode continuité
    - Un fusible grillé indique un court-circuit

 #. ☐ Tension au point Test VCC = 3.3 V ou 5 V ?

    - Multimètre en mode tension continue (DC)
    - Mesurer entre VCC et GND
    - Si pas de tension → Problème alimentation

Si Pas de Tension au Test VCC
-----------------------------

.. danger::
 **COUPER L’ALIMENTATION** avant toute vérification de composants !

Vérifier les composants d’alimentation :

.. admonition:: Composants à vérifier

 #. ☐ **Pont(s) redresseur(s) dans le bon sens ?**

    - Mono : BR1
    - Tri : BR1, BR2, BR3
    - Repérer la bande ou marquage sur la diode

 #. ☐ **Régulateur VR1** dans le bon sens ?

    - Vérifier l'orientation selon le schéma
    - Les 3 pattes doivent correspondre (E-C-B ou G-S-D)

 #. ☐ **Condensateurs C1/C2** polarité correcte ?

    - Bande blanche = côté négatif (-)
    - Vérifier marquage sur PCB
    - ⚠️ Si inversés : risque d’explosion à la mise sous tension !

 #. ☐ **Transformateur(s) bien soudé(s) ?**

    - Mono : TXFR1
    - Tri : TXFR1, TXFR2, TXFR3
    - Soudures brillantes et lisses (pas ternes) ?

Qualité des Soudures
--------------------

.. figure:: img/soudure-bonne-vs-mauvaise.png
 :align: center
 :alt: Comparaison soudure bonne vs mauvaise

 Exemples de bonnes et mauvaises soudures

**Caractéristiques d’une bonne soudure :**

- ✅ Aspect brillant et lisse
- ✅ Forme de volcan (concave)
- ✅ Mouille à la fois la patte et la pastille
- ✅ Pas de boule séparée

**Soudure froide (défectueuse) :**

- ❌ Aspect terne, granuleux
- ❌ Soudure en boule qui ne mouille pas
- ❌ Fissures visibles
- ❌ Contact électrique mauvais ou inexistant

**Solution :** Refaire les soudures suspectes :

#. Chauffer à nouveau avec fer à souder (350 °C)
#. Ajouter un peu de flux si disponible
#. Ajouter un peu de soudure fraîche
#. Laisser refroidir sans bouger

Pont de Soudure (Court-Circuit)
-------------------------------

**Symptôme :** Deux pistes ou broches reliées par erreur

.. figure:: img/pont-de-soudure.png
 :align: center
 :alt: Exemple de pont de soudure

 Pont de soudure entre deux broches

**Détection :**

- Inspection visuelle avec une loupe
- Multimètre en mode continuité entre broches qui ne devraient pas être connectées

**Solution — Retrait avec tresse à dessouder :**

#. Placer tresse à dessouder sur le pont
#. Appliquer fer à souder sur la tresse
#. La soudure est absorbée par capillarité
#. Répéter si nécessaire avec section propre de tresse

**Alternative — Retrait avec pompe à dessouder :**

#. Chauffer le pont avec fer à souder
#. Approcher la pompe
#. Activer la pompe (aspiration)
#. Nettoyer et recommencer si nécessaire

Si Tension Correcte mais Pas de Fonctionnement
----------------------------------------------

.. admonition:: Vérifications microcontrôleur

 #. ☐ **ATmega328** bien inséré dans le support ?

 - Toutes les pattes dans les trous ?
 - Pas de patte pliée sous le boîtier ?

 #. ☐ **ATmega328** dans le bon sens ?

 - ⚠️ **CRITIQUE** : Encoche alignée avec marquage PCB ?
 - Si inversé → **Puce détruite à la mise sous tension !**
 - Vérifier 3 fois avant d’alimenter

 #. ☐ **Firmware programmé ?**

 - Voir la section :ref:`test-logiciel-mono` ou :ref:`test-logiciel-tri`
 - ATmega328 vierge ne fait rien

Causes Fréquentes — Résumé
--------------------------

.. list-table::
 :widths: 30 40 30
 :header-rows: 1

 * - Symptôme
   - Cause Probable
   - Solution
 * - Aucune tension VCC
   - Fusible grillé
   - Trouver le court-circuit, remplacer le fusible
 * - Tension VCC faible (<3 V)
   - Régulateur défectueux
   - Vérifier l'orientation, remplacer
 * - Tension OK, rien ne fonctionne
   - ATmega328 mal inséré/inversé
   - Vérifier l'orientation, réinsérer
 * - Soudures ternes
   - Soudure froide
   - Refaire les soudures avec plus de chaleur

======================================
Problèmes de Programmation du Firmware
======================================

Le Firmware ne se Téléverse Pas
===============================

**Symptôme :** Erreur dans Arduino IDE lors du téléversement

.. code-block:: text

 avrdude: stk500_recv(): programmer is not responding
 avrdude: stk500_getsync() attempt 1 of 10: not in sync

Vérifications de la Connexion FTDI
----------------------------------

.. admonition:: Liste de contrôle — Connexion FTDI

 #. ☐ **Câblage FTDI correct ?**

    - **GND (noir)** → **GND** sur PCB
    - **TX (vert)** → **RX** sur PCB
    - **RX (blanc)** → **TX** sur PCB
    - ⚠️ **NE PAS** connecter VCC si routeur alimenté !

 #. ☐ **ATmega328 bien inséré ?**

    - Toutes les pattes dans le support ?
    - Orientation correcte (encoche) ?

 #. ☐ **Routeur alimenté en 230 V ?**

    - Le FTDI ne fournit **PAS** assez de courant
    - Alimentation secteur obligatoire

 #. ☐ **Bon port COM sélectionné dans Arduino IDE ?**

    - Menu : Outils → Port → COMX
    - Essayer chaque port disponible

 #. ☐ **Pilotes FTDI installés ?**

    - Télécharger les pilotes sur ftdichip.com
    - Windows : Gestionnaire de périphériques doit montrer « USB Serial Port »
    - Linux : ``dmesg | grep tty`` doit montrer nouveau périphérique

Problèmes Port USB Windows
--------------------------

**Symptôme :** Port COM n’apparaît pas dans Arduino IDE

**Solutions :**

#. **Vérifier Gestionnaire de périphériques**

 - Ouvrir : Panneau de configuration → Gestionnaire de périphériques
 - Chercher : « Ports (COM et LPT) »
 - Doit afficher : « USB Serial Port (COMx) »
 - Si point d’exclamation jaune → Pilote problématique

#. **Réinstaller pilotes FTDI**

 - Désinstaller pilote actuel (clic droit → Désinstaller)
 - Débrancher FTDI
 - Redémarrer ordinateur
 - Rebrancher FTDI
 - Windows devrait installer automatiquement

#. **Essayer autre port USB**

 - Certains ports USB peuvent avoir problèmes
 - Préférer ports USB directs (pas hub)

Problèmes Arduino IDE
---------------------

.. admonition:: Configuration Arduino IDE

 #. ☐ **Type de carte correct ?**

    - Menu : Outils → Type de carte → **Arduino Uno**
    - Pas Arduino Nano, pas Mega

 #. ☐ **Processeur correct ?** (si option disponible)

    - ATmega328P

 #. ☐ **Vitesse correcte ?**

    - 9600 bauds pour Moniteur Série

**Solutions supplémentaires :**

- Fermer et rouvrir Arduino IDE
- Débrancher/rebrancher FTDI
- Essayer sur autre ordinateur (test matériel vs logiciel)

Firmware se Téléverse mais Rien ne Fonctionne
=============================================

**Symptôme :** Téléversement réussi mais routeur inactif

Vérification via Moniteur Série
-------------------------------

#. **Ouvrir Moniteur Série**

   - Menu : Outils → Moniteur série
   - Ou raccourci : Ctrl+Maj+M

#. **Régler paramètres en bas à droite :**

   - **Baud rate :** 9600
   - **Line ending :** « Les deux, NL & CR »

#. **Appuyer sur bouton Reset du routeur**

#. **Vous devriez voir :**

   .. code-block:: text

      Mk2PVRouter v3.1 — Mono
      Initialisation...
      CT1: 0 W
      CT2: 0 W
      Sortie 1: OFF

**Si pas de messages :**

.. admonition:: Diagnostics oscillateur

 Le microcontrôleur nécessite un oscillateur pour fonctionner.

 #. ☐ **Quartz/résonateur bien soudé ?**

    - Composant à 2 pattes près de l’ATmega328
    - Soudures correctes ?

 #. ☐ **Condensateurs C6/C7 présents ?** (si quartz externe)

    - Condensateurs 22pF de chaque côté du quartz
    - Valeur correcte ?

**Si messages bizarres/illisibles :**

- Vérifier que le baud rate = 9600
- Si toujours illisible → Problème oscillateur (fréquence incorrecte)

Erreur « Out of Memory » lors de la Compilation
===============================================

**Symptôme :**

.. code-block:: text

 Sketch too big; see https://support.arduino.cc/hc/en-us/articles/360013825179

**Cause :** Trop de fonctionnalités activées dans config.h

**Solution :**

#. Ouvrir onglet ``config.h`` dans Arduino IDE
#. Désactiver fonctionnalités non nécessaires :

   .. code-block:: cpp

      // Commenter les lignes avec //
      // #define ENABLE_DEBUG // Désactive messages debug
      // #define ENABLE_RF_MODULE // Désactive module RF
      // #define ENABLE_RELAY_OUTPUT // Si que sorties triac

#. Recompiler et téléverser

=========================================
⚡ Problèmes Électriques — Tests et Usage
=========================================

Fusible Saute Immédiatement
===========================

.. danger::
 **DANGER — COURT-CIRCUIT PRÉSENT !**

 **NE PAS** remplacer le fusible sans trouver la cause !

 Un fusible qui saute protège contre incendie/destruction.
 Remplacer sans diagnostic = risque d’incendie.

**Symptôme :** Fusible·s grille(nt) à la mise sous tension

Causes Possibles
----------------

.. admonition:: Diagnostics court-circuit

 #. ☐ **Court-circuit dans transformateur(s)**

    - Mono : TXFR1
    - Tri : TXFR1, TXFR2, TXFR3

 - Mesurer la résistance des enroulements (doit être ~1-10 kΩ)
 - Si <10 Ω → Transformateur défectueux

 #. ☐ **Pont de soudure sur pistes haute tension**

 - Inspecter visuellement avec une loupe
 - Zone 230 V particulièrement critique

 #. ☐ **Condensateur en court-circuit**

 - C1 ou C2 défectueux
 - Rare mais possible

 #. ☐ **Régulateur VR1 défectueux**

 - Peut être en court-circuit si défaut fabrication
 - Ou endommagé par soudure trop chaude

Procédure de Diagnostic
-----------------------

.. danger::
 Débrancher l’alimentation et attendre 5 minutes avant ces tests !

 Les condensateurs peuvent rester chargés.

#. **Retirer le fusible**

#. **Mesurer la résistance entre phase et neutre**

    - Multimètre en mode Ohm (Ω)
    - Mesurer à l’entrée du transformateur
    - Valeur attendue : **> 1 kΩ**
    - Si **< 100 Ω** → Court-circuit présent

#. **Inspection visuelle minutieuse**

    - Loupe recommandée
    - Chercher :

      - Traces de brûlure
      - Soudures touchant plusieurs pistes
      - Composants noircis
      - Fils dénudés touchant boîtier métallique

#. **Test par élimination**

    - Dessouder un côté du/des transformateur·s (TXFR1 pour mono, ou TXFR1/TXFR2/TXFR3 pour tri)
    - Remesurer résistance
    - Si court-circuit persiste → Problème sur PCB
    - Si disparaît → Transformateur défectueux

#. **Remplacement fusible**

    - Utiliser **même valeur** que fusible d’origine
    - Type : temporisé (slow-blow) recommandé
    - ⚠️ Jamais de fusible plus fort !

Tensions Incorrectes aux Points de Test
=======================================

**Symptôme :** Tensions mesurées différentes des valeurs attendues

Valeurs de Référence
--------------------

.. list-table:: Tensions normales
 :widths: 30 35 35
 :header-rows: 1

 * - Point de Test
   - Valeur Attendue
   - Tolérance
 * - VCC (3.3 V)
   - 3.3 V
   - ±0.2 V (3.1-3.5 V)
 * - VCC (5 V)
   - 5.0 V
   - ±0.3 V (4.7-5.3 V)
 * - Sortie ADC (repos)
   - VCC/2
   - ±0.5 V
 * - Gate triac (actif)
   - ~2-5 V (pulsé)
   - Variable

Diagnostic par Tension
----------------------

**VCC trop faible (<3 V pour système 3.3 V) :**

- Régulateur VR1 défectueux ou mal orienté
- Court-circuit partiel consommant trop de courant
- Transformateur sous-dimensionné (mauvaise référence)

**VCC trop élevée (>5.5 V) :**

- ⚠️ **DANGER** pour ATmega328 (max absolu = 6 V)
- Régulateur absent ou court-circuité
- **COUPER L'ALIMENTATION IMMÉDIATEMENT**

**Tension ADC incorrecte (pas à VCC/2) :**

- Résistances R8/R9 (burden résistors) mauvaise valeur
- Condensateurs C11/C12/C13 défectueux
- Pont de soudure dans zone analogique

=================================
Problèmes d’Étalonnage et Mesures
=================================

Mesures de Puissance Incohérentes
=================================

**Symptôme :** Le routeur affiche des valeurs fantaisistes (très éloignées réalité)

Vérifications CT (Current Transformer)
--------------------------------------

.. admonition:: Liste de contrôle — CT

 #. ☐ **CT dans le bon sens ?**

    - Flèche sur CT doit pointer vers **source** (compteur/disjoncteur)
    - Pas vers la charge
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

    - Connecteur jack bien enfoncé
    - Pas de faux contact

Vérifications Électroniques
---------------------------

.. admonition:: Composants de mesure

 #. ☐ **Burden résistances correctes ?**

    - R8/R9 : Typiquement 120 Ω pour système 3.3 V
    - Vérifier la valeur avec un multimètre
    - Code couleur : Marron-Rouge-Marron-Or = 120 Ω

 #. ☐ **Condensateurs C11/C12/C13 bien soudés ?**

    - Forment filtre passe-bas anti-repliement
    - Valeurs typiques : 10nF ou 100nF

 #. ☐ **Pas de pont de soudure autour ADC ?**

    - Zone très sensible
    - Vérifier à la loupe

Valeurs de Référence
--------------------

**Test de cohérence :**

.. list-table:: Tests de validation mesures
 :widths: 40 30 30
 :header-rows: 1

 * - Condition
   - Valeur Attendue
   - Tolérance
 * - Sans charge (0 W réel)
   - 0 W ±10 W
   - Normal
 * - Avec charge 2000 W
   - 1900-2100 W
   - ±5% après étalonnage
 * - Production 3000 W
   - 2850-3150 W
   - ±5%
 * - Écart >20%
   - Problème matériel
   - À investiguer

**Si écart >20% après étalonnage :**

- CT défectueux (rare mais possible)
- Burden résistances mauvaise valeur
- Problème ADC du microcontrôleur
- Interférences électromagnétiques (câble CT trop long/près moteur)

Étalonnage ne Converge Pas
==========================

**Symptôme :** Impossible d’obtenir valeurs correctes malgré ajustements

**Causes possibles :**

#. **Charge de référence instable**

 - Utiliser une résistance pure (radiateur, chauffe-eau)
 - Pas de charge à découpage (ordinateur, LED)
 - Puissance doit être stable ±2%

#. **Mesure de référence inexacte**

 - Pince ampèremétrique : ±3% précision minimum
 - Wattmètre : Classe 1 minimum
 - Multimètre basique insuffisant

#. **Interférences**

 - Variateurs de vitesse moteur
 - Plaques à induction
 - Équipements RF à proximité

**Procédure recommandée :**

#. Couper TOUS les autres appareils
#. Utiliser une charge purement résistive 1500-2000 W
#. Laisser stabiliser 5 minutes
#. Mesurer avec un instrument calibré
#. Ajuster calibration
#. Vérifier avec une autre charge différente

==============================
Problèmes LED et Signalisation
==============================

LED ne s’Allume Jamais
======================

**Symptôme :** LED témoin ne s’allume pas malgré routage actif

Vérifications de Base
---------------------

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

    - Typiquement 220 Ω ou 470 Ω
    - Protège la LED
    - Si absente : LED peut griller

 #. ☐ **Carte sortie triac fonctionne ?**

    - Tester le routage avec une charge
    - Si charge activée mais pas LED → Problème LED/résistance
    - Si charge pas activée → Problème triac (voir section suivante)

Test de la LED
--------------

**Test avec pile 3 V (2× AA/AAA) :**

#. Dessouder LED du PCB
#. Connecter :

   - **+** pile → **Résistance 220 Ω** → **Anode LED** (patte longue)
   - **-** pile → **Cathode LED** (patte courte)

#. LED doit s’allumer

   - Si oui : LED OK, problème sur PCB
   - Si non : LED grillée, remplacer

LED Toujours Allumée
====================

**Symptôme :** LED reste allumée en permanence même sans excédent

**Causes possibles :**

#. **Triac en court-circuit**

   - Triac défectueux ou détruit
   - Mesurer la résistance MT1-MT2 (doit être >1 MΩ à froid)

#. **Opto-coupleur défectueux**

   - MOC3041/MOC3043 en court-circuit
   - Remplacer le composant

#. **Problème firmware**

   - Sortie forcée ON dans configuration
   - Vérifier le Moniteur Série Arduino IDE
   - Commandes de test actives ?

LED Clignote Bizarrement
========================

**Symptôme :** Comportement LED inattendu

.. list-table:: Diagnostic comportement LED
 :widths: 40 30 30
 :header-rows: 1

 * - Comportement
   - Signification
   - Action
 * - Toutes éteintes permanent
   - Pas d’excédent OU routeur non fonctionnel
   - Vérifier la production solaire et le moniteur série
 * - Toutes allumées permanent
   - Excédent max OU charge saturée
   - Normal si chauffe-eau à température
 * - Clignotement très rapide (<0.5s)
   - Beaucoup d’excédent (80-100%)
   - Normal en pleine production
 * - Clignotement lent (>2s)
   - Peu d’excédent (10-30%)
   - Normal début/fin journée
 * - Clignotement erratique
   - Mesures instables
   - Vérifier le CT et l'étalonnage

===============================================
🔥 Problèmes de Routage — Charge ne Chauffe Pas
===============================================

Routeur Fonctionne mais Charge Pas Alimentée
============================================

**Symptôme :** LEDs actives, routeur semble fonctionner, mais charge froide

Vérifications Triac
-------------------

.. danger::
 Manipulation haute tension ! Couper le disjoncteur avant intervention.

.. admonition:: Diagnostic étage de puissance

 #. ☐ **Triac bien soudé sur dissipateur ?**

    - Contact thermique ET électrique
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

    - **Phase** sur borne **L**
    - **Neutre** sur borne **N**
    - Vis bornier bien serrées

Test du Triac
-------------

**Mesure à froid (hors tension) :**

#. Couper l'alimentation
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

**Mesure signal gate :**

#. Oscilloscope ou multimètre AC sur gate triac
#. En fonctionnement :

   - Doit montrer impulsions 2-5 V
   - Fréquence 50/100 Hz (burst fire)
   - Si pas d’impulsions → Problème opto-coupleur ou routage signal

Vérifications Charge
--------------------

**Chauffe-eau :**

- ☐ Thermostat non déclenché ? (température max atteinte)
- ☐ Thermostat pas coupé manuellement ?
- ☐ Résistance chauffe-eau fonctionnelle ?

 - Tester résistance : doit être ~25-30 Ω pour 2000 W
 - Si infinie → Résistance coupée/brûlée

**Radiateur électrique :**

- ☐ Interrupteur radiateur allumé ?
- ☐ Thermostat radiateur pas en position MIN ?

**Test charge indépendamment :**

#. Déconnecter charge du routeur
#. Brancher directement sur prise secteur
#. Vérifier le fonctionnement
#. Si charge ne chauffe pas → Problème charge, pas routeur

Triac Surchauffe
================

**Symptôme :** Dissipateur très chaud (>60 °C au toucher)

.. warning::
 Surchauffe = risque de destruction du triac et incendie !

**Causes possibles :**

#. **Dissipateur sous-dimensionné**

   - Surface minimum requise selon puissance :

     - 500 W : 50 cm²
     - 1000 W : 100 cm²
     - 2000 W : 200 cm²
     - 3000 W : 300 cm²

#. **Contact thermique insuffisant**

   - Pâte thermique absente/mal appliquée
   - Vissage insuffisant
   - Surface dissipateur pas plane

#. **Ventilation insuffisante**

   - Boîtier trop confiné
   - Ajouter trous ventilation
   - Dissipateur orienté pour convection naturelle

**Solutions :**

- Ajouter dissipateur plus grand
- Améliorer contact thermique (pâte, serrage)
- Ajouter ventilation forcée (ventilateur 12 V)
- Réduire puissance charge si possible

================================
💻 Problèmes de Communication RF
================================

Module RF ne Répond Pas
=======================

**Symptôme :** Pas de communication radio (si module RF installé)

.. note::
 Cette section concerne uniquement les kits avec module RF optionnel.

Vérifications Matérielles
-------------------------

.. admonition:: Diagnostic module RF

 #. ☐ **Module RF bien soudé/enfiché ?**

    - Toutes broches en contact ?
    - Orientation correcte ?

 #. ☐ **Antenne connectée ?**

    - Module 433 MHz : antenne filaire 17 cm
    - Module 868 MHz : antenne filaire 8.6 cm

 #. ☐ **Firmware compilé avec RF activé ?**

    - Dans ``config.h`` : ``#define ENABLE_RF_MODULE``
    - Recompiler et téléverser si nécessaire

 #. ☐ **Messages RF dans Moniteur Série ?**

    - Doit afficher : « RF initialized » au démarrage
    - Si « RF init failed » → Problème communication

Dépannage Communication
-----------------------

**Test émetteur :**

#. Ouvrir Moniteur Série (115200 bauds)
#. Forcer émission commande test
#. Observer messages debug

**Problèmes fréquents :**

- Mauvaise broche SPI (vérifier schéma)
- Module 3.3 V alimenté en 5 V (destruction possible)
- Interférences (éloigner de charges puissance)

=================
Obtenir de l’Aide
=================

Si Aucune Solution ne Fonctionne
================================

Ressources Communautaires
-------------------------

#. **Forum communauté :** https://forum.example.com/mk2pvrouter

 - Moteur de recherche (problème déjà résolu ?)
 - Poster nouveau sujet avec détails

#. **Email support :** support@example.com

 - Temps réponse : 2-5 jours ouvrés

#. **GitHub Issues :** https://github.com/user/Mk2PVRouter/issues

 - Pour bugs firmware
 - Améliorations suggestions

Informations à Fournir
----------------------

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
 - Version kit (mono/tri, nombre sorties)
 - Système 3.3 V ou 5 V ?

📸 Photos Utiles — Exemples
---------------------------

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

Avant de Poster
---------------

**Checklist pré-demande :**

- ☐ J’ai lu toute la section pertinente du guide dépannage
- ☐ J’ai vérifié tous les points de la liste de contrôle
- ☐ J’ai cherché le problème sur forum (peut-être déjà résolu)
- ☐ J’ai préparé photos/mesures/infos nécessaires
- ☐ J’ai relu pour clarté et complétude

.. tip::
 Plus votre demande est précise et documentée, plus rapide sera la résolution !

============================================
🛠️ Annexe — Outils de Diagnostic Essentiels
============================================

Multimètre — Utilisation de Base
================================

**Mode Tension Continue (V⎓ ou VDC) :**

- Mesurer VCC et les tensions d'alimentation
- Sonde noire sur GND, rouge sur point à mesurer
- Calibres : 20 V pour 3.3 V/5 V, 200 V pour >12 V

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

Loupe ou Microscope USB
=======================

**Utilité :**

- Inspecter qualité soudures
- Détecter ponts microscopiques
- Vérifier l'orientation des composants CMS

**Recommandation :**

- Loupe ×5 à ×10 minimum
- Microscope USB 200× pour inspection détaillée
- Éclairage LED intégré essentiel

Oscilloscope (Optionnel)
========================

**Pour diagnostics avancés :**

- Visualiser signal gate triac
- Vérifier oscillateur ATmega328
- Analyser formes d’ondes ADC

**Alternative économique :**

- Oscilloscope USB 20 MHz (50-100€)
- Suffisant pour diagnostics DIY

Pince Ampèremétrique
====================

**Utilité :**

- Mesurer courant sans couper câble
- Vérifier puissance réelle charge
- Indispensable pour étalonnage

**Spécifications minimum :**

- Plage : 0-20 A AC
- Précision : ±3%
- Lecture True RMS recommandée

==========
Conclusion
==========

Ce guide de dépannage couvre les problèmes les plus fréquents rencontrés lors de l’assemblage et de l’utilisation du Mk2PVRouter.

.. important::
 **Règles d’or du dépannage :**

 #. Toujours couper l’alimentation avant intervention
 #. Procéder méthodiquement (listes de contrôle)
 #. Prendre photos AVANT toute modification
 #. Si doute : demander aide plutôt que forcer
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
