# MongoDB Document-Oriented Database Course - Final Exam

## Introduction
Ce projet est le rendu final du cours sur les bases de données orientées document, en particulier MongoDB. Au cours de ce projet, nous avons pratiqué diverses opérations sur MongoDB à l'aide de MQL (MongoDB Query Language) et de la bibliothèque Python `pymongo`.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- Python 3.8 ou version supérieure
- `pymongo` (installable via `pip3 install pymongo`)
- MongoDB 4.4 ou version supérieure

## Installation de MongoDB
Pour installer MongoDB sur Ubuntu, suivez ces étapes :

1. Mettez à jour le système :
    ```sh
    sudo apt-get update
    sudo apt-get upgrade -y
    ```

2. Ajoutez la clé GPG pour MongoDB :
    ```sh
    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
    ```

3. Ajoutez le dépôt de MongoDB :
    ```sh
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
    ```

4. Mettez à jour la base de données des paquets :
    ```sh
    sudo apt-get update
    ```

5. Installez MongoDB :
    ```sh
    sudo apt-get install -y mongodb-org
    ```

6. Démarrez le service MongoDB :
    ```sh
    sudo systemctl start mongod
    ```

7. Activez MongoDB pour qu'il démarre au démarrage du système :
    ```sh
    sudo systemctl enable mongod
    ```

## Préparation des données
Pour importer les données nécessaires à cet examen, exécutez les commandes suivantes :

```sh
cd sample_training
sudo wget https://dst-de.s3.eu-west-3.amazonaws.com/mongo_fr/books.json
mongoimport -d sample -c books --authenticationDatabase admin --username datascientest --password dst123 --file data/db/books.json

Exécution du script
Assurez-vous que pymongo est installé :

sh
Copy code
pip3 install pymongo
Exécutez le script exam_mongoDB.py :

sh
Copy code
python3 exam_mongoDB.py
Script exam_mongoDB.py
Le script exam_mongoDB.py contient les requêtes nécessaires pour répondre aux questions de l'examen. Les réponses sont enregistrées dans le fichier res.txt.

Contenu du script
Connexion à la base de données MongoDB
Affichage des bases de données disponibles
Affichage des collections disponibles dans la base de données sample
Affichage d'un document de la collection books
Affichage du nombre de documents dans la collection books
Exploration de la base de données avec des requêtes spécifiques
Questions de l'examen
Connexion à la base de données
Afficher la liste des bases de données disponibles
Afficher la liste des collections disponibles dans la base de données sample
Afficher un des documents de la collection books
Afficher le nombre de documents dans la collection books
Exploration de la base de données
Afficher le nombre de livres avec plus de 400 pages, puis le nombre de livres ayant plus de 400 pages et qui sont publiés
Afficher le nombre de livres ayant le mot-clé Android dans leur description
Grouper les documents par catégories et créer deux sets pour chaque index de catégorie
Afficher le nombre de livres contenant certains langages dans leur description longue : Python, Java, C++, Scala
Afficher diverses informations statistiques sur notre base de données
Extraire des informations depuis l'attribut publishedDate
Créer des attributs pour chaque auteur
Agréger selon le premier auteur et obtenir le nombre de publications par auteur
Remise de l'examen
Le rendu attendu est un dossier exam_<NOM> avec 2 fichiers :

exam.py : les requêtes précédées de la question
res.txt : les réponses obtenues suite à l'exécution du fichier exam.py
N'oubliez pas d'uploader votre examen sous le format d'une archive zip ou tar, dans l'onglet Mes Exams, après avoir validé tous les exercices du module.

Conclusion
Au travers de ce cours, nous avons vu l'importance des bases de données orientées document. Nous avons appris à utiliser MongoDB, à manipuler les documents, à utiliser MQL et le framework d'agrégation, ainsi qu'à interagir avec MongoDB depuis Python via pymongo. MongoDB Atlas est également recommandé pour une gestion simplifiée de vos bases de données.

License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

go
Copy code

Vous pouvez enregistrer ce texte dans un fichier nommé `README.md` dans le répertoire de votre projet.
