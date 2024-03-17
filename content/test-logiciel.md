(test-logiciel)=

Une fois le processeur en place, il peut être judicieux de vérifier que l'alimentation électrique est toujours correcte.  
En supposant que ce soit le cas, exécutons un croquis (programme) pour déterminer si le processeur fonctionne.

Pour cette prochaine étape, un dispositif de programmation adapté devra être mis en place.  
Des détails sur la configuration de l'environnement de développement intégré (IDE) Arduino peuvent être trouvés en haut de cette page.  
Un programmateur USB vers UART devra être branché sur le connecteur **FTDI** du {term}`PCB` comme indiqué ci-dessous.  
L'autre extrémité du programmateur doit être connectée via un câble USB approprié à l'installation de programmation (PC ou équivalent).

La broche à une extrémité du connecteur à 6 voies du programmateur sera étiquetée **Gnd**. Cette broche doit correspondre au marquage **0 V** sur le {term}`PCB`.

Ici, le programmeur FTDI est utilisé. Notez qu'il doit être monté dans l'autre sens.
La broche **Gnd** doit toujours être la plus proche du bord de la carte

Pour éviter de tordre le connecteur du programmateur, on peut fabriquer un simple câble d'extension comme indiqué ici.
Seules quatre des lignes sont réellement utilisées (données **Tx** & **Rx**, masse et réinitialisation).  
Aucune des lignes d'alimentations électriques n'est utilisée par cette carte.

Le fil noir est destiné à la connexion **GND** (ou **0 V**).

```{note}
La carte FTDI ne permet pas d'alimenter la carte-mère.

Le routeur devra toujours être alimenté par sa propre alimentation.
```