.. _installation-finale:

Installation Finale dans le Système Électrique
===============================================

⚠️⚠️⚠️ **DANGER DE MORT — HAUTE TENSION 230 V AC** ⚠️⚠️⚠️

Cette section décrit la connexion du Mk2PVRouter au réseau électrique de votre habitation.

**Cette opération présente des RISQUES MORTELS par électrocution.**

.. danger::
   ⚡ **TENSION MORTELLE 230 V AC, 380 V AC en triphasé** ⚡

   Le contact avec des conducteurs sous tension peut provoquer :

   - **Décès par électrocution** (arrêt cardiaque, brûlures internes)
   - **Brûlures graves** (arc électrique jusqu’à 3 000 °C)
   - **Incendie** (court-circuit, mauvaise connexion)
   - **Explosion** (défaut d’isolation)

   **Un seul instant d’inattention peut être FATAL.**

.. contents:: Sommaire
   :local:
   :depth: 2

Exigences Légales en France
----------------------------

Conformité Réglementaire Obligatoire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selon la **norme NF C 15-100** (installations électriques basse tension en France) :

☐ Installation par **électricien qualifié OBLIGATOIRE**

   Seul un professionnel certifié peut légalement modifier une installation électrique

☐ Conformité installation vérifiée par **Consuel**

   Organisme de contrôle des installations électriques

☐ Assurance habitation **DOIT être informée** de la modification

   Toute modification non déclarée peut entraîner refus d’indemnisation

☐ Respect des normes électriques en vigueur

   NF C 15-100 + réglementations locales

.. warning::
   ⚠️ **CONSÉQUENCES LÉGALES**

   En cas de non-conformité :

   - **Assurance habitation** : Refus d’indemnisation en cas de sinistre (incendie, dégât des eaux causé par installation défectueuse)
   - **Vente immobilière** : Diagnostic électrique obligatoire, non-conformité bloque la vente
   - **Responsabilité pénale** : En cas d’accident causé par installation non conforme
   - **Amendes** : Jusqu’à 3 000 € pour installation non déclarée

Recommandation Forte
^^^^^^^^^^^^^^^^^^^^^

.. important::
   🔴 **NOUS RECOMMANDONS VIVEMENT de faire appel à un électricien certifié**

   **Pourquoi ?**

   - Connaissance des normes en vigueur
   - Expérience des installations haute puissance
   - Équipement de sécurité approprié
   - Assurance responsabilité civile professionnelle
   - Attestation de conformité pour votre assurance

   **Coût estimé :** 200-500 € pour l’installation complète

   **Ce coût est DÉRISOIRE comparé aux risques encourus.**

Prérequis Avant Installation
-----------------------------

.. admonition:: 📋 Vérifications Obligatoires

   Avant TOUTE manipulation :

   ☐ **Mk2PVRouter complètement assemblé et testé**

      - Tous les tests logiciels effectués avec succès
      - Étalonnage (calibration) terminé
      - Aucun défaut détecté

   ☐ **Disjoncteur général coupé et verrouillé**

      - Placer un cadenas si possible
      - Afficher panneau « TRAVAUX EN COURS - NE PAS RÉENCLENCHER »

   ☐ **Absence de tension vérifiée avec multimètre**

      - Mesurer entre phase et neutre : 0 V
      - Mesurer entre phase et terre : 0 V
      - Refaire la mesure 3 fois pour être certain

   ☐ **Personne qualifiée présente** (si vous n’êtes pas électricien)

      - En cas d’accident, quelqu’un doit pouvoir intervenir
      - Connaissance des gestes de premiers secours recommandée

   ☐ **Téléphone à portée de main** pour appeler les secours (15 ou 18)

Matériel de Sécurité Requis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Équipement de Protection Individuelle (EPI)
""""""""""""""""""""""""""""""""""""""""""""

☐ **Gants isolants classe 00** (minimum 500 V :term:`AC`)

☐ **Chaussures de sécurité isolantes** (semelle isolée)

☐ **Tapis isolant** pour se tenir debout

☐ **Lunettes de protection** (protection contre arc électrique)

☐ **Vêtements en coton** (PAS de synthétique qui fond)

