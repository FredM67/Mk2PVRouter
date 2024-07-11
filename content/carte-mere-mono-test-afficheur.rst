.. _carte-mono-test-afficheur:

Test de la partie *afficheur*
"""""""""""""""""""""""""""""

Vous allez maintenant devoir tester l'afficheur 7 segments.

Pour cela, nous aurons besoin d'un croquis spécifique qui sera téléchargé dans l'Arduino.

Pré-requis
**********

Vérifiez les points suivants avant de continuer :

* Vous avez bien connecté l'adaptateur :term:`FTDI` à l'Arduino.
* Vous avez bien connecté l'adaptateur :term:`FTDI` à votre ordinateur.
* Le logiciel de programmation installé et prêt à l'emploi.
* Le routeur est alimenté en 230 V.

Téléchargement du croquis
*************************

Le croquis à télécharger est disponible en cliquant sur le lien suivant : `Vérification afficheur <https://mk2pvrouter.com/wp-content/uploads/2023/01/verification_afficheur.zip>`_.

Il vous suffit de décompresser le fichier et de l'ouvrir avec le logiciel de programmation.

.. hint::
   | Le croquis devra se trouver dans un dossier nommé ``verification_afficheur``.
   | Il est impératif que le dossier ainsi que le croquis contenu dans ce même dossier aient le même nom.

Vérification de l'afficheur
***************************

Une fois le croquis ouvert dans le logiciel de programmation, il est important de vérifier qu'il correspond à votre configuration.

Si votre routeur est équipé des deux circuits intégrés **IC3** et **IC4**, vous devrez activer la ligne suivante dans le croquis :

.. code-block:: cpp
    
   #define PIN_SAVING_HARDWARE

Si votre routeur n'est **pas** équipé des deux circuits intégrés **IC3** et **IC4**, vous devrez commenter la ligne suivante dans le croquis :

.. code-block:: cpp

   //#define PIN_SAVING_HARDWARE

Après avoir effectué cette modification, compilez le croquis et téléversez-le dans l'Arduino.

Une fois le téléversement terminé, l'afficheur 7 segments devrait afficher successivement tous les chiffres ainsi que le point pour chaque bloc de 7 segments.