.. _introduction:

Introduction
============

| Cette documentation couvre le Mk2PVRouter basé sur la carte universelle **3phaseDiverter**.
| Une seule carte-mère supporte toutes les configurations : monophasé, triphasé avec neutre, triphasé sans neutre et split-phase.
| La configuration se fait par le choix des composants à souder et la position des cavaliers (voir :ref:`choix-configuration`).

.. danger::
   ⚠️ **SÉCURITÉ AVANT TOUT** : Avant de commencer l’assemblage, lisez impérativement le chapitre :ref:`safety-overview`.

   Ce projet implique la manipulation de composants électroniques sensibles et, plus tard, de tensions dangereuses (230 V).

**Niveau de difficulté :** 🔧🔧🔧 Intermédiaire

- Nécessite des compétences de base en soudure
- Une bonne dextérité manuelle
- De la patience et de la minutie
- Compétences avec l’outil informatique

**Durée totale estimée :**

⏱️ **Temps d’assemblage complet :**

- Débutant en soudure : 7–9 heures (réparties sur plusieurs sessions)
- Expérience intermédiaire : 5–6 heures
- Expérimenté : 3–4 heures

.. tip::
   Il est recommandé de travailler par sessions de 2–3 heures maximum pour maintenir concentration et précision.

-------------

Contenu du kit
--------------

Dans le kit, vous trouverez :

* le circuit imprimé (:term:`PCB`) de la carte-mère universelle (composants :term:`CMS` déjà soudés en usine)
* les composants traversants à souder (le nombre dépend de votre configuration, voir :ref:`choix-configuration`)
* un ou plusieurs circuits imprimés pour chaque sortie :term:`triac <Triac>`
* une carte indicateur LED par étage de sortie (voir :ref:`carte-indicateur`)
* des composants électroniques (résistances, condensateurs…). |br|
  Attention, certains sont sensibles à l’électricité statique, il faut donc les manipuler avec soin.
* un boîtier
* des câbles

Étapes d’assemblage
-------------------

L’assemblage complet va nécessiter plusieurs étapes :

#. Soudure des composants traversants sur la carte-mère (voir :ref:`assemblage-carte-mere`)
#. Tests électriques de la carte-mère (voir :ref:`tests-electriques`)
#. Soudure et tests de la ou les cartes de sortie (voir :ref:`carte-sortie`)
#. Perçage du boîtier et des dissipateurs thermiques (voir :ref:`percages`)
#. Montage des circuits soudés dans le boîtier (voir :ref:`assemblage-boitier`)
#. Confection des câbles et câblage (voir :ref:`confection-cables`)
#. Installation du logiciel et firmware (voir chapitre :ref:`installation-logiciel`)
#. Tests logiciels et étalonnage (voir :ref:`logiciel-etalonnage-monophase` ou :ref:`logiciel-etalonnage-triphase`)

**Durées indicatives par étape :**

.. list-table::
   :header-rows: 1
   :widths: 50 25 25

   * - Étape
     - Débutant
     - Expérimenté
   * - Soudure carte-mère + tests
     - 3–4 h
     - 1,5–2 h
   * - Soudure cartes sortie + tests
     - 1,5–2 h
     - 45 min–1 h
   * - Perçages
     - 2–3 h
     - 1–1,5 h
   * - Montage dans boîtier
     - 1–2 h
     - 30 min–1 h
   * - Câblage
     - 2–3 h
     - 1–1,5 h
   * - Logiciel + étalonnage
     - 3–4 h
     - 2–3 h

Recommandations pour les étapes de soudure
------------------------------------------

La carte universelle est livrée avec tous les composants :term:`CMS` déjà soudés en usine. Vous n’avez qu’à souder les composants **traversants** (through-hole). Certains composants (microcontrôleur, optocoupleur) sont sensibles à l’électricité statique — manipulez-les avec soin et, si possible, mettez-vous à la terre pour éviter toute décharge électrostatique.

Composants polarisés
~~~~~~~~~~~~~~~~~~~~

Sur la carte-mère, un seul composant traversant est polarisé : le **condensateur électrolytique C3**.

.. warning::
   La bande blanche (signes −) sur le condensateur indique le côté **négatif**. Respectez la polarité indiquée sur le :term:`PCB`. Un condensateur électrolytique monté à l’envers peut chauffer, gonfler et éclater.

Le **support IC1** (ATmega328P) possède une encoche d’orientation qui doit correspondre au repère sur le :term:`PCB`. Le microcontrôleur sera inséré dans le support après les tests électriques.

Les autres composants traversants de la carte-mère (quartz, connecteurs, fusibles, transformateurs :term:`ZMPT101K`) ne sont pas polarisés ou ont un détrompeur mécanique.

Sur les **cartes de sortie** (étages triac), l’:term:`optocoupleur <Optocoupleur>` (MOC3043) et son support :term:`DIL` sont également orientés. Alignez le repère du composant avec le cercle sur le :term:`PCB`, et l’encoche du support avec le repère sérigraphié. Les résistances, connecteurs et le :term:`triac <Triac>` ne sont pas polarisés.

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