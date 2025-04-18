
Tests électriques
-----------------

Une fois les transformateurs en place, la carte est maintenant prête pour les tests électriques. |br|

C’est le bon moment pour vérifier que tous les joints soudés sont en bon état et que toutes les éclaboussures de soudure ont été éliminées.

Test de chaque sous-alimentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avant d’installer les circuits intégrés, le fonctionnement de l’alimentation doit être vérifié.

.. danger::
   **Alerte de sécurité**

   Pour poursuivre cette séquence de construction, un accès à la tension secteur **230 V** est requis.

   Veuillez ne pas passer à cette étape suivante à moins que vous soyez compétent pour le faire.

Nous effectuerons les tests suivants en alimentant le routeur via chacun des connecteurs secteur, l’un après l’autre. |br|
Ainsi, si une tension est incorrecte, il sera plus facile d’identifier la partie du circuit qui est défectueuse.

Si tout a été correctement assemblé, la sortie de l’alimentation devrait être d’environ **3,3 V**… ou **5 V** si un régulateur de tension **5 V** a été installé.

Cette tension peut être facilement vérifiée au niveau du point de test **Test VCC**, ainsi que **Test GND**, comme indiqué ici.

.. hint::
   N’oubliez pas de mettre votre multimètre sur la position *courant continu*, :term:`DC`, symbole **⎓** !

À l’exception du transformateur, qui peut sembler légèrement chaud après plusieurs minutes, aucun des composants de la carte ne doit présenter d’augmentation notable de la température.

Insertion du LM358 et test de Vref
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avec la tension correcte en place, les circuits intégrés peuvent maintenant être installés, après avoir coupé l’alimentation.

Le premier d’entre eux est LM358. |br|
Il s’agit d’un amplificateur opérationnel qui fournit une tension de référence intermédiaire pour les capteurs de tension et de courant.

Avec les packs Dual-in-Line, les broches devront peut-être être légèrement pliées vers l’intérieur pour s’insérer dans l’embase.
Cela peut être fait en *faisant rouler* doucement la puce de chaque côté, tour à tour.

Pour minimiser les risques de dommages électriques, cette opération doit être effectuée sur une surface protectrice telle qu’un sac antistatique.

Avec les broches bien alignées, le circuit intégré peut être délicatement placé sur son connecteur, comme indiqué ici.

.. warning::
   Les circuits intégrés doivent être installés dans le bon sens. Le point sur la puce doit être aligné avec l’encoche de l’image sérigraphiée.

Une fois que tout a été soigneusement vérifié, la puce peut être enfoncée fermement.

Avec **LM358** en place et la carte alimentée à nouveau, la référence de tension peut être mesurée. |br|
**Vref** doit être environ la moitié de la tension d’alimentation. Ici, nous testons une carte **3,3 V**.

Cette tension est accessible via le point de test **Test Vref** juste en dessous du **LM358**.

Insertion du processeur principal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le processeur principal, **ATmega328-P**, est installé de la même manière que pour **LM358**, toujours après avoir coupé l’alimentation.
Avec autant de broches, il est très facile pour l’une d’entre elles de se plier en dessous.

.. caution::
   Si ce circuit intégré est dans le mauvais sens lors de la mise sous tension, il ne fonctionnera probablement plus jamais !
