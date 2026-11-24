Résolution des Problèmes
""""""""""""""""""""""""

Erreur : `avrdude: stk500_recv(): programmer is not responding`
###############################################################

**Causes possibles :**

#. Mauvais port COM sélectionné → Essayer un autre port
#. Routeur non alimenté → Vérifier l’alimentation 230 V
#. Câblage FTDI incorrect → Vérifier TX ↔ RX inversés
#. ATmega328P mal inséré → Vérifier l’orientation et l’insertion complète
#. Fil DTR non câblé (avec des fils séparés) → pas de reset automatique : câbler la broche 6 (DTR)
#. ATmega328P sans *bootloader* → le graver avec un programmateur ISP
#. Cavalier 3,3 V/5 V de l’adaptateur mal placé → voir *Connexion du Routeur* plus haut

Erreur : ``static assertion failed: **** Please define 'gnu++17' in 'platform.txt' ! ****``
###########################################################################################

Le fichier `platform.txt` n’a pas été modifié correctement : le compilateur ne travaille pas en C++17. D’autres erreurs suivent ce message ; elles disparaissent avec la bonne modification.

**Solution :** Reprendre :ref:`arduino-cpp17-config`.

Port COM n’apparaît pas
#######################

#. Vérifier que les pilotes FTDI sont installés (:ref:`install-etape1-ftdi`)
#. Débrancher/rebrancher l’adaptateur FTDI
#. Redémarrer l’ordinateur

