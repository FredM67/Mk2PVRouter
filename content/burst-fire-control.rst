.. _burst-fire-control:

==================
Burst Fire Control
==================

Le burst fire control est une méthode de régulation utilisée pour piloter des charges électriques, en particulier des charges résistives comme les chauffe-eau ou les radiateurs. Cette méthode est souvent utilisée dans des systèmes comme le Mk2PVRouter pour optimiser l’utilisation de l’énergie excédentaire tout en minimisant les perturbations sur le réseau électrique.

Fonctionnement du Burst Fire Control
------------------------------------

Le principe du burst fire control repose sur l’envoi de **trains complets d’ondes sinusoïdales** au lieu de découper chaque cycle de la sinusoïde. Voici comment cela fonctionne :

- **Activation par périodes complètes** :

  - Le triac (composant électronique utilisé pour contrôler la puissance) est activé ou désactivé pour des périodes complètes correspondant à la fréquence du réseau (par exemple, 50 Hz en Europe ou 60 Hz en Amérique du Nord).
  - Cela signifie que le courant passe pendant un certain nombre de cycles complets de la sinusoïde, puis est coupé pendant d’autres cycles.

- **Pas de découpage intra-cycle** :

  - Contrairement au contrôle en phase (où le triac est activé à un moment précis dans chaque cycle), le burst fire control ne découpe pas les cycles individuels. Cela évite les transitions rapides qui peuvent générer des harmoniques.

- **Régulation de la puissance** :

  - La puissance moyenne délivrée à la charge est ajustée en modifiant le rapport entre les périodes activées et désactivées. Par exemple :

    - Si le triac est activé pendant 5 cycles et désactivé pendant 5 cycles, la puissance moyenne est de 50 %.
    - Si le triac est activé pendant 8 cycles et désactivé pendant 2 cycles, la puissance moyenne est de 80 %.

  - Ces rapports sont des moyennes : le Mk2PVRouter n’utilise pas de fenêtre fixe de N cycles (voir l’exemple ci-dessous).

Avantages du Burst Fire Control
-------------------------------

- **Réduction des harmoniques** :

  - Contrairement au contrôle en phase, le burst fire control ne génère pas d’harmoniques (multiples de 50 Hz) dans le réseau électrique. Les harmoniques sont des perturbations qui peuvent affecter la qualité du signal électrique et perturber d’autres appareils connectés au réseau.
  - Il n’est pas pour autant sans effet : avec de fortes charges, les mises en marche et arrêts successifs peuvent provoquer un léger papillotement (*flicker*) de l’éclairage.

- **Compatibilité avec les charges résistives** :

  - Ce mode est particulièrement adapté aux charges résistives (chauffe-eau, radiateurs, etc.), qui n’ont pas besoin d’une régulation fine de la puissance.
  - Les charges résistives tolèrent bien les interruptions périodiques de l’alimentation.

- **Faibles perturbations radio** :

  - Le triac ne commute qu’au passage par zéro de la tension, ce qui évite les parasites radio (CEM) que produit le contrôle en phase.

- **Simplicité de mise en œuvre** :

  - Le burst fire control est relativement simple à implémenter dans des systèmes électroniques, ce qui en fait une solution robuste et fiable.

Exemple d’utilisation dans le Mk2PVRouter
-----------------------------------------

Dans le Mk2PVRouter, le burst fire control est utilisé pour rediriger l’énergie excédentaire vers des charges résistives. Par exemple :

- Si un surplus d’énergie est détecté, le routeur active le triac pour un certain nombre de cycles complets, permettant à l’énergie excédentaire d’être consommée par un chauffe-eau.
- Lorsque le surplus diminue, le routeur réduit le nombre de cycles activés, ajustant ainsi la puissance délivrée à la charge.

Concrètement, la décision est prise une fois par période secteur (toutes les 20 ms à 50 Hz) : le routeur compare l’énergie excédentaire accumulée dans un « réservoir d’énergie » à des seuils, et peut alors mettre une charge en marche ou l’arrêter. L’optocoupleur à passage par zéro de l’étage de sortie (MOC3043M) fait que le triac ne commute qu’au passage par zéro de la tension.

Comparaison avec le Contrôle en Phase
-------------------------------------

+---------------------------+-----------------------------+-----------------------------+
| **Caractéristique**       | **Burst Fire Control**      | **Contrôle en Phase**       |
+===========================+=============================+=============================+
| **Harmoniques**           | Pas d’harmoniques           | Génère des harmoniques      |
+---------------------------+-----------------------------+-----------------------------+
| **Compatibilité**         | Idéal pour les charges      | Peut être utilisé pour des  |
|                           | résistives                  | charges variées             |
+---------------------------+-----------------------------+-----------------------------+
| **Complexité**            | Simple à implémenter        | Plus complexe               |
+---------------------------+-----------------------------+-----------------------------+
| **Perturbations radio**   | Faibles (zéro de tension)   | Plus élevées                |
+---------------------------+-----------------------------+-----------------------------+

Conclusion
----------

Le burst fire control est une méthode de régulation idéale pour des systèmes comme le Mk2PVRouter. Il garantit une utilisation efficace de l’énergie excédentaire tout en préservant la qualité du réseau électrique. Grâce à cette méthode, le Mk2PVRouter peut fonctionner de manière stable et respectueuse des normes électriques, tout en optimisant l’autoconsommation.
