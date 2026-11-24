Compilation et Téléversement
""""""""""""""""""""""""""""

.. admonition:: Checklist avant téléversement

   - [ ] Modifications sauvegardées dans `config.h`
   - [ ] Routeur alimenté (230 V)
   - [ ] Adaptateur FTDI connecté (USB + PCB)
   - [ ] Bon port COM sélectionné
   - [ ] Type de carte = Arduino Uno
   - [ ] ATmega328P avec le *bootloader* Arduino Uno : une puce vierge ne se programme pas par l’adaptateur FTDI, il faut d’abord y graver le *bootloader* avec un programmateur ISP

#. Cliquer sur le bouton **« Vérifier »** (✓) pour compiler

   - Attendre la compilation (1–2 minutes la première fois)
   - Vérifier qu’il n’y a **aucune erreur**

#. Si la compilation réussit, cliquer sur **« Téléverser »** (→)

   - Les LED **TX** et **RX** de l’adaptateur FTDI clignotent (si l’adaptateur en a)
   - Attendre le message **« Téléversement terminé »**

.. tip::
   Si la compilation échoue avec le message ``Please define 'gnu++17' in 'platform.txt'``,
   c’est que le fichier `platform.txt` n’a pas été correctement modifié (voir :ref:`arduino-cpp17-config`).

