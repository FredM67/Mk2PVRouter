.. _tests-electriques:

==================
Tests électriques
==================

⏱️ **Temps estimé** : 30-45 minutes

🔧 **Niveau de difficulté** : Intermédiaire

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Assemblage de la carte terminé (voir :ref:`assemblage-carte-mere`)
   | ☐ Support IC1 **vide** (ATmega328P PAS encore inséré)
   | ☐ Multimètre disponible (voltmètre et ohmmètre)
   | ☐ Câble secteur de test disponible

À ce stade, tous les composants traversants ont été soudés sur la carte-mère.

| Avant de passer aux tests, il est crucial d’effectuer une dernière vérification de chaque point de soudure.
| Assurez-vous que toutes les soudures sont propres, sans court-circuit, et que tous les composants sont correctement positionnés, qu’il ne reste pas de morceaux de pattes coupées.

Test de continuité (hors tension)
----------------------------------

Avant toute mise sous tension, effectuez les vérifications suivantes au multimètre en mode **ohmmètre/continuité** :

#. **Vérifiez l’absence de court-circuit** entre les rails d’alimentation :

   ☐ +5 V ↔ GND : doit être **circuit ouvert** (pas de continuité)

   ☐ +3,3 V ↔ GND : doit être **circuit ouvert** (pas de continuité)

#. **Vérifiez les fusibles** (si soudés) :

   ☐ Continuité à travers chaque porte-fusible (FS0, FS1, et FS2, FS3 en triphasé)

Premier test sous tension
--------------------------

.. danger::
   **TENSION SECTEUR 230 V — DANGER DE MORT**

   Ce test nécessite la connexion au secteur. Prenez toutes les précautions nécessaires :

   - Disjoncteur facilement accessible
   - Aucun contact avec la carte sous tension

.. warning::
   Le support IC1 doit être **VIDE** (pas d’ATmega328P) pendant ce test. L’insertion du microcontrôleur se fait après validation de l’alimentation.

#. **Connectez le câble secteur** au connecteur secteur (selon votre configuration)
#. **Mettez sous tension** via le disjoncteur

Test du rail +5 V
~~~~~~~~~~~~~~~~~~~

#. Réglez le multimètre en mode **voltmètre DC** (tension continue)
#. Mesurez la tension entre les points de test marqués **+5V** et **GND** sur le :term:`PCB`
#. **Valeur attendue** : **5,0 V ± 0,2 V**

   ✅ Si la tension est correcte, le module d’alimentation PS1 (RAC05E) fonctionne

   ❌ Si la tension est absente ou très différente :

   - Vérifiez les fusibles (FS0, FS1)
   - Vérifiez les soudures du module PS1
   - Vérifiez la diode TVS D1

#. **Vérifiez le condensateur C3** (polarisé) : après quelques secondes sous tension, vérifiez que C3 ne chauffe pas au toucher

   .. danger::
      Un condensateur électrolytique monté **à l’envers** peut chauffer, gonfler et éclater. Si C3 est chaud ou gonflé, **coupez immédiatement l’alimentation** et corrigez la polarité.

Test du rail +3,3 V
~~~~~~~~~~~~~~~~~~~~~

#. Mesurez la tension entre les points de test marqués **+3.3V** et **GND** sur le :term:`PCB`
#. **Valeur attendue** : **3,3 V ± 0,1 V**

   ✅ Si la tension est correcte, le régulateur :term:`LDO` U1 (AP2112K) fonctionne

   ❌ Si la tension est absente, vérifiez le rail +5 V d’abord

#. **Coupez l’alimentation secteur** et attendez 1 minute avant toute manipulation

.. note::
   La tension de référence VREF (1,1 V, bufferisée par l’amplificateur opérationnel LMV321A) ne peut être vérifiée qu’après insertion de l’ATmega328P **et** exécution du firmware. C’est le firmware qui active la référence interne 1,1 V du microcontrôleur. Ce test sera effectué lors de la phase :ref:`test-logiciel`.

Insertion de l’ATmega328P
--------------------------

.. danger::
   **COUPEZ L’ALIMENTATION SECTEUR** avant d’insérer le microcontrôleur.

.. warning::
   ⚠️ **ATTENTION** : Si l’ATmega328P est inséré à l’envers et la carte mise sous tension, le microcontrôleur sera **irrémédiablement détruit**.

#. Repérez l'**encoche** (ou le point) sur l’ATmega328P qui indique la broche 1
#. Alignez cette encoche avec celle du support IC1 et le repère sur le :term:`PCB`
#. Les broches peuvent nécessiter un léger pliage vers l’intérieur pour entrer dans le support. Utilisez une surface plane et anti-statique pour les ajuster délicatement.
#. Insérez le microcontrôleur dans le support en vérifiant qu’aucune broche ne se plie sous le composant

.. admonition:: ✅ Point de Contrôle — Tests Électriques

   Avant de passer au firmware, vérifiez :

   | ☐ **Rail +5 V** : 5,0 V ± 0,2 V ✅
   | ☐ **Rail +3,3 V** : 3,3 V ± 0,1 V ✅
   | ☐ **Pas de composant chaud** après 1 minute de fonctionnement
   | ☐ **ATmega328P inséré** correctement (encoche alignée)
   | ☐ **Aucune broche pliée** sous le microcontrôleur

.. |br| raw:: html

  <br/>
