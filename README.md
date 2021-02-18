# READ ME
### Utilisez les données publiques de l'OpenFoodFacts
**Startup Pur Beurre**
_______________________________
**Cahier des charges**

Pur Beurre connait bien les habitudes alimentaires des français.
Ceux-ci aimeraient changer leur alimentation, mais comment faire ?
* comment choisir un produit de substitution ?
* où l'acheter ?
_______________________________
**Comment installer le programme**

Les utilisateurs doivent, tout d'abord, installer les modules situés dans le fichier requirements dans le terminal.
Ensuite, créer et insérer les données dans la Base -> **off_db** nom de la Base de Données.
Puis lancer le programme.
``` shell
pip install -r requirements.txt
python -m off.importer_off_db
python -m off
```
Pour accéder à l'environnement virtuel, taper la ligne de commande suivante dans le Terminal :
``` shell
source env/bin/activate
```

_______________________________

**Description du parcours utilisateur**

*Customer Journey*

L'utilisateur a le choix entre plusieurs options :
1. Quel aliment souhaite-t-il remplacer ?
2. Taper **le produit** qu'il souhaite remplacer.
3. Retrouver **l'aliment** substitué.
4. Quitter

Si l'utilisateur choisi l'option **1**, il devra sélectionner **la catégorie** puis **l'aliment** qu'il désire remplacer.
-> Le programme propose **un substitut**, **sa description, un magasin où l'acheter, et un lien vers la page Open Food Facts**
-> L'utilisateur a la possibilité de sauvegarder le substitut dans la base de données.
Si l'utilisateur choisi l'option **2**, il peut taper le nom du produit directement dans le programme.
A tout moment, il peut retourner à la page principale en tapant **h**.
En cas de faute de frappe, il revient sur la question.

________________________________
**Fonctionnalités**

* Recherche de produits dans la base Open Food Facts
* L'utilisateur interagit avec le terminal
* Répéter la question en cas d'erreur de la saisie
* Recherche des produits dans la Base de Données
* Insérer les produits substitués choisis dans la Base de Données
_____________________________

Méthode Agile -> Users Stories / Tableau de tâches et sous tâches sur Trello :
https://trello.com/b/NbTMwPa1/p5-offapi
Schéma de la Base de Données -> MPD réaliser sur InDesign
Maquette réalisée sur InDesign
Base de Données sur PostgreSql, Postico (visualiser les tables, effectuer des queries)
Script Python


