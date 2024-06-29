Le triac, également connu sous le nom de triode pour courant alternatif, appartient à la catégorie des thyristors et sert d'interrupteur semi-conducteur. Il a la capacité unique de gérer le courant dans les deux directions, ce qui le rend idéal pour les applications utilisant du courant alternatif (AC).<br />
Utilisé pour ajuster la puissance fournie à des dispositifs purement résistifs comme des radiateurs, des chauffe-eau ou des lampes à incandescence, le triac permet de moduler avec précision l'énergie distribuée. Cela offre un contrôle fin sur le niveau de chaleur ou d'éclairage produit.

# Principe de Fonctionnement d'une Sortie Triac
Un triac est activé par un signal de déclenchement envoyé à sa broche de commande, également connue sous le nom de gâchette ou *gate*.<br />
Lorsque ce signal dépasse un seuil spécifique, le triac s'active et commence à conduire le courant, permettant ainsi son passage.<br />
Une fois activé, le triac continue de conduire le courant jusqu'à ce que celui-ci descende en dessous d'un certain niveau, souvent proche de zéro.<br />
Ce phénomène se produit automatiquement à la fin de chaque demi-cycle du courant alternatif, entraînant l'arrêt du passage du courant.

# Contrôle de la Puissance
Pour contrôler la puissance fournie à un appareil résistif, on utilise souvent une technique appelée variation de phase ou gradation.<br />
Elle consiste à retarder l'amorçage du triac dans chaque demi-cycle de la tension alternative. En ne déclenchant le triac que pendant une portion de chaque demi-cycle, on réduit la quantité d'énergie fournie à la charge.<br />
Plus le retard est important, plus la puissance transmise est faible, et inversement.<br />
Le principal inconvénient de cette méthode est qu'elle génère des harmoniques dans le réseau électrique.

Une autre approche consiste à ne laisser passer que des sinusoïdes complètes, une technique connue sous le nom de modulation par trains d'ondes ou *burst fire control*.<br />
Le principal inconvénient de cette méthode est que la gradation est moins précise, mais l'expérience a montré que cela ne pose pas de problème avec les compteurs électriques en France, quel que soit le modèle.<br />
Le principal **avantage** de cette méthode est qu'elle ne génère aucune harmonique dans le réseau électrique.

Pour ajuster la puissance délivrée à un dispositif résistif, on emploie couramment une méthode nommée modulation de phase ou gradation.<br />
Cette technique consiste à retarder l'activation du triac à un moment précis de chaque demi-cycle du courant alternatif.<br />
En activant le triac seulement durant une partie du demi-cycle, on diminue l'énergie transmise à l'appareil.<br />
Ainsi, plus le déclenchement du triac est retardé, moins la puissance fournie est élevée, et vice-versa.<br />
Toutefois, cette méthode a pour inconvénient de produire des harmoniques sur le réseau électrique.

Une alternative est de permettre uniquement le passage de cycles complets de sinusoïdes, une technique appelée modulation par trains d'ondes ou *burst fire control*.<br />
Bien que cette méthode offre une gradation moins fine, les tests montrent qu'elle ne présente pas de problème avec les compteurs électriques en France, indépendamment du modèle utilisé.<br />
Son **avantage principal** réside dans le fait qu'elle n'introduit pas d'harmoniques sur le réseau électrique.

# Applications typiques
- **Éclairage** : Les *dimmers*, ou variateurs de lumière, exploitent les triacs pour moduler l'intensité lumineuse. En ajustant le moment d'activation du triac, il est possible de faire varier la luminosité des lampes.
- **Chauffage** : Dans le cas des chauffages électriques, les triacs servent à contrôler la température. En changeant la durée pendant laquelle le courant est conduit, on peut régler la quantité de chaleur émise par l'appareil de chauffage.

## Avantages comparés à un relais
- **Contrôle Fin** : Le triac offre une gestion très précise de la puissance, ce qui est parfait pour les applications nécessitant un ajustement délicat.
- **Commutation Sans Bruit** : À l'inverse des relais mécaniques, les triacs fonctionnent sans produire de bruit de clic caractéristique lors de la commutation.
- **Absence de Composants Mobiles** : Le fait qu'il n'y ait pas de composants mobiles diminue l'usure due au mouvement, ce qui rend le système de commutation plus fiable et prolonge sa durée de vie.

