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

Si vous avez activé `TEMP_ENABLED`, le moniteur série affichera les adresses détectées :

.. code-block:: text

   Temperature sensor 0 address: 28 AA BB CC DD EE FF 01
   Temperature sensor 1 address: 28 AA BB CC DD EE FF 02

Copier ces adresses dans `config.h` (section sondes de température).