Équipement de Mesure et Outils
"""""""""""""""""""""""""""""""

☐ **Multimètre numérique** CAT III ou CAT IV (600 V minimum)

☐ **Testeur de tension sans contact** (VAT — Voltage Alert Tester)

☐ **Tournevis isolés** 1 000 V

☐ **Pince à dénuder isolée**

☐ **Lampe de poche** (en cas de coupure secteur)

Installation des Capteurs de Courant (:term:`CT`)
-------------------------------------------------

Les capteurs de courant (Current Transformers) se placent sur les câbles d’alimentation principale.

Emplacement des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^

**CT Grille — Mesure de la consommation/injection réseau**

Les :term:`CT` Grille sont des capteurs à clip installés sur les câbles de **phase** principaux, entre le compteur et le tableau électrique. Ils mesurent le bilan énergétique du foyer (consommation ou injection).

- **Monophasé** : 1 :term:`CT` à clip sur la phase unique (CT1)
- **Triphasé** : 3 :term:`CT` à clip sur les 3 phases (CT1, CT2, CT3)

**CT Diversion — Mesure de la puissance routée** (optionnel)

Le :term:`CT` Diversion est installé sur le câble reliant la sortie du routeur à la charge (chauffe-eau). Il permet de mesurer la puissance effectivement routée.

⚠️ Ce :term:`CT` n'est **PAS** un :term:`CT` à clip externe comme les :term:`CT` Grille — il est **intégré dans le boîtier** du Mk2PVRouter.

Schéma d'installation — Monophasé
""""""""""""""""""""""""""""""""""

.. graphviz::
   :caption: Emplacement des CT — Installation monophasée
   :align: center
   :alt: Schéma d'installation des capteurs de courant en monophasé

   digraph ct_mono {
       rankdir=LR;
       node [shape=box, style="rounded,filled", fontname="Arial", fontsize=11];
       edge [fontname="Arial", fontsize=10];
       nodesep=0.6;
       ranksep=0.9;
       bgcolor=transparent;

       compteur [label="Compteur\nLinky", fillcolor="#E3F2FD", color="#1976D2"];

       ct1 [label="CT1\n(Grille)\n→ vers maison", shape=ellipse, fillcolor="#FFF9C4", color="#F9A825", fontcolor="#E65100", penwidth=2];

       tableau [label="Tableau\nélectrique", fillcolor="#E8EAF6", color="#3F51B5"];

       disj [label="Disjoncteur\n2A / 6A\n(dédié routeur)", fillcolor="#F3E5F5", color="#7B1FA2"];

       subgraph cluster_router {
           label="Mk2PVRouter";
           style="filled,rounded";
           fillcolor="#E8F5E9";
           color="#388E3C";
           fontname="Arial";
           fontsize=12;
           labelloc="t";
           margin=15;

           routeur [label="Carte\nprincipale", fillcolor="#C8E6C9", color="#388E3C"];
           sortie [label="Étage\nde sortie\n(triac)", fillcolor="#C8E6C9", color="#388E3C"];
       }

       ct2 [label="CT2\n(Diversion)\n→ vers charge\n(optionnel)", shape=ellipse, fillcolor="#FFF9C4", color="#F9A825", fontcolor="#E65100", style="filled,dashed", penwidth=2];

       charge [label="Charge\n(chauffe-eau\n2-3 kW)", fillcolor="#FFCCBC", color="#D84315"];

       compteur -> ct1 [label="Phase (L)", color="#E53935", fontcolor="#E53935", penwidth=2];
       ct1 -> tableau [color="#E53935", penwidth=2];
       tableau -> disj [label="L + N + PE"];
       disj -> routeur [label="Alimentation"];
       routeur -> sortie [style=dashed, color="#666666"];
       sortie -> ct2 [label="Sortie triac", color="#E53935", penwidth=2];
       ct2 -> charge [color="#E53935", penwidth=2];
   }

Schéma d'installation — Triphasé
"""""""""""""""""""""""""""""""""

