Le triac, ou triode pour courant alternatif, est un composant électronique de la famille des thyristors utilisé comme interrupteur semi-conducteur pour contrôler la puissance délivrée à une charge électrique.<br />
Sa particularité est de pouvoir conduire le courant dans les deux sens et ainsi de travailler avec du courant alternatif (AC).<br />
Lorsqu'il est utilisé pour réguler la puissance fournie à un appareil purement résistif, tel qu'un radiateur électrique, un chauffe-eau ou une lampe à incandescence, le triac permet de moduler finement l'énergie transmise et donc de contrôler l'intensité de la chaleur ou de la lumière émise.

# Principe de Fonctionnement d'une Sortie Triac
Un triac est contrôlé par un signal de gâchette (ou signal de commande) appliqué à sa broche de commande, appelée gâchette ou *gate*.<br />
Lorsque ce signal atteint un certain seuil, le triac s'amorce et devient conducteur, permettant ainsi au courant de passer à travers lui.<br />
Une fois amorcé, il reste conducteur jusqu'à ce que le courant passant à travers lui tombe en dessous d'un certain niveau, généralement proche de zéro, ce qui se produit naturellement à chaque demi-cycle du courant alternatif.

# Contrôle de la Puissance
Pour contrôler la puissance fournie à un appareil résistif, on utilise souvent une technique appelée variation de phase ou gradation.<br />
Elle consiste à retarder l'amorçage du triac dans chaque demi-cycle de la tension alternative. En ne déclenchant le triac que pendant une portion de chaque demi-cycle, on réduit la quantité d'énergie fournie à la charge.<br />
Plus le retard est important, plus la puissance transmise est faible, et inversement.<br />
Le principal inconvénient de cette méthode est qu'elle génère des harmoniques dans le réseau électrique.

Une autre approche consiste à ne laisser passer que des sinusoïdes complètes, une technique connue sous le nom de modulation par trains d'ondes ou *burst fire control*.<br />
Le principal inconvénient de cette méthode est que la gradation est moins précise, mais l'expérience a montré que cela ne pose pas de problème avec les compteurs électriques en France, quel que soit le modèle.<br />
Le principal **avantage** de cette méthode est qu'elle ne génère aucune harmonique dans le réseau électrique.

# Applications Typiques
- **Éclairage** : Les variateurs de lumière utilisent des triacs pour ajuster l'intensité de l'éclairage. En contrôlant le moment où le triac s'amorce, on peut varier la luminosité de la lampe.
- **Chauffage** : Pour les radiateurs électriques, les triacs sont utilisés pour réguler la température. En modifiant le temps de conduction, on peut augmenter ou diminuer la chaleur produite par l'élément chauffant.

## Avantages par rapport à un relais
- **Contrôle Précis** : Le triac permet un contrôle très précis de la puissance, ce qui est idéal pour des applications où une régulation fine est nécessaire.
- **Commutation Silencieuse** : Contrairement aux relais mécaniques, les triacs commutent silencieusement, sans le bruit de claquement des contacts.
- **Pas de Pièces Mobiles** : L'absence de pièces mobiles réduit l'usure mécanique et augmente la fiabilité et la durée de vie du système de commutation.

# Considérations Techniques
- **Dissipation Thermique** : Les triacs génèrent de la chaleur lors de la conduction. Il est donc important de prévoir une dissipation thermique adéquate, souvent sous la forme de radiateurs ou dissipateurs.
- **Compatibilité de Charge** : Le courant étant haché, seuls des appareils purement résistifs peuvent être contrôlés par un triac.

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
