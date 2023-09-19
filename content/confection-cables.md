(confection-cables)=

# Confection des câbles

Il conviendra d'apporter un soin tout particulier pour la confection des multiples câbles nécessaires.  

Voici la liste des câbles dont nous aurons besoin :
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

Par exemple :
- **rouge** pour le **+**, **bleu** pour la *masse*
- ou si on prend du câble réseau, *couleur* pour le **+**, **blanc** pour la **masse**.
```

## Fil de mise à la terre

Ce sont des fils passifs qui permettront d'assurer la sécurité des personnes en cas de défaut d'isolation d'un ou plusieurs triacs.

Longueurs conseillées :
- boîtier 1 ou 2 sorties => 2 fils de chacun xx mm de long
- boîtier 3 ou 4 sorties => 4 fils
  - dissipateur haut gauche => xx&nbsp;mm
  - dissipateur haut droit => xx&nbsp;mm
  - dissipateur bas gauche => xx&nbsp;mm
  - dissipateur haut droit => xx&nbsp;mm

Les fils devront être dénudés sur environ 5&nbsp;mm et être sertis directement dans les cosses **sans** soudure.

## Câbles prise(s) jack

Ces câbles serviront à transmettre les mesures prises par la ou les pinces ampèremétriques (ou capteur de courant).  
Il conviendra donc d'y apporter le plus grand soin, afin de minimiser l'apparition de parasites.

````{admonition} Longueurs conseillées
```{exercise} Boîtier **1** ou **2** sorties
- **monophasé** => une paire xx&nbsp;mm de long
- **triphasé** => 3 paires de :
  - **255&nbsp;mm** pour **CT1**,
  - **300&nbsp;mm** pour **CT2** et 
  - **345&nbsp;mm** pour **CT3**.
```    

```{exercise} Boîtier **3** ou **4** sorties
- **monophasé** => une paire xx&nbsp;mm de long
- **triphasé** => 3 paires de :
  - **315&nbsp;mm** pour **CT1**,
  - **360&nbsp;mm** pour **CT2** et
  - **405&nbsp;mm** pour **CT3**.
```
````

## Câble(s) de contrôle

Ce sont des fils actifs qui permettront d'envoyer les commandes d'ouverture et fermeture aux triacs.

````{admonition} Longueurs conseillées
```{exercise} Boîtier **1** ou **2** sorties
- **monophasé**
  - étage de sortie **gauche** => xx&nbsp;mm
  - étage de sortie **droit** => xx&nbsp;mm
- **triphasé**
  - étage de sortie **gauche** => **140&nbsp;mm**
  - étage de sortie **droit** => **340&nbsp;mm**
```

```{exercise} Boîtier **3** ou **4** sorties
- **monophasé**
  - étage de sortie **haut gauche** => xx&nbsp;mm
  - étage de sortie **haut droit** => xx&nbsp;mm
  - étage de sortie **bas gauche** => xx&nbsp;mm
  - étage de sortie **bas droit** => xx&nbsp;mm
- **triphasé**
  - étage de sortie **haut gauche** => **200&nbsp;mm**
  - étage de sortie **haut droit** => **200&nbsp;mm**
  - étage de sortie **bas gauche** => **240&nbsp;mm**
  - étage de sortie **bas droit** => **360&nbsp;mm**
```
````