.. _introduction:

Introduction
============

| Cette documentation couvre le Mk2PVRouter basé sur la carte universelle **3phaseDiverter**.
| Une seule carte-mère supporte toutes les configurations : monophasé, triphasé avec neutre, triphasé sans neutre et split-phase.
| La configuration se fait par le choix des composants à souder et la position des cavaliers (voir :ref:`choix-configuration`).

.. danger::
   ⚠️ **SÉCURITÉ AVANT TOUT** : Avant de commencer l’assemblage, lisez impérativement le chapitre :ref:`safety-overview`.

   Ce projet implique la manipulation de composants électroniques sensibles et, plus tard, de tensions dangereuses (230 V).

**Niveau de difficulté :** 🔧🔧🔧 Intermédiaire

- Nécessite des compétences de base en soudure
- Une bonne dextérité manuelle
- De la patience et de la minutie

**Durée totale estimée :**

⏱️ **Temps d’assemblage complet :**
   - Débutant en soudure : 12-15 heures (réparties sur plusieurs sessions)
   - Expérience intermédiaire : 8-10 heures
   - Expérimenté : 5-7 heures

.. tip::
   Il est recommandé de travailler par sessions de 2-3 heures maximum pour maintenir concentration et précision.

-------------

Contenu du kit
--------------

Dans le kit, vous trouverez :

* le circuit imprimé (:term:`PCB`) de la carte-mère universelle (composants :term:`CMS` déjà soudés en usine)
* les composants traversants à souder (le nombre dépend de votre configuration, voir :ref:`choix-configuration`)
* un ou plusieurs circuits imprimés pour chaque sortie :term:`triac`
* des composants électroniques (résistances, condensateurs…). |br|
  Attention, certains sont sensibles à l’électricité statique, il faut donc les manipuler avec soin.
* un boîtier
* des câbles

Étapes d’assemblage
-------------------

L’assemblage complet va nécessiter plusieurs étapes :

#. Soudure des composants traversants sur la carte-mère (voir :ref:`assemblage-carte-mere`)
#. Tests électriques de la carte-mère (voir :ref:`tests-electriques`)
#. Soudure et tests de la ou les cartes de sortie (voir :ref:`carte-sortie`)
#. Perçage du boîtier et des dissipateurs thermiques (voir :ref:`percages`)
#. Montage des circuits soudés dans le boîtier (voir :ref:`assemblage-boitier`)
#. Confection des câbles et câblage (voir :ref:`confection-cables`)
#. Installation du logiciel et firmware (voir chapitre :ref:`installation-logiciel`)
#. Tests logiciels et étalonnage (voir :ref:`test-logiciel` et :ref:`etalonnage`)

**Durées indicatives par étape :**

.. list-table::
   :header-rows: 1
   :widths: 50 25 25

   * - Étape
     - Débutant
     - Expérimenté
   * - Soudure carte-mère + tests
     - 3-4 h
     - 1,5-2 h
   * - Soudure cartes sortie + tests
     - 1,5-2 h
     - 45 min-1 h
   * - Perçages
     - 2-3 h
     - 1-1,5 h
   * - Montage dans boîtier
     - 1-2 h
     - 30 min-1 h
   * - Câblage
     - 2-3 h
     - 1-1,5 h
   * - Logiciel + étalonnage
     - 3-4 h
     - 2-3 h

Recommandations pour les étapes de soudure
------------------------------------------

Les composants électroniques nécessaires sont très divers. Certains sont passifs (comme les résistances), tandis que d’autres sont actifs (comme l’AtMega328P).
Tous ces composants sont généralement sensibles à l’électricité statique.
Il est donc essentiel de les manipuler avec soin et, si possible, de se mettre à la terre pour éviter toute décharge électrostatique.

Composants Polarisés — Explication pour Débutants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Certains composants ont un **SENS OBLIGATOIRE** (comme une pile : + et -).

.. danger::
   ⚠️ Si installés à l’envers :

   - Le routeur NE FONCTIONNERA PAS
   - Le composant peut **EXPLOSER** (condensateurs électrolytiques)
   - Vous devrez potentiellement tout refaire

Composants à Surveiller
^^^^^^^^^^^^^^^^^^^^^^^

**1. Diodes** — Repérer la bande

   La bande sur la diode DOIT correspondre à la bande sur le :term:`PCB`.

   Les diodes ne laissent passer le courant que dans un sens. Si inversées, elles empêchent le circuit de fonctionner.

**2. Condensateurs électrolytiques** — Repérer la bande blanche (-)

   La bande blanche (parfois avec des signes -) indique le côté négatif.

   Ces condensateurs peuvent exploser s’ils sont soudés à l’envers !

**3. Circuits intégrés (IC)** — Repérer l’encoche ou le point

   L’encoche (ou le point marquant la broche 1) doit correspondre au dessin sur le :term:`PCB`.

   Les IC mal orientés ne fonctionneront pas et peuvent être endommagés.

**4. Régulateurs de tension** — Forme du boîtier

   Le régulateur a une forme particulière qui doit correspondre au dessin sur le :term:`PCB`.

💡 **Règle d’or :** VÉRIFIER 3 FOIS AVANT DE SOUDER !

Les composants non polarisés (résistances, condensateurs céramiques) peuvent être soudés dans n’importe quel sens.

Les composants varient également en taille, allant de quelques millimètres à plusieurs centimètres (dans le cas des transformateurs).

Pour des raisons pratiques, il est recommandé de procéder à la soudure en suivant un ordre précis basé sur la taille des composants.

Ainsi, l’ordre de soudure recommandé est le suivant :

#. Résistances et diodes, et éventuellement les ponts
#. Supports IC1 et IC2 (et éventuellement IC3, IC4 selon le kit) (ne pas insérer les circuits intégrés dans les supports à ce stade)
#. Condensateurs non polarisés « orange », oscillateur
#. Pont·s de diodes
#. Les fusibles
#. Tous les connecteurs SIL noirs et le connecteur d’affichage, le cas échéant
#. Condensateurs polarisés (noirs ou bleus)
#. Le socle pour l’antenne, le cas échéant
#. Le gros connecteur « haute tension »
#. Le·s régulateur·s de tension
#. Enfin, le·s transformateur·s

Suivre cette séquence précise permet d’éviter de tordre les pattes des composants ou d’avoir à utiliser de l’adhésif, entre autres.

Matériels nécessaires
---------------------

* fer à souder
* fil de soudure
* pince coupante
* pince à sertir les cosses ou pince multifonction
* tournevis cruciforme
* clé plate ou douille de **5,5**
* clé plate de **10**
* clé six pans de **2** et **2,5**
* une perceuse à colonne si possible, sinon n’importe quelle perceuse.
* foret métal de **3 mm**
* foret métal de **4 mm**
* foret (bois ou métal) de **8 mm**
* foret (bois ou métal) ou fraise de **20 mm**
* fraise de **35 mm**
* colle thermofusible
* gaine thermorétractable
* multimètre (au minimum voltmètre et ohmmètre)

Certains matériels sont optionnels (fraise de 35 mm, colle, gaine). Cependant, ils faciliteront certaines étapes et permettront de réaliser un travail plus soigné et mieux fini.

.. |br| raw:: html

  <br/>