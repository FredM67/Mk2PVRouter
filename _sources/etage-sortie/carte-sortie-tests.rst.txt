.. _carte-sortie-tests:

============================
Tests de la Carte de Sortie
============================

Lors de la construction d’un système complet, il peut être préférable de monter l’étage de sortie finalisé dans le boîtier avant de procéder à son test.

Les conseils suivants sont destinés aux situations où un étage de sortie doit être testé de manière indépendante.

.. danger::
   **Avertissement de Sécurité**

   Pour vérifier le bon fonctionnement du déclencheur et du :term:`triac <Triac>`, un accès à la tension du réseau électrique **230 V** CA est nécessaire.

   Faites preuve de la plus grande prudence et n’entamez cette étape que si vous avez les compétences nécessaires pour le faire en toute sécurité.

Voici une plate-forme construite qui permet de tester les cartes de sortie avec ou sans le :term:`triac <Triac>` soudé en place.

Lors du test d’une carte de sortie, il est important que le :term:`triac <Triac>` fasse partie du circuit électrique, sinon tout le courant de charge passera par le circuit :term:`optocoupleur <Optocoupleur>` et un ou plusieurs composants seront alors détruits immédiatement.

En tenant dûment compte de l’avertissement de sécurité ci-dessus, l’approche simple illustrée ci-dessous devrait convenir pour tester des cartes individuelles.

Configuration du Banc de Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Matériel nécessaire pour le test :**

☐ **Lampe à incandescence** 40–100 W (ou résistance chauffante équivalente)

☐ **Douille E27** avec câble secteur

☐ **Arduino ou microcontrôleur** (pour générer signal de commande)

☐ **Câbles de connexion** dupont mâle-femelle

☐ **Multimètre** (pour vérifier tensions)

☐ **Extincteur** à portée de main

☐ **Surface isolante et ininflammable** (céramique, bois sec — PAS métal)

Schéma de Montage du Test
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. graphviz::
   :caption: Configuration du banc de test pour carte de sortie triac (cliquer pour agrandir)
   :align: center
   :alt: Schéma de test complet pour carte de sortie triac

   digraph test_bench {
       // Configuration générale - Top to Bottom
       rankdir=TB;
       node [shape=box, style="rounded,filled", fontname="Arial"];
       edge [fontname="Arial", fontsize=10];
       splines=ortho;
       nodesep=0.8;
       ranksep=1.0;

       // Arduino en haut (zone basse tension)
       arduino [label="Arduino\nPin 9 (signal)\nGND", fillcolor="#64B5F6", color="#1976D2", fontcolor=white, width=2];

       // Cluster pour la carte de sortie au centre
       subgraph cluster_card {
           label="CARTE DE SORTIE SOUS TEST";
           style="filled,rounded";
           fillcolor="#FFF9E6";
           color="#666666";
           fontsize=12;
           fontcolor="#333333";
           labelloc="t";
           margin=20;

           // Sous-cluster: Colonne BASSE TENSION (gauche)
           subgraph cluster_low_voltage {
               label="Basse Tension";
               style="filled,dashed";
               fillcolor="#E8F5E9";
               color="#2E7D32";
               fontsize=10;
               fontcolor="#2E7D32";

               molex [label="Connecteur\nMolex IN", fillcolor="#90EE90", color="#2E7D32", width=1.5];
           }

           // Isolation galvanique (zone critique au centre)
           opto [label="Optocoupleur\nMOC3043\n━━━━━━━━━━━━━\nISOLATION\nGALVANIQUE", shape=box, fillcolor="#FFD54F", color="#F57C00", fontsize=10, style="filled,bold", width=2.2, height=1.2];

           // Sous-cluster: Colonne HAUTE TENSION (droite)
           subgraph cluster_high_voltage {
               label="Haute Tension";
               style="filled,dashed";
               fillcolor="#FFEBEE";
               color="#C62828";
               fontsize=10;
               fontcolor="#C62828";

               triac [label="Triac\nBTA41", fillcolor="#FF6B6B", fontcolor=white, color="#C62828", width=1.5];
               power_conn [label="Connecteur\nPuissance", fillcolor="#FFB6C1", color="#C2185B", width=1.5];

               // Organisation dans la colonne haute tension
               triac -> power_conn [label="", color="#F44336", penwidth=2];
           }

           // Connexions entre les zones
           molex -> opto [label="  Signal 3.3V-5V  ", color="#4CAF50", fontcolor="#2E7D32", fontsize=9];
           opto -> triac [label="  Déclenchement  ", color="#FF9800", fontcolor="#E65100", style="dashed", fontsize=9, constraint=true];

           // Forcer l’alignement horizontal des deux colonnes
           {rank=same; molex; opto; triac;}
       }

       // Légende en bas à gauche sous la carte
       legend [shape=none, margin=0, label=<
           <table border="0" cellborder="1" cellspacing="0" cellpadding="6">
           <tr><td colspan="2" bgcolor="#E0E0E0"><b>Légende</b></td></tr>
           <tr><td bgcolor="#90EE90">Vert</td><td align="left">Basse tension (3.3V-5V)</td></tr>
           <tr><td bgcolor="#FF6B6B"><font color="white">Rouge</font></td><td align="left">Haute tension (230V)</td></tr>
           <tr><td bgcolor="#FFD54F">Jaune</td><td align="left">Isolation galvanique</td></tr>
           </table>
       >];

       // Secteur et lampe en bas (zone haute tension)
       secteur [label="⚠️ 230 V ⚠️\nSecteur", fillcolor="#D32F2F", fontcolor=white, color="#B71C1C", penwidth=2, width=2];
       lampe [label="Lampe\nIncandescence\n100 W", shape=ellipse, fillcolor="#FFF59D", color="#F9A825", width=1.8];

       // Connexions externes verticales
       arduino -> molex [label="  Câble dupont (3.3V-5V)  ", color="#2196F3", fontcolor="#1565C0", fontsize=9];
       power_conn -> secteur [label="  Entrée 230V AC  ", color="#D32F2F", fontcolor="#B71C1C", penwidth=2, fontsize=9, dir=back];
       secteur -> lampe [label="  Charge 100W  ", color="#FF5722", fontcolor="#BF360C", penwidth=1.5, fontsize=9];

       // Positionner la légende à gauche, secteur au centre, lampe à droite
       // Utiliser des arêtes invisibles pour forcer l’ordre gauche-droite
       {
           rank=same;
           legend -> secteur -> lampe [style=invis];
       }
   }