.. graphviz::
   :caption: Emplacement des CT — Installation triphasée
   :align: center
   :alt: Schéma d'installation des capteurs de courant en triphasé

   digraph ct_tri {
       rankdir=LR;
       node [shape=box, style="rounded,filled", fontname="Arial", fontsize=11];
       edge [fontname="Arial", fontsize=10];
       nodesep=0.5;
       ranksep=0.9;
       bgcolor=transparent;

       compteur [label="Compteur\n(triphasé)", fillcolor="#E3F2FD", color="#1976D2"];

       ct1 [label="CT1\n(L1)\n→", shape=ellipse, fillcolor="#FFCDD2", color="#E53935", fontcolor="#B71C1C", penwidth=2];
       ct2 [label="CT2\n(L2)\n→", shape=ellipse, fillcolor="#FFE0B2", color="#FB8C00", fontcolor="#E65100", penwidth=2];
       ct3 [label="CT3\n(L3)\n→", shape=ellipse, fillcolor="#BBDEFB", color="#1E88E5", fontcolor="#0D47A1", penwidth=2];

       tableau [label="Tableau\nélectrique", fillcolor="#E8EAF6", color="#3F51B5"];

       disj [label="Disjoncteur\ntétrapolaire\n(dédié routeur)", fillcolor="#F3E5F5", color="#7B1FA2"];

       subgraph cluster_router {
           label="Mk2PVRouter";
           style="filled,rounded";
           fillcolor="#E8F5E9";
           color="#388E3C";
           fontname="Arial";
           fontsize=12;
           labelloc="t";
           margin=15;

           conn [label="Connecteur secteur\nPE | N | L1 | L2 | L3", fillcolor="#C8E6C9", color="#388E3C", shape=record];
           routeur [label="Carte principale\nCT1→L1 | CT2→L2 | CT3→L3", fillcolor="#C8E6C9", color="#388E3C"];
       }

       charges [label="Charges\n(chauffe-eau,\nradiateurs)", fillcolor="#FFCCBC", color="#D84315"];

       compteur -> ct1 [label="L1", color="#E53935", fontcolor="#E53935", penwidth=2];
       ct1 -> tableau [label="L1", color="#E53935", fontcolor="#E53935", penwidth=2];

       compteur -> ct2 [label="L2", color="#FB8C00", fontcolor="#FB8C00", penwidth=2];
       ct2 -> tableau [label="L2", color="#FB8C00", fontcolor="#FB8C00", penwidth=2];

       compteur -> ct3 [label="L3", color="#1E88E5", fontcolor="#1E88E5", penwidth=2];
       ct3 -> tableau [label="L3", color="#1E88E5", fontcolor="#1E88E5", penwidth=2];

       tableau -> disj [label="L1+L2+L3\n+N+PE"];
       disj -> conn;
       conn -> routeur [style=invis];
       routeur -> charges [label="Sorties triac", style=dashed];
   }

.. warning::
   **Chaque CT doit correspondre à la phase connectée sur le connecteur secteur du routeur.** La phase qui passe dans CT1 doit être raccordée sur **L1**, celle qui passe dans CT2 sur **L2**, et celle qui passe dans CT3 sur **L3**. Un décalage entre les CT et les phases provoquera des mesures de puissance incorrectes.

.. note::
   Les flèches (→) sur les :term:`CT` indiquent le sens d'installation : **vers la maison** (depuis le compteur). En triphasé sans neutre, CT3 n'est pas nécessaire (:term:`théorème de Blondel`).

Sens d’Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. danger::
   ⚠️ **LE SENS DES CT EST CRUCIAL**

   Un :term:`CT` installé à l’envers inversera le signe de la mesure :

   - Le routeur verra une **production** alors qu’il y a **consommation**
   - Le routeur verra une **consommation** alors qu’il y a **production**
   - **Résultat** : Le routeur fonctionnera à l’envers et **augmentera votre facture** au lieu de la réduire

**Règle de base :**

La **flèche** gravée sur le :term:`CT` doit pointer dans le **sens du flux d’énergie** :

- **CT Grille** : Flèche pointant **VERS la maison** (depuis le compteur)
- **CT Diversion** : Flèche pointant **VERS la charge** (chauffe-eau)

**Marquages K et L :**

La plupart des :term:`CT` portent des repères **K** et **L** sur le boîtier ou sur les fils du secondaire, en plus de la flèche :

