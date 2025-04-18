.. _etalonnage-tri:

Étalonnage
==========

Contrairement à la version monophasée, le modèle triphasé ne peut pas dévier de manière fiable l’énergie excédentaire sans nécessiter un étalonnage aussi précis que possible.
En effet, étant donné qu’en triphasé, le routeur calcule la somme algébrique des puissances instantanées sur chaque phase, il faut que les mesures soient aussi précises que possible.

Les composants électroniques ne sont jamais parfaits. Ils ont chacun des caractéristiques données accompagnées d’une tolérance. Les tolérances classiques sont de 5 ou 10 %. Il convient donc d’étalonner chaque ligne de mesure afin que la somme finale soit la plus juste possible.

Pour un étalonnage précis, une certaine forme de référence standard est nécessaire. Le compteur d’électricité installé peut souvent être utilisé à cette fin.

La plupart des compteurs d’électricité génèrent un flux d’impulsions optiques pour indiquer le taux de consommation d’énergie. En plaçant un transformateur de courant :term:`CT` autour de l’un des câbles d’alimentation entrants, et en exécutant le logiciel approprié sur le matériel en cours de test, un flux d’impulsions optiques similaire peut être généré.

Le taux du flux d’impulsions pour le matériel en cours de test peut être ajusté en modifiant la valeur ``f_powerCal`` pertinente. Lorsque les deux flux d’impulsions sont synchronisés, l’étalonnage correct a été atteint.

.. admonition:: Ligne de mesure

   Ensemble des composants constituant la prise de mesure. Elle part de l’Arduino jusqu’à la pince ampèremétrique en passant par les résistances, connecteurs et les câbles.

.. admonition:: Pré-requis

   Les pinces doivent être installées sur chaque phase correspondante par rapport à l’alimentation du routeur.

Sécurité
--------
Pour cette étape d’étalonnage, il faudra potentionnellement manipuler le câblage électrique. Il est donc impératif de respecter les consignes de sécurité.

.. danger::
   **ALERTE SÉCURITÉ**
   Potentiellement, selon l’appareil utilisé, il faudra modifier le câblage électrique. Avant toutes manipulations, il est impératif de couper l’alimentation au tableau électrique et de vérifier à l’aide d’un testeur de tension l’absence effective de tension.
   Dans le doute, couper le disjoncteur principal.

Principe de base
----------------

Cet étalonnage peut être réalisé selon plusieurs méthodes, selon que l’on possède ou non certains appareils de mesure (ampèremètre, wattmètre, voltmètre).

Pour simplifier la procédure, il est important d’avoir une consommation constante pendant l’étalonnage. Par exemple, branchez un radiateur électrique ou une bouilloire et débranchez tout le reste, y compris votre/vos système·s de production d’électricité.
L’utilisation d’un appareil purement résistif, donc sans ventilateur ni autre chose qu’une résistance, simplifiera grandement l’étalonnage.

Méthode avec le compteur de distribution
----------------------------------------

Cette méthode ne nécessite aucun appareil de mesure, mais n’est pas la plus rapide à réaliser.

À l’aide des flash du compteur (1 flash = 1 Wh consommé)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La plupart des compteurs génèrent un flux d’impulsions optiques pour montrer le taux auquel l’énergie est consommée. En installant un :term:`CT` autour de l’un des câbles d’alimentation entrants et en exécutant le logiciel approprié sur le routeur, un flux similaire d’impulsions optiques peut être généré.

Le débit du flux d’impulsions pour le routeur peut être ajusté en modifiant la valeur ``f_powerCal`` correspondante. Lorsque les deux flux d’impulsions sont synchronisés, un étalonnage correct a été réalisé.

Il faudra aller par tâtonnement. Si le flash du routeur est plus rapide que celui du compteur, il faut diminuer ``f_powerCal`` sinon l’augmenter.

À l’aide de l’affichage du compteur (plus simple et plus rapide)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il est possible également de relever la consommation affichée par le compteur sur la phase en cours d’étalonnage.
Il faudra alors faire correspondre la puissance affichée par le routeur dans le Moniteur Série de l’Arduino IDE avec celle affichée par le compteur.
D’où l’intérêt de ne pas avoir d’appareils qui vont se mettre en route sporadiquement (réfrigérateur…).

L’affichage dans le Moniteur Série se présente de comme ceci : ::

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

Méthode avec un appareil de mesure annexe
-----------------------------------------

Cette méthode nécessite un appareil de mesure, tel qu’un wattmètre, un compteur d’énergie portable, ou un autre dispositif de mesure de puissance.

Appareils de mesure possibles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~

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
