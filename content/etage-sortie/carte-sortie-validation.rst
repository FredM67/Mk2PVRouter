.. _carte-sortie-validation:

==========================================
Validation et Dépannage — Carte de Sortie
==========================================

Problème 1 : Lampe Ne S’Allume Jamais
-------------------------------------

**Causes possibles :**

☐ Câble de commande inversé

   **Test** : la broche 2 du connecteur Molex doit porter le signal (+), la broche 1 la masse ; inversé, la LED de l’optocoupleur n’est jamais alimentée

☐ :term:`Optocoupleur` mal inséré (sens inversé)

   **Test** : Retirer optocoupleur, vérifier repère alignement, réinsérer

☐ :term:`Optocoupleur` défectueux

   **Test** : Remplacer par optocoupleur neuf

☐ Résistance R1 mal soudée ou mauvaise valeur

   **Test** : Vérifier continuité, mesurer résistance (220 Ω pour 3,3 V, 390 Ω pour 5 V)

☐ :term:`Triac` défectueux (circuit ouvert)

   **Test** : un triac ouvert ne se distingue pas d’un triac sain à l’ohmmètre : hors tension, les deux bornes extérieures du connecteur de puissance donnent quelques MΩ ou OL dans les deux sens dans les deux cas. Si toutes les autres causes sont écartées, remplacer le triac

☐ Soudure froide sur patte :term:`triac <Triac>`

   **Action** : Refaire soudures triac avec fer très chaud (450 °C)

Problème 2 : Lampe Reste Allumée en Permanence
----------------------------------------------

**Causes possibles :**

☐ :term:`Triac` en court-circuit (détruit)

   **Test** : hors tension, une résistance de quelques ohms entre les deux bornes extérieures du connecteur de puissance confirme le court-circuit

   **Cause probable** : Surchauffe lors soudure, décharge électrostatique

   **Action** : Remplacer triac (attention ESD lors manipulation)

☐ Pont de soudure entre bornes :term:`triac <Triac>`

   **Test** : Inspection visuelle loupe, vérifier continuité

   **Action** : Retirer excédent soudure avec tresse

☐ :term:`Optocoupleur` défectueux (sortie en court-circuit)

   **Action** : Remplacer l’optocoupleur

Problème 3 : Grésillement ou Arc Électrique
-------------------------------------------

**Causes possibles :**

☐ Soudure insuffisante sur agrafes cuivre

   **Symptôme** : Arc entre agrafe et piste :term:`PCB`

   **Action** : **ARRÊTER IMMÉDIATEMENT**, refaire soudures avec beaucoup de soudure

☐ Écart entre :term:`triac <Triac>` et :term:`PCB` (mauvais contact)

   **Action** : Dessouder le triac, aplatir les pattes, ressouder avec triac bien plaqué

Problème 4 : Carte Chauffe Excessivement
----------------------------------------

**Causes possibles :**

☐ Résistance de contact trop élevée

   **Diagnostic** : hors tension, contrôle visuel et mécanique des soudures d’agrafes ; après un test en charge (secteur coupé et fiche débranchée), une agrafe nettement plus chaude que l’autre signale une mauvaise soudure

   **Action** : Refaire soudures avec fer 450 °C + soudure abondante

☐ Section agrafes cuivre insuffisante

   **Action** : Refaire les agrafes en cuivre massif 1,5 mm² (les trous de 1,5 mm n’acceptent pas de fil plus gros) et les souder généreusement

☐ Charge trop importante pour le dissipateur (> 3 000 W ~ 13 A)

   **Action** : Vérifier puissance charge (doit être ≤ 3 000 W), utiliser dissipateur plus grand si besoin

Validation Finale de la Carte
------------------------------

