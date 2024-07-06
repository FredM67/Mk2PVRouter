.. _burden-calc:

.. exercise:: Un peu de mathématiques
   :class: dropdown

   Voici les 3 formules qui vous permettront de calculer une inconnue à partir des 2 autres données connues.

   
   Calcul de la résistance de :term:`burden` en fonction de l'intensité efficace maximale :
   
   .. math::

      burden\_resistor = \frac{system\_voltage \times ct\_turns}{2 \times \sqrt{2} \times I_{RMS}}

   
   
   Calcul de l'intensité efficace maximale en fonction de la résistance de :term:`burden` :
   
   .. math::

      I_{RMS} = \frac{system\_voltage \times ct\_turns}{2 \times \sqrt{2} \times burden\_resistor}

   
   
   Calcul du nombre de tours de capteur en fonction de la résistance de :term:`burden` et de l'intensité efficace maximale :
   
   .. math::

      ct\_turns = \frac{2 \times \sqrt{2} \times I_{RMS}}{system\_voltage \times burden\_resistor}

   
   
   Dans notre cas précis, nous avons : :math:`ct\_turns = 2000`

   :math:`I_{RMS}` correspond à l'intensité efficace.

   Pour un appareil purement résistif (chauffe-eau, …), nous avons :math:`P_{RMS} = V_{RMS} \times I_{RMS}`.

   Exemple pour un chauffe-eau de **3000 W**, nous aurons donc :
   
   .. math::

      I_{RMS} = \frac{P_{RMS}}{V_{RMS}} = \frac{3000}{230} \approx 13 A.