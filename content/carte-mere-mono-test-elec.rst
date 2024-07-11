.. _carte-mere-mono-test-elec:

Tests électriques
^^^^^^^^^^^^^^^^^

Une fois le transformateur installé, la carte est prête pour les tests électriques.

C'est le moment idéal pour vérifier que toutes les soudures sont en bon état et qu'il n'y a pas de résidus de soudure.

Avant d'installer les circuits intégrés, il est important de vérifier le bon fonctionnement de l'alimentation.

.. danger::
   **Alerte de sécurité**

   Pour poursuivre cette séquence de construction, un accès à la tension secteur **230 V** est requis.

   Veuillez ne pas passer à cette étape suivante à moins que vous soyez compétent pour le faire.

| Sur la photo ci-dessous, une alimentation temporaire de 230 V CA via un fusible de 3 A a été connectée.
| Bien que cela ne soit pas requis par ce :term:`PCB`, une connexion à la terre offre un certain degré de sécurité dans le cas où l'opérateur entrerait accidentellement en contact avec la ligne 230 V :term:`AC`.

Si tout a été correctement assemblé, la sortie de l'alimentation devrait être d'environ **3,3 V** ou **5 V** si un régulateur de tension **5 V** a été installé.

Cette tension peut être facilement vérifiée au niveau du connecteur *access to power*, comme indiqué ici.

.. hint::
   N'oubliez pas de mettre votre multimètre sur la position *courant continu*, :term:`DC`, symbole **⎓** !

À l'exception du transformateur, qui peut sembler légèrement chaud après plusieurs minutes, aucun des composants de la carte ne doit présenter d'augmentation notable de la température.

Avec la tension correcte en place, les circuits intégrés peuvent maintenant être installés, **après avoir coupé l'alimentation**.

| Le premier d'entre eux est **IC2**.
| Il s'agit d'un amplificateur opérationnel qui fournit une tension de référence intermédiaire pour les capteurs de tension et de courant.

| Avec les packs Dual-in-Line, les broches devront peut-être être légèrement pliées vers l'intérieur pour s'insérer dans l'embase.
| Cela peut être fait en *faisant rouler* doucement la puce de chaque côté, tour à tour.

Pour minimiser les risques de dommages électriques, cette opération doit être effectuée sur une surface protectrice telle qu'un sac antistatique.

Avec les broches bien alignées, le circuit intégré peut être délicatement placé sur son connecteur, comme indiqué ici.

.. warning::
   Les circuits intégrés doivent être installés dans le bon sens. Le point ou l'encoche sur la puce doit être aligné avec l'encoche de l'image sérigraphiée.

Une fois que tout a été soigneusement vérifié, la puce peut être enfoncée fermement.

| Avec **IC2** en place et la carte alimentée à nouveau, le point milieu de la référence de tension peut être mesurée.
| **Vref** doit être environ la moitié de la tension d'alimentation. Ici, nous testons une carte **3,3 V**.

Un endroit pratique pour accéder à **Vref** se trouve à l'extrémité supérieure de **R6**. La prise d'antenne **SMA** est un point de masse pratique.

**Vref** est également accessible à divers autres endroits, comme indiqué sur le schéma de circuit de cette carte.

Une fois la tension vérifiée et confirmée correcte, vous pouvez insérer le processeur principal, **IC1**.

.. warning::
   Assurez-vous que l'alimentation est coupée avant d'insérer **IC1**.

| Le processeur principal, **IC1**, est installé de la même manière que pour **IC2**, toujours après avoir coupé l'alimentation.
| Avec autant de broches, il est très facile pour l'une d'entre elles de se plier en dessous.

.. caution::
   Si ce circuit intégré est dans le mauvais sens lors de la mise sous tension, il ne fonctionnera probablement plus jamais !
