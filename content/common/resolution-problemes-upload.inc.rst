Résolution des Problèmes
""""""""""""""""""""""""

Erreur : `avrdude: stk500_recv(): programmer is not responding`
###############################################################

**Causes possibles :**

#. Mauvais port COM sélectionné → Essayer un autre port
#. Routeur non alimenté → Vérifier l’alimentation 230 V
#. Câblage FTDI incorrect → Vérifier TX ↔ RX inversés
#. ATmega328 mal inséré → Vérifier l’orientation et l’insertion complète

Erreur : `error: ’constexpr’ does not name a type`
##################################################

Le fichier `platform.txt` n’a pas été modifié correctement.

**Solution :** Reprendre :ref:`arduino-cpp17-config`.

Port COM n’apparaît pas
#######################

#. Vérifier que les pilotes FTDI sont installés (:ref:`install-etape1-ftdi`)
#. Débrancher/rebrancher l’adaptateur FTDI
#. Redémarrer l’ordinateur

