.. _assemblage-monophase:

=========================================
Assemblage — Composants monophasé
=========================================

⏱️ **Temps estimé** : 30–45 minutes

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration monophasée, soudez les composants suivants en plus des composants communs.

.. hint::
   Soudez de préférence les composants les plus bas en premier : les composants déjà soudés gênent ainsi moins le retournement du :term:`PCB`.

Composants basse tension
--------------------------

.. note::
   Les connecteurs de sorties numériques (D2–D13) sont communs à toutes les configurations et déjà soudés à l’étape précédente (voir :ref:`assemblage-carte-mere`).

Connecteurs CT1 (et CT2 optionnel)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les connecteurs Molex SL 1×02 pour les transformateurs de courant.

#. Soudez le connecteur **CT1** (phase L1)

Si vous souhaitez mesurer la puissance de diversion (puissance routée vers la charge), soudez également le connecteur **CT2**.

.. todo:: Photo à fournir — connecteur(s) CT soudé(s) en configuration monophasée.

Résistances de burden (dépannage, CT à sortie courant uniquement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   La carte est conçue pour des CT à sortie tension **333 mV** : avec eux, il n’y a rien à souder ici. Une résistance de :term:`burden <Burden>` n’est qu’une **solution de dépannage**, si vous ne disposez que de CT à sortie courant (par ex. SCT-013-000).

   Un burden mal choisi, ou absent, peut détruire l’entrée :term:`ADC` : lisez d’abord les règles de la section :ref:`types-de-capteurs-de-courant-supportes` (CT à sortie courant).

#. Calculez la valeur de la résistance pour votre CT (voir :ref:`types-de-capteurs-de-courant-supportes`, CT à sortie courant)
#. Soudez une résistance axiale (pas de 12,7 mm) dans les **deux trous traversants** de l’empreinte de la diode :term:`TVS` :term:`CMS` **D13** pour CT1, et de **D23** si le connecteur CT2 est utilisé. Ces diodes sont déjà soudées en usine et restent en place : la résistance passe **par-dessus** (R18 et R28 sur le schéma)

Composants haute tension
--------------------------

.. danger::
   Les composants de cette section sont connectés au **secteur 230 V**. Vérifiez soigneusement chaque soudure.

Éclateurs à gaz GDT0, GDT1 (optionnel, CMS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chaque éclateur GDTx est monté **en série** avec la varistance RVx de même numéro, entre un conducteur et la terre (GDT0 avec RV0 sur le neutre, GDT1 avec RV1 sur L1). Montez-les **toujours par paire GDTx + RVx**, ou pas du tout : l’un sans l’autre ne protège rien.

Si ces paires sont fournies dans votre kit, soudez les éclateurs à gaz **avant** les autres composants haute tension — ce sont des composants :term:`CMS`.

#. Soudez **GDT0** et **GDT1**

.. todo:: Photo à fournir — GDT0 et GDT1 soudés (composants CMS).

Fusibles FS0, FS1
~~~~~~~~~~~~~~~~~~~

Les fusibles de protection de la phase et du neutre (1 A × 250 V).

#. Soudez le fusible **FS0** (neutre)
#. Soudez le fusible **FS1** (phase L1)

.. todo:: Photo à fournir — fusibles FS0 et FS1 soudés.

.. warning::
   Les fusibles réagissent à la chaleur — c’est leur principe de fonctionnement. Ne chauffez pas les broches plus de **2–3 secondes** par point de soudure pour éviter de les endommager.

Connecteur secteur (3 voies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le connecteur Phoenix Contact 3 voies (PE, N, L1) pour l’entrée secteur.

#. Soudez le connecteur secteur (3 voies)

.. todo:: Photo à fournir — connecteur Phoenix Contact 3 voies soudé.

Protection GM1 et varistances RV0, RV1 (optionnelles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   Les composants GM et RV ont un aspect et un pas de broches très similaires. **Vérifiez la sérigraphie** sur le :term:`PCB` avant de souder chaque composant pour ne pas les intervertir. Si vous n’avez que les GM (sans RV), assurez-vous de les placer sur les emplacements **GM** et non sur les emplacements RV.

La varistance combinée :term:`GDT`\+\ :term:`MOV` pour la protection de la phase L1.

#. Soudez le composant **GM1** sur son emplacement (vérifiez la sérigraphie)

Si vous montez les paires optionnelles GDTx + RVx (voir ci-dessus), soudez leurs varistances :

#. Soudez les varistances **RV0** et **RV1** (radial, 300 V) sur leurs emplacements respectifs

.. todo:: Photo à fournir — GM1 et varistances RV0/RV1 soudés (montrer la différence entre GM et RV).

Transformateur de tension TR1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le transformateur :term:`ZMPT101K` pour la mesure de tension de la phase L1.

#. Positionnez **TR1** sur le :term:`PCB`
#. Soudez les broches

.. todo:: Photo à fournir — transformateur TR1 soudé.

Condensateur film C1
~~~~~~~~~~~~~~~~~~~~~

Le condensateur de filtrage secteur 1 µF / 310 VAC (classe X2).

#. Soudez le condensateur **C1** — composant non polarisé

.. todo:: Photo à fournir — condensateur film C1 soudé.

Module d’alimentation PS1 (MPC10-5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le module d’alimentation AC-DC convertit le 230 VAC en 5 VDC (10 W).

#. Positionnez le module **PS1** sur le :term:`PCB`
#. Vérifiez l’orientation selon la sérigraphie
#. Soudez toutes les broches

.. todo:: Photo à fournir — module PS1 soudé, orientation correcte visible.

Self de mode commun FL1
~~~~~~~~~~~~~~~~~~~~~~~~

La self de mode commun (Schaffner) filtre les perturbations électromagnétiques sur les lignes secteur.

#. Positionnez **FL1** sur le :term:`PCB`
#. Soudez les broches

.. todo:: Photo à fournir — self de mode commun FL1 soudée.

.. admonition:: ✅ Point de Contrôle — Composants Monophasé

   Avant de continuer, vérifiez :

   **Basse tension :**

   | ☐ Connecteur CT1 soudé (+ CT2 si option diversion)

   **Haute tension :**

   | ☐ GDT0, GDT1 soudés (si les paires GDTx + RVx sont montées)
   | ☐ Fusibles FS0, FS1 soudés
   | ☐ Connecteur secteur (3 voies) soudé
   | ☐ GM1 soudé
   | ☐ Varistances RV0, RV1 soudées (avec GDT0, GDT1, par paire)
   | ☐ Transformateur TR1 soudé
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

Passez ensuite au chapitre :ref:`tests-electriques` pour vérifier le bon fonctionnement de la carte.
