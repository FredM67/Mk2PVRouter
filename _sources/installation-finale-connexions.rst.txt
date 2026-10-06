.. _installation-finale-connexions:

Capteurs de Courant et Connexions Électriques
==============================================

Installation des Capteurs de Courant (:term:`CT`)
---------------------------------------------------

Les capteurs de courant (Current Transformers) se placent sur les câbles d'alimentation principale.

Emplacement des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^

**CT Grille — Mesure de la consommation/injection réseau**

Les :term:`CT` Grille sont des capteurs à clip installés sur les câbles de **phase** principaux, entre le compteur et le tableau électrique. Ils mesurent le bilan énergétique du foyer (consommation ou injection).

- **Monophasé** : 1 :term:`CT` à clip sur la phase unique (CT1)
- **Triphasé avec neutre** : 3 :term:`CT` à clip sur les 3 phases (CT1, CT2, CT3)
- **Triphasé sans neutre** : 2 :term:`CT` suffisent (CT1, CT2) — :term:`théorème de Blondel <Théorème de Blondel>`

**CT Diversion — Mesure de la puissance routée** (optionnel)

Le :term:`CT` Diversion est installé sur le câble de phase reliant l'étage de sortie à la charge (chauffe-eau). Il mesure la puissance effectivement routée vers la charge.

⚠️ Ce :term:`CT` est un **tore** (anneau fermé) à travers lequel passe le câble de phase — contrairement aux :term:`CT` Grille qui sont des capteurs à clip ouvrant. Il est monté **à l'intérieur du boîtier** du Mk2PVRouter.

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
       sortie -> ct2 [label="Phase vers charge", color="#E53935", penwidth=2];
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

       etages [label="Étages de sortie\n(triac / relais)", fillcolor="#C8E6C9", color="#388E3C"];
       routeur -> etages [label="Signal\n(Molex)", style=dashed, color="#666666"];
       etages -> charges [label="Phase(s)\nvers charges", color="#E53935", penwidth=2];
   }

.. warning::
   **Chaque CT doit correspondre à la phase connectée sur le connecteur secteur du routeur.** La phase qui passe dans CT1 doit être raccordée sur **L1**, celle qui passe dans CT2 sur **L2**, et celle qui passe dans CT3 sur **L3**. Un décalage entre les CT et les phases provoquera des mesures de puissance incorrectes.

.. note::
   Les flèches (→) sur les :term:`CT` indiquent le sens d'installation : **vers la maison** (depuis le compteur). En triphasé sans neutre, CT3 n'est pas nécessaire (:term:`théorème de Blondel <Théorème de Blondel>`).

Sens d'Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. danger::
   ⚠️ **LE SENS DES CT EST CRUCIAL**

   Un :term:`CT` installé à l'envers inversera le signe de la mesure :

   - Le routeur verra une **production** alors qu'il y a **consommation**
   - Le routeur verra une **consommation** alors qu'il y a **production**
   - **Résultat** : Le routeur fonctionnera à l'envers et **augmentera votre facture** au lieu de la réduire

**Règle de base :**

La **flèche** gravée sur le :term:`CT` doit pointer dans le **sens du flux d'énergie** :

- **CT Grille** : Flèche pointant **VERS la maison** (depuis le compteur)
- **CT Diversion** : Flèche pointant **VERS la charge** (chauffe-eau)

**Marquages K et L :**

La plupart des :term:`CT` portent des repères **K** et **L** sur le boîtier ou sur les fils du secondaire, en plus de la flèche :

- **K** (parfois noté **K**, **P1** ou **S1**) : borne qui devient **positive** quand le courant circule dans le sens de la flèche
- **L** (parfois noté **L**, **P2** ou **S2**) : borne complémentaire

Ces marquages permettent de vérifier le raccordement au connecteur de la carte :

