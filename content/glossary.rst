
.. _glossary:

=========
Glossaire
=========

.. glossary::
   :sorted:

   CT
     | *Current Transformer* ou dans notre cas **pince ampèremétrique**.
     | La pince ampèremétrique, aussi appelée capteur de courant sans contact, est un type d'ampèremètre permettant de mesurer l'intensité du courant électrique circulant dans un fil conducteur sans avoir à ouvrir le circuit pour y placer un ampèremètre classique.

     .. seealso::
        | `Wikipédia, Pince ampèremétrique <https://fr.wikipedia.org/wiki/Pince_amp%C3%A8rem%C3%A9trique>`_
        | `CT sensors - An Introduction <https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/introduction.html>`_

   PCB
     | *printed circuit board* ou **circuit imprimé**.
     | Un circuit imprimé est un support, en général une plaque, permettant de maintenir et de relier électriquement un ensemble de composants électroniques entre eux, dans le but de réaliser un circuit électronique complexe. On le désigne aussi par le terme de carte électronique.
     
     .. seealso:: `Wikipédia, Circuit imprimé <https://fr.wikipedia.org/wiki/Circuit_imprim%C3%A9>`_

   Burden
     | Résistance de charge.
     | Si le capteur CT est du type "sortie courant" tel que le YHDC SCT-013-000, le signal de courant doit être converti en signal de tension avec une résistance de charge.
     .. seealso:: `CT Sensors - Interfacing with an Arduino <https://docs.openenergymonitor.org/electricity-monitoring/ct-sensors/interface-with-arduino.html>`_

   ADC
     | *Analog Digital Converter* ou convertisseur analogique/numérique.
     | Il permet de convertir un signal analogique, par exemple une tension, en un signal numérique, par exemple une valeur entre 0 et 1023.
     | Supposons que la plage de mesure aille de 0 à 5 V, alors, une tension d'entrée de 2.5 V correspondra à la valeur 511. Une tension de 5 V correspondra à une valeur de 1023.

   AC
     | *Alternative Current* ou courant alternatif.

   DC
     | *Direct Current* ou courant continu.

   Optocoupleur
     | Ou photocoupleur.
     | Ce composant électronique est capable de transmettre un signal d'un circuit électrique à un autre, sans qu'il y ait de contact galvanique entre eux, c'est-à-dire que les 2 circuits sont totalement isolés l'un de l'autre.

     .. seealso:: `Wikipédia, Photocoupleur <https://fr.wikipedia.org/wiki/Photocoupleur>`_
