(carte-sortie)=

# Étage de sortie

Un *Relais Statique* ou *SSR* (Solid State Relay) peut aussi être utilisé comme étage de sortie.

Pour les cartes de sortie, nous allons procéder de façon similaire, dans cet ordre :
1. résistances
2. support MOC
3. connecteur(s) Molex
4. connecteur de puissance
5. triac

```{danger}
Certaines soudures sur cette carte ont une très grande importance.

Il faudra veiller à donner une attention particulière à la **qualité** de chacune des soudure sur la partie **haute tension**.

Une soudure ratée peut entraîner la destruction immédiate de la carte avec risque d'incendie lors de la mise sous tension.
```

## Pose des *agrafes* en cuivre

La première étape du processus d'assemblage consiste à installer une paire d'*agrafes* en cuivre massif qui augmentent la capacité de la carte à supporter des courants élevés.
La section transversale recommandée est de 1,5 mm{sup}`2`compte tenu de la longueur très faible.

Les paires de trous correctes sont indiquées par les lignes épaisses dans la couche de sérigraphie. Ces trous sont espacés d'environ 5 mm.

Tout d’abord, le fil est plié dans une forme appropriée pour passer à travers ces trous.

Ensuite, les extrémités sont pliées vers l’extérieur et fermement pressées contre le dessous du PCB.

Lorsque les fils sont dans la bonne position, les quatre extrémités peuvent être coupées à longueur.

## Soudure des composants basse consommation

Une fois les agrafes en cuivre en place, tous les composants basse consommation peuvent désormais être installés.

Comme indiqué sur le schéma de circuit :
- **R1** = **120** &Omega; (lors du fonctionnement à partir d'une source en **3,3 V**, ou **180** &Omega; pour un fonctionnement en **5 V**)
- **R2** = **330** &Omega;
- **R3** = **360** &Omega;

Si vous installez un connecteur DIL pour l'optocoupleur ou circuit intégré *déclencheur*, l'encoche doit être en bas, à côté du cercle sur le PCB.

Ces caractéristiques indiquent toutes deux la broche 1.

## Soudure de la partie *haute puissance*/*haute tension*

```{danger}
La qualité des soudures sera primordiale pour cette étape.

Une soudure ratée peut entraîner la destruction immédiate de la carte avec risque d'incendie lors de la mise sous tension.
```

### Connecteur haute puissance

Ce composant peut être temporairement maintenu en place en pliant les agrafes en cuivre de manière à ce qu'elles viennent juste pincer les broches saillantes.

Ensuite, avec un bon fer chaud (régler la température à 450°C si possible), beaucoup de soudure peut être appliquée.

### Triac

De la même façon que précédemment, ce composant peut être temporairement maintenu en place en pliant les agrafes en cuivre de manière à ce qu'elles viennent juste pincer les broches saillantes.

Il faudrait laisser dépasser seulement 1-2 mm des pattes du triac.

Afin de faciliter cette opération mais aussi de protéger le triac des hautes températures, il est conseillé de plaquer le triac contre l'un des dissipateurs non encore monté que vous avez à disposition. On peut prendre une pince à linge par exemple, ou toute autre pince à ressort.

Pour les connexions en contact avec chacune des agrafes, un bon fer chaud et beaucoup de soudure sont nécessaires.

Lorsque vous soudez la broche centrale, assurez-vous que la soudure ne dépasse pas vers la broche de gâchette. Si tel est le cas, une partie de la soudure devra être soigneusement retirée.

```{warning}
Lors de la soudure du triac, veillez à bien vérifier que la soudure est "remontée" de l'autre côté du circuit. 

Cela assurera une continuité parfaite mais aussi une solidité accrue.
```

## Mise en place de l'optocoupleur

Ce minuscule composant à 6 broches forme le *pont* entre les côtés basse tension et haute tension.
Le point sur la puce (surligné ici en rouge) doit être à côté du cercle sur le PCB.

S'il est monté dans le mauvais sens, cela ne fonctionnera pas. Mais grâce à la disposition de ses pins, il devrait survivre à l’expérience.

## Test

Lors de la construction d'un système complet, il peut être plus approprié que l'étage de sortie terminé soit monté dans le boîtier avant d'être testé.

Les conseils ci-dessous sont proposés lorsqu'un étage de sortie doit être testé de manière isolée.

```{danger}
**Avertissement de Sécurité**

Pour tester que le déclencheur et le triac fonctionnent, un accès à la tension secteur 230 V CA est requis.

Veuillez faire très attention et n’entreprendre cette étape suivante que si vous êtes compétent pour le faire.
```

Voici une plate-forme construit qui permet de tester les cartes de sortie avec ou sans le triac soudé en place.

Cette plate-forme est affichée en haut de la page Galerie de photos.

Lors du test d'une carte de sortie, il est important que le triac fasse partie du circuit électrique, sinon tout le courant de charge passera par le circuit optocoupleur et un ou plusieurs composants seront alors détruits immédiatement.

En tenant dûment compte de l'avertissement de sécurité ci-dessus, l'approche simple illustrée ci-dessous devrait convenir pour tester des cartes individuelles.
