.. _installation-finale:

Installation Finale dans le Système Électrique
===============================================

⚠️⚠️⚠️ **DANGER DE MORT — HAUTE TENSION 230 V AC** ⚠️⚠️⚠️

Cette section décrit la connexion du Mk2PVRouter au réseau électrique de votre habitation.

**Cette opération présente des RISQUES MORTELS par électrocution.**

.. danger::
   ⚡ **TENSION MORTELLE 230 V AC, 400 V AC en triphasé** ⚡

   Le contact avec des conducteurs sous tension peut provoquer :

   - **Décès par électrocution** (arrêt cardiaque, brûlures internes)
   - **Brûlures graves** (arc électrique : plusieurs milliers de °C)
   - **Incendie** (court-circuit, mauvaise connexion)
   - **Explosion** (défaut d’isolation)

   **Un seul instant d’inattention peut être FATAL.**

Exigences Légales en France
----------------------------

Conformité Réglementaire
^^^^^^^^^^^^^^^^^^^^^^^^

La **norme NF C 15-100** fixe les règles techniques des installations électriques basse tension en France. Toute modification de votre installation doit les respecter, que vous la réalisiez vous-même ou que vous la confiiez à un électricien.

☐ Respect des normes électriques en vigueur

   NF C 15-100 + réglementations locales

☐ Assurance habitation informée de la modification

   Une modification non déclarée peut entraîner un refus d’indemnisation

.. warning::
   ⚠️ **RISQUES EN CAS DE NON-CONFORMITÉ**

   - **Assurance habitation** : Refus d’indemnisation possible en cas de sinistre (incendie, dégât des eaux causé par une installation défectueuse)
   - **Responsabilité** : Vous pouvez être tenu pour responsable d’un accident causé par une installation non conforme

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

   **Coût estimé :** 200–500 € pour l’installation complète

   **Ce coût est DÉRISOIRE comparé aux risques encourus.**

Prérequis Avant Installation
-----------------------------

.. admonition:: 📋 Vérifications Obligatoires

   Avant TOUTE manipulation :

   ☐ **Mk2PVRouter complètement assemblé et testé**

      - Tous les tests électriques et logiciels effectués avec succès
      - Aucun défaut détecté
      - L’étalonnage se fait **après** l’installation, une fois les capteurs de courant en place (voir :ref:`etalonnage-monophase` ou :ref:`etalonnage-triphase`)

   ☐ **Disjoncteur général coupé et verrouillé**

      - Placer un cadenas si possible
      - Afficher panneau « TRAVAUX EN COURS - NE PAS RÉENCLENCHER »
      - ⚠️ Disjoncteur général coupé, les câbles en amont (du compteur au disjoncteur de branchement) **restent sous tension**
      - ⚠️ Un onduleur photovoltaïque ou un onduleur hybride à batterie peut réalimenter des circuits : arrêtez-le selon sa notice

   ☐ **Équipements de protection individuelle portés** (voir ci-dessous) **avant** la vérification d’absence de tension

   ☐ **Absence de tension vérifiée avec un VAT** (vérificateur d’absence de tension bipolaire)

      - Tester le VAT sur une source sous tension connue **avant** et **après** la vérification
      - Vérifier entre tous les conducteurs : phase–neutre, phase–terre, neutre–terre, et entre phases en triphasé

   ☐ **Personne qualifiée présente** (si vous n’êtes pas électricien)

      - En cas d’accident, quelqu’un doit pouvoir intervenir
      - Connaissance des gestes de premiers secours recommandée

   ☐ **Téléphone à portée de main** pour appeler les secours (15, 18 ou 112)

Matériel de Sécurité Requis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Équipement de Protection Individuelle (EPI)
""""""""""""""""""""""""""""""""""""""""""""

☐ **Gants isolants classe 0** (1 000 V :term:`AC`)

☐ **Chaussures de sécurité isolantes** (semelle isolée)

☐ **Tapis isolant** pour se tenir debout

☐ **Lunettes de protection** (protection contre arc électrique)

☐ **Vêtements en coton** (PAS de synthétique qui fond)

Équipement de Mesure et Outils
"""""""""""""""""""""""""""""""

☐ **Multimètre numérique** CAT III 600 V minimum

☐ **VAT** (vérificateur d’absence de tension) bipolaire, à contact, conforme NF EN 61243-3. Un détecteur de tension sans contact peut compléter le VAT, jamais le remplacer : il ne prouve pas l’absence de tension.

☐ **Tournevis isolés** 1 000 V

☐ **Pince à dénuder isolée**

☐ **Lampe de poche** (en cas de coupure secteur)
