Ouverture du Moniteur Série
"""""""""""""""""""""""""""

#. Menu : **Outils → Moniteur série**
#. Configurer en bas à droite :

   - **Vitesse (baud rate)** : `9600`
   - **Fin de ligne** : sans importance (le routeur ne lit rien sur le port série)

Messages Attendus
"""""""""""""""""

L’ouverture du moniteur série redémarre le routeur (signal DTR). Après 3 secondes, il affiche sa configuration, terminée par `----`, puis une ligne de mesures toutes les 5 secondes (valeur par défaut de `DATALOG_PERIOD_IN_SECONDS`, dans `config_system.h`).

Exemple en triphasé, avec la sortie `HumanReadable` (extrait d’une capture réelle, lignes omises remplacées par « ... ») :

.. code-block:: text

   ----------------------------------
   Sketch ID: Mk2_3phase_RFdatalog_temp
   From branch 'dev', commit 0d88595e
   Build environment: basic
   Build on 2026-11-07 17:47:10+01:00
   ADC mode:       free-running
   Motherboard:    new (internal 1.1 V reference)
   Electrical settings
   ...
   Override feature is present
   *** Override Pins Configuration ***
   ...
   RF capability is NOT present
   Datalogging capability in Human-readable format
   ...
   ----
   308.52, P:-2, P1:0, P2:-1, P3:-1, V1:232.86, V2:232.88, V3:233.12, (minSampleSets/MC 32, #ofSampleSets 8011)
   316.57, P:0, P1:0, P2:0, P3:0, V1:232.75, V2:232.77, V3:233.02, (minSampleSets/MC 32, #ofSampleSets 8010)

Le contenu de la configuration dépend de `config.h` et de `calibration.h`. Dans les lignes de mesures, ``P`` est la puissance totale en W (positive en import), ``P1`` à ``P3`` celle de chaque phase et ``V1`` à ``V3`` les tensions. En monophasé, la ligne donne ``P:`` et ``V:``, puis, avec la sonde CT2, la puissance et l’énergie routées : ``diverted <W> W, <Wh> Wh``.

.. note::
   Avec le `config.h` fourni (`SERIAL_OUTPUT_TYPE` en `IoT`), la configuration s’affiche de la même façon, à 9600 bauds 8N1, puis le routeur passe en 7E1 pour le module mk2Wifi : les caractères illisibles qui suivent sont normaux. Pour lire les mesures au moniteur série, passer en `HumanReadable` (voir *Format de Sortie Série* plus haut).

Si Aucun Message n’Apparaît
"""""""""""""""""""""""""""

#. Vérifier que le bon baud rate est sélectionné (9600 bauds)
#. Vérifier le câblage FTDI (TX ↔ RX)
#. Vérifier que le routeur est alimenté
#. Vérifier l’oscillateur 16 MHz et les condensateurs C7/C8

Adresses des Sondes de Température
"""""""""""""""""""""""""""""""""""

Le routeur ne recherche pas les sondes : il lit celles dont les adresses sont dans `config.h`. En mode étalonnage (`CALIBRATION_MODE` à `true`, avec `TEMP_SENSOR_PRESENT`), il les liste au démarrage sur le moniteur série, avec la sortie lisible. Sinon, pour relever les adresses, téléverser l’exemple de la bibliothèque *OneWire* (**Fichier → Exemples → OneWire → DS18x20_Temperature**), en changeant au besoin la broche dans `OneWire ds(…)`. Le moniteur série affiche alors l’adresse de chaque sonde branchée :

.. code-block:: text

   ROM = 28 AA BB CC DD EE FF 1
   ROM = 28 AA BB CC DD EE FF 2

Copier ces adresses dans `config.h` (section sondes de température, chaque octet sous la forme `0x28`, `0xAA`…, un octet affiché `1` s’écrit `0x01`), puis téléverser à nouveau le firmware du routeur. Coller une étiquette avec l’adresse sur le câble de chaque sonde.


