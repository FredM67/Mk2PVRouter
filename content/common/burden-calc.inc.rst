.. exercise:: Un peu de mathématiques
   :class: dropdown

   Voici les 3 formules qui vous permettront de calculer une inconnue à partir des 2 autres données connues.

   Dans ces formules :

   - :math:`V_{REF}` = tension de référence interne de l’ATmega328P = **1,1 V**
   - :math:`N` = rapport de transformation du :term:`CT` (nombre de tours)
   - :math:`I_{max}` = intensité efficace maximale côté **primaire**, c’est-à-dire le calibre du disjoncteur qui protège le câble mesuré
   - :math:`R_{burden}` = résistance de charge en ohms

   Calcul de la résistance de :term:`burden <Burden>` en fonction de l’intensité efficace maximale :

   .. math::

      R_{burden} = \frac{V_{REF} \times N}{2 \times \sqrt{2} \times I_{max}}

   |
   | Calcul de l’intensité efficace maximale en fonction de la résistance de :term:`burden <Burden>` :

   .. math::

      I_{max} = \frac{V_{REF} \times N}{2 \times \sqrt{2} \times R_{burden}}

   |
   | Calcul du nombre de tours de capteur en fonction de la résistance de :term:`burden <Burden>` et de l’intensité efficace maximale :

   .. math::

      N = \frac{2 \times \sqrt{2} \times I_{max} \times R_{burden}}{V_{REF}}

   |
   | **Exemple concret** : CT de type SCT-013-000 (100 A / 50 mA, donc :math:`N = 2000`) avec :math:`R_{burden} = 22\,\Omega`

   .. math::

      I_{max} = \frac{1{,}1 \times 2000}{2 \times \sqrt{2} \times 22} \approx 35{,}4\,\text{A}

   Avec 22 Ω, le courant mesurable s’arrête donc à 35,4 A : ce burden ne convient que si le câble mesuré est protégé par un disjoncteur de **32 A au plus**. Ne le choisissez pas d’après la charge pilotée : un chauffe-eau de 3000 W ne tire qu’environ 13 A, mais le CT placé sur l’arrivée du réseau voit le courant de toute la maison.

   Pour un câble protégé par un disjoncteur de 60 A :

   .. math::

      R_{burden} = \frac{1{,}1 \times 2000}{2 \times \sqrt{2} \times 60} \approx 13{,}0\,\Omega

   La valeur normalisée immédiatement inférieure est **12 Ω**, qui mesure jusqu’à 64,8 A environ.
