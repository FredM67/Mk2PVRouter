.. _installation-finale:

Installation Finale dans le Système Électrique
===============================================

⚠️⚠️⚠️ **DANGER DE MORT — HAUTE TENSION 230 V AC** ⚠️⚠️⚠️

Cette section décrit la connexion du Mk2PVRouter au réseau électrique de votre habitation.

**Cette opération présente des RISQUES MORTELS par électrocution.**

.. danger::
   ⚡ **TENSION MORTELLE 230 V AC, 380 V AC en triphasé** ⚡

   Le contact avec des conducteurs sous tension peut provoquer :

   - **Décès par électrocution** (arrêt cardiaque, brûlures internes)
   - **Brûlures graves** (arc électrique jusqu’à 3 000 °C)
   - **Incendie** (court-circuit, mauvaise connexion)
   - **Explosion** (défaut d’isolation)

   **Un seul instant d’inattention peut être FATAL.**

.. contents:: Sommaire
   :local:
   :depth: 2

Exigences Légales en France
----------------------------

Conformité Réglementaire Obligatoire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selon la **norme NF C 15-100** (installations électriques basse tension en France) :

☐ Installation par **électricien qualifié OBLIGATOIRE**

   Seul un professionnel certifié peut légalement modifier une installation électrique

☐ Conformité installation vérifiée par **Consuel**

   Organisme de contrôle des installations électriques

☐ Assurance habitation **DOIT être informée** de la modification

   Toute modification non déclarée peut entraîner refus d’indemnisation

☐ Respect des normes électriques en vigueur

   NF C 15-100 + réglementations locales

.. warning::
   ⚠️ **CONSÉQUENCES LÉGALES**

   En cas de non-conformité :

   - **Assurance habitation** : Refus d’indemnisation en cas de sinistre (incendie, dégât des eaux causé par installation défectueuse)
   - **Vente immobilière** : Diagnostic électrique obligatoire, non-conformité bloque la vente
   - **Responsabilité pénale** : En cas d’accident causé par installation non conforme
   - **Amendes** : Jusqu’à 3 000 € pour installation non déclarée

Recommandation Forte
^^^^^^^^^^^^^^^^^^^^^

.. important::
   🔴 **NOUS RECOMMANDONS VIVEMENT de faire appel à un électricien certifié**

   **Pourquoi ?**

   - Connaissance des normes en vigueur
   - Expérience des installations haute puissance
   - Équipement de sécurité approprié
   - Assurance responsabilité civile professionnelle
   - Attestation de conformité pour votre assurance

   **Coût estimé :** 200-500 € pour l’installation complète

   **Ce coût est DÉRISOIRE comparé aux risques encourus.**

Prérequis Avant Installation
-----------------------------

.. admonition:: 📋 Vérifications Obligatoires

   Avant TOUTE manipulation :

   ☐ **Mk2PVRouter complètement assemblé et testé**

      - Tous les tests logiciels effectués avec succès
      - Étalonnage (calibration) terminé
      - Aucun défaut détecté

   ☐ **Disjoncteur général coupé et verrouillé**

      - Placer un cadenas si possible
      - Afficher panneau « TRAVAUX EN COURS - NE PAS RÉENCLENCHER »

   ☐ **Absence de tension vérifiée avec multimètre**

      - Mesurer entre phase et neutre : 0 V
      - Mesurer entre phase et terre : 0 V
      - Refaire la mesure 3 fois pour être certain

   ☐ **Personne qualifiée présente** (si vous n’êtes pas électricien)

      - En cas d’accident, quelqu’un doit pouvoir intervenir
      - Connaissance des gestes de premiers secours recommandée

   ☐ **Téléphone à portée de main** pour appeler les secours (15 ou 18)

Matériel de Sécurité Requis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Équipement de Protection Individuelle (EPI)
""""""""""""""""""""""""""""""""""""""""""""

☐ **Gants isolants classe 00** (minimum 500 V :term:`AC`)

