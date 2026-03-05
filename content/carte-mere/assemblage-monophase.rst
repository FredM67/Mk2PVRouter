.. _assemblage-monophase:

=========================================
Assemblage — Composants monophasé
=========================================

⏱️ **Temps estimé** : 30–45 minutes

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration monophasée ou split-phase, soudez les composants suivants en plus des composants communs.

.. hint::
   Les composants sont listés du plus bas au plus haut dans chaque groupe. En soudant dans cet ordre, les composants déjà soudés ne gênent pas le retournement du :term:`PCB`.

Composants basse tension
--------------------------

.. note::
   Les connecteurs de sorties numériques (D2–D13) sont communs à toutes les configurations et déjà soudés à l'étape précédente (voir :ref:`assemblage-carte-mere`).

Connecteurs CT1 (et CT2 optionnel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex SL 1×02 pour les transformateurs de courant.

#. Soudez le connecteur **CT1** (phase L1)

Si vous souhaitez mesurer la puissance de diversion (puissance routée vers la charge), soudez également le connecteur **CT2**.

.. todo:: Photo à fournir — connecteur(s) CT soudé(s) en configuration monophasée.

Composants haute tension
--------------------------

.. danger::
   Les composants de cette section sont connectés au **secteur 230 V**. Vérifiez soigneusement chaque soudure.

Éclateurs à gaz GDT0, GDT1 (optionnel, CMS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si fournis dans votre kit, soudez les éclateurs à gaz **avant** les autres composants haute tension — ce sont des composants :term:`CMS`.

#. Soudez **GDT0** et **GDT1**

.. todo:: Photo à fournir — GDT0 et GDT1 soudés (composants CMS).

Fusibles FS0, FS1
~~~~~~~~~~~~~~~~~~~

Les porte-fusibles pour la protection de la phase et du neutre (1 A × 250 V).

#. Soudez le porte-fusible **FS0** (neutre)
#. Soudez le porte-fusible **FS1** (phase L1)

.. todo:: Photo à fournir — porte-fusibles FS0 et FS1 soudés.

.. warning::
   Les fusibles réagissent à la chaleur — c'est leur principe de fonctionnement. Ne chauffez pas les broches plus de **2–3 secondes** par point de soudure pour éviter de les endommager.

Connecteur secteur (3 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 3 voies (PE, N, L1) pour l'entrée secteur.

#. Soudez le connecteur secteur (3 voies)

.. todo:: Photo à fournir — connecteur Phoenix Contact 3 voies soudé.

Protection GM1 et varistances RV0, RV1 (optionnelles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   Les composants GM et RV ont un aspect et un pas de broches très similaires. **Vérifiez la sérigraphie** sur le :term:`PCB` avant de souder chaque composant pour ne pas les intervertir. Si vous n'avez que les GM (sans RV), assurez-vous de les placer sur les emplacements **GM** et non sur les emplacements RV.

La varistance combinée :term:`GDT`\+\ :term:`MOV` pour la protection de la phase L1.

#. Soudez le composant **GM1** sur son emplacement (vérifiez la sérigraphie)

Si fournies dans votre kit, soudez les varistances optionnelles :

#. Soudez les varistances **RV0** et **RV1** (radial, 300 V) sur leurs emplacements respectifs

.. todo:: Photo à fournir — GM1 et varistances RV0/RV1 soudés (montrer la différence entre GM et RV).

Transformateur de tension TR1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le transformateur :term:`ZMPT101K` pour la mesure de tension de la phase L1.

#. Positionnez **TR1** sur le :term:`PCB`
#. Soudez les broches

.. todo:: Photo à fournir — transformateur TR1 soudé.

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

.. admonition:: ✅ Point de Contrôle — Composants Monophasé

   Avant de continuer, vérifiez :

   **Basse tension :**

   | ☐ Connecteur CT1 soudé (+ CT2 si option diversion)

   **Haute tension :**

   | ☐ GDT0, GDT1 soudés (si fournis)
   | ☐ Fusibles FS0, FS1 soudés
   | ☐ Connecteur secteur (3 voies) soudé
   | ☐ GM1 soudé
   | ☐ Varistances RV0, RV1 soudées (si fournies)
   | ☐ Transformateur TR1 soudé
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
