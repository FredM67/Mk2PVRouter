.. _carte-mere-presentation:

======================================
Présentation de la carte universelle
======================================

⏱️ **Temps de lecture** : 10–15 minutes

.. admonition:: 📋 Prérequis

   Avant de commencer ce chapitre :

   | ☐ Chapitre :ref:`safety-overview` lu et compris

Vue d’ensemble
--------------

La carte **3phaseDiverter** (rév. 6.0) est la carte principale universelle du Mk2 PV Router. Elle remplace les anciennes cartes monophasée et triphasée séparées par une carte unique capable de gérer les trois configurations supportées :

- **Monophasé** : une phase, un neutre (230 V)
- **Triphasé avec neutre** : trois phases + neutre (400 V / 230 V)
- **Triphasé 3 × 230 V sans neutre** : trois phases sans neutre, 230 V entre phases (voir :ref:`raccordement en 3 × 230 V <raccordement-3x230>`)

La sélection de la configuration se fait par les :term:`cavaliers de soudure <Cavalier de soudure>`, le choix des connecteurs et celui des composants traversants montés (voir :ref:`choix-configuration`) — tous les composants CMS sont identiques quelle que soit la configuration.

Caractéristiques principales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Microcontrôleur **ATmega328P** (16 MHz, DIP-28)
- Jusqu’à 3 capteurs de tension (:term:`ZMPT101K`, rapport 1000:1000)
- Jusqu’à 3 connecteurs de transformateur de courant :term:`CT` (CT1–CT3)
- Module radio **RFM69CW** (bande ISM 433/868 MHz) avec connecteur :term:`SMA`
- Alimentation AC-DC intégrée (**MPC10-5**, 5 V / 10 W)
- Régulateur :term:`LDO` **AP7361C-33E** (5 V → 3,3 V, 1 A)
- Protection parafoudre multiniveau (:term:`GDT`, fusibles, :term:`MOV`, self de mode commun)
- Buffer de la référence interne 1,1 V (AREF) par amplificateur opérationnel **LMV321A**
- Connecteurs d’extension : **TRIG_EXT**, **UART_EXT**, **FTDI**, **OLED**
- Compatible avec le module d’extension :term:`mk2Wifi`

Images de la carte
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Face avant (assemblée)
     - Face arrière
   * - .. figure:: ../img/mainboard-front.png
          :alt: Carte universelle — face avant assemblée
          :class: clickable-img

     - .. figure:: ../img/mainboard-back.png
          :alt: Carte universelle — face arrière
          :class: clickable-img

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Composants :term:`CMS` uniquement
     - Circuit imprimé nu
   * - .. figure:: ../img/mainboard-smd.png
          :alt: Carte universelle — composants CMS
          :class: clickable-img

     - .. figure:: ../img/mainboard-bare.png
          :class: clickable-img
          :alt: Carte universelle — PCB nu

Connecteurs
-----------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Sérigraphie
     - Type
     - Description
   * - PE / N / L1 / L2 / L3
     - Phoenix Contact MSTBV 2,5 (pas 5,08 mm)
     - Entrée secteur. En monophasé, un connecteur 3 voies est fourni (PE, N, L1).
   * - TRIG_EXT
     - Barrette mâle 1×06 (pas 2,54 mm)
     - Déclenchement / GPIO
   * - UART_EXT
     - Barrette mâle 1×06 (pas 2,54 mm)
     - UART + capteur DS18B20
   * - FTDI
     - Molex SL 1×06 (pas 2,54 mm)
     - Programmation / débogage
   * - OLED
     - Molex SL 1×04 (pas 2,54 mm)
     - Écran I2C (monophasé uniquement)
   * - SMA
     - :term:`SMA` vertical (50 Ω)
     - Antenne module :term:`RF`
   * - CT1
     - Molex SL 1×02 (pas 2,54 mm)
     - Entrée :term:`CT` L1
   * - CT2
     - Molex SL 1×02 (pas 2,54 mm)
     - Entrée :term:`CT` L2 en triphasé ; CT de diversion (optionnel) en monophasé
   * - CT3
     - Molex SL 1×02 (pas 2,54 mm)
     - Entrée :term:`CT` L3 (triphasé uniquement)
   * - D2 à D13
     - | Molex SL 1×02 (GND, I/O) +
       | Molex SL 1×03 (GND, I/O, +5 V) par sortie
     - Sorties numériques — voir :ref:`sorties-numeriques`

