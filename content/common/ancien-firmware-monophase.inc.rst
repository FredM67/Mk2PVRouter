.. note::
   **Anciennes cartes, ancien firmware.** Cette documentation décrit uniquement le firmware ``Mk2_1phase_RFdatalog_temp``. Le firmware ``Mk2_fasterControl_Full`` n’y est plus décrit : même avec une ancienne carte, on installe le nouveau firmware, dont les réglages sont ceux du firmware triphasé, avec les mêmes noms. Le ``config.h`` de l’ancien firmware ne convient pas : partez de celui qui est fourni.

   - **Carte-mère** : mettre ``PCB_VERSION`` à ``PcbVersion::OLD_SEG`` (carte Mk2 de Robin Emley, afficheur 7 segments) ou ``PcbVersion::OLD_OLED`` (seconde ancienne carte, afficheur OLED).
   - **Étalonnage** : vos valeurs ``powerCal_grid``, ``powerCal_diverted`` et ``f_voltageCal`` de l’ancien firmware se recopient dans ``f_powerCalOldBoard``, ``f_powerCalDivertedOldBoard`` et ``f_voltageCalOldBoard`` de ``calibration.h`` (``lpf_gain`` et ``alpha`` deviennent ``lpf_gainOldBoard`` et ``alphaOldBoard``).
   - **Sonde CT2** : faire passer par elle les fils de toutes les sorties locales, triacs et relais.

   Le détail est dans la section `Upgrading from Mk2_fasterControl_Full <https://github.com/FredM67/PVRouter-1-phase/blob/dev/CHANGELOG.md#upgrading-from-mk2_fastercontrol_full>`_ du journal des modifications du firmware (en anglais).

.. warning::
   Le firmware ``Mk2_1phase_RFdatalog_temp`` n’a pas encore tourné sur une vraie carte : il passe ses tests natifs, ses vérifications à la compilation et le simulateur de réseau. Sur une installation en service, gardez l’ancien firmware ``Mk2_fasterControl_Full`` en attendant.
