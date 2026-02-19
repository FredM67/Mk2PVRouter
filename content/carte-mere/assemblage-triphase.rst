.. _assemblage-triphase:

=========================================
Assemblage — Composants triphasé
=========================================

⏱️ **Temps estimé** : 45 min-1 heure

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration triphasée (avec ou sans neutre), soudez les composants suivants en plus des composants communs.

Fusibles FS0–FS3
-----------------

Les porte-fusibles pour la protection de toutes les phases et du neutre (1 A × 250 V).

#. Soudez les porte-fusibles **FS0** (neutre), **FS1** (L1), **FS2** (L2), **FS3** (L3)

Modules de protection GM1–GM3
------------------------------

Les modules varistance combinées GDT+MOV pour la protection de chaque phase.

#. Soudez les modules **GM1**, **GM2**, **GM3**

Transformateurs de tension TR1–TR3
-----------------------------------

Les transformateurs :term:`ZMPT101K` pour la mesure de tension de chaque phase.

#. Soudez **TR1** (L1), **TR2** (L2)
#. Soudez **TR3** (L3) — **triphasé avec neutre uniquement**

.. note::
   En configuration **sans neutre** (3 fils), le théorème de Blondel permet de déduire la tension L3 à partir de L1 et L2. Seuls TR1 et TR2 sont donc nécessaires.

Connecteurs CT1–CT3
--------------------

Les connecteurs Molex SL 1×02 pour les transformateurs de courant de chaque phase.

#. Soudez **CT1** (L1), **CT2** (L2)
#. Soudez **CT3** (L3) — **triphasé avec neutre uniquement**

.. note::
   En configuration **sans neutre**, le courant L3 est déduit des mesures de L1 et L2 (théorème de Blondel : N−1 capteurs suffisent pour N conducteurs).

Connecteur secteur (5 voies)
-----------------------------

Le connecteur Phoenix Contact 5 voies (PE, N, L1, L2, L3) pour l'entrée secteur.

#. Soudez le connecteur secteur (5 voies)

Protection optionnelle (RV0–RV3, GDT0–GDT3)
---------------------------------------------

Si fournis dans votre kit, soudez les composants de protection supplémentaires :

#. Varistances **RV0**, **RV1**, **RV2**, **RV3** (radial, 300 V)
#. Éclateurs à gaz **GDT0**, **GDT1**, **GDT2**, **GDT3**

.. admonition:: ✅ Point de Contrôle — Composants Triphasé

   Avant de continuer, vérifiez :

   | ☐ Fusibles FS0–FS3 soudés
   | ☐ Modules GM1–GM3 soudés
   | ☐ Transformateurs TR1–TR2 soudés (+ TR3 si triphasé avec neutre)
   | ☐ Connecteurs CT1–CT2 soudés (+ CT3 si triphasé avec neutre)
   | ☐ Connecteur secteur (5 voies) soudé
   | ☐ Protections optionnelles soudées (si fournies)
   | ☐ Toutes les soudures propres et brillantes

Inspection finale
-----------------

Avant de passer aux tests électriques, effectuez une inspection minutieuse de toute la carte.

.. admonition:: ✅ Point de Contrôle Final — Assemblage Carte-Mère

   | ☐ **Toutes les soudures vérifiées** : brillantes, sans pont, sans soudure froide
   | ☐ **Pas de morceaux de pattes** coupées sur la carte
   | ☐ **Pas de flux de soudure** résiduel entre les pistes
   | ☐ **Support IC1 vide** (ATmega328P PAS encore inséré)
   | ☐ **Cavaliers configurés** selon votre configuration
   | ☐ **Composants polarisés** vérifiés (C3)
   | ☐ **Carte propre** et exempte de débris

Passez ensuite au chapitre :ref:`tests-electriques` pour vérifier le bon fonctionnement de la carte.

.. |br| raw:: html

  <br/>