# Considérations Techniques
- **Dissipation Thermique** : L'utilisation des triacs entraîne une production de chaleur pendant leur fonctionnement. Il est crucial d'assurer une bonne évacuation de cette chaleur, généralement à l'aide de dispositifs tels que des radiateurs ou des dissipateurs thermiques.
- **Compatibilité de Charge** : Du fait que le triac interrompt le courant de manière périodique, seuls les équipements résistifs (comme les chauffages ou les lampes) sont adaptés pour être contrôlés par un triac.

# Composition d'un kit pour étage de sortie triac
Ce kit contient tout le nécessaire pour assembler un circuit de sortie :
- Un **circuit imprimé** qui distingue clairement les zones de basse et de haute tension de chaque côté.
- Une **résistance R1**, dont la valeur est choisie en fonction de la tension nominale du système et du modèle d'optocoupleur utilisé.
- Une **résistance R2**, sélectionnée selon le modèle d'optocoupleur.
- Une **résistance R3**.
- Un **support DIL** pour l'optocoupleur, comportant deux rangées de trois broches.
- Deux paires de **connecteurs type Molex**.
- Un **isolant** qui assure à la fois l'isolation électrique et la conduction thermique.
- Un **triac**, adapté aux exigences spécifiques de l'application.
- Un **connecteur de puissance** qui dispose habituellement de trois broches, la broche centrale étant inutilisée.
- Un **morceau de cuivre massif** de 1.5 mm² de section.
  
```{figure} img/Kit-sortie.jpg
:alt: Contenu d'un kit de sortie
:align: center
:scale: 25%

Contenu d'un kit de sortie
```

# Assemblage d'une carte de sortie
Pour les cartes de sortie, nous allons procéder de façon similaire, dans cet ordre :
1. résistances
2. support {term}`optocoupleur`
3. connecteur·s Molex
4. connecteur de puissance
5. triac

```{danger}
Il est crucial de prêter une attention particulière à la **qualité** des soudures sur la section **haute tension** de cette carte.

Une soudure mal réalisée peut provoquer une défaillance immédiate de la carte lors de la mise sous tension, avec un risque d'incendie.
```

---
## Installation des *agrafes* en cuivre massif
La première étape du montage consiste à installer des *agrafes* en cuivre pur pour augmenter la capacité de la carte à supporter des courants forts.

Il est recommandé d'utiliser du cuivre d'une section transversale de 1,5 mm², compte tenu de la courte distance entre le triac et le connecteur de puissance.

Les emplacements pour ces agrafes sont marqués sur le circuit imprimé par des lignes épaisses sur la couche de sérigraphie, avec un espacement d'environ 5 mm entre les trous.

Pour installer les agrafes, commencez par plier le fil de cuivre afin qu'il traverse ces trous.

Puis, pliez les extrémités vers l'extérieur et pressez-les fermement contre la face inférieure du circuit imprimé. L'utilisation d'une pince multiprise facilitera cette tâche, tout en prenant soin de ne pas abîmer le circuit.

Une fois les agrafes correctement mises en place, coupez les quatre extrémités à la longueur nécessaire.

```{figure} img/Pose-agrafes.jpg
:alt: Vue dessus/dessous, agrafes posées
:align: center
:scale: 25%

Vue dessus/dessous, agrafes posées
```

---
## Installation des composants de faible puissance, support DIL
Une fois les agrafes de cuivre mises en place, il est temps d'installer les composants qui nécessitent peu de puissance.

Selon le plan du circuit :
- La résistance **R1** doit être de **120 Ω** si le circuit est alimenté en **3,3 V**, ou de **180 Ω** pour une alimentation en **5 V**.
- La résistance **R2** doit avoir une valeur de **330 Ω**.
- La résistance **R3** doit être de **360 Ω**.

```{note}
Pour des besoins spécifiques, un autre type d'{term}`optocoupleur` pourrait être nécessaire.  
Dans ce cas, les valeurs des résistances peuvent varier.
```