- Si le sens du :term:`CT` est correct (flèche vers la maison) mais que la puissance affichée est **négative**, il suffit d' **inverser les deux fils** (K ↔ L) sur le connecteur Molex au lieu de retourner physiquement le CT.
- Inversement, inverser K et L revient au même que retourner le CT de 180°.

Procédure d'Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   ⚠️ **DISJONCTEUR GÉNÉRAL COUPÉ OBLIGATOIRE**

   Ne JAMAIS installer les :term:`CT` sous tension !

   Un :term:`CT` à sortie courant dont le secondaire est **ouvert** (non branché) se comporte comme un transformateur à vide : il peut développer une **tension de plusieurs centaines de volts** aux bornes de ses fils, suffisante pour provoquer un arc électrique, endommager le CT ou le circuit d'entrée de la carte.

   Même avec un CT à sortie tension (burden intégré), manipuler un CT autour d'un conducteur sous tension présente un risque d'électrocution.

#. **Couper le disjoncteur général** et vérifier absence de tension

#. **Identifier le câble de phase** principal (généralement rouge, marron ou noir)

   ⚠️ Ne PAS placer le :term:`CT` sur le neutre (bleu) ou la terre (vert/jaune)

#. **Brancher la fiche jack 3,5 mm du CT** dans la prise jack du câble adaptateur (relié au connecteur Molex de la carte) **avant** de clipser le CT sur le câble

   Le secondaire du CT doit toujours être **fermé sur sa charge** (le circuit de la carte) avant d'être traversé par un courant primaire. Clipser un CT à sortie courant sur un conducteur actif alors que son jack n'est pas branché risque de générer une surtension destructrice.

#. **Ouvrir le CT** en appuyant sur le clip de fermeture

#. **Placer le CT autour du câble de phase UNIQUEMENT**

   - Un seul conducteur doit passer dans le :term:`CT`
   - Ne pas passer plusieurs câbles ensemble (sauf si intentionnel pour mesure différentielle)

#. **Vérifier le sens** : Flèche vers la maison pour :term:`CT` Grille

#. **Refermer fermement le CT** jusqu'au clic de verrouillage

#. **Vérifier que le CT est bien clipsé** (tirer légèrement pour tester)

#. **Fixer le câble du CT** pour éviter qu'il se débranche par traction

