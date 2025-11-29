Connexion du Routeur
""""""""""""""""""""

Le PCB dispose d'un connecteur 6 broches pour l'adaptateur FTDI. Si votre adaptateur a un connecteur compatible, branchez-le directement — c'est la méthode la plus simple.

Si vous utilisez des fils individuels, suivez les instructions ci-dessous.

#. ⚠️ **Couper l'alimentation secteur** du routeur (disjoncteur)
#. Brancher l'adaptateur FTDI sur le routeur :

   +----------------+---------------------+------------------------+
   | Broche FTDI    | Broche PCB          | Couleur câble (FTDI)   |
   +================+=====================+========================+
   | GND            | 0 V (ou GND)        | Noir                   |
   +----------------+---------------------+------------------------+
   | TX (Transmit)  | RX (Receive)        | Vert ou Orange         |
   +----------------+---------------------+------------------------+
   | RX (Receive)   | TX (Transmit)       | Blanc ou Jaune         |
   +----------------+---------------------+------------------------+
   | VCC            | **NE PAS CONNECTER**| Rouge (laisser libre)  |
   +----------------+---------------------+------------------------+

.. danger::
   ⚠️ **Câblage manuel uniquement** : NE PAS connecter le fil VCC (rouge) de l'adaptateur FTDI au routeur !

   Cela peut endommager l'adaptateur FTDI ou le routeur.

#. Vérifier le cavalier ou switch de l'adaptateur FTDI :

   - Position **3.3 V** si routeur en 3.3 V
   - Position **5 V** si routeur en 5 V

#. Connecter l'adaptateur FTDI à l'ordinateur (port USB)

#. **Mettre le routeur sous tension** (réenclencher le disjoncteur)