```{hint}
Pour assurer que le support DIL soit correctement fixé et en contact total avec le circuit imprimé, commencez par souder une seule de ses broches. Ensuite, vérifiez que le support est bien en place et parfaitement aligné avant de procéder à la soudure des cinq broches restantes.
```

```{figure} img/Soudure-Rs-DIL.jpg
:alt: Vue dessus/dessous, résistances et support DIL soudés
:align: center
:scale: 25%

Vue dessus/dessous, résistances et support DIL soudés
```

## Soudure des connecteurs type Molex
Ces connecteurs ont une hauteur similaire au connecteur de puissance.  
Il sera recommandé de souder la broche centrale du connecteur de puissance en premier. En effet, ce dernier peut être facilement maintenu pour cette opération grâce aux agrafes précédemment installées.  
Une fois soudé, ce connecteur sera d'une grande aide pour souder les deux autres connecteurs type Molex.

```{figure} img/Maintien-connecteur.jpg
:alt: Connecteur de puissance, broche centrale soudée
:align: center
:scale: 25%

Connecteur de puissance, broche centrale soudée
```

```{figure} img/Soudure-Molex.jpg
:alt: Connecteurs type Molex soudés
:align: center
:scale: 25%

Connecteurs type Molex soudés
```

---
## Soudure de la partie *haute puissance*/*haute tension*

```{danger}
La qualité des soudures est d'une importance **capitale** pour cette étape.

Une soudure mal réalisée peut provoquer une défaillance immédiate de la carte lors de la mise sous tension, avec un risque d'incendie.
```

### Connecteur haute puissance

Ce composant peut être maintenu provisoirement en place en pliant légèrement les agrafes en cuivre pour qu'elles pincent les broches saillantes.

Ensuite, avec un fer à souder bien chaud (réglez la température à 450 °C si possible), appliquez généreusement de la soudure.

### Triac

De la même manière, ce composant peut être maintenu provisoirement en place en pliant légèrement les agrafes en cuivre pour qu'elles pincent les broches saillantes.

Seuls 1 à 2 mm des pattes du triac devraient dépasser.

Pour faciliter cette opération et aussi pour protéger le triac des hautes températures, il est conseillé de plaquer le triac contre l'un des dissipateurs non encore monté que vous avez à disposition. Vous pouvez utiliser une pince à linge ou toute autre pince à ressort.

Pour les soudures au niveau de chacune des agrafes, un bon fer chaud et beaucoup de soudure seront nécessaires.

```{warning}
Lors de la soudure du triac, veillez à bien vérifier que la soudure est *remontée* de l'autre côté du circuit.

Cela assurera une continuité parfaite mais aussi une solidité accrue.
```

---
## Installation de l'{term}`optocoupleur`

Ce petit composant à 6 broches fait office de *pont* entre les parties basse tension et haute tension du circuit.<br />
Le repère sur la puce (mis en évidence ici en rouge) doit être positionné à côté du cercle sur le {term}`PCB`.

Si ce composant est monté à l'envers, le circuit ne fonctionnera pas. Cependant, grâce à la disposition de ses broches, il devrait survivre à cette erreur.

---
# Test

Lors de la construction d'un système complet, il peut être préférable de monter l'étage de sortie finalisé dans le boîtier avant de procéder à son test.

Les conseils suivants sont destinés aux situations où un étage de sortie doit être testé de manière indépendante.

```{danger}
**Avertissement de Sécurité**

Pour vérifier le bon fonctionnement du déclencheur et du triac, un accès à la tension du réseau électrique **230 V** CA est nécessaire.

Faites preuve de la plus grande prudence et n'entamez cette étape que si vous avez les compétences nécessaires pour le faire en toute sécurité.
```

Voici une plate-forme construite qui permet de tester les cartes de sortie avec ou sans le triac soudé en place.

Lors du test d'une carte de sortie, il est important que le triac fasse partie du circuit électrique, sinon tout le courant de charge passera par le circuit {term}`optocoupleur` et un ou plusieurs composants seront alors détruits immédiatement.

En tenant dûment compte de l'avertissement de sécurité ci-dessus, l'approche simple illustrée ci-dessous devrait convenir pour tester des cartes individuelles.