- **K** (parfois noté **K**, **P1** ou **S1**) : borne qui devient **positive** quand le courant circule dans le sens de la flèche
- **L** (parfois noté **L**, **P2** ou **S2**) : borne complémentaire

Ces marquages permettent de vérifier le raccordement au connecteur de la carte :

- Si le sens du :term:`CT` est correct (flèche vers la maison) mais que la puissance affichée est **négative**, il suffit d’ **inverser les deux fils** (K ↔ L) sur le connecteur Molex au lieu de retourner physiquement le CT.
- Inversement, inverser K et L revient au même que retourner le CT de 180°.

Procédure d’Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   ⚠️ **DISJONCTEUR GÉNÉRAL COUPÉ OBLIGATOIRE**

   Ne JAMAIS installer les :term:`CT` sous tension !

   Un :term:`CT` à sortie courant dont le secondaire est **ouvert** (non branché) se comporte comme un transformateur à vide : il peut développer une **tension de plusieurs centaines de volts** aux bornes de ses fils, suffisante pour provoquer un arc électrique, endommager le CT ou le circuit d’entrée de la carte.

   Même avec un CT à sortie tension (burden intégré), manipuler un CT autour d’un conducteur sous tension présente un risque d’électrocution.

#. **Couper le disjoncteur général** et vérifier absence de tension

#. **Identifier le câble de phase** principal (généralement rouge, marron ou noir)

   ⚠️ Ne PAS placer le :term:`CT` sur le neutre (bleu) ou la terre (vert/jaune)

#. **Brancher la fiche jack 3,5 mm du CT** dans la prise jack du câble adaptateur (relié au connecteur Molex de la carte) **avant** de clipser le CT sur le câble

   Le secondaire du CT doit toujours être **fermé sur sa charge** (le circuit de la carte) avant d’être traversé par un courant primaire. Clipser un CT à sortie courant sur un conducteur actif alors que son jack n’est pas branché risque de générer une surtension destructrice.

#. **Ouvrir le CT** en appuyant sur le clip de fermeture

#. **Placer le CT autour du câble de phase UNIQUEMENT**

   - Un seul conducteur doit passer dans le :term:`CT`
   - Ne pas passer plusieurs câbles ensemble (sauf si intentionnel pour mesure différentielle)

#. **Vérifier le sens** : Flèche vers la maison pour :term:`CT` Grille

#. **Refermer fermement le CT** jusqu’au clic de verrouillage

#. **Vérifier que le CT est bien clipsé** (tirer légèrement pour tester)

#. **Fixer le câble du CT** pour éviter qu’il se débranche par traction

