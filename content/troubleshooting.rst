.. _troubleshooting:

*******************
Guide de Dépannage
*******************

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

==========================================
📋 Composants selon la configuration
==========================================

Ce guide couvre la carte universelle **3phaseDiverter** du Mk2PVRouter.

.. list-table:: Composants selon la version
 :widths: 40 30 30
 :header-rows: 1

 * - Composant
   - Monophasé
   - Triphasé
 * - Fusibles
   - FS0, FS1
   - FS0, FS1, FS2, FS3
 * - Transformateurs
   - TR1
   - TR1, TR2, TR3
 * - Modules de protection
   - GM1
   - GM1, GM2, GM3
 * - Régulateur 3,3 V/5 V
   - PS1 (RAC05E)
   - PS1 (RAC05E, commun)
 * - Capteurs de courant (CT)
   - 1 CT (phase principale)
   - 3 CT (un par phase)
 * - Sorties triac
   - 1 ou plusieurs (selon modèle)
   - 1 ou plusieurs (selon modèle)
 * - Sorties relais
   - 0 ou plusieurs (selon modèle)
   - 0 ou plusieurs (selon modèle)

.. note::
 Dans ce guide, les instructions utilisent la notation :

 - **Mono :** composants pour version monophasée
 - **Tri :** composants pour version triphasée

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
 #. ☐ **Fusibles intacts ?**

    - Mono : FS0, FS1
    - Tri : FS0, FS1, FS2, FS3
    - Vérifier avec multimètre en mode continuité
    - Un fusible grillé indique un court-circuit

 #. ☐ Tension au point Test VCC = 3,3 V ou 5 V ?

    - Multimètre en mode tension continue (DC)
    - Mesurer entre VCC et GND
    - Si pas de tension → Problème alimentation

Si Pas de Tension au Test VCC
-----------------------------

.. danger::
 **COUPER L’ALIMENTATION** avant toute vérification de composants !

Vérifier les composants d’alimentation :

.. admonition:: Composants à vérifier

 #. ☐ **Module PS1 (RAC05E)** dans le bon sens ?

    - Vérifier l’orientation selon le schéma
    - Vérifier que le point ou l’encoche du module correspond au repère sur le PCB

 #. ☐ **Condensateur C3** polarité correcte ?

    - Bande blanche = côté négatif (-)
    - Vérifier marquage sur PCB
    - ⚠️ Si inversé : risque d’explosion à la mise sous tension !

 #. ☐ **Transformateur·s bien soudé·s ?**

    - Mono : TR1
    - Tri : TR1, TR2, TR3
    - Soudures brillantes et lisses (pas ternes) ?

.. include:: common/qualite-soudures.inc.rst

Pont de Soudure (Court-Circuit)
-------------------------------

**Symptôme :** Deux pistes ou broches reliées par erreur

.. todo:: Ajouter photo de pont de soudure (img/pont-de-soudure.png)

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

 #. ☐ **ATmega328P** bien inséré dans le support ?

    - Toutes les pattes dans les trous ?
    - Pas de patte pliée sous le boîtier ?

 #. ☐ **ATmega328P** dans le bon sens ?

    - ⚠️ **CRITIQUE** : Encoche alignée avec marquage PCB ?
    - Si inversé → **Puce détruite à la mise sous tension !**
    - Vérifier 3 fois avant d’alimenter

 #. ☐ **Firmware programmé ?**

    - Voir la section :ref:`test-logiciel`
    - ATmega328P vierge ne fait rien

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
   - Vérifier l’orientation, remplacer
 * - Tension OK, rien ne fonctionne
   - ATmega328P mal inséré/inversé
   - Vérifier l’orientation, réinsérer
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

 #. ☐ **ATmega328P bien inséré ?**

    - Toutes les pattes dans le support ?
    - Orientation correcte (encoche) ?

 #. ☐ **Routeur alimenté en 230 V ?**

    - Le FTDI ne fournit **PAS** de courant
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

    - 9 600 bauds pour Moniteur Série

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

   - **Baud rate :** 9 600
   - **Fin de ligne :** « Les deux, CR+LF »

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

    - Composant à 2 pattes près de l’ATmega328P
    - Soudures correctes ?

 #. ☐ **Condensateurs C7/C8 présents ?** (si quartz externe)

    - Condensateurs 22 pF de chaque côté du quartz
    - Valeur correcte ?

