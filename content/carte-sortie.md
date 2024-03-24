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

# Assemblage d'une carte de sortie
Pour les cartes de sortie, nous allons procéder de façon similaire, dans cet ordre :
1. résistances
2. support MOC
3. connecteur·s Molex
4. connecteur de puissance
5. triac

```{danger}
Il est crucial de prêter une attention particulière à la **qualité** des soudures sur la section **haute tension** de cette carte.

Une soudure mal réalisée peut provoquer une défaillance immédiate de la carte lors de la mise sous tension, avec un risque potentiel d'incendie.
```

---
## Installation des *agrafes* en cuivre massif
La première étape de l'assemblage consiste à installer une paire d'*agrafes* en cuivre massif qui renforcent la capacité de la carte à gérer des courants élevés.

La section transversale recommandée est de 1,5 mm² en raison de la très faible longueur entre le triac et le connecteur de puissance.

Les paires de trous appropriées sont indiquées par les lignes épaisses sur la couche de sérigraphie. Ces trous sont espacés d'environ 5 mm.

Pour commencer, le fil est plié de manière à passer à travers ces trous.

Ensuite, les extrémités sont pliées vers l'extérieur et pressées fermement contre le dessous du {term}`PCB`.

Une fois les *agrafes* correctement positionnées, les quatre extrémités peuvent être coupées à la longueur appropriée.

---
## Soudure des composants faible puissance

Avec les agrafes en cuivre correctement positionnées, tous les composants de faible puissance peuvent maintenant être installés.

Comme le montre le schéma du circuit :
- **R1** doit être de **120 Ω** si le circuit fonctionne à partir d'une source de **3,3 V**, ou de **180 Ω** pour un fonctionnement à **5 V**.
- **R2** doit être de **330 Ω**.
- **R3** doit être de **360 Ω**.

Si vous installez un connecteur DIL pour l'{term}`optocoupleur` ou le circuit intégré *déclencheur*, veillez à ce que l'encoche soit positionnée en bas, à côté du cercle sur le {term}`PCB`.

Ces deux caractéristiques indiquent l'emplacement de la broche 1.

---
## Soudure de la partie *haute puissance*/*haute tension*

```{danger}
La qualité des soudures est d'une importance capitale pour cette étape.

Une soudure mal réalisée peut provoquer une défaillance immédiate de la carte lors de la mise sous tension, avec un risque potentiel d'incendie.
```

### Connecteur haute puissance

Ce composant peut être maintenu provisoirement en place en pliant légèrement les agrafes en cuivre pour qu'elles pincent les broches saillantes.

Ensuite, avec un fer à souder bien chaud (réglez la température à 450 °C si possible), appliquez généreusement de la soudure.

### Triac

De la même manière, ce composant peut être maintenu provisoirement en place en pliant légèrement les agrafes en cuivre pour qu'elles pincent les broches saillantes.

Seuls 1 à 2 mm des pattes du triac devraient dépasser.

Pour faciliter cette opération et aussi pour protéger le triac des hautes températures, il est conseillé de plaquer le triac contre l'un des dissipateurs non encore montés que vous avez à disposition. Vous pouvez utiliser une pince à linge ou toute autre pince à ressort.

Pour les connexions en contact avec chacune des agrafes, un bon fer chaud et beaucoup de soudure sont nécessaires.

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
