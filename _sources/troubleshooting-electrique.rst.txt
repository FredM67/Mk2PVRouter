.. _troubleshooting-electrique:

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

 #. ☐ **Module PS1 (MPC10-5) défectueux**

 - Peut être en court-circuit si défaut fabrication
 - Ou endommagé par soudure trop chaude

Procédure de Diagnostic
-----------------------

.. warning::
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

- Module PS1 (MPC10-5) défectueux, mal orienté ou mal soudé
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
    - Valeur calculée selon le CT — voir :ref:`carte-mere-presentation`

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