Vérification du Sens des :term:`CT` (Après Installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Une fois le routeur sous tension (après toutes les connexions) :

#. **Allumer un appareil de forte puissance** (bouilloire 2 000 W, radiateur)

#. **Observer l’affichage du routeur** (si écran présent) ou les logs série

#. **Vérifier que la puissance affichée est POSITIVE** quand vous consommez

   - Si la puissance est **négative** alors que vous consommez → **CT à l’envers**
   - Couper le disjoncteur, retourner le :term:`CT`, retester

Connexions Électriques au Tableau
----------------------------------

.. danger::
   ⚠️⚠️⚠️ **ZONE À HAUT RISQUE — TENSION MORTELLE** ⚠️⚠️⚠️

   Les opérations suivantes présentent un risque **MAXIMAL** d’électrocution.

   **SI VOUS N’ÊTES PAS ÉLECTRICIEN QUALIFIÉ, ARRÊTEZ-VOUS ICI.**

   Faites appel à un professionnel certifié.

Protection Électrique du Système
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   **Architecture du système :**

   - Le **Mk2PVRouter lui-même** consomme moins de **5 W** (alimentation électronique uniquement)
   - Les **circuits de puissance** (triacs) sont **indépendants** et pilotent les charges
   - Chaque **charge** (chauffe-eau, radiateur) conserve sa **propre protection** existante

Le Mk2PVRouter **électronique** nécessite un disjoncteur dédié pour son alimentation :

- **Type** : Disjoncteur divisionnaire bipolaire (Phase + Neutre)
- **Calibre** : 2 A ou 6 A (suffisant pour l’électronique < 5 W)
- **Courbe** : Type C (protection usage courant)
- **Pouvoir de coupure** : Minimum 4,5 kA (6 kA ou 10 kA recommandé)

.. important::
   ⚠️ **POURQUOI UN DISJONCTEUR DÉDIÉ ?**

   - **Isolation** : Permet de couper uniquement le routeur sans affecter les charges
   - **Protection** : Protège l’électronique du routeur uniquement
   - **Maintenance** : Facilite les interventions futures
   - **Sécurité** : En cas de défaut électronique, seul le routeur est déconnecté

.. warning::
   **Les charges restent protégées par leurs disjoncteurs d’origine**

   Le Mk2PVRouter ne remplace PAS la protection existante des charges :

   - Chauffe-eau : Conserve son disjoncteur 16 A ou 20 A
   - Radiateur : Conserve son disjoncteur adapté à sa puissance
   - Le routeur **pilote** les triacs, mais ne **protège pas** les charges

Câblage du Mk2PVRouter
^^^^^^^^^^^^^^^^^^^^^^^

**Pour l’alimentation du Mk2PVRouter électronique (< 5 W) :**

- **Section** : 0,75 mm² ou 1,5 mm² (largement suffisant)
- **Protection** : Disjoncteur 2 A ou 6 A

**Pour les charges pilotées (les câbles existants sont conservés) :**

La section des câbles des charges dépend de leur puissance (ces câbles sont normalement **déjà installés**) :

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Puissance charge
     - Section câble minimum
     - Disjoncteur max
   * - Jusqu’à 2 300 W
     - 1,5  mm²
     - 10 A
   * - 2 300 W - 3 680 W
     - 2,5 mm²
     - 16 A
   * - 3 680 W - 5 750 W
     - 4 mm²
     - 25 A
   * - 5 750 W - 7 360 W
     - 6 mm²
     - 32 A

.. note::
   **Ces sections concernent les charges uniquement, PAS le Mk2PVRouter.**

   Pour un **chauffe-eau classique 2 000-3 000 W**, les câbles existants sont normalement en **2,5 mm²** avec disjoncteur **16 A** ou **20 A**.

   Le Mk2PVRouter se branche **en parallèle** pour piloter la charge, il ne remplace pas ces câbles.

Schéma de Raccordement
^^^^^^^^^^^^^^^^^^^^^^

**Monophasé (230 V) :**

Connexions entre le tableau électrique et le MK2PVRouter :

- **L (Phase)** : du disjoncteur 16 A bipolaire → entrée L du routeur
- **N (Neutre)** : du disjoncteur → entrée N du routeur
- **⏚ (Terre)** : du disjoncteur → entrée PE du routeur

Les charges (chauffe-eau, radiateur…) sont raccordées aux sorties de l’étage de sortie (carte triac ou relais), pas au connecteur d’alimentation de la carte-mère.

**Triphasé (3 × 230 V = 400 V) :**

Connexions entre le tableau électrique et le MK2PVRouter :

- **L1 (Phase 1)** : du disjoncteur tétrapolaire 16 A → entrée L1 du routeur
- **L2 (Phase 2)** : du disjoncteur → entrée L2 du routeur
- **L3 (Phase 3)** : du disjoncteur → entrée L3 du routeur
- **N (Neutre)** : du disjoncteur → entrée N du routeur
- **⏚ (Terre)** : du disjoncteur → entrée PE du routeur

Les charges sont raccordées aux sorties des étages de sortie (une carte triac ou relais par phase).

Raccordement des étages de sortie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chaque étage de sortie (carte :term:`triac` ou relais) se raccorde à la fois à la carte-mère (signal de commande) et au circuit de puissance de la charge.

**Côté basse tension (signal) :**

- Reliez le connecteur Molex de l’étage de sortie à la sortie numérique correspondante de la carte-mère (D2–D13) à l’aide d’un câble Molex 2 fils.
- Chaque étage de sortie est piloté par **une seule** sortie numérique.

**Côté haute tension (puissance) :**

Le connecteur de puissance de l’étage de sortie a 3 broches : la broche centrale est inutilisée, les deux broches extérieures raccordent la **phase** en série avec la charge à travers le :term:`triac`.

- **Entrée phase** : depuis le disjoncteur dédié à la charge → broche du connecteur de puissance
- **Sortie phase** : autre broche du connecteur de puissance → charge (chauffe-eau, radiateur…)
- **Neutre** : du disjoncteur → directement à la charge (ne passe **pas** par l’étage de sortie)
- **Terre** : du disjoncteur → directement à la charge et au dissipateur du triac

.. warning::
   Le :term:`triac` ne coupe que la **phase**. Le neutre reste connecté en permanence à la charge. Pour intervenir sur la charge, il faut couper son disjoncteur dédié.

.. important::
   Chaque charge pilotée doit être protégée par son **propre disjoncteur**, distinct du disjoncteur d’alimentation du routeur.

Chaque étage de sortie constitue un **circuit de puissance indépendant**. Le nombre d’étages de sortie dépend du nombre de charges à piloter, pas de la configuration du routeur :

- **Charge monophasée** (chauffe-eau classique, radiateur) : **1 étage de sortie** par charge, protégé par un disjoncteur bipolaire (16 A ou 20 A selon la puissance).
- **Charge triphasée sans neutre** (chauffe-eau triphasé en triangle) : **2 étages de sortie** pour la même charge, protégés par un **unique disjoncteur tétrapolaire**.
- **Charge triphasée avec neutre** (chauffe-eau triphasé en étoile) : **3 étages de sortie** pour la même charge, protégés par un **unique disjoncteur tétrapolaire**.

.. warning::
   Pour une charge triphasée, tous les étages de sortie associés doivent être protégés par un **seul disjoncteur multipolaire**. L’utilisation de disjoncteurs unipolaires séparés est dangereuse : en cas de coupure d’une seule phase, la charge triphasée peut être endommagée ou provoquer un déséquilibre.

Procédure de Connexion (Électricien Qualifié)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **COUPER le disjoncteur général** du tableau

#. **Vérifier l’absence de tension** avec multimètre ET testeur sans contact

#. **Attendre 5 minutes** (décharge des condensateurs éventuels)

#. **Porter les EPI** (gants isolants, chaussures de sécurité)

#. **Installer le disjoncteur dédié** 16 A dans le tableau

#. **Connecter les câbles d’alimentation** au disjoncteur :

   - Phase (L) : Câble rouge/marron/noir
   - Neutre (N) : Câble bleu
   - Terre (⏚) : Câble vert/jaune

#. **Connecter les câbles vers le Mk2PVRouter** :

   - Respecter les couleurs (Phase, Neutre, Terre)
   - Serrer les connexions au couple recommandé (tournevis dynamométrique)
   - Vérifier qu’aucun brin de cuivre ne dépasse du bornier

#. **Connecter les câbles vers la charge** (chauffe-eau, radiateur)

#. **Vérifier toutes les connexions** (tirer légèrement sur chaque câble)

#. **Vérifier qu’aucun outil ne reste dans le tableau**

Première Mise Sous Tension
---------------------------

Liste de Vérification Finale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: ✅ Checklist Avant Première Mise Sous Tension

   Avant de réenclencher le disjoncteur :

   ☐ Toutes les connexions serrées et vérifiées

   ☐ Aucun brin de cuivre apparent

   ☐ :term:`CT` installés dans le bon sens (flèche vérifiée)

   ☐ Câbles de section correcte pour la puissance

   ☐ Disjoncteur dédié correctement dimensionné

   ☐ Tous les couvercles du tableau refermés

   ☐ Aucun outil ne reste dans le tableau

   ☐ Extincteur à portée de main

   ☐ Personne présente pour surveiller

   ☐ Téléphone à portée pour appeler secours si besoin

Procédure de Mise Sous Tension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Laisser le disjoncteur du Mk2PVRouter en position OFF**

#. **Réenclencher le disjoncteur général** du tableau

#. **Vérifier que le reste de l’installation fonctionne** (lumières, prises)

#. **Se positionner devant le tableau** avec extincteur à portée

#. **Enclencher le disjoncteur dédié du Mk2PVRouter**

#. **Observer pendant 30 secondes** :

   - Pas d’odeur de brûlé
   - Pas de fumée
   - Pas de grésillement
   - Disjoncteur ne saute pas

#. **Vérifier le fonctionnement du Mk2PVRouter** :

   - LED d’alimentation allumée
   - Écran affiche des données (si présent)
   - Pas de bruit anormal

Surveillance Post-Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pendant les **premières 24 heures** :

- ⚠️ **Rester à proximité les 2 premières heures** de fonctionnement

- ⚠️ **Vérifier régulièrement** (toutes les 30 minutes au début) :

  - Pas d’échauffement anormal des connexions (toucher avec dos de la main)
  - Pas d’odeur de brûlé
  - Pas de fumée
  - Fonctionnement correct du routeur

- ⚠️ **Si le moindre problème est détecté** :

  #. Couper IMMÉDIATEMENT le disjoncteur du Mk2PVRouter
  #. Couper le disjoncteur général si fumée ou odeur forte
  #. Laisser refroidir 30 minutes
  #. Inspecter visuellement toutes les connexions
  #. Faire vérifier par un électricien avant de remettre sous tension

Tests de Fonctionnement
------------------------

Test de Détection de Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Allumer un appareil de forte puissance** (bouilloire, radiateur 2 000 W)

#. **Observer l’affichage du routeur** :

   - La puissance consommée doit être affichée en positif
   - Le routeur ne doit PAS activer la charge

#. **Éteindre l’appareil**

#. **Simuler une production** (si possible, ou attendre production solaire)

   - Si injection réseau détectée → Le routeur doit activer la charge
   - Puissance doit être affichée en négatif (injection)

Test de Sécurité :term:`triac`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si le routeur utilise un :term:`triac` pour moduler la puissance :

#. **Vérifier que la charge ne s’active PAS** en l’absence de production

#. **Simuler une petite production** (< 500 W)

   - Charge doit s’activer partiellement (modulation)

#. **Simuler forte production** (> puissance de la charge)

   - Charge doit s’activer à 100 %

#. **Couper la production simulée brutalement**

   - Charge doit se désactiver immédiatement
   - Pas d’injection réseau parasite

Test de Coupure d’Urgence
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Couper le disjoncteur dédié du routeur**

   - Le routeur doit s’éteindre immédiatement
   - La charge doit se désactiver

#. **Réenclencher le disjoncteur**

   - Le routeur doit redémarrer normalement
   - Pas de défaut affiché

Résolution de Problèmes Courants
---------------------------------

Le routeur ne s’allume pas
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Disjoncteur pas enclenché ou défectueux

☐ Fusible grillé sur le routeur

☐ Connexion d’alimentation desserrée

☐ Transformateur d’alimentation défectueux

☐ Court-circuit sur l’alimentation

**Actions :**

#. Vérifier que le disjoncteur est bien enclenché
#. Mesurer la tension aux bornes d’alimentation du routeur (230 V attendu)
#. Vérifier les fusibles sur le routeur
#. Inspecter visuellement toutes les soudures

Le routeur fonctionne à l’envers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptôme :** Le routeur active la charge quand vous consommez et la désactive quand vous produisez

**Cause :** :term:`CT` installé à l’envers

**Solution :**

#. Couper le disjoncteur général
#. Retourner le :term:`CT` (inverser le sens de la flèche)
#. Remettre sous tension et retester

La charge ne s’active jamais
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ :term:`triac` défectueux (court-circuit ou ouvert)

☐ Connexion charge desserrée

☐ Charge défectueuse (chauffe-eau HS)

☐ Problème logiciel (seuil de déclenchement trop élevé)

**Actions :**

#. Vérifier les logs du routeur (seuil, puissance mesurée)
#. Vérifier la résistance de la charge (multimètre)
#. Tester le triac avec un multimètre
#. Vérifier les paramètres logiciels

Le disjoncteur saute
^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Court-circuit dans le routeur ou la charge

☐ Surcharge (charge trop puissante pour le calibre du disjoncteur)

☐ Défaut d’isolation (fuite à la terre)

☐ Disjoncteur défectueux ou sous-dimensionné

**Actions :**

#. **NE PAS réenclencher immédiatement**
#. Débrancher la charge du routeur
#. Réenclencher le disjoncteur → Si le disjoncteur tient : Le problème vient de la charge
#. Si le disjoncteur saute toujours : Le problème vient du routeur → Faire vérifier par un électricien

Odeur de brûlé
^^^^^^^^^^^^^^

**ACTION IMMÉDIATE :**

#. ⚠️ **COUPER LE DISJONCTEUR GÉNÉRAL IMMÉDIATEMENT**
#. ⚠️ **Évacuer si fumée importante**
#. ⚠️ **Appeler les pompiers (18) si flammes visibles**
#. Laisser refroidir 30 minutes minimum
#. **Faire inspecter par un électricien** avant de remettre sous tension

Maintenance et Surveillance
----------------------------

Vérifications Périodiques
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tous les 6 mois :**

☐ Inspecter visuellement toutes les connexions

☐ Vérifier qu’aucune connexion n’est desserrée (vibrations)

☐ Vérifier l’absence d’échauffement anormal

☐ Nettoyer la poussière accumulée (disjoncteur coupé)

☐ Vérifier le bon fonctionnement du routeur

**Tous les ans :**

☐ Faire vérifier l’installation par un électricien

☐ Vérifier l’étalonnage du routeur

☐ Contrôler l’usure des contacts du :term:`triac`

☐ Vérifier les :term:`CT` (clip de fermeture pas cassé)

Signes d’Alerte
^^^^^^^^^^^^^^^^

**Appeler un électricien IMMÉDIATEMENT si :**

⚠️ Odeur de brûlé persistante

⚠️ Échauffement anormal d’une connexion

⚠️ Grésillement ou bruit anormal

⚠️ Disjoncteur qui saute régulièrement

⚠️ Fumée, même légère

⚠️ Fonctionnement erratique du routeur

Dépose et Remplacement
^^^^^^^^^^^^^^^^^^^^^^^

Si vous devez déposer le routeur :

#. **Couper le disjoncteur dédié**

#. **Couper le disjoncteur général** (sécurité supplémentaire)

#. **Vérifier l’absence de tension**

#. **Débrancher les CT** en premier

#. **Débrancher l’alimentation** du routeur

#. **Débrancher la charge**

#. **Retirer le routeur**

Pour le remplacement, suivre la procédure d’installation depuis le début.

Numéros d’Urgence
-----------------

En cas de problème grave :

.. important::
   📞 **Numéros d’urgence en France**

   - **15** : SAMU (urgence médicale - électrocution)
   - **18** : Pompiers (incendie électrique)
   - **112** : Numéro d’urgence européen (fonctionne partout)

   **En cas d’électrocution :**

   #. **NE PAS toucher la victime** si encore sous tension
   #. **Couper le disjoncteur général IMMÉDIATEMENT**
   #. **Appeler le 15** (SAMU)
   #. Pratiquer massage cardiaque si formation aux premiers secours
   #. Ne pas déplacer la victime sauf danger immédiat

Ressources Complémentaires
---------------------------

.. admonition:: 📚 Documentation Technique

   - **Norme NF C 15-100** : https://www.promotelec.com/
   - **Guide Consuel** : https://www.consuel.com/
   - **Formation habilitation électrique** : Rechercher « formation habilitation électrique » + votre ville

.. admonition:: 🔧 Forum et Support

   - **Forum Mk2PVRouter** : [Lien vers forum si existe]
   - **Support technique** : [Email/Contact support]

Avertissement Final
-------------------

.. danger::
   ⚡ **DERNIER AVERTISSEMENT** ⚡

   L’installation d’un équipement électrique dans le tableau de distribution est une opération **À HAUT RISQUE** :

   - Risque de **MORT par électrocution**
   - Risque **d’INCENDIE**
   - Risque de **dégâts matériels** importants

   **Ce guide est fourni à titre informatif UNIQUEMENT.**

   **Les auteurs déclinent toute responsabilité en cas d’accident, de dommage matériel ou corporel résultant d’une installation non conforme ou réalisée par une personne non qualifiée.**

   **Pour votre sécurité et celle de votre famille, faites appel à un électricien certifié.**

   **Votre vie n’a pas de prix.**
