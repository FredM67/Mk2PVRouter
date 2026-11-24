.. _assemblage-boitier:

==========
Assemblage
==========

Après avoir effectué toutes les étapes précédentes (soudure de la carte-mère, préparation du boîtier, perçage du dissipateur, étage·s de sortie et confection des câbles), il est temps d’assembler le tout.

.. tip::
   **Durée estimée** : 30 à 45 minutes

   **Outils nécessaires** :

   - clés six pans
   - clés plates
   - Pâte thermique (pour le triac) (option)
   - Clé à douille ou pince (pour écrous M3 et M4)

Ordre d’Assemblage
------------------

Il est possible de réaliser l’assemblage dans n’importe quel ordre, cependant, il sera plus pratique de le réaliser comme ceci :

#. **Mise en place des presse-étoupe** — Visser sans serrer complètement (ajustement final après passage des câbles)

#. **Fixation du ou des dissipateurs sur le boîtier**, y compris fils de terre

   - Fixer en même temps la cosse du fil de terre vert/jaune (voir :ref:`confection-cables`) sur le dissipateur, métal contre métal
   - Serrer les vis de manière croisée pour assurer un contact uniforme

#. **Fixation du ou des étages de sortie sur chaque dissipateur** (visser le triac)

   - Placer l’isolant fourni avec le kit (isolation électrique et conduction thermique) entre la patte métallique du triac et le dissipateur
   - Visser fermement pour assurer un bon contact thermique, sans serrer excessivement

#. **Fixation du ou des étages de sortie dans le boîtier** (visser le :term:`PCB`)

   - Utiliser les entretoises pour maintenir le PCB à distance du boîtier

#. **Fixation de la carte-mère dans le boîtier**

   - Aligner les trous de montage du PCB avec les entretoises
   - Visser le PCB aux entretoises

#. **Mise en place des prises jack** (CT) et des éventuels boutons/témoins

   - Prises jack : pour les :term:`CT` de mesure du réseau électrique
   - Bouton reset (connecteur RESET de la carte-mère), en option

#. **Mise en place des câbles**

   - Faire passer tous les câbles par les presse-étoupe
   - Connecter les câbles de commande (carte-mère → étages de sortie) et les câbles de témoin LED (étages de sortie → cartes indicateur), broche 1 sur broche 1
   - Raccorder le secteur et les charges comme décrit dans :ref:`raccordement-etages-sortie`
   - Serrer définitivement les presse-étoupe
