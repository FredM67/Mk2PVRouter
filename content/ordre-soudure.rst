.. _ordre-soudure:

Ordre de soudure
----------------

| Il est fortement recommandé de suivre l'ordre de soudure indiqué.
|
| Cela vous vous épargnera des soucis par rapport au maintien des composants lors de la soudure.
| En effet, les composants à souder sont insérés sur la face *avant* du circuit imprimé, tandis que la soudure se fait sur la face *arrière*.
| Il faudra donc à chaque fois retourner le circuit imprimé pour souder les composants.
| 
| Si vous soudez un composant haut en premier, par exemple un transformateur, tous les autres composants auront tendance à tomber lorsque vous retournerez le circuit imprimé pour les souder.

Voici l'ordre de soudure recommandé :
1. *jumper·s*,
2. résistances,
3. diodes
4. socles de circuits intégrés,
5. oscillateur et ses 2 condensateurs associés,
6. condensateurs céramiques non polarisés,
7. pont·s de diodes,
8. régulateur de tension (format transistor),
9. inductance,
10. socle FTDI
11. socles de CTs et socle·s de sortie,
12. condensateurs électrolytiques polarisés,
13. fusibles,
14. connecteur·s d'alimentation,
15. varistance·s,
16. régulateur de tension,
17. transformateur·s

.. note::
   Cette liste est exhaustive et peut varier en fonction de la configuration de votre carte mère.