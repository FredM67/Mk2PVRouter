Le triac, ou triode pour courant alternatif, est un composant électronique de la famille des thyristors utilisé comme interrupteur semi-conducteur pour contrôler la puissance délivrée à une charge électrique.   
Sa particularité est de pouvoir conduire le courant dans les deux sens et ainsi de travailler avec du courant alternatif (AC).   
Lorsqu'il est utilisé pour réguler la puissance fournie à un appareil purement résistif, tel qu'un radiateur électrique, un chauffe-eau ou une lampe à incandescence, le triac permet de moduler finement l'énergie transmise et donc de contrôler l'intensité de la chaleur ou de la lumière émise.

# Principe de Fonctionnement d'une Sortie Triac
Un triac est contrôlé par un signal de gâchette (ou signal de commande) appliqué à sa broche de commande, appelée gâchette ou *gate*.   
Lorsque ce signal atteint un certain seuil, le triac s'amorce et devient conducteur, permettant ainsi au courant de passer à travers lui.   
Une fois amorcé, il reste conducteur jusqu'à ce que le courant passant à travers lui tombe en dessous d'un certain niveau, généralement proche de zéro, ce qui se produit naturellement à chaque demi-cycle du courant alternatif.

# Contrôle de la Puissance
Pour contrôler la puissance fournie à un appareil résistif, on utilise souvent une technique appelée variation de phase ou gradation.   
Elle consiste à retarder l'amorçage du triac dans chaque demi-cycle de la tension alternative. En ne déclenchant le triac que pendant une portion de chaque demi-cycle, on réduit la quantité d'énergie fournie à la charge.   
Plus le retard est important, plus la puissance transmise est faible, et inversement.   
Le principal inconvénient de cette méthode est qu'elle génère des harmoniques dans le réseau électrique.

Une autre approche consiste à ne laisser passer que des sinusoïdes complètes, une technique connue sous le nom de modulation par trains d'ondes ou *burst fire control*.   
Le principal inconvénient de cette méthode est que la gradation est moins précise, mais l'expérience a montré que cela ne pose pas de problème avec les compteurs électriques en France, quel que soit le modèle.   
Le principal **avantage** de cette méthode est qu'elle ne génère aucune harmonique dans le réseau électrique.

# Applications Typiques
- **Éclairage** : Les variateurs de lumière utilisent des triacs pour ajuster l'intensité de l'éclairage. En contrôlant le moment où le triac s'amorce, on peut varier la luminosité de la lampe.
- **Chauffage** : Pour les radiateurs électriques, les triacs sont utilisés pour réguler la température. En modifiant le temps de conduction, on peut augmenter ou diminuer la chaleur produite par l'élément chauffant.

## Avantages par rapport à un relais
- **Contrôle Précis** : Le triac permet un contrôle très précis de la puissance, ce qui est idéal pour des applications où une régulation fine est nécessaire.
- **Commutation Silencieuse** : Contrairement aux relais mécaniques, les triacs commutent silencieusement, sans le bruit de claquement des contacts.
- **Pas de Pièces Mobiles** : L'absence de pièces mobiles réduit l'usure mécanique et augmente la fiabilité et la durée de vie du système de commutation.

# Considérations Techniques
- **Dissipation Thermique** : Les triacs génèrent de la chaleur lors de la conduction. Il est donc important de prévoir une dissipation thermique adéquate, souvent sous la forme de radiateurs.
- **Compatibilité de Charge** : Le courant étant haché, seuls des appareils purement résistifs peuvent être contrôlés par un triac.

# Assemblage d'une carte de sortie
Pour les cartes de sortie, nous allons procéder de façon similaire, dans cet ordre :
1. résistances
2. support MOC
3. connecteur·s Molex
4. connecteur de puissance
5. triac

```{danger}
Certaines soudures sur cette carte ont une très grande importance.

Il faudra veiller à donner une attention particulière à la **qualité** de chacune des soudures sur la partie **haute tension**.

Une soudure ratée peut entraîner la destruction immédiate de la carte avec risque d'incendie lors de la mise sous tension.
```

---
## Pose des *agrafes* en cuivre

La première étape du processus d'assemblage consiste à installer une paire d'*agrafes* en cuivre massif qui augmentent la capacité de la carte à supporter des courants élevés.
La section transversale recommandée est de 1,5 mm{sup}`2`compte tenu de la longueur très faible.

