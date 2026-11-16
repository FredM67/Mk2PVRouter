.. _installation-finale-mise-en-service:

Mise en Service et Maintenance
===============================

Première Mise Sous Tension
---------------------------

Liste de Vérification Finale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: ✅ Checklist Avant Première Mise Sous Tension

   Avant de réenclencher le disjoncteur :

   ☐ Toutes les connexions serrées et vérifiées

   ☐ Aucun brin de cuivre apparent

   ☐ :term:`CT` installés dans le bon sens (flèche vérifiée)

   ☐ Câbles de section correcte pour la puissance

   ☐ Disjoncteur dédié correctement dimensionné

   ☐ Tous les couvercles du tableau refermés

   ☐ Aucun outil ne reste dans le tableau

   ☐ Extincteur à portée de main

   ☐ Personne présente pour surveiller

   ☐ Téléphone à portée pour appeler secours si besoin

Procédure de Mise Sous Tension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Laisser les disjoncteurs du routeur ET des charges en position OFF**

#. **Réenclencher le disjoncteur général** du tableau

#. **Vérifier que le reste de l'installation fonctionne** (lumières, prises)

#. **Se positionner devant le tableau** avec extincteur à portée

#. **Enclencher le disjoncteur dédié du Mk2PVRouter**

#. **Observer pendant 30 secondes** :

   - Pas d'odeur de brûlé
   - Pas de fumée
   - Pas de grésillement
   - Disjoncteur ne saute pas

#. **Vérifier le fonctionnement du Mk2PVRouter** :

   - LED d'alimentation allumée
   - Écran affiche des données (si présent)
   - Pas de bruit anormal

#. **Enclencher les disjoncteurs des charges** un par un, en vérifiant après chaque enclenchement l'absence d'anomalie (odeur, grésillement, disjoncteur qui saute)

Surveillance Post-Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pendant les **premières 24 heures** :

- ⚠️ **Rester à proximité les 2 premières heures** de fonctionnement

- ⚠️ **Vérifier régulièrement** (toutes les 30 minutes au début) :

  - Pas d'échauffement anormal des connexions et du dissipateur du :term:`triac <Triac>` (toucher avec dos de la main — le dissipateur peut être tiède, mais pas brûlant)
  - Pas d'odeur de brûlé
  - Pas de fumée
  - Fonctionnement correct du routeur

- ⚠️ **Si le moindre problème est détecté** :

  #. Couper IMMÉDIATEMENT le disjoncteur du Mk2PVRouter
  #. Couper le disjoncteur général si fumée ou odeur forte
  #. Laisser refroidir 30 minutes
  #. Inspecter visuellement toutes les connexions
  #. Faire vérifier par un électricien avant de remettre sous tension

Tests de Fonctionnement
------------------------

Test de Détection de Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Allumer un appareil de forte puissance** (bouilloire, radiateur 2 000 W)

#. **Observer l'affichage du routeur** :

   - La puissance consommée doit être affichée en positif
   - Le routeur ne doit PAS activer la charge

#. **Éteindre l'appareil**

#. **Simuler une production** (si possible, ou attendre production solaire)

   - Si injection réseau détectée → Le routeur doit activer la charge
   - Puissance doit être affichée en négatif (injection)

