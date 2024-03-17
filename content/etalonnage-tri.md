(etalonnage-tri)=

# Étalonnage

Contrairement à la version monophasée, le modèle triphasé ne peut pas dévier de manière fiable l'énergie excédentaire sans nécessiter un étalonnage aussi précis que possible.  
En effet, étant donné qu'en triphasé, le routeur calcule la somme algébrique des puissances instantanées sur chaque phase, il faut que les mesures soient aussi précises que possible.

Les composants électroniques ne sont jamais parfaits. Ils ont chacun des caractéristiques données accompagnées d'une tolérance. Les tolérances classiques sont de 5 ou 10 %. Il convient donc d'étalonner chaque ligne de mesure afin que la somme finale soit la plus juste possible.

Pour un étalonnage précis, une certaine forme de référence standard est nécessaire. Le compteur d'électricité installé peut souvent être utilisé à cette fin.

La plupart des compteurs d'électricité génèrent un flux d'impulsions optiques pour indiquer le taux de consommation d'énergie. En plaçant un transformateur de courant {term}`CT` autour de l'un des câbles d'alimentation entrants, et en exécutant le logiciel approprié sur le matériel en cours de test, un flux d'impulsions optiques similaire peut être généré.

Le taux du flux d'impulsions pour le matériel en cours de test peut être ajusté en modifiant la valeur ```f_powerCal``` pertinente. Lorsque les deux flux d'impulsions sont synchronisés, l'étalonnage correct a été atteint.

```{admonition} Ligne de mesure
Ensemble des composants constituants la prise de mesure. Elle part de l'Arduino jusqu'à la pince ampèremétrique en passant par les résistances, connecteurs et les câbles.
```

```{admonition} Pré-requis
Les pinces doivent être installées sur chaque phase correspondante par rapport à l'alimentation du routeur.
```

## {term}`CT`s *grille/réseau*
