(burden-calc)=

````{exercise} Un peu de mathématiques
Voici les 3 formules qui vous permettront de calculer une inconnue à partir des 2 autres données connues.

> Calcul de la résistance de burden en fonction de l'intensité efficace maximale :
> ```{math}
> burden\_resistor = {system\_voltage * ct\_turns \over 2 * \sqrt{2} * I_{RMS}}
> ```

> Calcul de l'intensité efficace maximale en fonction de la résistance de {term}`burden` :
> ```{math}
> I_{RMS} = {system\_voltage * ct\_turns \over 2 * \sqrt{2} * burden\_resistor }
> ```

> Calcul du nombre de tours de capteur en fonction de la résistance de {term}`burden` et de l'intensité efficace maximale :
> ```{math}
> ct\_turns = {2 * \sqrt{2} * I_{RMS} \over system\_voltage * burden\_resistor}
> ```

Dans notre cas précis, nous avons : {math}`ct\_turns = 2000`

**{math}`I_{RMS}`** correspond à l'intensité efficace.<br />
Pour un appareil purement résistif (chauffe-eau, …), nous avons {math}`P_{RMS} = V_{RMS} * I_{RMS}`.<br />

Exemple pour un chauffe-eau de 3000 W, nous aurons donc 
```{math}
I_{RMS} = {P_{RMS} \over V_{RMS}} = {3000 \over 230} \approx 13 A.
```
````