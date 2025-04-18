
Ordre de soudure
----------------

| Il est fortement recommandé de suivre l’ordre de soudure indiqué.
|
| Cela vous vous épargnera des soucis par rapport au maintien des composants lors de la soudure.
| En effet, les composants à souder sont insérés sur la face *avant* du circuit imprimé, tandis que la soudure se fait sur la face *arrière*.
| Il faudra donc à chaque fois retourner le circuit imprimé pour souder les composants.
| 
| Si vous soudez un composant haut en premier, par exemple un transformateur, tous les autres composants auront tendance à tomber lorsque vous retournerez le circuit imprimé pour les souder.

Voici l’ordre de soudure recommandé :

#. *jumper·s*,
#. résistances,
#. diodes,
#. socles de circuits intégrés,
#. oscillateur et ses 2 condensateurs associés,
#. condensateurs céramiques non polarisés,
#. pont·s de diodes,
#. fusibles,
#. connecteur·s d’alimentation,
#. socle FTDI,
#. socles de CTs et socle·s de sortie,
#. inductance,
#. condensateurs électrolytiques polarisés,
#. varistance·s,
#. régulateur de tension (format transistor),
#. transformateur·s

.. note::
   Cette liste est exhaustive et peut varier en fonction de la configuration de votre carte mère.