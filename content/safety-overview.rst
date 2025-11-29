.. _safety-overview:

******************************************************
Sécurité - À Lire Absolument Avant de Commencer
******************************************************

.. danger::
   **AVERTISSEMENT IMPORTANT**

   Ce projet implique la manipulation de tensions MORTELLES (230V AC) et l'utilisation d'outils
   potentiellement dangereux. Des blessures graves, voire mortelles, peuvent survenir en cas de
   non-respect des consignes de sécurité.

   **Ce projet n'est PAS adapté aux enfants.**

   En poursuivant ce projet, vous reconnaissez les risques et assumez l'entière responsabilité
   de votre sécurité et de celle de votre entourage.

.. contents:: Sommaire de Sécurité
   :local:
   :depth: 2

=====================
Vue d'Ensemble
=====================

Ce chapitre couvre tous les aspects de sécurité liés à l'assemblage, aux tests et à l'installation
du Mk2PVRouter. Il est **OBLIGATOIRE** de lire et comprendre ce chapitre avant de commencer.

Dangers Principaux
==================

1. **Électrocution (230V AC)** - PEUT ÊTRE MORTEL
--------------------------------------------------

Le courant alternatif 230V présent dans les installations domestiques peut provoquer :

- **Arrêt cardiaque** (fibrillation ventriculaire)
- **Brûlures graves** internes et externes
- **Contractions musculaires** empêchant de lâcher la source
- **MORT** en quelques secondes

.. warning::
   **Un courant de seulement 30 mA peut être mortel!**

   Le 230V domestique peut fournir plusieurs ampères - largement suffisant pour tuer.

Situations à Risque Électrique dans ce Projet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Tests de la carte-mère avec alimentation secteur
- Soudure des connecteurs haute tension
- Tests des cartes de sortie sous tension
- Étalonnage du routeur (manipulation du câblage domestique)
- Installation finale dans le tableau électrique

2. **Brûlures (Fer à Souder 200-450°C)**
-----------------------------------------

Un fer à souder peut causer :

- Brûlures au 2ème ou 3ème degré instantanées
- Incendie si laissé sans surveillance
- Inhalation de fumées toxiques (flux de soudure)

3. **Incendie**
---------------

Plusieurs sources de risque d'incendie :

- **Soudures défectueuses** sur circuits haute puissance → Surchauffe → Incendie
- **Court-circuits** dans le routeur → Arcs électriques → Incendie
- **Fer à souder** laissé sans surveillance → Ignition matériaux
- **Surcharge électrique** lors des tests → Composants en feu

4. **Blessures Mécaniques**
---------------------------

- **Perceuse/Drill press** : Entraînement de pièces, projections
- **Outils coupants** : Coupures, entailles
- **Projections métalliques** : Blessures aux yeux

=====================
Équipement de Protection Obligatoire
=====================

Équipement de Base (Toutes Étapes)
-----------------------------------

.. admonition:: Équipement Minimum Requis

   - **Lunettes de protection** : Protection contre projections (soudure, perçage)
   - **Vêtements adaptés** : Manches longues, pas de vêtements synthétiques (fondent facilement)
   - **Chaussures fermées** : Protection contre chutes d'objets, outils électriques
   - **Cheveux attachés** : Si cheveux longs (risque entraînement outils rotatifs)

Équipement pour Soudure
-----------------------

- **Lunettes de protection** (obligatoire)
- **Support fer à souder** incombustible
- **Ventilation adéquate** ou extracteur de fumées
- **Surface de travail ininflammable** (métal, céramique, pas bois/plastique)
- **Éponge ou laine de laiton** pour nettoyer panne

Équipement pour Manipulation 230V
----------------------------------

.. danger::
   **Équipement OBLIGATOIRE pour toute manipulation haute tension**

- **Testeur de tension** sans contact (détecteur VAT)
- **Multimètre** avec protection CAT II 300V minimum
- **Gants isolants** (classe 0 minimum, 1000V)
- **Tapis isolant** ou chaussures isolantes
- **Outils isolés** (tournevis, pinces avec poignées isolées)

