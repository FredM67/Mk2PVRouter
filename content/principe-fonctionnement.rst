.. _principe-fonctionnement:

Principe de fonctionnement
==========================

Le Mk2PVRouter est conçu pour optimiser l’autoconsommation d’énergie produite par un système photovoltaïque. Son fonctionnement repose sur la surveillance en temps réel du **bilan énergétique au point de raccordement** et sur la gestion intelligente des surplus d’énergie.

Voici les étapes principales du fonctionnement du Mk2PVRouter :

#. **Surveillance du bilan énergétique** :

   - Le routeur mesure en permanence le courant et la tension au point de raccordement au réseau électrique.
   - Il calcule le **bilan énergétique** en temps réel, c’est-à-dire la différence entre la puissance injectée dans le réseau et la puissance prélevée.
   - Si le bilan est positif (excédent d’énergie), cela signifie que la production dépasse la consommation.

#. **Détection des surplus d’énergie** :

   - Lorsque le bilan énergétique est positif, le Mk2PVRouter détecte un surplus d’énergie.
   - Ce surplus, qui serait normalement réinjecté dans le réseau, est redirigé vers des charges spécifiques.

#. **Gestion des charges** :

   - Le Mk2PVRouter redirige l’énergie excédentaire vers des appareils résistifs tels que des chauffe-eaux, radiateurs ou planchers chauffants.
   - Grâce à ses modules de sortie-relais, il peut également activer ou désactiver des appareils selon des seuils de surplus et d’import configurables.

#. **Étalonnage et précision** :

   - En triphasé, le routeur doit être étalonné (voir :ref:`etalonnage-triphase`) : il additionne les trois phases, et une seule phase mal mesurée fausse la somme. En monophasé, l’étalonnage n’est pas nécessaire pour dévier vers les triacs, mais il donne des valeurs réalistes et sert à tous les réglages en watts (voir :ref:`etalonnage-monophase`).

#. **Avantages** :

   - Réduction des pertes d’énergie en maximisant l’autoconsommation.
   - Diminution de la dépendance au réseau électrique.
   - Optimisation des coûts énergétiques.

.. graphviz:: principe-fonctionnement.dot
   :align: center
   :alt: Schéma de fonctionnement du Mk2PVRouter
   :caption: Schéma illustrant le fonctionnement du Mk2PVRouter.

Exemple d’utilisation
---------------------

| Prenons l’exemple d’un foyer équipé d’un système photovoltaïque et d’un chauffe-eau électrique :

- Pendant la journée, le système photovoltaïque produit de l’électricité.
- Si la production dépasse la consommation du foyer (par exemple, lorsque les occupants sont absents), le Mk2PVRouter détecte ce surplus via le bilan énergétique.
- Le surplus est redirigé vers le chauffe-eau, permettant de chauffer l’eau sans consommer d’électricité du réseau.
- Lorsque le chauffe-eau atteint la température souhaitée, le routeur peut rediriger l’énergie vers d’autres charges ou arrêter la redirection.

Fonctionnement des LED
----------------------

Le Mk2PVRouter est équipé de LED pour indiquer l’état des sorties triac. Chaque LED est montée sur une petite carte dédiée, la **carte indicateur** (voir :ref:`carte-indicateur`), raccordée au signal de commande de l’étage de sortie. Ces LED fournissent des informations visuelles sur la quantité d’énergie routée :

- **Allumage de la LED** :

  - La LED suit la commande du triac, cycle secteur par cycle secteur : allumée, la sortie est commandée. Cela ne garantit pas que la charge consomme (son thermostat peut être ouvert).

- **Clignotement de la LED** :

  - Plus la LED reste allumée longtemps, plus la puissance routée est élevée. Ce n’est pas la vitesse du clignotement qui compte, mais la part du temps où elle est allumée.
  
- **LED fixe** :
  
  - Une LED allumée de manière fixe peut indiquer deux situations :

    #. La charge connectée consomme 100 % de l’énergie routée.
    #. La charge connectée ne consomme plus d’énergie, par exemple lorsque la température souhaitée est atteinte (dans le cas d’un chauffe-eau ou d’un radiateur).

.. note::
   Une LED fixe ne signifie pas nécessairement que l’énergie est toujours consommée. Cela peut également indiquer que la charge a atteint son seuil de fonctionnement (par exemple, un chauffe-eau ayant atteint sa température maximale).

Ces indications permettent de vérifier visuellement le fonctionnement du routeur et de s’assurer que l’énergie excédentaire est correctement redirigée vers les charges.

Mode de régulation des triacs
-----------------------------

Le Mk2PVRouter utilise un mode de régulation appelé **burst fire control** pour piloter les triacs. Ce mode consiste à envoyer des trains complets d’ondes sinusoïdales au lieu de découper chaque cycle. En d’autres termes, le triac est activé ou désactivé pour des périodes complètes de la fréquence du réseau (par exemple, 50 Hz en Europe).

Avantages du *burst fire control*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Réduction des harmoniques** :

  - Contrairement à d’autres modes de régulation (comme le contrôle en phase), le burst fire control ne génère pas les harmoniques du découpage de phase. En revanche, il allume et éteint la charge par cycles entiers, ce qui peut provoquer un papillotement de l’éclairage (*flicker*) avec les grosses charges ; le firmware propose pour cela un mode « anti-flicker ».  

- **Efficacité énergétique** :

  - En minimisant les pertes liées à la commutation, ce mode de régulation améliore l’efficacité globale du système.

- **Compatibilité avec les charges résistives** :

  - Ce mode est particulièrement adapté aux charges purement résistives, comme les chauffe-eaux ou les radiateurs, qui n’ont pas besoin d’une régulation fine de la puissance.

Ce mode de régulation permet d’utiliser l’énergie excédentaire sans les perturbations du découpage de phase.

Pour plus d’informations sur le *burst fire control*, consultez la section :ref:`burst-fire-control`.

Fonctionnalités avancées
------------------------

Le Mk2PVRouter offre également des fonctionnalités avancées :

- **Programmation horaire** :
  
  - Avec un tarif heures creuses, permet de forcer la marche de certaines charges pendant les heures creuses (le firmware n’a pas d’horloge : ces marches forcées sont comptées depuis le début des heures creuses).

- **Gestion multi-phases** :

  - En triphasé, le routeur équilibre la **somme** des trois phases (un bilan global, comme le compteur) ; ses charges peuvent être réparties sur n’importe quelle phase.

- **Surveillance et journalisation** :

  - Les données de bilan énergétique peuvent être enregistrées pour analyse.

- **Interfaçage avec Home Assistant** :

  - En ajoutant le module **mk2Wifi** (ESP32-C6), le Mk2PVRouter peut être intégré à Home Assistant pour une gestion centralisée et une visualisation des données en temps réel.
  - Il est également possible de piloter certaines fonctions du routeur via Home Assistant, comme la **marche forcée**.

  .. note::
     Pour le routeur triphasé, le :ref:`configurateur <configurateur-triphase>` génère un fichier YAML ESPHome prêt à l’emploi, cohérent avec la configuration du routeur. Pour plus de détails sur l’intégration avec Home Assistant, consultez aussi ce `Gist <https://gist.github.com/FredM67/986e1cb0fc020fa6324ccc151006af99>`_.