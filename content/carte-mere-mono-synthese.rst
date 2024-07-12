.. _carte-mere-mono-synthese:

Synthèse
--------

Voici l'inventaire spécifique à chaque configuration :

* :ref:`A <carte-mere-mono-A>` : 1 à 12 sorties triac et/ou relais, **sans afficheur**, **sans module RF**
* :ref:`B <carte-mere-mono-B>` : 1 à 2 sorties triac et/ou relais, **avec afficheur**, **sans module RF**
* :ref:`C <carte-mere-mono-C>` : 3 à 7 sorties triac et/ou relais, **avec afficheur**, **sans module RF**
* :ref:`D <carte-mere-mono-D>` : 0 à 2 sorties triac et/ou relais, **avec afficheur**, **avec module RF** (émetteur ou récepteur)
* :ref:`E <carte-mere-mono-E>` : 0 à 7 sorties triac et/ou relais, **sans afficheur**, **avec module RF** (émetteur ou récepteur)

.. table:: Inventaire des composants pour chaque configuration
   :header-rows: 1

   ============= === === === === ===
   \              A   B   C   D   E
   ============= === === === === ===
   **R11-R18**    -   X   X   X   -
   **CN1/Nappe**  -   X   X   X   -
   **IC3-IC4**    -   -   X   X   -
   **VR2**        -   -   -   X   X
   **C8-C9**      -   -   -   X   X
   **RF**         -   -   -   X   X
   **R21-R26**    -   -   -   X   -
   ============= === === === === ===
