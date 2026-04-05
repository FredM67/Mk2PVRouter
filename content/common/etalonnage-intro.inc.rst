Introduction
------------

Lorsqu'il fonctionne avec les paramètres par défaut, le routeur Mk2PVRouter peut dévier de manière fiable l'énergie excédentaire sans nécessiter d'étalonnage. Cependant, pour fournir une indication précise de l'énergie déviée, le système doit être étalonné.

Pour un étalonnage précis, une certaine forme de référence standard est nécessaire. Le compteur d'électricité installé peut souvent être utilisé à cette fin.

La plupart des compteurs d'électricité génèrent un flux d'impulsions optiques pour indiquer le taux de consommation d'énergie. En plaçant un transformateur de courant :term:`CT` autour de l'un des câbles d'alimentation entrants, et en exécutant le logiciel approprié sur le matériel en cours de test, un flux d'impulsions optiques similaire peut être généré.

.. admonition:: Ligne de mesure

   Ensemble des composants constituant la prise de mesure. Elle part de l'Arduino jusqu'à la pince ampèremétrique en passant par les résistances, connecteurs et les câbles.

Sécurité
--------

Pour cette étape d'étalonnage, il faudra potentiellement manipuler le câblage électrique. Il est donc impératif de respecter les consignes de sécurité.

.. danger::
   **ALERTE SÉCURITÉ**

   Potentiellement, selon l'appareil utilisé, il faudra modifier le câblage électrique. Avant toutes manipulations, il est impératif de couper l'alimentation au tableau électrique et de vérifier à l'aide d'un testeur de tension l'absence effective de tension.
   Dans le doute, couper le disjoncteur principal.

Principe de base
~~~~~~~~~~~~~~~~

Cet étalonnage peut être réalisé selon plusieurs méthodes, selon que l'on possède ou non certains appareils de mesure (ampèremètre, wattmètre, voltmètre).

Pour simplifier la procédure, il est important d'avoir une consommation constante pendant l'étalonnage. Par exemple, branchez un radiateur électrique ou une bouilloire et débranchez tout le reste, y compris votre/vos système·s de production d'électricité.
L'utilisation d'un appareil purement résistif, donc sans ventilateur ni autre chose qu'une résistance, simplifiera grandement l'étalonnage.

.. admonition:: Pré-requis

   Les pinces doivent être installées sur chaque phase correspondante par rapport à l'alimentation du routeur.
