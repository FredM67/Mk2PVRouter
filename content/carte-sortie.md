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

Ensuite, les extrémités sont pliées vers l’extérieur et fermement pressées contre le dessous de la planche…

Lorsque les fils sont dans la bonne position, les quatre extrémités peuvent être coupées à longueur.

## Soudure des composants basse consommation

Une fois les agrafes en cuivre en place, tous les composants basse consommation peuvent désormais être installés.

Comme indiqué sur le schéma de circuit :
- R1 = 120 {math}`omega` (lors du fonctionnement à partir d'une source de 3,3 V, ou 180 {math}`omega` pour un fonctionnement de 5 V)
- R2 = 330 {math}`omega` (celui en bas à gauche de la paire)
- R3 = 360 {math}`omega` (celui en haut à droite de la paire)

Si vous installez un connecteur DIL pour l'opto-isolateur ou le circuit intégré *déclencheur*, l'encoche doit être en bas, à côté du cercle sur le PCB.
Ces caractéristiques indiquent toutes deux la broche 1.

## Soudure de la partie haute puissance

```{danger}
La qualité des soudures sera primordiale pour cette partie.
Une soudure ratée peut entraîner la destruction immédiate de la carte avec risque d'incendie lors de la mise sous tension.
```

## Test

Lors de la construction d'un système complet, il peut être plus approprié que l'étage de sortie terminé soit monté dans le boîtier avant d'être testé.
Les conseils ci-dessous sont proposés lorsqu'un étage de sortie doit être testé de manière isolée.

```{danger}
:title: Avertissement de Sécurité
Pour tester que le déclencheur et le triac fonctionnent, un accès à la tension secteur 230 V CA est requis.
Veuillez faire très attention et n’entreprendre cette étape suivante que si vous êtes compétent pour le faire.
```

Voici une plate-forme construit qui permet de tester les cartes de sortie avec ou sans le triac soudé en place.
Cette plate-forme est affichée en haut de la page Galerie de photos.
Lors du test d'une carte de sortie, il est important que le triac fasse partie du circuit électrique, sinon tout le courant de charge passera par le circuit opto-isolateur et un ou plusieurs composants seront alors détruits immédiatement.

En tenant dûment compte de l'avertissement de sécurité ci-dessus, l'approche simple illustrée ci-dessous devrait convenir pour tester des cartes individuelles.