Test de Sécurité :term:`triac <Triac>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Vérifier que la charge ne s'active PAS** en l'absence de production solaire

#. **Attendre une période de production solaire** (journée ensoleillée)

   - Quand la production dépasse la consommation du foyer, le routeur doit activer la charge
   - Plus l'excédent est important, plus la puissance routée augmente
   - Observer la montée progressive de la puissance routée sur l'écran ou les logs série

#. **Quand la production diminue** (passage nuageux, fin de journée)

   - La puissance routée doit diminuer en proportion
   - Dès que la consommation dépasse la production, la charge doit se désactiver complètement
   - Aucune injection réseau ne doit subsister

Test de Coupure d'Urgence
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Couper le disjoncteur dédié du routeur**

   - Le routeur doit s'éteindre immédiatement
   - La charge doit se désactiver

#. **Réenclencher le disjoncteur**

   - Le routeur doit redémarrer normalement
   - Pas de défaut affiché

Résolution de Problèmes Courants
---------------------------------

Le routeur ne s'allume pas
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Disjoncteur pas enclenché ou défectueux

☐ Fusible grillé sur la carte-mère (un fusible par conducteur actif : 2 en monophasé N+L, 4 en triphasé N+L1+L2+L3)

☐ Connexion d'alimentation desserrée

☐ Transformateur d'alimentation défectueux

☐ Court-circuit sur l'alimentation

**Actions :**

#. Vérifier que le disjoncteur est bien enclenché
#. Mesurer la tension en sortie du disjoncteur dédié (230 V attendu entre phase et neutre)
#. Vérifier les fusibles sur le routeur
#. Inspecter visuellement toutes les soudures

Le routeur fonctionne à l'envers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptôme :** Le routeur active la charge quand vous consommez et la désactive quand vous produisez

**Cause :** :term:`CT` installé à l'envers

**Solution :**

#. Couper le disjoncteur général
#. Retourner le :term:`CT` (inverser le sens de la flèche), ou inverser les fils K ↔ L sur le connecteur jack
#. Remettre sous tension et retester

La charge ne s'active jamais
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ :term:`triac <Triac>` défectueux (court-circuit ou ouvert)

☐ Connexion charge desserrée

☐ Charge défectueuse (chauffe-eau HS)

☐ Problème logiciel (seuil de déclenchement trop élevé)

**Actions :**

#. Vérifier les logs du routeur (seuil, puissance mesurée)
#. Vérifier la résistance de la charge (multimètre)
#. Tester le triac avec un multimètre
#. Vérifier les paramètres logiciels

Le disjoncteur saute
^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Court-circuit dans le routeur ou la charge

☐ Surcharge (charge trop puissante pour le calibre du disjoncteur)

☐ Défaut d'isolation (fuite à la terre)

☐ Disjoncteur défectueux ou sous-dimensionné

**Actions :**

#. **NE PAS réenclencher immédiatement**
#. Débrancher la charge du routeur
#. Réenclencher le disjoncteur → Si le disjoncteur tient : Le problème vient de la charge
#. Si le disjoncteur saute toujours : Le problème vient du routeur → Faire vérifier par un électricien

Odeur de brûlé
^^^^^^^^^^^^^^

**ACTION IMMÉDIATE :**

#. ⚠️ **COUPER LE DISJONCTEUR GÉNÉRAL IMMÉDIATEMENT**
#. ⚠️ **Évacuer si fumée importante**
#. ⚠️ **Appeler les pompiers (18) si flammes visibles**
#. Laisser refroidir 30 minutes minimum
#. **Faire inspecter par un électricien** avant de remettre sous tension

Maintenance et Surveillance
----------------------------

Vérifications Périodiques
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tous les 6 mois :**

☐ Inspecter visuellement toutes les connexions

☐ Vérifier qu'aucune connexion n'est desserrée (vibrations)

☐ Vérifier l'absence d'échauffement anormal

☐ Nettoyer la poussière accumulée (disjoncteur coupé)

☐ Vérifier le bon fonctionnement du routeur

**Tous les ans :**

☐ Faire vérifier l'installation par un électricien

☐ Vérifier l'étalonnage du routeur

☐ Vérifier l'état du :term:`triac <Triac>` et de son dissipateur (traces de surchauffe, décoloration)

☐ Vérifier les :term:`CT` (clip de fermeture pas cassé)

Signes d'Alerte
^^^^^^^^^^^^^^^^

**Appeler un électricien IMMÉDIATEMENT si :**

⚠️ Odeur de brûlé persistante

⚠️ Échauffement anormal d'une connexion

⚠️ Grésillement ou bruit anormal

⚠️ Disjoncteur qui saute régulièrement

⚠️ Fumée, même légère

⚠️ Fonctionnement erratique du routeur

Dépose et Remplacement
^^^^^^^^^^^^^^^^^^^^^^^

Si vous devez déposer le routeur :

#. **Couper le disjoncteur dédié**

#. **Couper le disjoncteur général** (sécurité supplémentaire)

#. **Vérifier l'absence de tension**

#. **Débrancher les charges** des étages de sortie

#. **Débrancher l'alimentation** du routeur (câble secteur)

#. **Ouvrir les CT** (déclipser) puis débrancher les jacks

#. **Retirer le routeur**

Pour le remplacement, suivre la procédure d'installation depuis le début.

Numéros d'Urgence
-----------------

En cas de problème grave :

.. important::
   📞 **Numéros d'urgence en France**

   - **15** : SAMU (urgence médicale - électrocution)
   - **18** : Pompiers (incendie électrique)
   - **112** : Numéro d'urgence européen (fonctionne partout)

   **En cas d'électrocution :**

   #. **NE PAS toucher la victime** si encore sous tension
   #. **Couper le disjoncteur général IMMÉDIATEMENT**
   #. **Appeler le 15** (SAMU)
   #. Pratiquer massage cardiaque si formation aux premiers secours
   #. Ne pas déplacer la victime sauf danger immédiat

Ressources Complémentaires
---------------------------

.. admonition:: 📚 Documentation Technique

   - **Norme NF C 15-100** : https://www.promotelec.com/
   - **Guide Consuel** : https://www.consuel.com/
   - **Formation habilitation électrique** : Rechercher « formation habilitation électrique » + votre ville

.. admonition:: 🔧 Forum et Support

   - **GitHub Issues** : https://github.com/FredM67/Mk2PVRouter/issues
   - **GitHub Discussions** : https://github.com/FredM67/PVRouter-3-phase/discussions

Avertissement Final
-------------------

.. danger::
   ⚡ **DERNIER AVERTISSEMENT** ⚡

   L'installation d'un équipement électrique dans le tableau de distribution est une opération **À HAUT RISQUE** :

   - Risque de **MORT par électrocution**
   - Risque **d'INCENDIE**
   - Risque de **dégâts matériels** importants

   **Ce guide est fourni à titre informatif UNIQUEMENT.**

   **Les auteurs déclinent toute responsabilité en cas d'accident, de dommage matériel ou corporel résultant d'une installation non conforme ou réalisée par une personne non qualifiée.**

   **Pour votre sécurité et celle de votre famille, faites appel à un électricien certifié.**

   **Votre vie n'a pas de prix.**