**Si messages bizarres/illisibles :**

- Vérifier que le baud rate = 9 600
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

 #. ☐ **Court-circuit dans transformateur·s**

    - Mono : TR1
    - Tri : TR1, TR2, TR3

 - Mesurer la résistance des enroulements (doit être ~1–10 kΩ)
 - Si <10 Ω → Transformateur défectueux

 #. ☐ **Pont de soudure sur pistes haute tension**

 - Inspecter visuellement avec une loupe
 - Zone 230 V particulièrement critique

 #. ☐ **Condensateur en court-circuit**

 - C1 (condensateur film secteur) ou C3 (électrolytique) défectueux
 - Rare mais possible

 #. ☐ **Module PS1 (RAC05E) défectueux**

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

    - Dessouder un côté du/des transformateur·s (TR1 pour mono, ou TR1/TR2/TR3 pour tri)
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
 * - VCC (3,3 V)
   - 3,3 V
   - ±0,2 V (3,1–3,5 V)
 * - VCC (5 V)
   - 5,0 V
   - ±0,3 V (4,7–5,3 V)
 * - Sortie ADC (repos)
   - VCC/2
   - ±0,5 V
 * - Gate triac (actif)
   - ~2–5 V (pulsé)
   - Variable

Diagnostic par Tension
----------------------

**VCC trop faible (<3 V pour système 3,3 V) :**

- Module PS1 (RAC05E) défectueux, mal orienté ou mal soudé
- Court-circuit partiel consommant trop de courant

**VCC trop élevée (>5,5 V) :**

- ⚠️ **DANGER** pour ATmega328P (max absolu = 6 V)
- Régulateur absent ou court-circuité
- **COUPER L’ALIMENTATION IMMÉDIATEMENT**

**Tension ADC incorrecte (pas à VCC/2) :**

- Résistances de burden R18/R28/R38 mauvaise valeur ou absentes (uniquement si CT à sortie courant)
- Condensateurs de filtrage défectueux (CMS, soudés en usine)
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

    - Emplacements R18 / R28 / R38 (THT, un par CT)
    - Uniquement nécessaires avec des CT à sortie courant (ex. : SCT-013-000)
    - Pas nécessaires avec des CT à sortie tension (burden intégré)
    - Valeur calculée selon le CT — voir :ref:`carte-mere-presentation`

 #. ☐ **Diodes TVS de protection présentes ?**

    - Composants CMS soudés en usine sur les mêmes pastilles que les burden
    - Vérifier visuellement qu’aucune n’est manquante ou décollée

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
 * - Avec charge 2 000 W
   - 1 900–2100 W
   - ±5% après étalonnage
 * - Production 3 000 W
   - 2 850–3150 W
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
#. Utiliser une charge purement résistive 1 500–2000 W
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
   - Beaucoup d’excédent (80–100%)
   - Normal en pleine production
 * - Clignotement lent (>2s)
   - Peu d’excédent (10–30%)
   - Normal début/fin journée
 * - Clignotement erratique
   - Mesures instables
   - Vérifier le CT et l’étalonnage

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

**Mesure signal gate :**

#. Oscilloscope ou multimètre AC sur gate triac
#. En fonctionnement :

   - Doit montrer impulsions 2–5 V
   - Fréquence 50/100 Hz (burst fire)
   - Si pas d’impulsions → Problème opto-coupleur ou routage signal

Vérifications Charge
--------------------

**Chauffe-eau :**

- ☐ Thermostat non déclenché ? (température max atteinte)
- ☐ Thermostat pas coupé manuellement ?
- ☐ Résistance chauffe-eau fonctionnelle ?

 - Tester résistance : doit être ~25–30 Ω pour 2 000 W
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
- Si charge >3 kW : répartir la puissance sur plusieurs étages de sortie ou réduire la puissance de la charge


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

