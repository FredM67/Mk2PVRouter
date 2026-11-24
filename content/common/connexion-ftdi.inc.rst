Connexion du Routeur
""""""""""""""""""""

Le kit est livré avec un **adaptateur FTDI** : une petite carte avec un connecteur USB d’un côté et 6 broches mâles de l’autre. Ces 6 broches ont le même ordre que le connecteur FTDI (J0) de la carte-mère : chaque broche de l’adaptateur se relie à la broche de même rang du connecteur, sans croisement.

#. ⚠️ **Couper l’alimentation secteur** du routeur (disjoncteur)
#. Brancher l’adaptateur FTDI sur le connecteur FTDI (J0) du routeur. La broche 1 (GND) est marquée « GND> » sur la sérigraphie.

   +------------------------+-----------------------------------+
   | Broche de l’adaptateur | Connecteur FTDI (J0) de la carte  |
   +========================+===================================+
   | GND                    | Broche 1 : GND                    |
   +------------------------+-----------------------------------+
   | CTS                    | Broche 2 : non connectée          |
   +------------------------+-----------------------------------+
   | VCC                    | Broche 3 : non connectée          |
   +------------------------+-----------------------------------+
   | TX (émission)          | Broche 4 : RX de l’ATmega328P     |
   +------------------------+-----------------------------------+
   | RX (réception)         | Broche 5 : TX de l’ATmega328P     |
   +------------------------+-----------------------------------+
   | DTR                    | Broche 6 : DTR, reset automatique |
   +------------------------+-----------------------------------+

   .. warning::
      ⚠️ Vérifiez que **GND** de l’adaptateur arrive bien sur la broche 1 (« GND> ») : branché à l’envers, l’adaptateur ne communique pas. La liaison **DTR** est indispensable : sans elle, l’ATmega328P n’est pas redémarré automatiquement pour le téléversement, qui échoue (« not in sync »).

      La broche 3 (VCC) du connecteur n’est reliée à rien sur la carte : le routeur n’est jamais alimenté par l’adaptateur, il reste alimenté par le secteur.

#. Vérifier le cavalier ou le commutateur de l’adaptateur FTDI : sa tension doit être celle de l’ATmega328P. Sur la carte universelle, c’est **3,3 V** (position d’usine du cavalier **V sel.**, voir :ref:`cavaliers`) ; **5 V** seulement si ce cavalier a été passé en 5 V.

#. Connecter l’adaptateur FTDI à l’ordinateur (port USB)

#. **Mettre le routeur sous tension** (réenclencher le disjoncteur)
