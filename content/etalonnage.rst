.. _etalonnage:

==========
Étalonnage
==========

⏱️ **Temps estimé** : 45 min-2 heures selon la configuration

🔧 **Niveau de difficulté** : Intermédiaire (mono) / Avancé (tri)

⚠️ **Niveau de risque** : Élevé (manipulation 230 V sous tension)

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris
   | ☐ Tests électriques effectués (voir :ref:`tests-electriques`)
   | ☐ Firmware installé et fonctionnel (voir :ref:`test-logiciel`)
   | ☐ Routeur alimenté par le secteur
   | ☐ Multimètre ou wattmètre disponible
   | ☐ Accès au compteur d’électricité

.. contents:: Sommaire
    :local:
    :depth: 2

Introduction
------------

Lorsqu’il fonctionne avec les paramètres par défaut, le routeur Mk2PVRouter peut dévier de manière fiable l’énergie excédentaire sans nécessiter d’étalonnage. Cependant, pour fournir une indication précise de l’énergie déviée, le système doit être étalonné.

Pour un étalonnage précis, une certaine forme de référence standard est nécessaire. Le compteur d’électricité installé peut souvent être utilisé à cette fin.

La plupart des compteurs d’électricité génèrent un flux d’impulsions optiques pour indiquer le taux de consommation d’énergie. En plaçant un transformateur de courant :term:`CT` autour de l’un des câbles d’alimentation entrants, et en exécutant le logiciel approprié sur le matériel en cours de test, un flux d’impulsions optiques similaire peut être généré.

.. important::
   **Configuration triphasée** : Contrairement à la version monophasée, le modèle triphasé ne peut pas dévier de manière fiable l’énergie excédentaire sans un étalonnage aussi précis que possible. En effet, étant donné qu’en triphasé, le routeur calcule la somme algébrique des puissances instantanées sur chaque phase, il faut que les mesures soient aussi précises que possible.

   Les composants électroniques ne sont jamais parfaits. Ils ont chacun des caractéristiques données accompagnées d’une tolérance. Les tolérances classiques sont de 5 ou 10 %. Il convient donc d’étalonner chaque ligne de mesure afin que la somme finale soit la plus juste possible.

.. admonition:: Ligne de mesure

   Ensemble des composants constituant la prise de mesure. Elle part de l’Arduino jusqu'à la pince ampèremétrique en passant par les résistances, connecteurs et les câbles.

Sécurité
--------

Pour cette étape d’étalonnage, il faudra potentiellement manipuler le câblage électrique. Il est donc impératif de respecter les consignes de sécurité.

.. danger::
   **ALERTE SÉCURITÉ**

   Potentiellement, selon l’appareil utilisé, il faudra modifier le câblage électrique. Avant toutes manipulations, il est impératif de couper l’alimentation au tableau électrique et de vérifier à l’aide d’un testeur de tension l’absence effective de tension.
   Dans le doute, couper le disjoncteur principal.

Principe de base
~~~~~~~~~~~~~~~~

Cet étalonnage peut être réalisé selon plusieurs méthodes, selon que l’on possède ou non certains appareils de mesure (ampèremètre, wattmètre, voltmètre).

Pour simplifier la procédure, il est important d’avoir une consommation constante pendant l’étalonnage. Par exemple, branchez un radiateur électrique ou une bouilloire et débranchez tout le reste, y compris votre/vos système·s de production d’électricité.
L’utilisation d’un appareil purement résistif, donc sans ventilateur ni autre chose qu’une résistance, simplifiera grandement l’étalonnage.

.. admonition:: Pré-requis

   Les pinces doivent être installées sur chaque phase correspondante par rapport à l’alimentation du routeur.


Étalonnage — Monophasé
-----------------------

:term:`CT` *grille/réseau*
~~~~~~~~~~~~~~~~~~~~~~~~~~

Lors de l’étalonnage d’un nouvel ensemble de matériel, la première étape consiste à étalonner le canal **CT1**. À cette fin, le matériel en cours de test doit exécuter le programme ``cal_CT1_v_meter.ino``, qui est disponible sur la page de téléchargements.

Le taux du flux d’impulsions pour le matériel en cours de test peut être ajusté en modifiant la valeur de ``powerCal_grid``. Lorsque les deux flux d’impulsions sont synchronisés, l’étalonnage correct a été atteint.