Brochage des connecteurs
-------------------------

PE / N / L1 / L2 / L3 — Entrée secteur (1×5 Phoenix Contact)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Sérigraphie
     - Signal
   * - PE
     - Terre (conducteur de protection)
   * - N
     - Neutre
   * - L1
     - Phase 1
   * - L2
     - Phase 2
   * - L3
     - Phase 3

En monophasé, un connecteur 3 voies est fourni (PE, N, L1).

TRIG_EXT — Déclenchement/GPIO (1×6 barrette mâle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - D8
   * - 3
     - D7
   * - 4
     - D6
   * - 5
     - D5
   * - 6
     - D9

UART_EXT — UART + DS18B20 (1×6 barrette mâle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - DS18B20
   * - 3
     - +5 V
   * - 4
     - RX
   * - 5
     - TX
   * - 6
     - DTR

Les noms des signaux (TX, RX) sont du point de vue de la **carte principale** : TX transporte les données émises par l’ATmega328P, RX les données reçues.

FTDI — Programmation/débogage (1×6 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - CTS (NC)
   * - 3
     - VCC (NC)
   * - 4
     - TXO
   * - 5
     - RXI
   * - 6
     - DTR

Brochage compatible avec les adaptateurs FTDI standard. Le signal DTR permet l’auto-reset pour le téléversement via le bootloader Arduino.

OLED — Écran I2C (1×4 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - GND
   * - 2
     - VCC
   * - 3
     - SCL
   * - 4
     - SDA

.. important::
   Le bus I2C est partagé sur les broches A4 (SDA) et A5 (SCL) de l’ATmega328P. En mode triphasé, ces broches sont affectées à la mesure de tension/courant L3 — l’écran OLED n’est alors **pas disponible**. Le choix est effectué par les cavaliers **SDA** et **SCL** (voir :ref:`cavaliers`).

CT1 / CT2 / CT3 — Transformateurs de courant (1×2 Molex SL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Broche
     - Signal
   * - 1
     - Signal CT
   * - 2
     - AGND

CT1 est utilisé en monophasé et en triphasé. CT2 mesure L2 en triphasé ; en monophasé, il peut mesurer la puissance routée (optionnel). CT3 n’est utilisé qu’en triphasé avec neutre.

.. _sorties-numeriques:

Sorties numériques D2–D13
~~~~~~~~~~~~~~~~~~~~~~~~~~

Chaque sortie numérique (D2 à D13) dispose de **deux connecteurs Molex SL** sur la carte :

- **1×02** (2 broches) : GND, I/O
- **1×03** (3 broches) : GND, I/O, +5 V

Le connecteur **1×03** (GND, I/O, +5 V) sert aux **cartes de sortie relais**, qui ont besoin du +5 V pour leur bobine. La broche +5 V de ces connecteurs est reliée au **rail +5 V**, activé par le cavalier **+5V Rail** (voir ci-dessous). Le connecteur **1×02** (GND, I/O) sert à l’**étage de sortie** :term:`triac <Triac>`, qui n’a besoin que du signal de commande : ses deux connecteurs 2 broches sont en parallèle, la carte indicateur LED se branche sur le second (voir :ref:`carte-indicateur`). Avec une carte relais sur le 1×03, la carte indicateur peut se brancher sur le 1×02.

.. list-table:: Disponibilité des sorties numériques
   :header-rows: 1
   :widths: 15 85

   * - Sortie
     - Remarques
   * - D2\*
     - Réservée au module :term:`RF` (IRQ). Libre si le module RF n’est pas soudé.
   * - D3
     - Capteur DS18B20 (si cavalier TEMP en position routeur). Libre si TEMP en position mk2Wifi.
   * - D4
     - Libre
   * - D5#–D9#
     - Broches du routeur reliées au connecteur TRIG_EXT, marquées d’un **dièse (#)** sur la sérigraphie car partagées avec le module :term:`mk2Wifi`. Par défaut, les charges sont sur D5–D7 en triphasé (D5 en monophasé) ; le mk2Wifi peut piloter les autres comme entrées du routeur (marche forcée, arrêt du routage…), voir :ref:`presentation-mk2wifi`. Utilisées par le mk2Wifi si celui-ci est présent et que le cavalier correspondant est fermé (voir ci-dessous). Libres sinon.
   * - D10\*
     - SPI SS — réservée au module :term:`RF`. Libre si le module RF n’est pas soudé.
   * - D11\*
     - SPI MOSI — réservée au module :term:`RF`. Libre si le module RF n’est pas soudé.
   * - D12\*
     - SPI MISO — réservée au module :term:`RF`. Libre si le module RF n’est pas soudé.
   * - D13\*
     - SPI SCK — réservée au module :term:`RF`. Libre si le module RF n’est pas soudé.

Les sorties marquées d’un **astérisque (\*)** sur la sérigraphie sont réservées au module RF (RFM69CW) lorsqu’il est soudé. Les sorties marquées d’un **dièse (#)** sont partagées avec le module :term:`mk2Wifi` (voir ci-dessous). Si le module concerné n’est pas présent, ces sorties sont librement utilisables.

.. _types-de-capteurs-de-courant-supportes:

Types de capteurs de courant supportés
---------------------------------------

La carte universelle est conçue pour fonctionner avec deux types de capteurs de courant :

.. note::
   Quel que soit le type de CT, le boîtier porte généralement une **flèche** indiquant le sens du courant primaire. Les repères habituels sont :

   - côté primaire (le câble mesuré) : **P1** / **P2** (ou **K** / **L**), la flèche allant de P1 vers P2 ;
   - côté secondaire (les fils vers la carte) : **S1** / **S2** (ou **k** / **l**). S1 est la borne positive quand le courant primaire entre par P1.

   Ces marquages sont importants lors du raccordement aux connecteurs CT de la carte (voir :ref:`installation-finale`).

**CT à sortie tension (333 mV)** — recommandé
   Les capteurs à sortie tension (par ex. SCT-023R-005 ou équivalent 333 mV) intègrent leur propre résistance de :term:`burden <Burden>`. Le signal de tension est directement compatible avec l’entrée :term:`ADC` du microcontrôleur. **Aucun composant supplémentaire n’est nécessaire** sur la carte.

   C’est le type de CT recommandé pour la carte universelle.

**CT à sortie courant** — solution de dépannage, avec burden THT
   La carte est conçue pour des CT à sortie tension 333 mV. Un CT à sortie courant avec sa résistance de :term:`burden <Burden>` n’est qu’une solution de dépannage, par exemple en attendant des CT 333 mV.

   Les capteurs à sortie courant (par ex. YHDC SCT-013-000, 100 A / 50 mA) délivrent un courant proportionnel au courant mesuré. Ce courant doit être converti en tension par une résistance de :term:`burden <Burden>` soudée sur la carte, une par connecteur CT1 / CT2 / CT3 (R18 / R28 / R38 sur le schéma).

   Elle n’a pas d’empreinte propre : elle partage celle de la diode :term:`TVS` :term:`CMS` de protection **D13** / **D23** / **D33**, déjà soudée en usine, qui protège l’entrée de l’:term:`ADC` si un CT à sortie courant est branché sans burden. Cette empreinte double comporte, en plus des pastilles CMS de la diode, **deux trous traversants** au pas de 12,7 mm reliés aux mêmes signaux : la résistance s’y soude, **par-dessus** la diode, qui reste en place.

   La valeur du burden doit être calculée pour que la tension crête ne dépasse pas **0,55 V** (soit la moitié de la plage :term:`ADC` avec VREF = 1,1 V) :

   .. math::

      R_{burden} = \frac{V_{REF}}{2 \times \sqrt{2} \times I_{secondaire\_RMS}} = \frac{0{,}55}{I_{secondaire\_crête}}

   Où :math:`I_{secondaire\_RMS} = I_{primaire\_RMS} / N` (N = rapport de transformation du CT).

   **Puissance** : la résistance dissipe :math:`P = I_{secondaire\_RMS}^2 \times R_{burden}`. Faites le calcul avec le courant secondaire **nominal** du CT : c’est le pire cas.

   **Précision** : prenez une résistance à couche métallique à 1 %. Avec 5 %, la mesure est fausse d’autant, et seul l’étalonnage le rattrape.

   **Exemple complet** : le CT le plus courant, le YHDC SCT-013-000 (100 A / 50 mA), sur un câble de 50 A au maximum.

   #. Rapport de transformation : :math:`N = 100 / 0{,}05 = 2000`.
   #. Courant secondaire à 50 A : :math:`I_{sec} = 50 / 2000 = 25\,\text{mA RMS}`.
   #. Burden : :math:`R_{burden} = \frac{1{,}1 \times 2000}{2 \times \sqrt{2} \times 50} \approx 15{,}6\,\Omega`. La valeur normalisée immédiatement inférieure est **15 Ω**.
   #. Vérification : à 50 A, la tension crête vaut :math:`0{,}025 \times \sqrt{2} \times 15 \approx 0{,}53\,\text{V}`, sous la limite de 0,55 V. Avec 15 Ω, le courant mesurable va jusqu’à 51,9 A environ.
   #. Puissance : à 50 A, :math:`0{,}025^2 \times 15 \approx 9\,\text{mW}` ; au courant nominal du CT (100 A, 50 mA), :math:`0{,}05^2 \times 15 \approx 38\,\text{mW}`. Une résistance de **0,25 W** suffit largement (l’emplacement, au pas de 12,7 mm, accepte aussi une 0,5 W).

   Retenez la limite de ce choix : si le courant dépassait nettement 50 A, la tension crête dépasserait 0,55 V (1,06 V à 100 A). D’où la règle : dimensionner le burden pour le courant **maximal** du câble.

   .. danger::
      **Un burden mal choisi peut détruire l’entrée ADC.**

      Un CT à sortie courant impose son courant : c’est la résistance de burden qui fixe la tension envoyée vers l’ATmega328P (:math:`V = R_{burden} \times I_{secondaire}`).

      - **Valeur trop forte**, ou courant plus fort que prévu : la tension crête dépasse 0,55 V. Le signal est d’abord écrêté (mesures fausses), puis l’entrée de l’ATmega328P est poussée hors de ses limites. La diode :term:`TVS` limite la surtension, mais le microcontrôleur peut quand même être endommagé.
      - **Pas de burden** : le secondaire du CT est presque ouvert et sa tension monte très haut. La TVS n’est pas faite pour absorber ce courant en permanence : elle peut griller, l’entrée ADC avec elle, et la tension est dangereuse au toucher.

      Pour l’éviter :

      - calculez le burden pour le courant **maximal** du câble mesuré (le calibre du disjoncteur qui le protège), pas pour le courant habituel ;
      - prenez la valeur normalisée immédiatement **inférieure**, jamais supérieure ;
      - vérifiez la résistance à l’ohmmètre avant de la souder (les anneaux de couleur se confondent facilement) ;
      - soudez le burden **avant** de brancher le CT ; branchez le CT sur la carte avant de le refermer sur le câble, et ouvrez-le avant de le débrancher.

.. raw:: html

   <details style="margin: 1em 0; border: 1px solid #ccc; border-radius: 4px; padding: 0;">
   <summary style="cursor: pointer; padding: 0.75em 1em; background: #f8f8f8; font-weight: bold;">🧮 Calculateur de résistance de burden</summary>
   <div style="padding: 1em;">
   <p>Entrez les caractéristiques de votre CT pour calculer la résistance de burden adaptée.</p>
   <table style="border-collapse: collapse; width: 100%;">
   <tr>
     <td style="padding: 6px 8px;"><label for="ct_ratio_primary">Courant primaire nominal du CT (A) :</label></td>
     <td style="padding: 6px 8px;"><input type="number" id="ct_ratio_primary" value="100" min="1" step="1" style="width: 100px; padding: 4px;"></td>
   </tr>
   <tr>
     <td style="padding: 6px 8px;"><label for="ct_ratio_secondary">Courant secondaire nominal (mA) :</label></td>
     <td style="padding: 6px 8px;"><input type="number" id="ct_ratio_secondary" value="50" min="1" step="1" style="width: 100px; padding: 4px;"></td>
   </tr>
   <tr>
     <td style="padding: 6px 8px;"><label for="i_max">Courant max souhaité côté primaire (A) :</label></td>
     <td style="padding: 6px 8px;"><input type="number" id="i_max" value="50" min="1" step="1" style="width: 100px; padding: 4px;"></td>
   </tr>
   </table>
   <p style="margin-top: 0.75em;">
     <button onclick="calcBurden()" style="padding: 6px 16px; cursor: pointer; background: #2980b9; color: white; border: none; border-radius: 3px;">Calculer</button>
   </p>
   <div id="burden_result" style="margin-top: 0.5em; padding: 0.75em; background: #eef; border-radius: 4px; display: none;"></div>
   <script>
   function calcBurden() {
     var Ip = parseFloat(document.getElementById('ct_ratio_primary').value);
     var Is_mA = parseFloat(document.getElementById('ct_ratio_secondary').value);
     var Imax = parseFloat(document.getElementById('i_max').value);
     var N = Ip / (Is_mA / 1000);
     var Vref = 1.1;
     var R = (Vref * N) / (2 * Math.sqrt(2) * Imax);
     var Imax_sec_rms = Imax / N * 1000;
     var Vpeak = Imax_sec_rms / 1000 * Math.sqrt(2) * R;

     /* E24 standard resistor values */
     var e24 = [1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1];
     var std = [];
     for (var dec = 0.1; dec <= 10000; dec *= 10) {
       for (var j = 0; j < e24.length; j++) std.push(+(e24[j] * dec).toPrecision(2));
     }
     std.sort(function(a,b){return a-b;});
     var Rstd = std[0];
     for (var k = 0; k < std.length; k++) {
       if (std[k] <= R) Rstd = std[k];
       else break;
     }
     var Imax_with_std = (Vref * N) / (2 * Math.sqrt(2) * Rstd);

     var res = document.getElementById('burden_result');
     res.style.display = 'block';
     res.innerHTML =
       '<b>Rapport de transformation N</b> = ' + N.toFixed(0) + '<br>' +
       '<b>R<sub>burden</sub> calculé</b> = ' + R.toFixed(1) + ' Ω<br>' +
       '<b>Valeur standard E24 recommandée</b> = <b style="color: #c0392b;">' + Rstd + ' Ω</b> (valeur inférieure la plus proche)<br>' +
       '<b>Courant max mesurable avec ' + Rstd + ' Ω</b> = ' + Imax_with_std.toFixed(1) + ' A RMS';
   }
   </script>
   </div>
   </details>

.. include:: ../common/burden-calc.inc.rst

Alimentation
------------

Chaîne d’alimentation
~~~~~~~~~~~~~~~~~~~~~~

Le secteur entre par le connecteur d’entrée secteur (**PE / N / L1 / L2 / L3**) et traverse une chaîne de protection avant d’atteindre le module d’alimentation :

.. code-block:: text

   Secteur → Fusibles (FS0–FS3)
          → GM1–GM3 : entre chaque phase et le neutre
          → RVx en série avec GDTx : entre chaque conducteur et la terre (optionnels, par paire)
          → L1 et N : condensateur film (C1) → self de mode commun (FL1)
          → PS1 (MPC10-5) : 230 VAC → 5 VDC, 10 W
          → D1 (SMBJ7.0A) : protection TVS côté 5 V
          → U1 (AP7361C-33E) : 5 V → 3,3 V, 1 A

Protection contre les surtensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La carte intègre plusieurs niveaux de protection contre les surtensions transitoires (foudre, commutations sur le réseau). Deux niveaux sont obligatoires, un troisième est optionnel.

**Niveau 1 — Modules de protection GM1–GM3** (obligatoire)

Chaque phase est protégée par un module combiné :term:`GDT`\+\ :term:`MOV`. Ces modules constituent la protection principale des circuits de mesure. GM1 protège la phase L1, GM2 la phase L2, GM3 la phase L3 (triphasé avec neutre uniquement).

**Niveau 2 — Fusibles FS0–FS3** (obligatoire)

Les fusibles protègent l’installation contre les surintensités. Ils sont dimensionnés pour couper en cas de court-circuit sur la carte, par exemple une varistance en fin de vie ou un défaut du module d’alimentation PS1 ou du condensateur C1.

**Niveau 3 — Varistances RV0–RV3 et éclateurs GDT0–GDT3** (optionnel)

Ce niveau de protection supplémentaire est recommandé pour les installations exposées aux surtensions (zones rurales, lignes aériennes, régions à forte activité orageuse). Chaque varistance :term:`MOV` RVx est montée **en série** avec l’éclateur :term:`GDT` de même numéro (GDTx), après les fusibles, entre un conducteur et la terre : RV0 + GDT0 sur le neutre, RV1 + GDT1 sur L1, RV2 + GDT2 sur L2, RV3 + GDT3 sur L3. Alors que GM1–GM3 protègent entre phase et neutre, ces paires protègent entre les conducteurs et la terre.

.. note::
   Les composants optionnels (RV0–RV3, GDT0–GDT3) ne sont pas fournis dans le kit de base. Ils peuvent être ajoutés ultérieurement sans modifier le reste du circuit, mais **toujours par paire RVx + GDTx** : montés en série, l’un sans l’autre n’a aucun effet.

Rails d’alimentation
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 15 70

   * - Rail
     - Tension
     - Usage
   * - +5 V
     - 5 V
     - Entrée du régulateur U1, connecteur UART_EXT (broche 3), connecteurs DS18B20 et broche +5 V des sorties numériques (via cavalier « +5V Rail »). La broche VCC du connecteur FTDI n’est pas reliée.
   * - +3,3 V
     - 3,3 V
     - ATmega328P, module RFM69CW
   * - AVCC
     - 3,3 V (filtré)
     - Alimentation analogique de l’ATmega328P (ADC), de l’amplificateur LMV321A et du connecteur OLED
   * - VREF
     - 1,1 V
     - Référence interne (AREF) de l’ATmega328P, tamponnée par le LMV321A (point de test VREF)
   * - GND
     - 0 V
     - Masse numérique
   * - AGND
     - 0 V
     - Masse analogique

Cavalier « +5V Rail »
~~~~~~~~~~~~~~~~~~~~~~~~

Le cavalier de soudure **« +5V Rail »** (situé en haut à droite de la carte) permet d’activer le **rail +5 V** qui alimente la broche VCC des connecteurs 1×03 des sorties numériques. Ce rail est principalement destiné aux **cartes de sortie relais**, qui nécessitent du +5 V pour alimenter la bobine du relais.

- **Fermé** : le rail +5 V est actif sur les connecteurs 1×03 — obligatoire si des relais sont utilisés
- **Ouvert** (défaut) : le rail +5 V est déconnecté des connecteurs de sortie

.. warning::
   Ne fermez ce cavalier que si vous utilisez des cartes de sortie relais. Les cartes de sortie :term:`triac <Triac>` n’ont pas besoin de cette alimentation.

LED témoins
~~~~~~~~~~~~~~

Deux LED témoins :term:`CMS` sont situées en haut à gauche de la carte :

- **ON** : allumée lorsque la carte est sous tension
- **+5V** : allumée lorsque le rail +5 V des sorties est actif (cavalier « +5V Rail » fermé)

Intégration du module mk2Wifi
------------------------------

La carte principale est conçue pour accueillir le module d’extension :term:`mk2Wifi` via les connecteurs TRIG_EXT et UART_EXT. La zone réservée au module est repérée par un **rectangle hachuré** sur la sérigraphie de la face avant, autour des connecteurs concernés.

Signaux échangés :

- La carte principale utilise des **barrettes mâles**, le module mk2Wifi des **barrettes femelles**
- L’alimentation +5 V est fournie par la carte principale via UART_EXT broche 3
- L’UART (TX/RX) assure la communication série avec le module d’extension
- Le signal DS18B20 est acheminé via UART_EXT broche 2 pour la mesure de température 1-Wire
- Les signaux GPIO D5–D9 fournissent les sorties de déclenchement/commande via TRIG_EXT
- Le bus I2C (SCL/SDA) est **local au module mk2Wifi uniquement** — il n’est pas routé vers la carte principale

La zone hachurée sur la sérigraphie indique les connecteurs de sortie (D5#–D9#) potentiellement utilisés par le module mk2Wifi. Ces sorties restent cependant **utilisables pour d’autres usages**, même lorsque le module mk2Wifi est présent. Dans ce cas :

.. warning::
   Si vous utilisez une sortie D5–D9 pour un étage de sortie alors que le module mk2Wifi est branché :

   - N’activez sur le mk2Wifi **que les cavaliers** (D5–D9) correspondant aux sorties réellement gérées par l’ESP32 (voir :ref:`presentation-mk2wifi`)
   - **Ne jamais utiliser une même broche** à la fois par le mk2Wifi et par un autre périphérique — cela créerait un conflit de bus pouvant endommager les composants

.. |br| raw:: html

  <br/>
