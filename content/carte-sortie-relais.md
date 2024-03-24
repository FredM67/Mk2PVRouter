Une sortie relais *tout-ou-rien* est un composant électronique utilisé pour contrôler l'alimentation électrique d'un appareil ou d'un circuit.   
Le terme *tout-ou-rien* indique que le relais n'a que deux états possibles : soit il est activé (fermé) et laisse passer le courant, soit il est désactivé (ouvert) et coupe le courant.

Lorsqu'il s'agit de contrôler un appareil contenant de l'électronique, l'utilisation d'une sortie relais *tout-ou-rien* est souvent préférée à celle d'une sortie triac. La principale raison de ce choix réside dans la nature de la charge à contrôler : les appareils électroniques ont des besoins en commutation différents de ceux des appareils purement résistifs comme des chauffages, chauffe-eau ou des lampes à incandescence.

# Principe de Fonctionnement d'une Sortie Relais *tout-ou-rien*

Une sortie relais *tout-ou-rien* est composée d'une bobine qui, lorsqu'elle est alimentée en tension, génère un champ magnétique. Ce champ magnétique actionne un levier qui ferme un contact, permettant ainsi le passage du courant électrique. Lorsque la tension n'est plus appliquée à la bobine, un ressort ou un système similaire ramène le contact en position ouverte, ce qui interrompt le circuit et coupe le courant.

# Avantages pour les Appareils Électroniques
- **Isolation Galvanique** : La commande par relais *tout-ou-rien* offre une isolation galvanique entre le circuit de commande (la bobine) et le circuit de puissance (les contacts). Cette séparation est essentielle pour protéger les composants électroniques sensibles des hautes tensions et des interférences potentielles.
- **Compatibilité avec Diverses Charges** : Contrairement aux sorties triac, qui sont optimales pour les charges résistives et peuvent présenter des problèmes avec des charges inductives ou capacitives, les relais peuvent commuter de manière fiable des appareils électroniques qui possèdent des alimentations à découpage, des moteurs, ou des composants inductifs sans risque de dysfonctionnement.
- **Pas de Semi-Conduction** : Les sorties triac sont des dispositifs semi-conducteurs qui peuvent conduire partiellement, créant des situations où un appareil électronique pourrait recevoir une tension insuffisante ou erratique. Les relais, en revanche, offrent une commutation nette et complète, ce qui est préférable pour les appareils électroniques nécessitant une alimentation stable.

# Considérations Techniques
Les cartes-relais que nous utilisons ne sont pas conçues pour commuter des charges de grande puissance.   
En effet, chaque action de commutation (passage de fermé à ouvert, ou d'ouvert à fermé) peut potentiellement créer un arc électrique entre les contacts du relais.   
Cet arc peut, à terme, user les contacts. Il se peut qu'un jour, ces contacts restent collés (l'arc aurait en quelque sorte soudé les contacts ensemble) ou soient carbonisés, auquel cas ils ne pourraient plus conduire l'électricité.

C'est pourquoi ces cartes-relais doivent être utilisées **uniquement** pour commander un relais de puissance réel, similaire aux contacteurs Heures Creuses/Heures Pleines que l'on trouve dans un tableau électrique.

---
# Test