Pour chaque unité d’énergie mesurée au point de connexion au réseau via **CT1**, une impulsion sera générée au port de sortie. |br|
Le taux des impulsions peut être modifié en changeant la valeur de ``powerCal_grid``. Un flux d’impulsions similaire sera visible au compteur.

Pour avancer un flux d’impulsions par rapport à l’autre, un second chemin pour le courant devra passer à travers **CT1**. |br|
La puissance consommée par n’importe quel petit appareil fera l’affaire — un seul de ses cœurs actifs doit passer à travers **CT1** — et le courant peut circuler dans les deux sens. |br|
Lorsque l’appareil est éteint, le fil supplémentaire n’aura aucun effet sur les performances du :term:`CT`, car aucun courant ne le traverse.

Lorsque la valeur correcte a été trouvée pour ``powerCal_grid``, cette même valeur peut être utilisée avec n’importe quel croquis de routeur Mk2PVRouter qui doit être exécuté sur le **même matériel**.


.. admonition:: ✅ Point de Contrôle — Étalonnage CT Grille

   Avant de passer à l’étalonnage du :term:`CT` diversion, vérifiez :

   | ☐ **Programme cal_CT1_v_meter.ino** téléversé et fonctionnel
   | ☐ **Valeur powerCal_grid trouvée** et notée (à conserver précieusement)
   | ☐ Flux d’impulsions synchronisé avec le compteur
   | ☐ Test de vérification effectué (appareil de puissance connue)
   | ☐ Valeur stable et reproductible

:term:`CT` *diversion*
~~~~~~~~~~~~~~~~~~~~~~

Ayant obtenu la valeur correcte pour ``powerCal_grid``, le canal *grid* peut ensuite être utilisé pour étalonner le canal *diverted power* qui utilise **CT2**. |br|
À cette fin, le matériel en cours de test doit exécuter le programme ``cal_CT2_v_CT1.ino``, qui est disponible sur la page de téléchargements. |br|
Le paramètre ``powerCal_grid`` doit être réglé à la valeur correcte comme déterminé précédemment dans la première partie de ce processus.

Les deux **CTs** devraient être montés autour du même fil porteur de courant. Si **CT2** a été intégré dans un système complet, le commutateur de marche forcée peut être utilisé pour forcer le courant à travers ce câblage. |br|
Le canal **CT2** d’une carte autonome peut être étalonné en utilisant simplement un câble d’extension modifié qui fonctionne entre n’importe quelle prise de courant pratique et un appareil approprié.

Lorsque la valeur correcte a été trouvée pour ``powerCal_diverted``, cette même valeur peut être utilisée avec n’importe quel croquis de routeur Mk2PVRouter qui doit être exécuté sur le **même matériel**.


.. admonition:: ✅ Point de Contrôle — Étalonnage Monophasé Complet

   Avant de passer à l’installation finale, vérifiez :

   | ☐ **Programme cal_CT2_v_CT1.ino** téléversé avec powerCal_grid correct
   | ☐ **Valeur powerCal_diverted trouvée** et notée
   | ☐ Deux :term:`CT`\s montés autour du même fil donnent mesures identiques
   | ☐ Documentation des valeurs : powerCal_grid et powerCal_diverted conservées
   | ☐ **:term:`CT`\s marqués** (CT1 = grille, CT2 = diversion)


Étalonnage — Triphasé
----------------------

En triphasé, chaque phase doit être étalonnée individuellement. Le paramètre à ajuster est ``f_powerCal`` pour chaque phase.

Méthode avec le compteur de distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette méthode ne nécessite aucun appareil de mesure, mais n’est pas la plus rapide à réaliser.

À l’aide des flash du compteur (1 flash = 1 Wh consommé)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La plupart des compteurs génèrent un flux d’impulsions optiques pour montrer le taux auquel l’énergie est consommée. En installant un :term:`CT` autour de l’un des câbles d’alimentation entrants et en exécutant le logiciel approprié sur le routeur, un flux similaire d’impulsions optiques peut être généré.

Le débit du flux d’impulsions pour le routeur peut être ajusté en modifiant la valeur ``f_powerCal`` correspondante. Lorsque les deux flux d’impulsions sont synchronisés, un étalonnage correct a été réalisé.

