.. _assemblage-triphase:

=========================================
Assemblage — Composants triphasé
=========================================

⏱️ **Temps estimé** : 45 min–1 heure

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration triphasée (avec ou sans neutre), soudez les composants suivants en plus des composants communs.

.. hint::
   Les composants sont listés du plus bas au plus haut dans chaque groupe. En soudant dans cet ordre, les composants déjà soudés ne gênent pas le retournement du :term:`PCB`.

Composants basse tension
--------------------------

.. note::
   Les connecteurs de sorties numériques (D2–D13) sont communs à toutes les configurations et déjà soudés à l'étape précédente (voir :ref:`assemblage-carte-mere`).

Connecteurs CT1–CT3
~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex SL 1×02 pour les transformateurs de courant de chaque phase.

#. Soudez **CT1** (L1), **CT2** (L2)
#. Soudez **CT3** (L3) — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — connecteurs CT1–CT3 soudés en configuration triphasée.

.. note::
   En configuration **sans neutre**, le courant L3 est déduit des mesures de L1 et L2 (:term:`théorème de Blondel` : N−1 capteurs suffisent pour N conducteurs).

Composants haute tension
--------------------------

.. danger::
   Les composants de cette section sont connectés au **secteur 230 V**. Vérifiez soigneusement chaque soudure.

Éclateurs à gaz GDT0–GDT3 (optionnel, CMS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si fournis dans votre kit, soudez les éclateurs à gaz **avant** les autres composants haute tension — ce sont des composants :term:`CMS`.

#. Soudez **GDT0**, **GDT1**, **GDT2**, **GDT3**

.. todo:: Photo à fournir — GDT0–GDT3 soudés (composants CMS).

Fusibles FS0–FS3
~~~~~~~~~~~~~~~~~~

Les porte-fusibles pour la protection de toutes les phases et du neutre (1 A × 250 V).

#. Soudez les porte-fusibles **FS0** (neutre), **FS1** (L1), **FS2** (L2), **FS3** (L3)

.. todo:: Photo à fournir — porte-fusibles FS0–FS3 soudés.

.. warning::
   Les fusibles réagissent à la chaleur — c'est leur principe de fonctionnement. Ne chauffez pas les broches plus de **2–3 secondes** par point de soudure pour éviter de les endommager.

Connecteur secteur (5 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 5 voies (PE, N, L1, L2, L3) pour l'entrée secteur.

#. Soudez le connecteur secteur (5 voies)

.. todo:: Photo à fournir — connecteur Phoenix Contact 5 voies soudé.

Protection GM1–GM3 et varistances RV0–RV3 (optionnelles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   Les composants GM et RV ont un aspect et un pas de broches très similaires. **Vérifiez la sérigraphie** sur le :term:`PCB` avant de souder chaque composant pour ne pas les intervertir. Si vous n'avez que les GM (sans RV), assurez-vous de les placer sur les emplacements **GM** et non sur les emplacements RV.

Les varistances combinées :term:`GDT`\+\ :term:`MOV` pour la protection de chaque phase.

#. Soudez les composants **GM1**, **GM2**, **GM3** sur leurs emplacements respectifs (vérifiez la sérigraphie)

Si fournies dans votre kit, soudez les varistances optionnelles :

#. Soudez les varistances **RV0**, **RV1**, **RV2**, **RV3** (radial, 300 V) sur leurs emplacements respectifs

.. todo:: Photo à fournir — GM1–GM3 et varistances RV0–RV3 soudés (montrer la différence entre GM et RV).

Transformateurs de tension TR1–TR3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les transformateurs :term:`ZMPT101K` pour la mesure de tension de chaque phase.

#. Soudez **TR1** (L1), **TR2** (L2)
#. Soudez **TR3** (L3) — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — transformateurs TR1–TR3 soudés.

.. note::
   En configuration **sans neutre** (3 fils), le :term:`théorème de Blondel` permet de déduire la tension L3 à partir de L1 et L2. Seuls TR1 et TR2 sont donc nécessaires.

Condensateur film C1
~~~~~~~~~~~~~~~~~~~~~

Le condensateur de filtrage secteur 1 µF / 310 VAC (classe X2).

#. Soudez le condensateur **C1** — composant non polarisé

.. todo:: Photo à fournir — condensateur film C1 soudé.

Module d'alimentation PS1 (MPC10-5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le module d'alimentation AC-DC convertit le 230 VAC en 5 VDC (3 W).

#. Positionnez le module **PS1** sur le :term:`PCB`
#. Vérifiez l'orientation selon la sérigraphie
#. Soudez toutes les broches

.. todo:: Photo à fournir — module PS1 soudé, orientation correcte visible.

Self de mode commun FL1
~~~~~~~~~~~~~~~~~~~~~~~~

La self de mode commun (Schaffner) filtre les perturbations électromagnétiques sur les lignes secteur.

#. Positionnez **FL1** sur le :term:`PCB`
#. Soudez les broches

.. todo:: Photo à fournir — self de mode commun FL1 soudée.

.. admonition:: ✅ Point de Contrôle — Composants Triphasé

   Avant de continuer, vérifiez :

   **Basse tension :**

   | ☐ Connecteurs CT1–CT2 soudés (+ CT3 si triphasé avec neutre)

   **Haute tension :**

   | ☐ GDT0–GDT3 soudés (si fournis)
   | ☐ Fusibles FS0–FS3 soudés
   | ☐ Connecteur secteur (5 voies) soudé
   | ☐ GM1–GM3 soudés
   | ☐ Varistances RV0–RV3 soudées (si fournies)
   | ☐ Transformateurs TR1–TR2 soudés (+ TR3 si triphasé avec neutre)
   | ☐ Condensateur film C1 soudé
   | ☐ Module d'alimentation PS1 soudé et orienté correctement
   | ☐ Self de mode commun FL1 soudée

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
