.. _assemblage-monophase:

=========================================
Assemblage — Composants monophasé
=========================================

⏱️ **Temps estimé** : 30-45 minutes

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Composants communs soudés et vérifiés (voir :ref:`assemblage-carte-mere`)

En configuration monophasée ou split-phase, soudez les composants suivants en plus des composants communs.

Fusibles FS0, FS1
-------------------

Les porte-fusibles pour la protection de la phase et du neutre (1 A × 250 V).

#. Soudez le porte-fusible **FS0** (neutre)
#. Soudez le porte-fusible **FS1** (phase L1)

Module de protection GM1
-------------------------

Le module varistance combinée GDT+MOV pour la protection de la phase L1.

#. Soudez le module **GM1**

Transformateur de tension TR1
------------------------------

Le transformateur :term:`ZMPT101K` pour la mesure de tension de la phase L1.

#. Positionnez **TR1** sur le :term:`PCB`
#. Soudez les broches

Connecteur CT1
---------------

Le connecteur Molex SL 1×02 pour le transformateur de courant de la phase L1.

#. Soudez le connecteur **CT1**

Connecteur CT2 (optionnel)
---------------------------

Si vous souhaitez mesurer la puissance de diversion (puissance routée vers la charge), soudez le connecteur **CT2**.

Connecteur PWR1 (3 voies)
---------------------------

Le connecteur Phoenix Contact 3 voies (Terre, Neutre, L1) pour l'entrée secteur.

#. Soudez le connecteur **PWR1** (3 voies)

Protection optionnelle (RV0, RV1, GDT0, GDT1)
------------------------------------------------

Si fournis dans votre kit, soudez les composants de protection supplémentaires :

#. Varistances **RV0** et **RV1** (radial, 300 V)
#. Éclateurs à gaz **GDT0** et **GDT1**

.. admonition:: ✅ Point de Contrôle — Composants Monophasé

   Avant de continuer, vérifiez :

   | ☐ Fusibles FS0, FS1 soudés
   | ☐ Module GM1 soudé
   | ☐ Transformateur TR1 soudé
   | ☐ Connecteur CT1 soudé (+ CT2 si option diversion)
   | ☐ Connecteur PWR1 (3 voies) soudé
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
