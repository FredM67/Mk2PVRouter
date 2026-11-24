Connexion du Routeur
""""""""""""""""""""

Le PCB dispose d’un connecteur 6 broches pour l’adaptateur FTDI. Si votre adaptateur a un connecteur compatible, branchez-le directement — c’est la méthode la plus simple.

Si vous utilisez des fils individuels, suivez les instructions ci-dessous.

#. ⚠️ **Couper l’alimentation secteur** du routeur (disjoncteur)
#. Brancher l’adaptateur FTDI sur le connecteur FTDI (J0) du routeur. La broche 1 (GND) est marquée « GND> » sur la sérigraphie.

   +------------------------+-----------------------------------+----------------------------+
   | Broche de l’adaptateur | Connecteur FTDI (J0) de la carte  | Fil du câble FTDI TTL-232R |
   +========================+===================================+============================+
   | GND                    | Broche 1 : GND                    | Noir                       |
   +------------------------+-----------------------------------+----------------------------+
   | CTS                    | Broche 2 : non connectée          | Marron (laisser libre)     |
   +------------------------+-----------------------------------+----------------------------+
   | VCC                    | Broche 3 : non connectée          | Rouge (laisser libre)      |
   +------------------------+-----------------------------------+----------------------------+
   | TX (émission)          | Broche 4 : RX de l’ATmega328P     | Orange                     |
   +------------------------+-----------------------------------+----------------------------+
   | RX (réception)         | Broche 5 : TX de l’ATmega328P     | Jaune                      |
   +------------------------+-----------------------------------+----------------------------+
   | DTR (ou RTS)           | Broche 6 : DTR, reset automatique | Vert (RTS)                 |
   +------------------------+-----------------------------------+----------------------------+

   .. warning::
      ⚠️ **Câblage avec des fils séparés** : le fil **DTR** est indispensable. Sans DTR, l’ATmega328P n’est pas redémarré automatiquement pour le téléversement, qui échoue (« not in sync »).

      Le fil VCC (rouge) de l’adaptateur reste libre : la broche 3 du connecteur n’est reliée à rien sur la carte, et le routeur ne doit jamais être alimenté par l’adaptateur. Ne le reliez à aucune autre broche.

#. Vérifier le cavalier ou le commutateur de l’adaptateur FTDI : sa tension doit être celle de l’ATmega328P. Sur la carte universelle, c’est **3,3 V** (position d’usine du cavalier **V sel.**, voir :ref:`cavaliers`) ; **5 V** seulement si ce cavalier a été passé en 5 V.

#. Connecter l’adaptateur FTDI à l’ordinateur (port USB)

#. **Mettre le routeur sous tension** (réenclencher le disjoncteur)