Procédure de Test Complète
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. danger::
   ⚠️ **RAPPEL SÉCURITÉ — 230 V SECTEUR**

   - Extincteur à portée de main
   - Aucun contact avec les parties sous tension
   - Disjoncteur facilement accessible
   - Personne présente pour surveiller
   - Premier test : durée maximale 2 minutes

Étape 1 : Vérifications Préalables (HORS TENSION)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Inspection visuelle complète de la carte**

   ☐ Toutes les soudures haute puissance re-vérifiées

   ☐ Pas de court-circuit visible

   ☐ Pas de composant mal orienté

   ☐ :term:`Optocoupleur` correctement inséré (repère aligné)

#. **Test de continuité au multimètre**

   ☐ Mesurer résistance entre bornes connecteur puissance : **doit être ∞ Ω** (circuit ouvert)

   ☐ Mesurer résistance :term:`optocoupleur <Optocoupleur>` côté commande : **quelques kΩ** (LED interne)

   ☐ Vérifier absence de court-circuit entre pistes basse/haute tension

#. **Montage du banc de test**

   ☐ Connecter lampe au connecteur de puissance de la carte

   ☐ Connecter Arduino pin 9 → Molex IN (signal commande)

   ☐ Connecter Arduino GND → Molex GND

Étape 2 : Test Sans Tension Secteur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Programmer Arduino avec signal test**

   .. code-block:: cpp

      void setup() {
        pinMode(9, OUTPUT);
      }

      void loop() {
        digitalWrite(9, HIGH);  // Commande ON
        delay(2000);            // 2 secondes
        digitalWrite(9, LOW);   // Commande OFF
        delay(2000);            // 2 secondes
      }

#. **Alimenter Arduino uniquement (PAS de secteur 230 V)**