Équipement de Sécurité Général
-------------------------------

- **Extincteur** : Type ABC, 2kg minimum, vérifié annuellement
- **Détecteur de fumée** : Fonctionnel et testé
- **Téléphone** : À portée pour appel urgence
- **Trousse premiers secours** : Compresses stériles, pansements brûlures

=====================
Règles de Sécurité par Type d'Opération
=====================

Sécurité Soudure
================

Avant de Commencer
------------------

.. admonition:: Checklist Pré-Soudure

   [ ] Espace de travail dégagé (pas de papiers, tissus, produits inflammables)
   [ ] Surface de travail ininflammable
   [ ] Ventilation suffisante (fenêtre ouverte ou extracteur)
   [ ] Lunettes de protection portées
   [ ] Support fer à souder à portée de main
   [ ] Extincteur accessible (< 3 mètres)
   [ ] Quelqu'un informé que vous soudez (en cas d'urgence)

Pendant la Soudure
-------------------

**À FAIRE:**

- ✓ Toujours reposer le fer sur son support
- ✓ Souder dans un endroit bien ventilé
- ✓ Prendre des pauses toutes les 30-45 minutes
- ✓ Garder une éponge humide pour nettoyer la panne
- ✓ Tenir le fer par la poignée isolée uniquement

**À NE JAMAIS FAIRE:**

- ✗ Toucher la panne ou le fil chauffant (200-450°C!)
- ✗ Laisser le fer allumé sans surveillance
- ✗ Souder près de matériaux inflammables
- ✗ Respirer directement les fumées de soudure
- ✗ Poser le fer sur des surfaces combustibles

En Cas de Brûlure
-----------------

1. **Refroidir immédiatement** : Eau froide courante 10-15 minutes
2. **Ne pas percer les cloques**
3. **Couvrir avec compresse stérile**
4. **Si brûlure >5cm ou profonde** : Consulter médecin/urgences

.. warning::
   Les brûlures de fer à souder sont souvent plus graves qu'elles ne paraissent!
   Le métal chaud pénètre profondément dans les tissus.

Fumées de Soudure
-----------------

Les fumées de soudure contiennent :

- Particules métalliques (plomb si soudure plombée)
- Colophane (flux) : irritant respiratoire
- Gaz toxiques

**Protection:**

- Travailler dans endroit ventilé
- Utiliser extracteur de fumées si disponible
- Ne pas respirer directement les fumées
- Faire des pauses à l'air frais

Sécurité Électrique
===================

Règles d'Or (230V AC)
---------------------

.. danger::
   **LES 5 RÈGLES D'OR DE LA SÉCURITÉ ÉLECTRIQUE**

   Ces règles DOIVENT être respectées pour toute intervention sur installation électrique:

   1. **CONSIGNER** : Couper l'alimentation au disjoncteur
   2. **CONDAMNER** : Verrouiller le disjoncteur (cadenas si possible)
   3. **IDENTIFIER** : Vérifier que c'est bien le bon circuit
   4. **VÉRIFIER L'ABSENCE DE TENSION** : Avec testeur adapté
   5. **METTRE À LA TERRE** : Connecter la terre avant toute manipulation

Vérification Absence de Tension
--------------------------------

**TOUJOURS** vérifier l'absence de tension avant de toucher des conducteurs:

