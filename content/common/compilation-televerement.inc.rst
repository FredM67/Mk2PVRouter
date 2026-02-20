Compilation et Téléversement
""""""""""""""""""""""""""""

.. admonition:: Checklist avant téléversement

   - [ ] Modifications sauvegardées dans `config.h`
   - [ ] Routeur alimenté (230 V)
   - [ ] Adaptateur FTDI connecté (USB + PCB)
   - [ ] Bon port COM sélectionné
   - [ ] Type de carte = Arduino Uno

#. Cliquer sur le bouton **« Vérifier »** (✓) pour compiler

   - Attendre la compilation (1–2 minutes la première fois)
   - Vérifier qu’il n’y a **aucune erreur**

#. Si la compilation réussit, cliquer sur **« Téléverser »** (→)

   - La LED **TX** sur l’adaptateur FTDI clignote
   - La LED **RX** sur le routeur clignote
   - Attendre le message **« Téléversement terminé »**

.. tip::
   Si la compilation échoue avec des erreurs sur `std::array` ou `constexpr`,
   c’est que le fichier `platform.txt` n’a pas été correctement modifié (voir :ref:`arduino-cpp17-config`).