#. Ouvrir Moniteur Série (9 600 bauds)
#. Forcer émission commande test
#. Observer messages debug

**Problèmes fréquents :**

- Mauvaise broche SPI (vérifier schéma)
- Module 3,3 V alimenté en 5 V (destruction possible)
- Interférences (éloigner de charges puissance)

======================================
📡 Problèmes du Module mk2Wifi
======================================

.. note::
   Cette section concerne uniquement les kits équipés du module d’extension :term:`mk2Wifi` (ESP32-C3).

Le Module ne s’Allume Pas
=========================

**Symptôme :** LED D1 du module éteinte lorsque la carte principale est sous tension

.. admonition:: Liste de contrôle — Alimentation mk2Wifi

   #. ☐ **Carte principale sous tension ?**

      - La mk2Wifi est alimentée en +5 V par la carte principale via UART_EXT broche 3
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

   #. ☐ **Cavalier V sel. en position 3,3 V ?**

      - Si le cavalier V sel. a été basculé en 5 V, le module est **détruit**
      - Voir :ref:`cavaliers`

Programmation USB-C Impossible
==============================

**Symptôme :** L’ESP32-C3 n’est pas détecté par l’ordinateur via USB-C

.. admonition:: Liste de contrôle — Connexion USB-C

   #. ☐ **Module débranché de la carte principale ?**

      - Le module **doit** être déconnecté de la carte principale pendant la programmation USB-C
      - Les deux alimentations +5 V (USB et carte principale) ne sont pas isolées

   #. ☐ **Mode téléchargement activé ?**

      - Maintenir le bouton **SW1** enfoncé pendant la mise sous tension (branchement du câble USB-C)
      - Relâcher SW1 après la connexion
      - Sans cette manipulation, le module démarre en mode normal (pas en mode programmation)

   #. ☐ **Câble USB-C avec données ?**

      - Certains câbles USB-C sont **charge uniquement** (pas de fils de données)
      - Essayer un autre câble connu pour transférer des données

   #. ☐ **Port USB fonctionnel ?**

      - Essayer un autre port USB (préférer un port direct, pas un hub)

   #. ☐ **Pilotes USB-série ?**

      - L’ESP32-C3 dispose d’un contrôleur **USB-série/JTAG intégré** — aucun pilote externe normalement nécessaire
      - Windows : vérifier dans le Gestionnaire de périphériques qu’un nouveau port COM apparaît
      - Linux : ``dmesg | grep tty`` doit montrer un nouveau périphérique

Pas de Communication avec la Carte Principale
==============================================

**Symptôme :** Module alimenté (LED D1 allumée) mais aucune donnée reçue de la carte principale

.. admonition:: Liste de contrôle — Communication UART

   #. ☐ **Module dans le bon sens ?**

      - Un branchement inversé empêche la communication
      - Vérifier l’alignement des sérigraphies TRIG_EXT et UART_EXT

   #. ☐ **Firmware carte principale programmé ?**

      - L’ATmega328P doit être programmé avec un firmware compatible mk2Wifi
      - Vérifier via le moniteur série de la carte principale

   #. ☐ **Barrettes bien soudées ?**

      - Vérifier les soudures sur les barrettes du module mk2Wifi
      - Vérifier les soudures des connecteurs TRIG_EXT et UART_EXT sur la carte principale
      - Soudure froide = contact intermittent

Connexion WiFi Impossible
=========================

**Symptôme :** Le module ne se connecte pas au réseau WiFi

**Vérifications :**

#. **Réseau en 2,4 GHz ?**

   - L’ESP32-C3 supporte **uniquement le 2,4 GHz** (802.11 b/g/n)
   - Les réseaux 5 GHz ne sont **pas visibles** par le module
   - Si votre box utilise un SSID unique pour 2,4 et 5 GHz, essayez de séparer les bandes

#. **Identifiants corrects ?**

   - Vérifier le SSID et le mot de passe dans la configuration du firmware
   - Attention aux majuscules/minuscules et aux caractères spéciaux

