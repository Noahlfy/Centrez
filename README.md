# Centrez
Créer un logiciel de la comptabilité pour les associations d'école d'ingénieur

# Avantages de l'appli poir Centrale
Les pièces justificatives ne sont pas perdues d'une année sur l'autre
L'accès pour CLA est géré facilement
Les audits sont réalisées beaucoup plus facilement -> Accès temporaires en lecture.
Un contrôle continu facile
Plus besoin de créer ses sheets pour les listes, la compta est facile à comprendre grâce à l'outil, notamment grâce à une détection d'erreurs

Potentiellement plus besoin d'un expert comptable pour CLA


# Ici je vais noter toutes les idées de fonctionnalités que je pourrais ajouter

Travail collaboratif
Importer des fichiers excels/sheet dans le logiciels, et des pièces justificatives rapidement
Exporter les fichiers en .xlsx
Produire bilan et compte de résultat à tout moment
Gérer un budget (laisser assez de marge pour le faire à sa sauce) et à chaque fois qu'une facture est ajoutée, le grand livre est rempli
Remplissage simplifié pour la partie double : une fonctionnalité "Partie double auto" qui rempli automatiquement la banque
Insérer ses relevés bancaires de manière automatique. 

# Beaucoup plus dur mais pourquoi pas

Remplissage auto après importation de factures

# Essentielles à ajouter
Gérer les accès, notamment avec un ajout d'associations, et des utilisateurs qui peuvent accéder aux associations voulues
Respecter la RGPD, jsp trop comment faire, on va bien trouver... (gérer les accès en lecture, en édition, etc.)

# Pour la compta
Documentation sur les numéros de comptes


# Fonctionnalités autres pour la gestion d'asso

Onglet "Juridique" : Rappel des échéances, modèles à utiliser, ...



# Détail des fonctionnalités pour dev
Ajouter une prévisualisation des pièces justificatives
faire en sorte d'ajouter les pièces justificatives directement dans la ligne (et ça l'ajoute directement au répertoire ensuite) (demander le nom de la pièces pour cela)

Suivi des subventions
Faire l'import des Lydia automatiquement.

# Détail de la structure

0. Page de connexion

Possibilité de relier cela au site de CLA pour que quand un élève est trésorier, il ait les accès. 
Possibilité d'avoir des accès en écriture temporaire pour les passations (les anciens trez ont des accès temporaires pour finir)

1. Accueil

- Mes associations
    Fonds disponibles
    Partager -> Autorise à partager son accès à d'autres, aussi bien en édition, qu'en lecture. Accès temporaire si possible

- Quand on clique sur une asso, on arrive sur le dashbord de l'asso => Option pour se deconnecter de l'asso


2. Comptabilité
    Plusieurs pages : 
    -> Grand Livre - équivalent balance comptable (=> classé) mais détaillé
    -> Pointage
    -> Catégories - là où on rempli. On sélectionne sa catégorie :
        Toutes les lignes existantes sur l'exercice sont affichées
        Lorsqu'on ajoute une ligne, on a des champs à remplir (dans le tableau ou un champ en bas (au choix))
        et on propose une contrepartie (Type compte en banque)
    -> Gestion des chèques de caution 

    OPTIONS :
        Obligatoires
        - Sélection de l'exercice
        - Export/import Excel
        - Produire le bilan/Compte de résultat
        - Remplissage auto partie double

        - Ajout d'une pièce justificative => la pièce est directement mise au bon endroit dans le répertoire si elle n'y est
          pas déjà
        - Prévisualisation des pièces justificatives

        Facultatives :
        - Lecture automatique de la facture (l'idéal c'est de prendre la photo du téléphone, que ça s'enregistre et se mette tout seul dans le logiciel)
        - Lecture d'un relevé bancaire
        - "auto-suggestion" basée sur historique


3. Budget
    Plusieurs pages : 
    -> Récap à l'année
    -> Par événement : Liste déroulante pour choisir avec affichage par défaut d'un event
        Champs présents dans la page : 
        - Nom de l'événement (modifiable avec bouton à cliquer) date de l'événement, nombre de personnes attendues
        - Tableau libre sur quelques colonnes : 
        Dépenses : 
        Catégorie (possibilité de fusionner) || Element || Quantité unitaire (donner des options d'unités) || Prix unitaire || Quantité voulue
        Recettes : Element, prix unitaire

        Contrainte sur les résultats : 
        Dépenses : Total / ligne = Arrondi.sup((quantité unitaire) * ((Prix unitaire)/(Quantité unitaire)))
        Recettes : Total / ligne = (element)*(prix unitaire)
    
    OPTIONS : 
        Obligatoires : 
        - Possibilité de faire du copier-coller de budget, les dupliquer
        - Modifier le nom des colonnes (mettre une option dans le menu)
        - Fixer le tableau PREVISIONNEL pour le dupliquer et le modifier pour arriver vers une solution final où on met à jour au fur et à mesure.
        

        Facultatives :
        - Insérer des références
        - Produire automatiquement les budgets pour Centrale

        Idée : possibilité de faire des détails dans les budgets, typiquement quand on a une recette. 
        1. On donne un nom, un nombre de personnes, nom de l'élément (pour le tableau)
        2. On donne les références des aliments (création d'une base de donnée modifiable)
        3. On donne les proportions de la recette
        4. On ajoute dans le budget avec les calculs nécessaires pour remplir les cases.

4. Pièces justificatives

// Simple répertoire design épuré, qui est gérable directement dans le site, mais qui est aussi présent dans le gestionnaire
   de fichier

5. Edition de documents

-> On verra plus tard

6. Juridique
7. Documentation