Vérification du Sens des :term:`CT` (Après Installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Une fois le routeur sous tension (après toutes les connexions) :

#. **Allumer un appareil de forte puissance** (bouilloire 2 000 W, radiateur)

#. **Observer l'affichage du routeur** (si écran présent) ou les logs série

#. **Vérifier que la puissance affichée est POSITIVE** quand vous consommez

   - Si la puissance est **négative** alors que vous consommez → **CT à l'envers**
   - Couper le disjoncteur, retourner le :term:`CT`, retester

Connexions Électriques au Tableau
----------------------------------

.. danger::
   ⚠️⚠️⚠️ **ZONE À HAUT RISQUE — TENSION MORTELLE** ⚠️⚠️⚠️

   Les opérations suivantes présentent un risque **MAXIMAL** d'électrocution.

   **SI VOUS N'ÊTES PAS ÉLECTRICIEN QUALIFIÉ, ARRÊTEZ-VOUS ICI.**

   Faites appel à un professionnel certifié.

Protection Électrique du Système
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   **Architecture du système :**

   - Le **Mk2PVRouter lui-même** consomme moins de **5 W** (alimentation électronique uniquement)
   - Les **circuits de puissance** (triacs) sont **indépendants** et pilotent les charges
   - Chaque **charge** (chauffe-eau, radiateur) conserve sa **propre protection** existante

Le Mk2PVRouter **électronique** nécessite un disjoncteur dédié pour son alimentation :

- **Type** : Disjoncteur divisionnaire bipolaire en monophasé (Phase + Neutre), tétrapolaire en triphasé (3 Phases + Neutre)
- **Calibre** : 2 A ou 6 A (suffisant pour l'électronique < 5 W)
- **Courbe** : Type C (protection usage courant)
- **Pouvoir de coupure** : Minimum 4,5 kA (6 kA ou 10 kA recommandé)

.. important::
   ⚠️ **POURQUOI UN DISJONCTEUR DÉDIÉ ?**

   - **Isolation** : Permet de couper uniquement le routeur sans affecter les charges
   - **Protection** : Protège l'électronique du routeur uniquement
   - **Maintenance** : Facilite les interventions futures
   - **Sécurité** : En cas de défaut électronique, seul le routeur est déconnecté

.. warning::
   **Les charges restent protégées par leurs disjoncteurs d'origine**

   Le Mk2PVRouter ne remplace PAS la protection existante des charges :

   - Chauffe-eau : Conserve son disjoncteur 16 A ou 20 A
   - Radiateur : Conserve son disjoncteur adapté à sa puissance
   - Le routeur **pilote** les triacs, mais ne **protège pas** les charges

Câblage d'alimentation du Mk2PVRouter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le routeur lui-même consomme moins de 5 W (alimentation électronique uniquement). Son câble d'alimentation relie le disjoncteur dédié (voir ci-dessus) au connecteur secteur de la carte-mère (PE, N, L1 et éventuellement L2, L3) :

- **Section** : 0,75 mm² ou 1,5 mm² (largement suffisant)
- **Nombre de conducteurs** : 3 fils en monophasé (PE + N + L), 5 fils en triphasé (PE + N + L1 + L2 + L3)

Sections de câbles des charges
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les charges (chauffe-eau, radiateur…) sont raccordées aux étages de sortie, **pas à la carte-mère**. L'étage de sortie (:term:`triac <Triac>` ou relais) s'insère dans le circuit de phase existant de la charge. En général, les câbles entre le disjoncteur de la charge et la charge elle-même sont **déjà en place** et n'ont pas besoin d'être remplacés.

À titre indicatif, voici les sections minimales selon la norme NF C 15-100 :

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Puissance charge
     - Section câble minimum
     - Disjoncteur max
   * - Jusqu'à 2 300 W
     - 1,5 mm²
     - 10 A
   * - 2 300 W - 3 680 W
     - 2,5 mm²
     - 16 A
   * - 3 680 W - 5 750 W
     - 4 mm²
     - 25 A
   * - 5 750 W - 7 360 W
     - 6 mm²
     - 32 A

Pour un **chauffe-eau classique 2 000–3 000 W**, les câbles existants sont normalement en **2,5 mm²** avec disjoncteur **16 A** ou **20 A**.

Schéma de Raccordement
^^^^^^^^^^^^^^^^^^^^^^

**Monophasé (230 V) :**

Connexions entre le tableau électrique et le MK2PVRouter :

- **L (Phase)** : du disjoncteur dédié bipolaire (2 A ou 6 A) → entrée L du routeur
- **N (Neutre)** : du disjoncteur → entrée N du routeur
- **⏚ (Terre)** : du disjoncteur → entrée PE du routeur

Le raccordement des charges aux étages de sortie est détaillé dans la section suivante.

**Triphasé (3 × 230 V = 400 V) :**

Connexions entre le tableau électrique et le MK2PVRouter :

- **L1 (Phase 1)** : du disjoncteur dédié tétrapolaire (2 A ou 6 A) → entrée L1 du routeur
- **L2 (Phase 2)** : du disjoncteur → entrée L2 du routeur
- **L3 (Phase 3)** : du disjoncteur → entrée L3 du routeur
- **N (Neutre)** : du disjoncteur → entrée N du routeur
- **⏚ (Terre)** : du disjoncteur → entrée PE du routeur

Le raccordement des charges aux étages de sortie est détaillé dans la section suivante.

.. _raccordement-etages-sortie:

Raccordement des étages de sortie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chaque étage de sortie (carte :term:`triac <Triac>` ou relais) se raccorde à la fois à la carte-mère (signal de commande) et au circuit de puissance de la charge.

**Côté basse tension (signal) :**

- Reliez le connecteur Molex de l'étage de sortie à la sortie numérique correspondante de la carte-mère (D2–D13) à l'aide d'un câble Molex 2 fils.
- Chaque étage de sortie est piloté par **une seule** sortie numérique.

**Côté haute tension (puissance) :**

Le connecteur de puissance de l'étage de sortie a 3 broches : la broche centrale est inutilisée, les deux broches extérieures raccordent la **phase** en série avec la charge à travers le :term:`triac <Triac>`.

- **Entrée phase** : depuis le disjoncteur dédié à la charge → broche du connecteur de puissance
- **Sortie phase** : autre broche du connecteur de puissance → charge (chauffe-eau, radiateur…)
- **Neutre** : du disjoncteur → directement à la charge (ne passe **pas** par l'étage de sortie)
- **Terre** : du disjoncteur → directement à la charge et au dissipateur du triac

.. warning::
   Le :term:`triac <Triac>` ne coupe que la **phase**. Le neutre reste connecté en permanence à la charge. Pour intervenir sur la charge, il faut couper son disjoncteur dédié.

.. important::
   Chaque charge pilotée doit être protégée par son **propre disjoncteur**, distinct du disjoncteur d'alimentation du routeur.

Chaque étage de sortie constitue un **circuit de puissance indépendant**. Le nombre d'étages de sortie dépend du nombre de charges à piloter, pas de la configuration du routeur :

- **Charge monophasée** (chauffe-eau classique, radiateur) : **1 étage de sortie** par charge, protégé par un disjoncteur bipolaire (16 A ou 20 A selon la puissance).
- **Charge triphasée sans neutre** (chauffe-eau triphasé en triangle) : **2 étages de sortie** pour la même charge, protégés par un **unique disjoncteur tétrapolaire**.
- **Charge triphasée avec neutre** (chauffe-eau triphasé en étoile) : **3 étages de sortie** pour la même charge, protégés par un **unique disjoncteur tétrapolaire**.

.. warning::
   Pour une charge triphasée, tous les étages de sortie associés doivent être protégés par un **seul disjoncteur multipolaire**. L'utilisation de disjoncteurs unipolaires séparés est dangereuse : en cas de coupure d'une seule phase, la charge triphasée peut être endommagée ou provoquer un déséquilibre.

Procédure de Connexion (Électricien Qualifié)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **COUPER le disjoncteur général** du tableau

#. **Vérifier l'absence de tension** avec multimètre ET testeur sans contact

#. **Attendre 5 minutes** (décharge des condensateurs éventuels)

#. **Porter les EPI** (gants isolants, chaussures de sécurité)

#. **Installer le disjoncteur dédié du routeur** dans le tableau (2 A ou 6 A, voir ci-dessus)

#. **Vérifier les disjoncteurs des charges** pilotées (un disjoncteur par charge monophasée, un disjoncteur multipolaire par charge triphasée)

#. **Connecter les câbles d'alimentation** au disjoncteur :

   - Phase (L) : Câble rouge/marron/noir
   - Neutre (N) : Câble bleu
   - Terre (⏚) : Câble vert/jaune

#. **Connecter les câbles vers le Mk2PVRouter** :

   - Respecter les couleurs (Phase, Neutre, Terre)
   - Serrer les connexions au couple recommandé (tournevis dynamométrique)
   - Vérifier qu'aucun brin de cuivre ne dépasse du bornier

#. **Connecter les étages de sortie** aux charges via leurs connecteurs de puissance (voir :ref:`raccordement-etages-sortie`)

#. **Vérifier toutes les connexions** (tirer légèrement sur chaque câble)

#. **Vérifier qu'aucun outil ne reste dans le tableau**
