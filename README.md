# Gestionnaire de Serveurs Informatiques et de Services

Ce sujet va vous permettre de fournir une interface de gestion de serveurs informatiques et des services qui seront déployé dessus. Le gestionnaire pourra ajouter des serveurs, démarrer des services,… Le schéma de données est le suivant

des serveurs (id, nom, type de serveur, nombre de processeur, capacité mémoire, capacité de stockage)
des type de serveurs (id, type, description)
des utilisateurs (id, nom, prénom, email)
des services (id, nom du service, date de lancement, espace mémoire utilisé, mémoire vive nécessaire, serveur de lancement)
des applications (id, nom de l'application, logo, utilisateur)
usage des ressources qui lient des applications à l'ensemble des services qu'elles peuvent utiliser (web, DB, stockage, …)

Vous devez implémenter un CRUD pour chacun de ces types de données. vous préparerez la base en avance et la remplirez avec des type de serveurs, des serveurs, des services, et des utilisateurs.

Votre site web pourra permettre la saisie de nouveaux serveurs, services  et application. L'ajout de service et d'application vérifiera que l'espace mémoire et le nombre de processeur est suffisant sur la machine. Vous pourrez aussi insérer une application et ses services associés déployé sur un serveur à l'aide d'un fichier. La structure du fichier attendu se trouvera dans le site web

Vous aurez la possibilité de générer une fiche des services lancés sur un serveur. 
