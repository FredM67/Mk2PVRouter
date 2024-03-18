(confection-cables)=

# Confection des câbles

Il conviendra d'apporter un soin tout particulier pour la confection des multiples câbles nécessaires.  

Voici la liste des câbles dont nous aurons besoin :
- câble relié à la prise jack (3 pour la version triphasée)
- câble relié au bouton *reset* (uniquement triphasé)
- câble de contrôle (un par étage de sortie)
- câble de témoin LED (un par étage de sortie et/ou sortie relais).
- câbles d'alimentation (uniquement version monophasé)
- fil de mise à la terre (un par dissipateur)

```{note}
Toutes les longueurs préconisées sont basées sur les implantations de la carte-mère décrites {ref}`ici<boitier:Fixations de la carte-mère>`.
```

```{admonition} Conseil
Les câbles très basse tension sont composés de 2 fils tressés.  
Il est **fortement** recommandé de se fixer une convention de couleur, selon le contenu du kit et/ou les câbles que l'on utilisera de son propre stock.

Par exemple :
- **rouge** pour le **+**, **bleu** pour la *masse*
- ou si on prend du câble réseau, *couleur* pour le **+**, *couleur/blanc* pour la **masse**.
```

---

## Fil de mise à la terre

Ce sont des fils passifs qui permettront d'assurer la sécurité des personnes en cas de défaut d'isolation d'un ou plusieurs triacs.

````{admonition} Longueurs conseillées
- boîtier 1 ou 2 sorties => 2 fils de chacun xx mm de long
- boîtier 3 ou 4 sorties => 4 fils
  - dissipateur haut gauche => xx mm
  - dissipateur haut droit => xx mm
  - dissipateur bas gauche => 245 mm
  - dissipateur haut droit => xx mm
````

Les fils devront être dénudés sur environ 5 mm et être sertis directement dans les cosses **sans** soudure.

---

## Câbles prise·s jack

Ces câbles serviront à transmettre les mesures prises par la ou les pinces ampèremétriques (ou capteur de courant).  
Il conviendra donc d'y apporter le plus grand soin, afin de minimiser l'apparition de parasites.

````{admonition} Longueurs conseillées
```{exercise} Version monophasée
- Boîtier **1** ou **2** sorties
  xx mm de long
- Boîtier **3** ou **4** sorties
  xx mm de long
```    

```{exercise} Version triphasée
- Boîtier **1** ou **2** sorties
  - **255 mm** pour **{term}`CT`1**,
  - **300 mm** pour **{term}`CT`2** et
  - **345 mm** pour **{term}`CT`3**.
- Boîtier **3** ou **4** sorties
  - **315 mm** pour **{term}`CT`1**,
  - **360 mm** pour **{term}`CT`2** et
  - **405 mm** pour **{term}`CT`3**.
```
````

---

## Câble·s de contrôle

Ce sont des fils *actifs* qui permettront d'envoyer les commandes d'ouverture et fermeture aux triacs.

````{admonition} Longueurs conseillées
```{exercise} Version monophasée
- Boîtier **1** ou **2** sorties
  - étage de sortie **gauche** => xx mm
  - étage de sortie **droit** => xx mm
- Boîtier **3** ou **4** sorties
  - étage de sortie **haut gauche** => xx mm
  - étage de sortie **haut droit** => xx mm
  - étage de sortie **bas gauche** => xx mm
  - étage de sortie **bas droit** => xx mm
```

```{exercise} Version triphasée
- Boîtier **1** ou **2** sorties
  - étage de sortie **gauche** => **140 mm**
  - étage de sortie **droit** => **340 mm**
- Boîtier **3** ou **4** sorties
  - étage de sortie **haut gauche** => **200 mm**
  - étage de sortie **haut droit** => **250 mm**
  - étage de sortie **bas gauche** => **200 mm**
  - étage de sortie **bas droit** => **360 mm**
```
````

---

## Câble·s de témoin·s LED

Ce sont des fils *actifs* qui sont repiqués sur la commande de l'étage de sortie et permettent de visualiser l'état de chaque sortie :
- allumé => le courant passe (triac fermé)
- éteint => le courant ne passe pas (triac ouvert).

Les longueurs indiquées permettent d'ouvrir le couvercle et de le déposer sur le dessus du boîtier sans qu'aucun fil ne soit tendu.  
Bien sûr, il est possible de faire des câbles plus courts, ou plus longs !

```{admonition} Longueurs conseillées
- Boîtier **1** ou **2** sorties
  - étage de sortie **gauche** => **400 mm**
  - étage de sortie **droit** => **470 mm**
- Boîtier **3** ou **4** sorties
  - étage de sortie **haut gauche** => **440 mm**
  - étage de sortie **haut droit** => **510 mm**
  - étage de sortie **bas gauche** => **580 mm**
  - étage de sortie **bas droit** => **650 mm**
```