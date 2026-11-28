.. _assemblage-triphase:

=========================================
Assemblage — Composants triphasé
=========================================

⏱️ **Temps estimé** : 45 min–1 heure

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration triphasée (avec neutre, ou 3 × 230 V sans neutre), soudez les composants suivants en plus des composants communs.

.. hint::
   Soudez de préférence les composants les plus bas en premier : les composants déjà soudés gênent ainsi moins le retournement du :term:`PCB`.

Composants basse tension
--------------------------

.. note::
   Les connecteurs de sorties numériques (D2–D13) sont communs à toutes les configurations et déjà soudés à l’étape précédente (voir :ref:`assemblage-carte-mere`).

Connecteurs CT1–CT3
~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex SL 1×02 pour les transformateurs de courant de chaque phase.

#. Soudez **CT1** (L1), **CT2** (L2)
#. Soudez **CT3** (L3) — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — connecteurs CT1–CT3 soudés en configuration triphasée.

Résistances de burden (dépannage, CT à sortie courant uniquement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   La carte est conçue pour des CT à sortie tension **333 mV** : avec eux, il n’y a rien à souder ici. Une résistance de :term:`burden <Burden>` n’est qu’une **solution de dépannage**, si vous ne disposez que de CT à sortie courant (par ex. SCT-013-000).

   Un burden mal choisi, ou absent, peut détruire l’entrée :term:`ADC` : lisez d’abord les règles de la section :ref:`types-de-capteurs-de-courant-supportes` (CT à sortie courant).

#. Calculez la valeur de la résistance pour votre CT (voir :ref:`types-de-capteurs-de-courant-supportes`, CT à sortie courant)
#. Soudez une résistance axiale (pas de 12,7 mm) dans les **deux trous traversants** de l’empreinte de la diode :term:`TVS` :term:`CMS` **D13** pour CT1, de **D23** pour CT2 et de **D33** pour CT3 (triphasé avec neutre). Ces diodes sont déjà soudées en usine et restent en place : la résistance passe **par-dessus** (R18, R28 et R38 sur le schéma)

.. note::
   En configuration **3 × 230 V sans neutre**, la borne L3 n’est pas raccordée : FS3, GM3, RV3, GDT3, TR3 et CT3 ne servent pas.

   Seuls les CT1 et CT2 sont utilisés : l’une des phases sert de référence et n’a pas besoin de capteur (:term:`théorème de Blondel <Théorème de Blondel>`, voir :ref:`raccordement en 3 × 230 V <raccordement-3x230>`).

Composants haute tension
--------------------------

.. danger::
   Les composants de cette section sont connectés au **secteur** : 230 V entre phase et neutre, 400 V entre phases en triphasé avec neutre. Vérifiez soigneusement chaque soudure.

Paires optionnelles GDT0–GDT3 + RV0–RV3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chaque éclateur GDTx est monté **en série** avec la varistance RVx de même numéro, entre un conducteur et la terre (GDT0 avec RV0 sur le neutre, GDT1 avec RV1 sur L1, GDT2 avec RV2 sur L2, GDT3 avec RV3 sur L3). Montez-les **toujours par paire GDTx + RVx**, ou pas du tout : l’un sans l’autre ne protège rien.

Un éclateur GDTx est toujours fourni avec sa varistance RVx. Si ces paires sont dans votre kit, soudez les éclateurs à gaz **avant** les autres composants haute tension — ce sont des composants :term:`CMS` —, puis leurs varistances.

#. Soudez **GDT0** (borne N), **GDT1** (L1), **GDT2** (L2)
#. Soudez **GDT3** (L3) — **triphasé avec neutre uniquement**
#. Soudez les varistances **RV0**, **RV1**, **RV2** (radial, 300 V), et **RV3** en triphasé avec neutre uniquement (vérifiez la sérigraphie : RV, et non GM)

.. todo:: Photo à fournir — paires GDT0–GDT3 + RV0–RV3 soudées.

Fusibles FS0–FS3
~~~~~~~~~~~~~~~~~~

Les fusibles de protection de chaque conducteur (250 V ; de 0,75 à 1,25 A selon l’approvisionnement).

#. Soudez les fusibles **FS0** (borne N), **FS1** (L1), **FS2** (L2)
#. Soudez **FS3** (L3) — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — fusibles FS0–FS3 soudés.

.. warning::
   Les fusibles réagissent à la chaleur — c’est leur principe de fonctionnement. Ne chauffez pas les broches plus de **2–3 secondes** par point de soudure pour éviter de les endommager.

Connecteur secteur (5 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 5 voies (PE, N, L1, L2, L3) pour l’entrée secteur.

#. Soudez le connecteur secteur (5 voies)

.. todo:: Photo à fournir — connecteur Phoenix Contact 5 voies soudé.

Protection GM1–GM3
~~~~~~~~~~~~~~~~~~

.. warning::
   Les composants GM et les varistances ont un aspect et un pas de broches très similaires. **Vérifiez la sérigraphie** sur le :term:`PCB` : les composants de la protection de base, modules combinés ou simples varistances, vont sur les emplacements **GM**. Les emplacements **RV** ne reçoivent que les varistances des paires optionnelles GDTx + RVx.

La protection entre chaque phase et le neutre. Ces emplacements font partie de la protection de base : ils sont toujours équipés. Selon l’approvisionnement, le kit fournit pour eux des varistances combinées :term:`GDT`\+\ :term:`MOV` (GM), difficiles à trouver en petites quantités, ou de simples varistances, qui se soudent de la même façon.

#. Soudez les composants fournis (GM ou varistances) sur les emplacements **GM1** et **GM2** (vérifiez la sérigraphie)
#. Soudez celui de l’emplacement **GM3** — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — GM1–GM3 soudés (montrer la différence entre les emplacements GM et RV).

Transformateurs de tension TR1–TR3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les transformateurs :term:`ZMPT101K` pour la mesure de tension de chaque phase.

#. Soudez **TR1** (L1), **TR2** (L2)
#. Soudez **TR3** (L3) — **triphasé avec neutre uniquement**

.. todo:: Photo à fournir — transformateurs TR1–TR3 soudés.

.. note::
   En configuration **3 × 230 V sans neutre** (3 fils), l’une des phases est raccordée sur la borne N du routeur et sert de référence : TR1 et TR2 mesurent la tension des deux autres phases par rapport à elle. Seuls TR1 et TR2 sont donc nécessaires (voir :ref:`raccordement en 3 × 230 V <raccordement-3x230>`).

Condensateur film C1
~~~~~~~~~~~~~~~~~~~~~

Le condensateur de filtrage secteur 1 µF / 310 VAC (classe X2).

#. Soudez le condensateur **C1** — composant non polarisé

.. todo:: Photo à fournir — condensateur film C1 soudé.

Module d’alimentation PS1 (MPC10-5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le module d’alimentation AC-DC convertit le 230 VAC en 5 VDC (10 W).

#. Positionnez le module **PS1** sur le :term:`PCB`
#. Vérifiez l’orientation selon la sérigraphie
#. Soudez toutes les broches

.. todo:: Photo à fournir — module PS1 soudé, orientation correcte visible.

Self de mode commun FL1
~~~~~~~~~~~~~~~~~~~~~~~~

La self de mode commun (Schaffner) filtre les perturbations électromagnétiques sur les lignes secteur.

#. Positionnez **FL1** sur le :term:`PCB`
#. Soudez les broches

.. todo:: Photo à fournir — self de mode commun FL1 soudée.

.. admonition:: ✅ Point de Contrôle — Composants Triphasé

   Avant de continuer, vérifiez :

   **Basse tension :**

   | ☐ Connecteurs CT1–CT2 soudés (+ CT3 si triphasé avec neutre)

   **Haute tension :**

   | ☐ GDT0–GDT2 soudés, + GDT3 si triphasé avec neutre (si les paires GDTx + RVx sont montées)
   | ☐ Fusibles FS0–FS2 soudés (+ FS3 si triphasé avec neutre)
   | ☐ Connecteur secteur (5 voies) soudé
   | ☐ GM1–GM2 soudés (+ GM3 si triphasé avec neutre)
   | ☐ Varistances RV0–RV2 (+ RV3 si triphasé avec neutre) soudées, avec leur GDT, par paire
   | ☐ Transformateurs TR1–TR2 soudés (+ TR3 si triphasé avec neutre)
   | ☐ Condensateur film C1 soudé
   | ☐ Module d’alimentation PS1 soudé et orienté correctement
   | ☐ Self de mode commun FL1 soudée

   | ☐ Toutes les soudures propres et brillantes

Inspection finale
-----------------

Avant de passer aux tests électriques, effectuez une inspection minutieuse de toute la carte.

.. admonition:: ✅ Point de Contrôle Final — Assemblage Carte-Mère

   | ☐ **Toutes les soudures vérifiées** : brillantes, sans pont, sans soudure froide
   | ☐ **Pas de morceaux de pattes** coupées sur la carte
   | ☐ **Pas de flux de soudure** résiduel entre les pistes
   | ☐ **Support IC1 vide** (ATmega328P PAS encore inséré)
   | ☐ **Cavaliers configurés** selon votre configuration
   | ☐ **Composants orientés** vérifiés (support IC1, module PS1)
   | ☐ **Carte propre** et exempte de débris

Passez ensuite au chapitre :ref:`tests-electriques` pour vérifier le bon fonctionnement de la carte.
