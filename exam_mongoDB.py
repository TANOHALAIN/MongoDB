#!/usr/bin/env python3

from pymongo import MongoClient
from pprint import pprint
import zipfile
import os
import sys

# Connexion à la base de données MongoDB
client = MongoClient(
    host="127.0.0.1",
    port=27017,
    username="datascientest",
    password="dst123",
    authSource="admin"
)

db = client['sample']
books = db['books']

# (b) Afficher la liste des bases de données disponibles
print("Liste des bases de données disponibles:")
pprint(client.list_database_names())

# (c) Afficher la liste des collections disponibles dans la base de données 'sample'
print("\nListe des collections dans la base de données 'sample':")
pprint(db.list_collection_names())

# (d) Afficher un des documents de la collection 'books'
print("\nUn document de la collection 'books':")
pprint(books.find_one())

# (e) Afficher le nombre de documents dans la collection 'books'
print("\nNombre de documents dans la collection 'books':")
print(books.count_documents({}))

# Exploration de la base de données avec des requêtes spécifiques

# (a) Afficher le nombre de livres avec plus de 400 pages et publiés
more_than_400_pages = books.count_documents({"pageCount": {"$gt": 400}})
published_and_more_than_400 = books.count_documents({"pageCount": {"$gt": 400}, "status": "PUBLISH"})
print("\nLivres avec plus de 400 pages:", more_than_400_pages)
print("Livres publiés avec plus de 400 pages:", published_and_more_than_400)

# (b) Afficher le nombre de livres ayant le mot-clé 'Android' dans leur description
android_in_description = books.count_documents({"$or": [
    {"shortDescription": {"$regex": "Android", "$options": "i"}},
    {"longDescription": {"$regex": "Android", "$options": "i"}}
]})
print("\nNombre de livres ayant le mot-clé 'Android' dans leur description:", android_in_description)

# (c) Grouper les documents par catégories et créer deux sets pour chaque index de catégorie
pipeline_group_categories = [
    {"$group": {
        "_id": None,
        "categories_0": {"$addToSet": {"$arrayElemAt": ["$categories", 0]}},
        "categories_1": {"$addToSet": {"$arrayElemAt": ["$categories", 1]}}
    }}
]
print("\nGrouper les documents par catégories :")
pprint(list(books.aggregate(pipeline_group_categories)))

# (d) Afficher le nombre de livres contenant certains langages dans leur description longue
languages = ["Python", "Java", "C++", "Scala"]
count_languages = books.count_documents({
    "longDescription": {"$regex": "|".join(languages), "$options": "i"}
})
print("\nNombre de livres contenant certains langages dans leur description longue :", count_languages)

# (e) Informations statistiques sur les pages par catégorie
pipeline_stats_pages = [
    {"$unwind": "$categories"},
    {"$group": {
        "_id": "$categories",
        "max_pages": {"$max": "$pageCount"},
        "min_pages": {"$min": "$pageCount"},
        "avg_pages": {"$avg": "$pageCount"}
    }}
]
print("\nStatistiques sur les pages par catégorie :")
pprint(list(books.aggregate(pipeline_stats_pages)))

# (f) Extraire l'année, le mois et le jour de publication pour les livres publiés après 2009
pipeline_pub_date = [
    {"$match": {"publishedDate": {"$gte": "2009-01-01T00:00:00Z"}}},
    {"$project": {
        "title": 1,
        "year": {"$year": "$publishedDate"},
        "month": {"$month": "$publishedDate"},
        "day": {"$dayOfMonth": "$publishedDate"}
    }},
    {"$limit": 20}
]
print("\nLivres publiés après 2009 :")
pprint(list(books.aggregate(pipeline_pub_date)))

# (g) Créer des attributs pour chaque auteur
pipeline_authors = [
    {"$project": {
        "title": 1,
        "authors": 1,
        "author_1": {"$arrayElemAt": ["$authors", 0]},
        "author_2": {"$arrayElemAt": ["$authors", 1]},
        "author_3": {"$arrayElemAt": ["$authors", 2]},
        "author_4": {"$arrayElemAt": ["$authors", 3]}
    }},
    {"$limit": 20}
]
print("\nCréer des attributs pour chaque auteur :")
pprint(list(books.aggregate(pipeline_authors)))

# (h) Agréger selon le premier auteur et obtenir le nombre de publications par auteur
pipeline_first_author = [
    {"$project": {"first_author": {"$arrayElemAt": ["$authors", 0]}}},
    {"$group": {"_id": "$first_author", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
]
print("\nNombre de publications par auteur :")
pprint(list(books.aggregate(pipeline_first_author)))

# (i) [OPTIONNEL] Distribution du nombre d'auteurs
pipeline_num_authors = [
    {"$project": {"num_authors": {"$size": "$authors"}}},
    {"$group": {"_id": "$num_authors", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]
print("\nDistribution du nombre d'auteurs :")
pprint(list(books.aggregate(pipeline_num_authors)))

# (j) [OPTIONNEL] Occurrence de chaque auteur selon son index
pipeline_author_occurrence = [
    {"$unwind": "$authors"},
    {"$group": {"_id": "$authors", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 20}
]
print("\nOccurrence de chaque auteur selon son index :")
pprint(list(books.aggregate(pipeline_author_occurrence)))

# Enregistrer la sortie dans un fichier res.txt
with open('res.txt', 'w') as f:
    old_stdout = sys.stdout
    sys.stdout = f
    try:
        # Ré-exécuter les impressions pour enregistrer les résultats
        print("Liste des bases de données disponibles:")
        pprint(client.list_database_names())

        print("\nListe des collections dans la base de données 'sample':")
        pprint(db.list_collection_names())

        print("\nUn document de la collection 'books':")
        pprint(books.find_one())

        print("\nNombre de documents dans la collection 'books':")
        print(books.count_documents({}))

        print("\nLivres avec plus de 400 pages:", more_than_400_pages)
        print("Livres publiés avec plus de 400 pages:", published_and_more_than_400)

        print("\nNombre de livres ayant le mot-clé 'Android' dans leur description:", android_in_description)

        print("\nGrouper les documents par catégories :")
        pprint(list(books.aggregate(pipeline_group_categories)))

        print("\nNombre de livres contenant certains langages dans leur description longue :", count_languages)

        print("\nStatistiques sur les pages par catégorie :")
        pprint(list(books.aggregate(pipeline_stats_pages)))

        print("\nLivres publiés après 2009 :")
        pprint(list(books.aggregate(pipeline_pub_date)))

        print("\nCréer des attributs pour chaque auteur :")
        pprint(list(books.aggregate(pipeline_authors)))

        print("\nNombre de publications par auteur :")
        pprint(list(books.aggregate(pipeline_first_author)))

        print("\nDistribution du nombre d'auteurs :")
        pprint(list(books.aggregate(pipeline_num_authors)))

        print("\nOccurrence de chaque auteur selon son index :")
        pprint(list(books.aggregate(pipeline_author_occurrence)))
    finally:
        sys.stdout = old_stdout

# Créer l'archive ZIP
with zipfile.ZipFile('exam_TanohAlain.zip', 'w') as zipf:
    zipf.write('exam_mongoDB.py')
    zipf.write('res.txt')

print("Le fichier zip a été créé avec succès.")

