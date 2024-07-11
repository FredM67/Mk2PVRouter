.. _test-logiciel-mono:

Tests logiciel
^^^^^^^^^^^^^^

| Une fois le processeur installé, il serait judicieux de vérifier que l'alimentation électrique fonctionne toujours correctement.
| Si c'est le cas, nous pouvons exécuter un croquis (programme) pour vérifier si le processeur fonctionne correctement.

| Nous allons maintenant tester le bon fonctionnement des autres parties matérielles de la carte-mère.
| Cela permettra à la fois de s'assurer que le processeur est opérationnel et de vérifier que les autres composants sont correctement installés et/ou assemblés.

| Pour cette prochaine étape, un dispositif de programmation approprié doit être mis en place.

.. contents:: Sommaire
    :local:
    :depth: 1

Pré-requis
""""""""""

Pour cette étape, il vous faudra :

* Un ordinateur (PC ou équivalent) avec un port USB libre. Cet ordinateur peut fonctionner sous Windows, MacOS ou Linux.
* Un programmateur USB vers UART (par exemple, un programmateur :term:`FTDI`).
* Un câble USB approprié pour connecter le programmateur à l'ordinateur de programmation.
* Un câble d'alimentation électrique pour le routeur.

Carte USB vers UART
*******************

| Un programmateur USB vers UART est nécessaire pour télécharger le croquis (programme) sur le processeur.
| Ce programmateur est également utilisé pour surveiller les messages de débogage envoyés par le processeur.

| Selon le système d'exploitation (Windows, MacOS ou Linux) de l'ordinateur de programmation, il peut être nécessaire d'installer un pilote pour le programmateur.
| Les pilotes pour le programmateur :term:`FTDI` sont disponibles sur le site Web du fabricant.

| Les pilotes disponibles sur le site `FTDI <https://www.ftdichip.com/>`_ devraient convenir à la plupart des cas d'utilisation.
| Il conviendra de choisir les pilotes de type **VCP** (Virtual COM Port).

Logiciel de programmation
*************************

Pour programmer l'Arduino, vous aurez besoin d'un logiciel de programmation.

| Le logiciel le plus convivial et le plus simple pour accomplir cette tâche est l'Arduino IDE.
| Il est facile à installer et à utiliser, et il est spécialement conçu pour programmer des cartes Arduino.

| Cependant, vous pouvez également utiliser Visual Studio Code avec l'extension PlatformIO.
| Cette combinaison offre un environnement de développement plus avancé et de nombreuses fonctionnalités supplémentaires pour les utilisateurs expérimentés.

Assurez-vous d'installer l'un de ces logiciels avant de continuer avec la programmation de votre carte.

| L'**Arduino IDE** peut être téléchargé à partir du site `Arduino <https://www.arduino.cc/en/software>`_.
| Pour Windows, veillez à choisir la version **Windows** et non :strike:`Windows App`.

| Si vous êtes totalement débutant dans le domaine de l'Arduino, nous vous recommandons de consulter le tutoriel `Découverte de l'Arduino <https://zestedesavoir.com/tutoriels/686/arduino-premiers-pas-en-informatique-embarquee/742_decouverte-de-larduino/>`_ par exemple.
| Il y en a beaucoup d'autres disponibles sur Internet.

Mise en place
*************

.. admonition:: Remarque
   :class: tip

   La carte :term:`FTDI` dispose d'un commutateur ou d'un cavalier pour choisir entre **3,3 V** et **5 V**.
   Assurez-vous que le cavalier est correctement positionné pour la tension de fonctionnement de la carte-mère.

| Un programmateur USB vers UART doit être connecté au connecteur :term:`FTDI` du :term:`PCB` comme indiqué ci-dessous.
| L'autre extrémité du programmateur doit être connectée à l'ordinateur de programmation (PC ou équivalent) via un câble USB approprié.

La broche à une extrémité du connecteur à 6 voies du programmateur sera étiquetée **Gnd**. Cette broche doit correspondre au marquage **0 V** sur le :term:`PCB`.

| Ici, nous utilisons le programmateur :term:`FTDI`. Notez qu'il doit être monté dans le sens inverse.
| La broche **Gnd** doit toujours être la plus proche du bord de la carte.

| Pour éviter de tordre le connecteur du programmateur, vous pouvez fabriquer un simple câble d'extension comme indiqué ici.
| Seules quatre des lignes sont réellement utilisées (données **Tx** & **Rx**, masse et réinitialisation).
| Aucune des lignes d'alimentation électrique n'est utilisée par cette carte.

Le fil noir est destiné à la connexion **GND** (ou **0 V**).

.. note::
   La carte :term:`FTDI` ne peut pas alimenter la carte-mère.

   Le routeur doit toujours être alimenté par sa propre source d'alimentation.

.. include:: carte-mere-mono-test-afficheur.rst

.. include:: test-mono-mesures.rst