#. **Mesurer tension aux bornes du :term:`triac <Triac>`** avec multimètre

   - **Signal HIGH** : Devrait y avoir quelques volts (LED :term:`optocoupleur <Optocoupleur>` allumée)
   - **Signal LOW** : 0 V (LED optocoupleur éteinte)

   ✅ Si OK : L’:term:`optocoupleur <Optocoupleur>` fonctionne correctement

   ❌ Si pas de variation : Vérifier soudures, orientation optocoupleur, résistances R1-R3

Étape 3 : Premier Test Sous Tension 230 V
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. danger::
   ⚠️⚠️⚠️ **DANGER — TENSION MORTELLE 230 V** ⚠️⚠️⚠️

   À partir de maintenant, **AUCUN CONTACT** avec la carte ou la lampe.

   Restez à **50 cm minimum** de la zone de test.

#. **Vérifier une dernière fois :**

   ☐ Lampe correctement connectée

   ☐ Arduino alimenté et programme en cours

   ☐ Extincteur à portée

   ☐ Disjoncteur accessible

#. **Brancher la lampe sur secteur 230 V**

#. **Observer pendant 30 secondes**

   **✅ Comportement NORMAL attendu :**

   - Lampe s’allume et s’éteint toutes les 2 secondes (suivant programme Arduino)
   - Pas d’odeur de brûlé
   - Pas de fumée
   - Pas de grésillement
   - Commutation silencieuse (pas de clic)

   **❌ Comportement ANORMAL — COUPER IMMÉDIATEMENT :**

   - Lampe reste allumée en permanence → :term:`Triac` en court-circuit
   - Lampe ne s’allume jamais → Triac ne conduit pas (défaut ou mal soudé)
   - Fumée ou odeur → Composant en surchauffe
   - Grésillement → Mauvais contact, arc électrique

#. **Si test réussi : Laisser fonctionner 2 minutes**

   - Surveiller température carte (main au-dessus, sans toucher)
   - Carte doit rester froide ou tiède (légèrement chaude acceptable)
   - :term:`Triac` peut être tiède après 2 minutes (normal)

#. **Couper alimentation secteur**

#. **Attendre 1 minute** (décharge condensateurs éventuels)

Étape 4 : Test de Charge Progressive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si le test précédent a réussi, vous pouvez tester avec une charge plus importante.

#. **Remplacer la lampe par une charge plus importante** (100 W ou radiateur 500–1 000 W)

#. **Répéter test pendant 5 minutes**

   - Surveiller température :term:`triac <Triac>` (devrait rester < 60 °C au toucher)
   - Vérifier commutation toujours fonctionnelle


Résultats Attendus du Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Carte Fonctionnelle
^^^^^^^^^^^^^^^^^^^

**✅ SUCCÈS — La carte fonctionne correctement si :**

☑ Lampe s’allume/s’éteint selon signal Arduino

☑ Commutation silencieuse (pas de clic mécanique comme relais)

☑ Aucune odeur ou fumée pendant 5 minutes de fonctionnement

☑ Température carte reste raisonnable (< 60 °C)


☑ Pas de grésillement ni arc électrique

**➜ La carte est prête pour l’installation dans le boîtier**

Carte Défectueuse
^^^^^^^^^^^^^^^^^

**❌ ÉCHEC — La carte a un problème si :**

☒ Lampe reste allumée en permanence

   **Diagnostic** : :term:`Triac` en court-circuit (détruit ou mal soudé)

   **Action** : Remplacer triac

☒ Lampe ne s’allume jamais

   **Diagnostic** : Circuit :term:`optocoupleur <Optocoupleur>` défectueux ou :term:`triac <Triac>` ouvert

   **Action** : Vérifier optocoupleur (sens, soudures), vérifier résistances R1-R3

☒ Lampe clignote aléatoirement

   **Diagnostic** : Mauvais contact, soudure froide

   **Action** : Re-vérifier toutes les soudures haute puissance

☒ Fumée ou odeur de brûlé

   **Diagnostic** : Surchauffe composant (soudure insuffisante, court-circuit)

   **Action** : **ARRÊTER IMMÉDIATEMENT**, inspecter visuellement, refaire soudures

☒ Carte chauffe excessivement (> 80 °C)

   **Diagnostic** : Résistance de contact trop élevée (agrafes mal soudées)

   **Action** : Refaire soudures agrafes cuivre avec fer très chaud