1. Utiliser un testeur de tension **adapté** (VAT)
2. **Tester le testeur** sur une prise sous tension connue AVANT (vérifier qu'il fonctionne)
3. Tester sur les conducteurs à manipuler
4. Si le testeur indique présence tension → **NE PAS TOUCHER**
5. **Tester le testeur** APRÈS pour s'assurer qu'il fonctionne toujours

.. warning::
   Un testeur défectueux peut indiquer "pas de tension" alors que le circuit est sous tension!
   C'est pourquoi il faut le tester avant ET après.

Procédure de Consignation
--------------------------

Avant toute intervention sur câblage domestique :

1. **Identifier le disjoncteur** concerné au tableau
2. **Couper le disjoncteur** (position "Off" ou "0")
3. **Si possible:** Poser un cadenas ou signalisation "NE PAS RALLUMER - Travaux en cours"
4. **Tester l'absence de tension** avec VAT (voir procédure ci-dessus)
5. **SEULEMENT ENSUITE** : Manipuler les conducteurs

.. danger::
   **JAMAIS DE TRAVAUX SOUS TENSION pour ce projet!**

   Ce projet ne nécessite AUCUNE intervention sous tension. Si vous pensez devoir
   travailler sous tension, vous faites quelque chose de travers. STOP et demandez conseil.

Protection Différentielle
--------------------------

Votre installation DOIT être protégée par :

- **Disjoncteur différentiel 30mA** (obligatoire en France)
- **Disjoncteur magnéto-thermique** adapté au circuit (généralement 16A pour prises)

.. note::
   Le différentiel 30mA détecte les fuites de courant et coupe l'alimentation
   en quelques millisecondes. Il peut vous sauver la vie!

   Testez votre différentiel mensuellement (bouton "Test").

Distance de Sécurité
--------------------

Lors de tests sous tension :

- **Garder une main dans le dos** (évite courant traversant le cœur)
- **Ne jamais toucher deux points** du circuit simultanément
- **Rester à distance** : Utiliser sondes de test, pas les doigts
- **Porter chaussures isolantes** ou être sur tapis isolant
- **Travailler à sec** : Mains sèches, pas de flaques d'eau

Sécurité Perçage/Usinage
=========================

Perceuse à Colonne / Perceuse Manuelle
---------------------------------------

.. danger::
   **RISQUES MAJEURS**

   - **Entraînement** de la pièce (rotation violente si perceuse attrape)
   - **Projection** de copeaux métalliques (risque yeux)
   - **Entraînement** de cheveux, vêtements, gants
   - **Électrocution** si câblage défectueux

Règles Obligatoires
-------------------

.. admonition:: Checklist Perçage

   [ ] **Lunettes de protection** portées (OBLIGATOIRE!)
   [ ] **Cheveux attachés** si longs
   [ ] **PAS de gants** (risque entraînement)
   [ ] **Vêtements près du corps** (pas de manches larges)
   [ ] **Pièce FIXÉE** (étau, serre-joints) - JAMAIS tenue à la main
   [ ] **Vitesse adaptée** au matériau (aluminium: lent, plastique: moyen)
   [ ] **Zone dégagée** autour de la perceuse

Technique Sûre
--------------

1. **Fixer la pièce fermement** : Utiliser étau ou serre-joints

   .. warning::
      JAMAIS tenir une pièce à la main pendant le perçage!
      Si le foret accroche, la pièce peut tourner violemment et vous blesser.

2. **Commencer avec foret pilote** : Percer petit (2-3mm) puis agrandir

3. **Avancer progressivement** : Ne pas forcer, laisser l'outil travailler

4. **Retirer le foret régulièrement** : Évacuer les copeaux

5. **Arrêter complètement** avant de retirer la pièce

Matériaux Spécifiques
---------------------

- **Aluminium (dissipateur)** : Vitesse lente, huile de coupe, forets HSS
- **Plastique ABS (boîtier)** : Vitesse moyenne, PAS d'huile, forets bois/métal
- **Attention** : Plastique peut fondre si vitesse trop élevée

Sécurité Incendie
=================

Prévention
----------

**Pendant la Soudure:**

- Extincteur ABC à portée de main (< 3 mètres)
- Surface de travail ininflammable
- Pas de matériaux combustibles à proximité (<50cm)
- Détecteur de fumée fonctionnel
- Ne jamais laisser fer allumé sans surveillance

**Pendant les Tests Électriques:**

- Surveillez les 5 premières minutes de fonctionnement
- Guettez odeurs anormales (plastique brûlé)
- Guettez fumées
- Écoutez grésillements/crépitements anormaux

Signes Avant-Coureurs
---------------------

**Arrêter IMMÉDIATEMENT si:**

- Odeur de brûlé/plastique fondu
- Fumée visible
- Chaleur excessive au toucher
- Grésillements/crépitements
- Étincelles visibles

Intervention Incendie
---------------------

**En cas de fumée ou flammes:**

1. **COUPER L'ALIMENTATION** immédiatement (disjoncteur)
2. **Si feu de soudure** : Étouffer avec chiffon humide ou extincteur
3. **Si feu électrique** : Extincteur CO2 ou poudre (PAS D'EAU!)
4. **Si feu non maîtrisé** : Évacuer et appeler pompiers (18)
5. **NE JAMAIS utiliser d'eau** sur feu électrique (risque électrocution)

.. danger::
   **Ne tentez d'éteindre un feu QUE si:**

   - Il est de petite taille (< 1m²)
   - Vous avez un extincteur adapté
   - Vous savez l'utiliser
   - Une issue de secours est accessible

   **Sinon : ÉVACUEZ et appelez les pompiers (18)**

Utilisation Extincteur
----------------------

Technique **PLMV** :

- **P** : Pointer la lance vers la base des flammes
- **L** : Lâcher la gâchette/percuter la cartouche
- **M** : Mettre en action (presser la gâchette)
- **V** : Viser la base, balayer latéralement

.. note::
   Familiarisez-vous avec votre extincteur AVANT l'urgence!
   Lisez le mode d'emploi, localisez la gâchette/percuteur.

=====================
Compétences Requises par Étape
=====================

Le tableau suivant indique le niveau de compétence requis et les risques associés à chaque étape:

.. list-table:: Évaluation des Risques par Chapitre
   :header-rows: 1
   :widths: 30 20 20 30

   * - Chapitre
     - Compétence Requise
     - Risques
     - Supervision Recommandée
   * - Soudure carte-mère
     - Débutant+ (avec pratique)
     - Brûlures (moyen)
     - Oui (1ère fois)
   * - Soudure carte-sortie
     - Intermédiaire
     - Brûlures, incendie (élevé)
     - Oui
   * - Perçage boîtier
     - Débutant
     - Projections (faible)
     - Optionnel
   * - Assemblage
     - Débutant
     - Minimal
     - Non
   * - **Tests électriques (230V)**
     - **Intermédiaire+**
     - **MORTEL**
     - **OUI - Électricien**
   * - **Étalonnage**
     - **Avancé**
     - **MORTEL**
     - **OUI - Électricien**
   * - **Installation finale**
     - **Expert**
     - **MORTEL**
     - **ÉLECTRICIEN CERTIFIÉ**

.. danger::
   Les étapes marquées "MORTEL" nécessitent une **formation en électricité** ou
   la **supervision d'un électricien qualifié**.

   **En France, l'installation finale DOIT être réalisée par un électricien certifié**
   pour la conformité NF C 15-100 et la couverture d'assurance.

=====================
Procédures d'Urgence
=====================

En Cas d'Électrocution
=======================

.. danger::
   **VITALE : Chaque seconde compte!**

Si quelqu'un est électrocuté :

1. **NE PAS TOUCHER LA VICTIME** si encore en contact avec source électrique
2. **COUPER L'ALIMENTATION** au disjoncteur (si accessible sans danger)
3. **Appeler les secours** : SAMU (15) ou Pompiers (18) ou Urgences (112)
4. **Si la victime ne respire pas** : Réanimation cardio-pulmonaire (si formation)
5. **Position latérale de sécurité** si inconscient mais respire

Signes d'Électrocution
-----------------------

- Perte de conscience
- Arrêt respiratoire
- Absence de pouls
- Brûlures (entrée et sortie du courant)
- Contractions musculaires
- Confusion, désorientation

.. warning::
   **Même après électrocution "mineure":**

   Consultez un médecin! Des lésions cardiaques peuvent apparaître plusieurs heures après.
   Le courant électrique peut provoquer des troubles du rythme cardiaque différés.

En Cas de Brûlure
=================

Brûlures Mineures (< 5cm, superficielles)
------------------------------------------

1. Refroidir immédiatement à l'eau froide courante (15-20 minutes)
2. Retirer bijoux/vêtements avant gonflement
3. Ne pas percer les cloques
4. Couvrir avec compresse stérile non adhérente
5. Surveiller infection (rougeur croissante, pus)

Brûlures Graves (> 5cm, profondes, électriques)
------------------------------------------------

1. Appeler SAMU (15) immédiatement
2. Refroidir à l'eau froide
3. Couvrir avec linge propre (pas de coton)
4. **Ne pas appliquer** : Glace, beurre, dentifrice (mythes!)
5. Surveiller état général (choc, pâleur)

.. danger::
   **Brûlures électriques : TOUJOURS consulter un médecin!**

   Les brûlures électriques sont souvent plus graves qu'elles ne paraissent.
   Le courant provoque des dégâts internes invisibles (muscles, nerfs, vaisseaux).

Numéros d'Urgence (France)
===========================

- **SAMU** : 15
- **Pompiers** : 18
- **Urgences européennes** : 112
- **Centre anti-poison** : Consulter liste par région

**Informations à fournir aux secours:**

- Votre adresse exacte
- Nombre de victimes
- Nature de l'accident (électrocution, brûlure, etc.)
- État de la victime (conscient? respire?)
- Votre numéro de téléphone

=====================
Liste de Contrôle Avant de Commencer
=====================

Évaluation Personnelle
======================

.. admonition:: Auto-Évaluation des Compétences

   **Avant d'acheter le kit, évaluez honnêtement vos compétences:**

   Soudure :
   [ ] J'ai déjà soudé des composants électroniques (au moins 10 fois)
   [ ] Je sais reconnaître une bonne soudure d'une mauvaise
   [ ] Je sais comment dessouder un composant

   Électricité :
   [ ] Je comprends la différence entre AC et DC
   [ ] Je sais utiliser un multimètre (mesurer tension, continuité)
   [ ] Je connais les dangers du 230V AC
   [ ] Je sais comment couper l'alimentation au tableau électrique
   [ ] J'ai déjà câblé un circuit domestique OU je serai supervisé par un électricien

   Mécanique :
   [ ] J'ai déjà utilisé une perceuse
   [ ] Je sais comment sécuriser une pièce pour perçage
   [ ] Je possède ou ai accès aux outils nécessaires

   **Si vous avez coché NON à plus de 2 questions :**
   → Formez-vous AVANT de commencer ce projet
   → Ou faites-vous aider par quelqu'un d'expérimenté

Ressources de Formation
------------------------

Si vous manquez de compétences, formez-vous d'abord :

**Soudure:**

- Achetez un kit d'entraînement (~10-15€)
- Regardez tutoriels YouTube "apprendre à souder"
- Pratiquez sur composants jetables
- Faites vérifier vos soudures par quelqu'un d'expérimenté

**Électricité:**

- Suivez formation électricité domestique (Fab Lab, associations)
- Lisez guides sécurité électrique
- **NE PAS apprendre sur ce projet** (trop dangereux)

**Outils:**

- Fab Labs, hackerspaces offrent accès outils et formation
- Cours bricolage magasins bricolage (Leroy Merlin, Castorama)

Checklist Avant Assemblage
===========================

.. admonition:: Vérifications Obligatoires

   **Avant de commencer l'assemblage du Mk2PVRouter :**

   Lecture :
   [ ] J'ai lu et compris ce chapitre sécurité ENTIÈREMENT
   [ ] J'ai lu la documentation technique pertinente (mono ou tri)
   [ ] Je comprends les étapes du projet

   Équipement de sécurité :
   [ ] Lunettes de protection
   [ ] Extincteur ABC (2kg min, vérifié)
   [ ] Détecteur de fumée fonctionnel
   [ ] Trousse premiers secours
   [ ] Testeur de tension (pour étapes 230V)
   [ ] Gants isolants (pour étapes 230V)

   Environnement :
   [ ] Espace de travail dégagé et bien éclairé
   [ ] Surface de travail ininflammable
   [ ] Ventilation suffisante
   [ ] Quelqu'un informé de mon activité (en cas d'urgence)
   [ ] Téléphone à portée pour appel secours

   Compétences :
   [ ] Je possède les compétences requises OU j'ai supervision adaptée
   [ ] J'ai pratiqué la soudure sur kit d'entraînement
   [ ] Je connais l'emplacement du disjoncteur principal
   [ ] Je connais les gestes premiers secours de base

Reconnaissance de Risques
==========================

.. admonition:: Déclaration de Compréhension des Risques

   **En poursuivant ce projet, je reconnais avoir compris que :**

   - Ce projet implique des **tensions MORTELLES** (230V AC)
   - Des **brûlures graves** peuvent survenir (fer à souder, composants chauds)
   - Un **risque d'incendie** existe à plusieurs étapes
   - Des **blessures mécaniques** peuvent se produire (outils)
   - Je dois **respecter scrupuleusement** toutes les consignes de sécurité
   - En cas de doute, je dois **ARRÊTER** et demander conseil
   - J'assume l'**entière responsabilité** de ma sécurité
   - Je ne tiendrai pas les auteurs de la documentation responsables en cas d'accident

   **Si vous n'êtes pas d'accord avec ces points, NE POURSUIVEZ PAS ce projet.**

Cas d'Exclusion
===============

**Vous NE DEVEZ PAS poursuivre ce projet si :**

- Vous êtes mineur (< 18 ans) sans supervision adulte compétente
- Vous n'avez jamais soudé et refusez de vous entraîner d'abord
- Vous n'avez aucune connaissance en électricité et ne voulez pas être supervisé
- Vous n'avez pas accès à l'équipement de sécurité minimum
- Vous avez peur de l'électricité (sentiment légitime = prudence!)
- Vous voulez "aller vite" et sauter les étapes de vérification
- Vous pensez "ça n'arrive qu'aux autres"

.. warning::
   **La prudence n'est PAS de la lâcheté!**

   Reconnaître ses limites et demander de l'aide est une FORCE.
   Il vaut mieux abandonner le projet que de se retrouver à l'hôpital... ou pire.

=====================
En Conclusion
=====================

Ce projet est **techniquement accessible** à un amateur motivé et prudent.

Cependant, il comporte des **risques réels et sérieux** qui ne doivent pas être sous-estimés.

**La clé du succès :**

- 📚 **Information** : Lisez toute la documentation avant de commencer
- 🎓 **Formation** : Acquérez les compétences manquantes
- 🛡️ **Protection** : Équipez-vous correctement
- 🤝 **Prudence** : N'hésitez pas à demander de l'aide
- ⏱️ **Patience** : Ne vous précipitez jamais

.. admonition:: Conseil Final

   **Si vous avez le moindre doute sur votre capacité à réaliser ce projet en sécurité :**

   - Faites-vous aider par quelqu'un d'expérimenté
   - Suivez des formations (Fab Labs, associations)
   - Pour les parties 230V : Faites appel à un électricien

   **Votre vie et celle de votre famille valent infiniment plus que le coût d'un professionnel.**

=====================
Prêt à Continuer ?
=====================

Si vous avez lu et compris ce chapitre, que vous possédez l'équipement de sécurité requis,
et que vous vous sentez capable de procéder en toute sécurité, vous pouvez passer au chapitre suivant :

- :ref:`introduction` : Vue d'ensemble du projet et liste du matériel

**En cas de doute, relisez ce chapitre ou demandez conseil avant de poursuivre.**

.. note::
   **Signaler un problème de sécurité dans cette documentation :**

   Si vous identifiez un risque qui n'est pas mentionné ou insuffisamment couvert,
   merci de le signaler pour que la documentation puisse être améliorée.

   Contact : [Email ou lien forum]

----

**Restez en sécurité. Bon courage pour votre projet! 💪**
