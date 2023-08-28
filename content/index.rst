.. Mk2PVRouter documentation master file, created by
   sphinx-quickstart on Mon Aug 28 10:50:52 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue dans la documentation du Mk2PVRouter !
================================================

Le Mk2PVRouter permet de mesurer et d’optimiser l'excédent de production d’une installation photovoltaïque/éolienne/... et d’effectuer la diversion (ou routage) de celui-ci vers une ou plusieurs charges résistives, la résistance d'un chauffe-eau ou d'un radiateur électrique par exemple.
Ainsi il permet d’augmenter significativement la part d’autoconsommation de l’énergie produite.

La mesure de la puissance active est effectuée en permanence sur l'ensemble des entrées (plusieurs milliers de fois par seconde).
Selon le surplus disponible, cette puissance est envoyée toutes les 10ms vers une ou plusieurs sorties de régulation de type "Proportionnelle Intégrale" afin de piloter les sorties et d’assurer le plus précisément possible le maintien d'une consommation/injection nulle au point de raccordement.

Grace aux modules sortie-relais, il peut aussi gérer des installations de chauffage ou toutes sortes d'appareils avec ses fonctions de programmateurs horaire, temporisations, thermostats, préparation ECS, chauffage... toutes configurables librement.

Ce routeur existe en 2 versions, une monophasé, exclusivement pour les raccordements monophasés, et une triphasé pour les raccordements en triphasés. Seul le raccordement est important, peu importe que la production d'électricité soit en monophasé ou que l'on utilise que des appareils monophasés.

.. callout:: À retenir

   Peu importe l'installation de production d'électricité (monophasée, biphasée, triphasée), le routeur DOIT correspondre au type de raccordement.

   Raccordement triphasé = routeur triphasé


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction.md
   carte-mere-tri.md
