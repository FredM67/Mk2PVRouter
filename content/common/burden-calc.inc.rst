.. exercise:: Un peu de mathématiques
   :class: dropdown

   Voici les 3 formules qui vous permettront de calculer une inconnue à partir des 2 autres données connues.

   Dans ces formules :

   - :math:`V_{REF}` = tension de référence interne de l'ATmega328P = **1,1 V**
   - :math:`N` = rapport de transformation du :term:`CT` (nombre de tours)
   - :math:`I_{RMS}` = intensité efficace maximale côté **primaire** (le courant mesuré)
   - :math:`R_{burden}` = résistance de charge en ohms

   Calcul de la résistance de :term:`burden` en fonction de l'intensité efficace maximale :

   .. math::

      R_{burden} = \frac{V_{REF} \times N}{2 \times \sqrt{2} \times I_{RMS}}

   |
   | Calcul de l'intensité efficace maximale en fonction de la résistance de :term:`burden` :

   .. math::

      I_{RMS} = \frac{V_{REF} \times N}{2 \times \sqrt{2} \times R_{burden}}

   |
   | Calcul du nombre de tours de capteur en fonction de la résistance de :term:`burden` et de l'intensité efficace maximale :

   .. math::

      N = \frac{2 \times \sqrt{2} \times I_{RMS} \times R_{burden}}{V_{REF}}

   |
   | **Exemple concret** : CT de type SCT-013-000 (100 A / 50 mA, donc :math:`N = 2000`) avec :math:`R_{burden} = 22\,\Omega`

   .. math::

      I_{RMS\_max} = \frac{1{,}1 \times 2000}{2 \times \sqrt{2} \times 22} \approx 35{,}4\,\text{A}

   Pour un appareil purement résistif (chauffe-eau…), nous avons :math:`P_{RMS} = V_{RMS} \times I_{RMS}`.

   Exemple pour un chauffe-eau de **3000 W** :

   .. math::

      I_{RMS} = \frac{P_{RMS}}{V_{RMS}} = \frac{3000}{230} \approx 13\,\text{A}

   Un burden de 22 Ω avec un CT de 2000 tours est donc largement suffisant pour cette application.