☐ **Chaussures de sécurité isolantes** (semelle isolée)

☐ **Tapis isolant** pour se tenir debout

☐ **Lunettes de protection** (protection contre arc électrique)

☐ **Vêtements en coton** (PAS de synthétique qui fond)

Équipement de Mesure et Outils
"""""""""""""""""""""""""""""""

☐ **Multimètre numérique** CAT III ou CAT IV (600 V minimum)

☐ **Testeur de tension sans contact** (VAT — Voltage Alert Tester)

☐ **Tournevis isolés** 1 000 V

☐ **Pince à dénuder isolée**

☐ **Lampe de poche** (en cas de coupure secteur)

Installation des Capteurs de Courant (:term:`CT`)
------------------------------------------

Les capteurs de courant (Current Transformers) se placent sur les câbles d’alimentation principale.

Emplacement des :term:`CT`
^^^^^^^^^^^^^^^^^^

.. figure:: img/schema-installation-ct.png
   :align: center
   :alt: Schéma d’installation des capteurs de courant
   :scale: 50 %

   Position recommandée des capteurs de courant sur l’installation

**CT Grille — Mesure de la consommation/injection réseau**

   :term:`CT`·s à clip installé·s sur le câble de **phase** principal arrivant du compteur Linky/Enedis

   - **Monophasé** : 1 :term:`CT` à clip sur la phase unique (CT1)
   - **Triphasé** : 3 :term:`CT` à clip sur les 3 phases (CT1, CT2, CT3)

**CT Diversion — Mesure de la puissance routée** (optionnel)

   :term:`CT` **intégré dans le boîtier** du Mk2PVRouter, connecté sur le câble relié à la charge

   ⚠️ Ce :term:`CT` n’est **PAS** un :term:`CT` à clip externe comme les :term:`CT` Grille

Sens d’Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. danger::
   ⚠️ **LE SENS DES CT EST CRUCIAL**

   Un :term:`CT` installé à l’envers inversera le signe de la mesure :

   - Le routeur verra une **production** alors qu’il y a **consommation**
   - Le routeur verra une **consommation** alors qu’il y a **production**
   - **Résultat** : Le routeur fonctionnera à l’envers et **augmentera votre facture** au lieu de la réduire

**Règle de base :**

La **flèche** gravée sur le :term:`CT` doit pointer dans le **sens du flux d’énergie** :

- **CT Grille** : Flèche pointant **VERS la maison** (depuis le compteur)
- **CT Diversion** : Flèche pointant **VERS la charge** (chauffe-eau)

Procédure d’Installation des :term:`CT`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   ⚠️ **DISJONCTEUR GÉNÉRAL COUPÉ OBLIGATOIRE**

   Ne JAMAIS installer les :term:`CT` sous tension !

#. **Couper le disjoncteur général** et vérifier absence de tension

#. **Identifier le câble de phase** principal (généralement rouge, marron ou noir)

   ⚠️ Ne PAS placer le :term:`CT` sur le neutre (bleu) ou la terre (vert/jaune)

#. **Ouvrir le CT** en appuyant sur le clip de fermeture

#. **Placer le CT autour du câble de phase UNIQUEMENT**

   - Un seul conducteur doit passer dans le :term:`CT`
   - Ne pas passer plusieurs câbles ensemble (sauf si intentionnel pour mesure différentielle)

#. **Vérifier le sens** : Flèche vers la maison pour :term:`CT` Grille

#. **Refermer fermement le CT** jusqu’au clic de verrouillage

#. **Vérifier que le CT est bien clipsé** (tirer légèrement pour tester)

#. **Fixer le câble du CT** pour éviter qu’il se débranche par traction