Il faudra aller par tâtonnement. Si le flash du routeur est plus rapide que celui du compteur, il faut diminuer ``f_powerCal`` sinon l’augmenter.

À l’aide de l’affichage du compteur (plus simple et plus rapide)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il est possible également de relever la consommation affichée par le compteur sur la phase en cours d’étalonnage.
Il faudra alors faire correspondre la puissance affichée par le routeur dans le Moniteur Série de l’Arduino IDE avec celle affichée par le compteur.
D’où l’intérêt de ne pas avoir d’appareils qui vont se mettre en route sporadiquement (réfrigérateur…).

L’affichage dans le Moniteur Série se présente comme ceci : ::

    1797.67, P:-21, P1:368, P2:-113, P3:-276, V1:233.24, V2:233.82, V3:233.84, (minSampleSets/MC 32, #ofSampleSets 8014)
    1793.61, P:-18, P1:367, P2:-110, P3:-275, V1:233.46, V2:233.93, V3:233.99, (minSampleSets/MC 32, #ofSampleSets 8013)
    1780.56, P:-18, P1:374, P2:-116, P3:-276, V1:233.09, V2:233.53, V3:233.67, (minSampleSets/MC 32, #ofSampleSets 8014)
    1804.21, P:-24, P1:371, P2:-118, P3:-277, V1:233.04, V2:233.48, V3:233.55, (minSampleSets/MC 32, #ofSampleSets 8015)

``P1``, ``P2``, ``P3`` représentent les puissances moyennées sur 5 secondes sur chaque phase. ``P`` est la puissance totale moyenne totale sur 5 secondes.
Si j’étalonne la phase **L1**, alors **P1** devra afficher la même valeur que celle affichée par le compteur pour cette même phase.

.. hint::
   Les numéros de phase sont purement arbitraires, la phase **L1** du routeur correspondant à la phase branchée sur le connecteur **L1**, mais ce n’est pas forcément la phase branchée sur le bornier **L1** du compteur.

Comment trouver le bon ``f_powerCal`` du premier coup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avant de télécharger le sketch d’étalonnage, je veille à définir les valeurs comme ceci :

.. code-block:: cpp

   constexpr float f_powerCal[NO_OF_PHASES]{0.05000f, 0.05000f, 0.05000f};

| Supposons que le compteur affiche **2250**, et que le log du routeur affiche **2000**.
| On aura alors :

.. math::

   f_{powerCal} = 0.05000 * {2250 \over 2000} = 0.05625

.. note::
   La valeur ``0.05000`` dans la formule correspond à la valeur inscrite dans le sketch téléversé.
   Si le sketch contient une autre valeur, il conviendra alors d’adapter la formule en conséquence.

.. hint::
   Après avoir calculé le ``f_powerCal`` de la phase en cours d’étalonnage et saisi sa valeur dans le sketch, il peut être judicieux de téléverser à nouveau sur le routeur et de s’assurer maintenant, la valeur affichée dans le log correspond à celle du compteur.

En triphasé, il faudra répéter l’opération sur chacune des phases.
Une ligne de mesure comprend TOUS les composants en partant de la pince jusqu’au convertisseur analogique du microcontrôleur.

.. important::
   Chaque pince devra alors être marquée pour savoir à quelle ligne elle correspond.


.. admonition:: ✅ Point de Contrôle — Étalonnage Méthode Compteur

   Après avoir étalonné les 3 phases avec le compteur, vérifiez :

   | ☐ **f_powerCal trouvé pour CHAQUE phase** (L1, L2, L3)
   | ☐ Valeur de chaque phase synchronisée avec compteur
   | ☐ **Chaque CT marqué** avec son numéro de phase correspondant
   | ☐ Documentation complète : f_powerCal[0], f_powerCal[1], f_powerCal[2]
   | ☐ Test de vérification sur les 3 phases (somme = puissance totale compteur)


Méthode avec un appareil de mesure annexe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette méthode nécessite un appareil de mesure, tel qu’un wattmètre, un compteur d’énergie portable, ou un autre dispositif de mesure de puissance.

Appareils de mesure possibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Wattmètre portable** :

  - Affiche directement la puissance consommée en watts.
  - Idéal pour des mesures instantanées.

* **Compteur d’énergie portable** :

  - Permet de mesurer la consommation d’énergie sur une période donnée (kWh).
  - Utile pour des mesures prolongées.

* **Multimètre avec fonction wattmètre** :

  - Polyvalent, peut également mesurer la tension et le courant.
  - Peut nécessiter des calculs manuels pour obtenir la puissance (P = U × I).

* **Compteur d’énergie triphasé** :

  - Permet de mesurer directement les trois phases sans déplacer l’appareil.
  - Idéal pour des installations triphasées complexes.

Étapes pour l’étalonnage
^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Préparation** :

   - Coupez l’alimentation électrique au tableau pour garantir la sécurité.
   - Installez l’appareil de mesure sur la phase correspondante (par exemple, **L1**).
   - Connectez la pince ampèremétrique du routeur à la même phase.

#. **Mesure de la puissance** :

   - Rétablissez l’alimentation électrique.
   - Allumez un appareil purement résistif (par exemple, un radiateur ou une bouilloire).
   - Relevez la puissance affichée par l’appareil de mesure.

#. **Ajustement de ``f_powerCal``** :

   - Comparez la puissance mesurée par l’appareil avec celle affichée dans le Moniteur Série de l’Arduino IDE.
   - Utilisez la formule suivante pour ajuster la valeur de ``f_powerCal`` :

     .. math::

        f_{powerCal} = f_{powerCal_{initial}} * \frac{P_{\text{mesuré}}}{P_{routeur}}

     Où :

     - :math:`f_{powerCal_{initial}}` est la valeur initiale définie dans le sketch Arduino.
     - :math:`P_{\text{mesuré}}` est la puissance mesurée par l’appareil.
     - :math:`P_{routeur}` est la puissance affichée par le routeur.

#. **Validation** :

   - Téléversez le sketch mis à jour sur le routeur.
   - Vérifiez que la puissance affichée par le routeur correspond à celle mesurée par l’appareil.
   - Répétez l’opération pour chaque phase (**L1**, **L2**, **L3**).

.. attention::
   La phase doit correspondre. Si vous étalonnez la phase **L1**, le chauffe-eau DOIT être branché sur **L1** et la pince du routeur DOIT être celle qui correspond à la phase **L1**

Chauffe-eau triphasé
^^^^^^^^^^^^^^^^^^^^^

Si vous utilisez un chauffe-eau triphasé comme appareil d’étalonnage, suivez ces étapes spécifiques :

* Branchez l’appareil de mesure sur une phase du chauffe-eau ainsi que la pince du routeur correspondante.
* Si l’appareil de mesure est triphasé, il n’est pas nécessaire de le déplacer de phase en phase. Sinon, déplacez-le sur chaque phase pour effectuer les mesures.
* Relevez les valeurs de puissance pour chaque phase et ajustez ``f_powerCal`` en conséquence.

| Exemple : supposons que le compteur/wattmètre affiche **2250**, et que le log du routeur affiche **2000**.
| On aura alors :

.. math::

   f_{powerCal} = 0.05000 * {2250 \over 2000} = 0.05625

| Répétez l’opération pour chaque phase. Une ligne de mesure comprend TOUS les composants en partant de la pince jusqu’au convertisseur analogique du microcontrôleur.

.. important::
   Chaque pince devra être marquée pour savoir à quelle ligne elle correspond.

.. admonition:: ✅ Point de Contrôle Final — Étalonnage Complet

   Avant de passer à l’installation finale, vérifiez :

   **Monophasé :**

   | ☐ **powerCal_grid** et **powerCal_diverted** trouvés et notés
   | ☐ :term:`CT`\s marqués (CT1 = grille, CT2 = diversion)

   **Triphasé :**

   | ☐ **f_powerCal validé pour L1, L2, L3** avec appareil de mesure
   | ☐ Chaque phase mesure correctement (écart < 2 %)
   | ☐ **CTs marqués de manière PERMANENTE** (L1, L2, L3)
   | ☐ Test avec charge équilibrée : somme des phases = mesure compteur

   **Commun :**

   ☐ Documentation finale complète et conservée en lieu sûr

   ⚠️ **CRITIQUE : Ne JAMAIS intervertir les CTs après étalonnage** ⚠️

.. |br| raw:: html

  <br/>
