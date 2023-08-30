.. Mk2PVRouter documentation master file, created by
   sphinx-quickstart on Mon Aug 28 10:50:52 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue dans la documentation du Mk2PVRouter !
================================================

Le MK2 PV Router est l’accessoire indispensable lorsque l’on souhaite optimiser son autoconsommation.

Particulièrement adapté à l’alimentation de résistances (chauffe eau, radiateur, sol chauffant) du fait de son alimentation à puissance variable, il saura orienter votre surplus vers le ou les équipements raccordés.

Le routeur surveille en permanence la production d’énergie de votre système en autoconsommation et redirige tout excédent d’électricité vers les charges branchées.
Grace aux modules sortie-relais, il peut aussi gérer des installations de chauffage ou toutes sortes d'appareils avec ses fonctions de programmateurs horaire, temporisations, thermostats, préparation ECS, chauffage... toutes configurables librement.

Ce routeur existe en 2 versions, une version monophasé, exclusivement pour les raccordements monophasés, et une triphasé pour les raccordements en triphasés. Seul le raccordement est important, peu importe que la production d'électricité soit en monophasé ou que l'on utilise que des appareils monophasés.

.. callout:: À retenir

   Peu importe l'installation de production d'électricité (monophasée, biphasée, triphasée), le routeur DOIT correspondre au type de raccordement.

   Raccordement triphasé = routeur triphasé

.. figure:: img/Schema-dimplantation.png
   :align: center
   :alt: Schéma d'implantation
   
   Schéma d'implantation.

Les 2 graphiques suivants vous montrent une production et une consommation typiques d'un foyer.
Les pics importants représentent la consommation classique dûe au fonctionnement d'un chauffe-eau.

.. figure:: img/Production-et-consommation-journaliere-sans-MK2-PV-Router.png
   :align: center
   :alt: Sans Mk2PVRouter

   Production et consommation typiques SANS Mk2PVRouter

.. figure:: img/Production-et-consommation-journaliere-avec-MK2-PV-Router.png
   :align: center
   :alt: Avec Mk2PVRouter

   Production et consommation typiques AVEC Mk2PVRouter

Le routeur va permettre de décaler la consommation du chauffe-eau aux moments où l'on produit sa propre électricité gratuite (hors amortissement bien sûr du système de production).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction.md
   carte-mere-mono.md
   carte-mere-tri.md
   carte-sortie-triac.md
   boitier.md
   dissipateur.md
   