Vérification du Sens des :term:`CT` (Après Installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Une fois le routeur sous tension (après toutes les connexions) :

#. **Allumer un appareil de forte puissance** (bouilloire 2 000 W, radiateur)

#. **Observer l’affichage du routeur** (si écran présent) ou les logs série

#. **Vérifier que la puissance affichée est POSITIVE** quand vous consommez

   - Si la puissance est **négative** alors que vous consommez → **CT à l’envers**
   - Couper le disjoncteur, retourner le :term:`CT`, retester

Connexions Électriques au Tableau
----------------------------------

.. danger::
   ⚠️⚠️⚠️ **ZONE À HAUT RISQUE — TENSION MORTELLE** ⚠️⚠️⚠️

   Les opérations suivantes présentent un risque **MAXIMAL** d’électrocution.

   **SI VOUS N’ÊTES PAS ÉLECTRICIEN QUALIFIÉ, ARRÊTEZ-VOUS ICI.**

   Faites appel à un professionnel certifié.

Protection Électrique du Système
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   **Architecture du système :**

   - Le **Mk2PVRouter lui-même** consomme moins de **5 W** (alimentation électronique uniquement)
   - Les **circuits de puissance** (triacs) sont **indépendants** et pilotent les charges
   - Chaque **charge** (chauffe-eau, radiateur) conserve sa **propre protection** existante

Le Mk2PVRouter **électronique** nécessite un disjoncteur dédié pour son alimentation :

- **Type** : Disjoncteur divisionnaire bipolaire (Phase + Neutre)
- **Calibre** : 2 A ou 6 A (suffisant pour l’électronique < 5 W)
- **Courbe** : Type C (protection usage courant)
- **Pouvoir de coupure** : Minimum 4,5 kA (6 kA ou 10 kA recommandé)

.. important::
   ⚠️ **POURQUOI UN DISJONCTEUR DÉDIÉ ?**

   - **Isolation** : Permet de couper uniquement le routeur sans affecter les charges
   - **Protection** : Protège l’électronique du routeur uniquement
   - **Maintenance** : Facilite les interventions futures
   - **Sécurité** : En cas de défaut électronique, seul le routeur est déconnecté

.. warning::
   **Les charges restent protégées par leurs disjoncteurs d’origine**

   Le Mk2PVRouter ne remplace PAS la protection existante des charges :

   - Chauffe-eau : Conserve son disjoncteur 16 A ou 20 A
   - Radiateur : Conserve son disjoncteur adapté à sa puissance
   - Le routeur **pilote** les triacs, mais ne **protège pas** les charges

Câblage du Mk2PVRouter
^^^^^^^^^^^^^^^^^^^^^^^

**Pour l’alimentation du Mk2PVRouter électronique (< 5 W) :**

- **Section** : 0,75 mm² ou 1,5 mm² (largement suffisant)
- **Protection** : Disjoncteur 2 A ou 6 A

**Pour les charges pilotées (les câbles existants sont conservés) :**

La section des câbles des charges dépend de leur puissance (ces câbles sont normalement **déjà installés**) :

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Puissance charge
     - Section câble minimum
     - Disjoncteur max
   * - Jusqu’à 2 300 W
     - 1,5  mm²
     - 10 A
   * - 2 300 W - 3 680 W
     - 2,5 mm²
     - 16 A
   * - 3 680 W - 5 750 W
     - 4 mm²
     - 25 A
   * - 5 750 W - 7 360 W
     - 6 mm²
     - 32 A

.. note::
   **Ces sections concernent les charges uniquement, PAS le Mk2PVRouter.**

   Pour un **chauffe-eau classique 2 000-3 000 W**, les câbles existants sont normalement en **2,5 mm²** avec disjoncteur **16 A** ou **20 A**.

   Le Mk2PVRouter se branche **en parallèle** pour piloter la charge, il ne remplace pas ces câbles.

Schéma de Raccordement
^^^^^^^^^^^^^^^^^^^^^^

**Monophasé (230 V) :**

.. code-block:: text

   TABLEAU ÉLECTRIQUE                    MK2PVROUTER
   ┌─────────────────┐                  ┌───────────────┐
   │                 │                  │               │
   │  Disjoncteur    │                  │  Entrée 230 V │
   │  16 A Bipolaire │                  │               │
   │                 │                  │  L  ──────────┼─── Vers charge
   │   L ────────────┼──────────────────┼─ Phase        │    (chauffe-eau)
   │                 │                  │               │
   │   N ────────────┼──────────────────┼─ Neutre       │
   │                 │                  │               │
   │  ⏚ ─────────────┼──────────────────┼─ Terre        │
   │                 │                  │               │
   └─────────────────┘                  └───────────────┘

**Triphasé (3 × 230 V = 400 V) :**

.. code-block:: text

   TABLEAU ÉLECTRIQUE                    MK2PVROUTER
   ┌─────────────────┐                  ┌──────────────┐
   │                 │                  │              │
   │  Disjoncteur    │                  │  Entrée 3~   │
   │  Tétrapolaire   │                  │              │
   │  16 A           │                  │  L1 ─────────┼─── Charge phase 1
   │                 │                  │              │
   │   L1 ───────────┼──────────────────┼─ Phase 1     │
   │   L2 ───────────┼──────────────────┼─ Phase 2     │
   │   L3 ───────────┼──────────────────┼─ Phase 3     │
   │   N  ───────────┼──────────────────┼─ Neutre      │
   │   ⏚  ───────────┼──────────────────┼─ Terre       │
   │                 │                  │              │
   └─────────────────┘                  └──────────────┘

Procédure de Connexion (Électricien Qualifié)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **COUPER le disjoncteur général** du tableau

#. **Vérifier l’absence de tension** avec multimètre ET testeur sans contact

#. **Attendre 5 minutes** (décharge des condensateurs éventuels)

#. **Porter les EPI** (gants isolants, chaussures de sécurité)

#. **Installer le disjoncteur dédié** 16 A dans le tableau

#. **Connecter les câbles d’alimentation** au disjoncteur :

   - Phase (L) : Câble rouge/marron/noir
   - Neutre (N) : Câble bleu
   - Terre (⏚) : Câble vert/jaune

#. **Connecter les câbles vers le Mk2PVRouter** :

   - Respecter les couleurs (Phase, Neutre, Terre)
   - Serrer les connexions au couple recommandé (tournevis dynamométrique)
   - Vérifier qu’aucun brin de cuivre ne dépasse du bornier

#. **Connecter les câbles vers la charge** (chauffe-eau, radiateur)

#. **Vérifier toutes les connexions** (tirer légèrement sur chaque câble)

#. **Vérifier qu’aucun outil ne reste dans le tableau**

Première Mise Sous Tension
---------------------------

Liste de Vérification Finale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: ✅ Checklist Avant Première Mise Sous Tension

   Avant de réenclencher le disjoncteur :

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

#. **Laisser le disjoncteur du Mk2PVRouter en position OFF**

#. **Réenclencher le disjoncteur général** du tableau

#. **Vérifier que le reste de l’installation fonctionne** (lumières, prises)

#. **Se positionner devant le tableau** avec extincteur à portée

#. **Enclencher le disjoncteur dédié du Mk2PVRouter**

#. **Observer pendant 30 secondes** :

   - Pas d’odeur de brûlé
   - Pas de fumée
   - Pas de grésillement
   - Disjoncteur ne saute pas

#. **Vérifier le fonctionnement du Mk2PVRouter** :

   - LED d'alimentation allumée
   - Écran affiche des données (si présent)
   - Pas de bruit anormal

Surveillance Post-Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pendant les **premières 24 heures** :

- ⚠️ **Rester à proximité les 2 premières heures** de fonctionnement

- ⚠️ **Vérifier régulièrement** (toutes les 30 minutes au début) :

  - Pas d’échauffement anormal des connexions (toucher avec dos de la main)
  - Pas d’odeur de brûlé
  - Pas de fumée
  - Fonctionnement correct du routeur

- ⚠️ **Si le moindre problème est détecté** :

  #. Couper IMMÉDIATEMENT le disjoncteur du Mk2PVRouter
  #. Couper le disjoncteur général si fumée ou odeur forte
  #. Laisser refroidir 30 minutes
  #. Inspecter visuellement toutes les connexions
  #. Faire vérifier par un électricien avant de remettre sous tension

Tests de Fonctionnement
------------------------

Test de Détection de Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Allumer un appareil de forte puissance** (bouilloire, radiateur 2 000 W)

#. **Observer l’affichage du routeur** :

   - La puissance consommée doit être affichée en positif
   - Le routeur ne doit PAS activer la charge

#. **Éteindre l’appareil**

#. **Simuler une production** (si possible, ou attendre production solaire)

   - Si injection réseau détectée → Le routeur doit activer la charge
   - Puissance doit être affichée en négatif (injection)

Test de Sécurité :term:`triac`
^^^^^^^^^^^^^^^^^^^^^^

Si le routeur utilise un :term:`triac` pour moduler la puissance :

#. **Vérifier que la charge ne s’active PAS** en l’absence de production

#. **Simuler une petite production** (< 500 W)

   - Charge doit s’activer partiellement (modulation)

#. **Simuler forte production** (> puissance de la charge)

   - Charge doit s’activer à 100 %

#. **Couper la production simulée brutalement**

   - Charge doit se désactiver immédiatement
   - Pas d’injection réseau parasite

Test de Coupure d’Urgence
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Couper le disjoncteur dédié du routeur**

   - Le routeur doit s’éteindre immédiatement
   - La charge doit se désactiver

#. **Réenclencher le disjoncteur**

   - Le routeur doit redémarrer normalement
   - Pas de défaut affiché

Résolution de Problèmes Courants
---------------------------------

Le routeur ne s’allume pas
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Disjoncteur pas enclenché ou défectueux

☐ Fusible grillé sur le routeur

☐ Connexion d’alimentation desserrée

☐ Transformateur d’alimentation défectueux

☐ Court-circuit sur l’alimentation

**Actions :**

#. Vérifier que le disjoncteur est bien enclenché
#. Mesurer la tension aux bornes d’alimentation du routeur (230 V attendu)
#. Vérifier les fusibles sur le routeur
#. Inspecter visuellement toutes les soudures

Le routeur fonctionne à l’envers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Symptôme :** Le routeur active la charge quand vous consommez et la désactive quand vous produisez

**Cause :** :term:`CT` installé à l’envers

**Solution :**

#. Couper le disjoncteur général
#. Retourner le :term:`CT` (inverser le sens de la flèche)
#. Remettre sous tension et retester

La charge ne s’active jamais
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ :term:`triac` défectueux (court-circuit ou ouvert)

☐ Connexion charge desserrée

☐ Charge défectueuse (chauffe-eau HS)

☐ Problème logiciel (seuil de déclenchement trop élevé)

**Actions :**

#. Vérifier les logs du routeur (seuil, puissance mesurée)
#. Vérifier la résistance de la charge (multimètre)
#. Tester le triac avec un multimètre
#. Vérifier les paramètres logiciels

Le disjoncteur saute
^^^^^^^^^^^^^^^^^^^^^

**Causes possibles :**

☐ Court-circuit dans le routeur ou la charge

☐ Surcharge (charge trop puissante pour le calibre du disjoncteur)

☐ Défaut d’isolation (fuite à la terre)

☐ Disjoncteur défectueux ou sous-dimensionné

**Actions :**

#. **NE PAS réenclencher immédiatement**
#. Débrancher la charge du routeur
#. Réenclencher le disjoncteur → Si le disjoncteur tient : Le problème vient de la charge
#. Si le disjoncteur saute toujours : Le problème vient du routeur → Faire vérifier par un électricien

Odeur de brûlé
^^^^^^^^^^^^^^

**ACTION IMMÉDIATE :**

#. ⚠️ **COUPER LE DISJONCTEUR GÉNÉRAL IMMÉDIATEMENT**
#. ⚠️ **Évacuer si fumée importante**
#. ⚠️ **Appeler les pompiers (18) si flammes visibles**
#. Laisser refroidir 30 minutes minimum
#. **Faire inspecter par un électricien** avant de remettre sous tension

Maintenance et Surveillance
----------------------------

Vérifications Périodiques
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tous les 6 mois :**

☐ Inspecter visuellement toutes les connexions

☐ Vérifier qu’aucune connexion n’est desserrée (vibrations)

☐ Vérifier l’absence d’échauffement anormal

☐ Nettoyer la poussière accumulée (disjoncteur coupé)

☐ Vérifier le bon fonctionnement du routeur

**Tous les ans :**

☐ Faire vérifier l’installation par un électricien

☐ Vérifier l’étalonnage du routeur

☐ Contrôler l’usure des contacts du :term:`triac`

☐ Vérifier les :term:`CT` (clip de fermeture pas cassé)

Signes d’Alerte
^^^^^^^^^^^^^^^^

**Appeler un électricien IMMÉDIATEMENT si :**

⚠️ Odeur de brûlé persistante

⚠️ Échauffement anormal d’une connexion

⚠️ Grésillement ou bruit anormal

⚠️ Disjoncteur qui saute régulièrement

⚠️ Fumée, même légère

⚠️ Fonctionnement erratique du routeur

Dépose et Remplacement
^^^^^^^^^^^^^^^^^^^^^^^

Si vous devez déposer le routeur :

#. **Couper le disjoncteur dédié**

#. **Couper le disjoncteur général** (sécurité supplémentaire)

#. **Vérifier l’absence de tension**

#. **Débrancher les CT** en premier

#. **Débrancher l’alimentation** du routeur

#. **Débrancher la charge**

#. **Retirer le routeur**

Pour le remplacement, suivre la procédure d’installation depuis le début.

Numéros d’Urgence
-----------------

En cas de problème grave :

.. important::
   📞 **Numéros d’urgence en France**

   - **15** : SAMU (urgence médicale - électrocution)
   - **18** : Pompiers (incendie électrique)
   - **112** : Numéro d’urgence européen (fonctionne partout)

   **En cas d’électrocution :**

   #. **NE PAS toucher la victime** si encore sous tension
   #. **Couper le disjoncteur général IMMÉDIATEMENT**
   #. **Appeler le 15** (SAMU)
   #. Pratiquer massage cardiaque si formation aux premiers secours
   #. Ne pas déplacer la victime sauf danger immédiat

Ressources Complémentaires
---------------------------

.. admonition:: 📚 Documentation Technique

   - **Norme NF C 15-100** : https://www.promotelec.com/
   - **Guide Consuel** : https://www.consuel.com/
   - **Formation habilitation électrique** : Rechercher « formation habilitation électrique » + votre ville

.. admonition:: 🔧 Forum et Support

   - **Forum Mk2PVRouter** : [Lien vers forum si existe]
   - **Support technique** : [Email/Contact support]

Avertissement Final
-------------------

.. danger::
   ⚡ **DERNIER AVERTISSEMENT** ⚡

   L’installation d’un équipement électrique dans le tableau de distribution est une opération **À HAUT RISQUE** :

   - Risque de **MORT par électrocution**
   - Risque **d’INCENDIE**
   - Risque de **dégâts matériels** importants

   **Ce guide est fourni à titre informatif UNIQUEMENT.**

   **Les auteurs déclinent toute responsabilité en cas d’accident, de dommage matériel ou corporel résultant d’une installation non conforme ou réalisée par une personne non qualifiée.**

   **Pour votre sécurité et celle de votre famille, faites appel à un électricien certifié.**

   **Votre vie n’a pas de prix.**
