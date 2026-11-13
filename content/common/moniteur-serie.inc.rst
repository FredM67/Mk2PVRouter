Ouverture du Moniteur Série
"""""""""""""""""""""""""""

#. Menu : **Outils → Moniteur série**
#. Configurer en bas à droite :

   - **Vitesse (baud rate)** : `9600`
   - **Fin de ligne** : `Retour chariot et Nouvelle ligne` (NL & CR)

Messages Attendus
"""""""""""""""""

Si tout fonctionne, vous devriez voir des messages s’afficher :

.. code-block:: text

   Mk2PVRouter v3.x
   Initialisation...
   CT1: 0 W
   CT2: 0 W  (si triphasé)
   CT3: 0 W  (si triphasé)
   Grid: 230 V
   Load 1: OFF
   Load 2: OFF

.. note::
   Les valeurs exactes dépendent de votre installation et de l’étalonnage.

Si Aucun Message n’Apparaît
"""""""""""""""""""""""""""

#. Vérifier que le bon baud rate est sélectionné (9600 bauds)
#. Vérifier le câblage FTDI (TX ↔ RX)
#. Vérifier que le routeur est alimenté
#. Vérifier l’oscillateur 16 MHz et les condensateurs C7/C8

Adresses des Sondes de Température
"""""""""""""""""""""""""""""""""""

Le routeur ne recherche pas les sondes : il lit celles dont les adresses sont dans `config.h`. Pour relever les adresses, téléverser l’exemple de la bibliothèque *OneWire* (**Fichier → Exemples → OneWire → DS18x20_Temperature**), en changeant au besoin la broche dans `OneWire ds(…)`. Le moniteur série affiche alors l’adresse de chaque sonde branchée :

.. code-block:: text

   ROM = 28 AA BB CC DD EE FF 1
   ROM = 28 AA BB CC DD EE FF 2

Copier ces adresses dans `config.h` (section sondes de température, chaque octet sous la forme `0x28`, `0xAA`…, un octet affiché `1` s’écrit `0x01`), puis téléverser à nouveau le firmware du routeur. Coller une étiquette avec l’adresse sur le câble de chaque sonde.