Les paires de trous correctes sont indiquées par les lignes épaisses dans la couche de sérigraphie. Ces trous sont espacés d'environ 5 mm.

Tout d’abord, le fil est plié dans une forme appropriée pour passer à travers ces trous.

Ensuite, les extrémités sont pliées vers l’extérieur et fermement pressées contre le dessous du {term}`PCB`.

Lorsque les fils sont dans la bonne position, les quatre extrémités peuvent être coupées à longueur.


---
## Soudure des composants basse consommation

Une fois les agrafes en cuivre en place, tous les composants basse consommation peuvent désormais être installés.

Comme indiqué sur le schéma de circuit :
- **R1** = **120 Ω** (lors du fonctionnement à partir d'une source en **3,3 V**, ou **180 Ω** pour un fonctionnement en **5 V**)
- **R2** = **330 Ω**
- **R3** = **360 Ω**

Si vous installez un connecteur DIL pour l'{term}`optocoupleur` ou circuit intégré *déclencheur*, l'encoche doit être en bas, à côté du cercle sur le {term}`PCB`.

Ces caractéristiques indiquent toutes deux la broche 1.


---
## Soudure de la partie *haute puissance*/*haute tension*

```{danger}
La qualité des soudures sera primordiale pour cette étape.

Une soudure ratée peut entraîner la destruction immédiate de la carte avec risque d'incendie lors de la mise sous tension.
```

### Connecteur haute puissance

Ce composant peut être temporairement maintenu en place en pliant les agrafes en cuivre de manière à ce qu'elles viennent juste pincer les broches saillantes.

Ensuite, avec un bon fer chaud (régler la température à 450 °C si possible), beaucoup de soudure peut être appliquée.

### Triac

De la même façon que précédemment, ce composant peut être temporairement maintenu en place en pliant les agrafes en cuivre de manière à ce qu'elles viennent juste pincer les broches saillantes.

Il faudrait laisser dépasser seulement 1-2 mm des pattes du triac.

Afin de faciliter cette opération mais aussi de protéger le triac des hautes températures, il est conseillé de plaquer le triac contre l'un des dissipateurs non encore monté que vous avez à disposition. On peut prendre une pince à linge par exemple, ou toute autre pince à ressort.

Pour les connexions en contact avec chacune des agrafes, un bon fer chaud et beaucoup de soudure sont nécessaires.

Lorsque vous soudez la broche centrale, assurez-vous que la soudure ne dépasse pas vers la broche de gâchette. Si tel est le cas, une partie de la soudure devra être soigneusement retirée.

```{warning}
Lors de la soudure du triac, veillez à bien vérifier que la soudure est "remontée" de l'autre côté du circuit. 

Cela assurera une continuité parfaite mais aussi une solidité accrue.
```


---
## Mise en place de l'{term}`optocoupleur`

Ce minuscule composant à 6 broches forme le *pont* entre les côtés basse tension et haute tension.
Le point sur la puce (surligné ici en rouge) doit être à côté du cercle sur le {term}`PCB`.

S'il est monté dans le mauvais sens, cela ne fonctionnera pas. Mais grâce à la disposition de ses pins, il devrait survivre à l’expérience.


---
# Test

Lors de la construction d'un système complet, il peut être plus approprié que l'étage de sortie terminé soit monté dans le boîtier avant d'être testé.

Les conseils ci-dessous sont proposés lorsqu'un étage de sortie doit être testé de manière isolée.

```{danger}
**Avertissement de Sécurité**

Pour tester que le déclencheur et le triac fonctionnent, un accès à la tension secteur **230 V** CA est requis.

Veuillez faire très attention et n’entreprendre cette étape suivante que si vous êtes compétent pour le faire.
```

Voici une plate-forme construit qui permet de tester les cartes de sortie avec ou sans le triac soudé en place.

Cette plate-forme est affichée en haut de la page Galerie de photos.

Lors du test d'une carte de sortie, il est important que le triac fasse partie du circuit électrique, sinon tout le courant de charge passera par le circuit {term}`optocoupleur` et un ou plusieurs composants seront alors détruits immédiatement.

En tenant dûment compte de l'avertissement de sécurité ci-dessus, l'approche simple illustrée ci-dessous devrait convenir pour tester des cartes individuelles.
