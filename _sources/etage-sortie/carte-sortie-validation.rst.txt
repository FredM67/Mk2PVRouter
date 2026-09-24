.. _carte-sortie-validation:

==========================================
Validation et Dépannage — Carte de Sortie
==========================================

Problème 1 : Lampe Ne S’Allume Jamais
-------------------------------------

**Causes possibles :**

☐ :term:`Optocoupleur` mal inséré (sens inversé)

   **Test** : Retirer optocoupleur, vérifier repère alignement, réinsérer

☐ :term:`Optocoupleur` défectueux

   **Test** : Remplacer par optocoupleur neuf

☐ Résistance R1 mal soudée ou mauvaise valeur

   **Test** : Vérifier continuité, mesurer résistance (120 Ω pour 3,3 V, 180 Ω pour 5 V)

☐ :term:`Triac` défectueux (circuit ouvert)

   **Test** : Mesurer résistance bornes triac (devrait être quelques Ω dans un sens)

☐ Soudure froide sur patte :term:`triac <Triac>`

   **Action** : Refaire soudures triac avec fer très chaud (450 °C)

Problème 2 : Lampe Reste Allumée en Permanence
----------------------------------------------

**Causes possibles :**

☐ :term:`Triac` en court-circuit (détruit)

   **Cause probable** : Surchauffe lors soudure, décharge électrostatique

   **Action** : Remplacer triac (attention ESD lors manipulation)

☐ Pont de soudure entre bornes :term:`triac <Triac>`

   **Test** : Inspection visuelle loupe, vérifier continuité

   **Action** : Retirer excédent soudure avec tresse

☐ Condensateur parasite (rare)

   **Action** : Vérifier pistes :term:`PCB` pas de court-circuit

Problème 3 : Grésillement ou Arc Électrique
-------------------------------------------

**Causes possibles :**

☐ Soudure insuffisante sur agrafes cuivre

   **Symptôme** : Arc entre agrafe et piste :term:`PCB`

   **Action** : **ARRÊTER IMMÉDIATEMENT**, refaire soudures avec beaucoup de soudure

☐ Écart entre :term:`triac <Triac>` et :term:`PCB` (mauvais contact)

   **Action** : Dessouder triac, aplatir pattes, ressouder avec triac bien plaqué

☐ Condensateur de snubber manquant (si prévu sur schéma)

   **Action** : Ajouter condensateur + résistance snubber selon schéma

Problème 4 : Carte Chauffe Excessivement
----------------------------------------

**Causes possibles :**

☐ Résistance de contact trop élevée

   **Diagnostic** : Mesurer tension chute entre agrafe et piste (< 0,1 V attendu)

   **Action** : Refaire soudures avec fer 450 °C + soudure abondante

☐ Section agrafes cuivre insuffisante

   **Action** : Remplacer par cuivre 2,5 mm² au lieu de 1,5 mm²

☐ Charge trop importante pour le dissipateur (> 3 000 W ~ 13 A)

   **Action** : Vérifier puissance charge (doit être ≤ 3 000 W), utiliser dissipateur plus grand si besoin

Validation Finale de la Carte
------------------------------

Checklist Avant Installation
----------------------------

.. admonition:: ✅ Validation Complète — Carte de Sortie

   Avant de considérer la carte comme validée :

   ☐ **Test fonctionnel réussi** : Lampe s’allume/s’éteint correctement

   ☐ **Test charge 100 W réussi** : 5 minutes sans problème

   ☐ **Température acceptable** : Carte et :term:`triac <Triac>` < 60 °C

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
- **Valeur R1** : _____ Ω (120 Ω pour 3,3 V, 180 Ω pour 5 V)
- **Valeur R2** : _____ Ω (330 Ω)
- **Valeur R3** : _____ Ω (360 Ω)
- **Référence :term:`triac <Triac>`** : __________ (ex :  BTA41-600B)
- **Charge testée** : _____ W (ex : 100 W)
- **Durée test** : _____ minutes
- **Résultat** : ☐ ✅ Validée  ☐ ❌ Défectueuse

Prochaines Étapes
-----------------

Après Validation de TOUTES les Cartes
-------------------------------------

Une fois que vous avez assemblé et testé avec succès :

✅ **Carte-mère** (monophasée ou triphasée) — testée électriquement

✅ **Toutes les cartes de sortie** (autant que de sorties souhaitées) — testées individuellement

**Vous pouvez passer aux chapitres suivants :**

#. **Perçages du boîtier** — :ref:`percage-carte-mere`

   Préparer le boîtier pour accueillir les cartes et les dissipateurs

#. **Câblage interne**

   Connexion carte-mère ↔ cartes de sortie ↔ secteur

#. **Montage des dissipateurs**

   Fixation des triacs sur dissipateurs thermiques en façade

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
-----------------------

- **Datasheet** :term:`triac <Triac>` BTA41 : Caractéristiques électriques, courbes thermiques
- **Datasheet** :term:`optocoupleur <Optocoupleur>` MOC3043 : Schéma interne, caractéristiques LED
- **Guide soudure haute puissance** : :ref:`soldering-tutorial`

.. admonition:: 🎯 Récapitulatif Final

   **Vous avez maintenant assemblé une carte de sortie triac fonctionnelle !**

   Cette carte utilise un :term:`triac <Triac>` BTA41 (40 A nominaux) mais, en raison de la taille du dissipateur, la charge est limitée à **3 000 W** (~13 A à 230 V) pour un fonctionnement sûr et fiable.

   **Points clés à retenir :**

   - Soudures haute puissance = **CRITIQUE** pour sécurité
   - Test progressif (sans tension → basse charge → haute charge)
   - :term:`Triac` fonctionne UNIQUEMENT avec charges résistives
   - Commutation silencieuse = avantage majeur vs relais mécanique

   **Félicitations pour votre travail minutieux ! 🎉**

.. |br| raw:: html

  <br/>