Checklist Avant Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: ✅ Validation Complète — Carte de Sortie

   Avant de considérer la carte comme validée :

   ☐ **Test fonctionnel réussi** : Lampe s’allume/s’éteint correctement

   ☐ **Tests réussis** : lampe (2 minutes) et, si effectué, test en charge (5 minutes) sans problème

   ☐ **Température acceptable** : dissipateur < 60 °C, vérifiée secteur coupé et fiche débranchée

   ☐ **Aucune odeur ou fumée** durant tous les tests

   ☐ **Soudures haute puissance re-vérifiées** visuellement (loupe)

   ☐ **Pas de grésillement** ni arc électrique

   ☐ **Commutation silencieuse** (caractéristique du triac)

   ☐ **Documentation** : Valeurs R1-R3 notées, tension système (3,3 V ou 5 V) notée

   **Si TOUS les points sont cochés → La carte est validée et prête pour montage final**

Documentation de la Carte Testée
--------------------------------

Il est recommandé de noter sur un papier (à conserver avec la carte) :

- **Date du test** : ___/___/______
- **Tension système** : ☐ 3,3 V  ☐ 5 V
- **Valeur R1** : _____ Ω (220 Ω pour 3,3 V, 390 Ω pour 5 V)
- **Valeur R2** : _____ Ω (330 Ω)
- **Valeur R3** : _____ Ω (360 Ω)
- **Référence :term:`triac <Triac>`** : __________ (BTA41-600B ou BTA41-800B)
- **Charge testée** : _____ W (ex : 100 W)
- **Durée test** : _____ minutes
- **Résultat** : ☐ ✅ Validée  ☐ ❌ Défectueuse

Prochaines Étapes
-----------------

Après Validation de TOUTES les Cartes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Une fois que vous avez assemblé et testé avec succès :

✅ **Carte-mère** — testée électriquement

✅ **Toutes les cartes de sortie** (autant que de sorties souhaitées) — testées individuellement

**Vous pouvez passer aux chapitres suivants :**

#. **Perçages du boîtier** — :ref:`percages`

   Préparer le boîtier pour accueillir les cartes et les dissipateurs

#. **Confection des câbles** — :ref:`confection-cables`

   Câbles de commande, de témoin LED, de prise jack et de terre

#. **Assemblage** — :ref:`assemblage-boitier`

   Fixation des dissipateurs sur les côtés du boîtier, des triacs sur les dissipateurs, puis des cartes

#. **Installation du logiciel**

   Téléversement firmware, configuration, étalonnage

#. **Tests système complet**

   Validation fonctionnelle de l’ensemble avant installation finale

.. tip::
   💡 **Conseil Important**

   **Conservez les cartes de sortie testées dans un endroit propre et sec.**

   Évitez de toucher les pistes haute tension avec les doigts (graisse → oxydation).

   Si stockage prolongé (> 1 mois), protégez avec film antistatique.

Ressources Complémentaires
---------------------------

Documentation Technique
~~~~~~~~~~~~~~~~~~~~~~~

- **Datasheet** :term:`triac <Triac>` BTA41 : Caractéristiques électriques, courbes thermiques
- **Datasheet** :term:`optocoupleur <Optocoupleur>` MOC3043 : Schéma interne, caractéristiques LED
- **Guide soudure haute puissance** : :ref:`soldering-haute-puissance`

.. admonition:: 🎯 Récapitulatif Final

   **Vous avez maintenant assemblé une carte de sortie triac fonctionnelle !**

   Cette carte utilise un :term:`triac <Triac>` BTA41 (41 A nominaux) mais, en raison de la taille du dissipateur, la charge est limitée à **3 000 W** (~13 A à 230 V) pour un fonctionnement sûr et fiable.

   **Points clés à retenir :**

   - Soudures haute puissance = **CRITIQUE** pour sécurité
   - Test progressif (sans tension → basse charge → haute charge)
   - :term:`Triac` fonctionne UNIQUEMENT avec charges résistives
   - Commutation silencieuse = avantage majeur vs relais mécanique

   **Félicitations pour votre travail minutieux ! 🎉**