#. **Signal suffisant ?**

   - Le module est souvent installé dans un boîtier métallique (tableau électrique)
   - Le métal atténue fortement le signal WiFi
   - Rapprocher le point d’accès ou utiliser un répéteur WiFi

#. **Firmware WiFi configuré ?**

   - Vérifier que le firmware chargé inclut la configuration WiFi
   - Un firmware vierge ne se connecte à aucun réseau

Mise à Jour OTA Échoue
=======================

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

- Revenir à la programmation par **USB-C** (voir procédure initiale dans :ref:`installation-mk2wifi`)
- Maintenir SW1 enfoncé pour entrer en mode téléchargement

Écran OLED Vide ou Incorrect
=============================

**Symptôme :** L’écran OLED branché sur le connecteur mk2Wifi n’affiche rien ou des caractères incohérents

.. admonition:: Liste de contrôle — OLED mk2Wifi

   #. ☐ **Écran branché sur le bon connecteur ?**

      - L’écran doit être branché sur le connecteur **OLED de la mk2Wifi**, pas sur celui de la carte principale
      - Le bus I2C de la mk2Wifi est **indépendant** de celui de la carte principale

   #. ☐ **Type d’écran compatible ?**

      - Vérifier le contrôleur : SSD1306 ou SH1106
      - L’adresse I2C doit correspondre (typiquement 0x3C ou 0x3D)
      - Vérifier la configuration dans le firmware

   #. ☐ **Brochage correct ?**

      - Ordre des broches : GND, VCC, SCL, SDA
      - Certains écrans ont un brochage différent — vérifier avant de brancher

Capteur DS18B20 — Pas de Température
=====================================

**Symptôme :** La température n’est pas mesurée malgré un capteur DS18B20 branché

.. admonition:: Liste de contrôle — DS18B20

   #. ☐ **Cavalier TEMP en bonne position ?**

      - En position **3–centre** : le DS18B20 est géré par la mk2Wifi (ESP32-C3)
      - En position **1–centre** : le DS18B20 est géré par la carte principale (ATmega328P, broche D3)
      - Voir :ref:`cavaliers`

   #. ☐ **Capteur correctement branché ?**

      - Vérifier la polarité (GND, DATA, VCC)
      - Un branchement inversé peut endommager le capteur

   #. ☐ **Résistance de pull-up présente ?**

      - Le bus 1-Wire nécessite une résistance de pull-up de 4,7 kΩ
      - Vérifier si elle est déjà présente sur la carte ou sur le câble du capteur

=================
Obtenir de l’Aide
=================

Si Aucune Solution ne Fonctionne
================================

Ressources Communautaires
-------------------------

#. **Communauté Facebook :** https://www.facebook.com/groups/3571488193062570

   - Moteur de recherche (problème déjà résolu ?)
   - Poster nouveau sujet avec détails

#. **Email support :** support@mk2pvrouter.fr

   - Temps réponse : 2–5 jours ouvrés

#. **GitHub Issues :** https://github.com/FredM67/Mk2PVRouter/issues

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
 - Configuration (mono/tri, nombre sorties)
 - Système 3,3 V ou 5 V ?

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

Loupe ou Microscope USB
=======================

**Utilité :**

- Inspecter qualité soudures
- Détecter ponts microscopiques
- Vérifier l’orientation des composants CMS

**Recommandation :**

- Loupe ×5 à ×10 minimum
- Microscope USB 200× pour inspection détaillée
- Éclairage LED intégré essentiel

Oscilloscope (Optionnel)
========================

**Pour diagnostics avancés :**

- Visualiser signal gate triac
- Vérifier oscillateur ATmega328P
- Analyser formes d’ondes ADC

**Alternative économique :**

- Oscilloscope USB 20 MHz (50–100€)
- Suffisant pour diagnostics DIY

Pince Ampèremétrique
====================

**Utilité :**

- Mesurer courant sans couper câble
- Vérifier puissance réelle charge
- Indispensable pour étalonnage

**Spécifications minimum :**

- Plage : 0–20 A AC
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
