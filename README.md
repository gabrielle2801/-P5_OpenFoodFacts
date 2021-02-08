# READ ME
### Utilisez les données publiques de l'OpenFoodFacts

**Startup Pur Beurre**
_______________________________
**Cahier des charges**

Pur Beurre connait bien les habitudes alimentaires des français.
Ceux-ci aimeraient changer leur alimentation, mais comment faire ?
* Comment choisir un produit de substitution ?
* Où l'acheter ?
_______________________________
**Comment installer le programme**

Les utilisateurs doivent installer les modules situés dans le fichier requirements,
en tapant la ligne de commande suivante :
Le programme crée une Base de Données "off_db" PostgreSQL avec un password.
Pour utiliser le programme, ils doivent lancer le programme avec la ligne de commande suivante :
**python -m off**
_______________________________

**Description du parcours utilisateur**

*Customer Journey*

L'utilisateur a le choix entre plusieurs options :
1. Quel aliment souhaite-t-il remplacer ?
2. Taper **le produit** qu'il souhaite remplacer.
3. Retrouver **ses aliments** substitués.
4. Quitter

Si l'utilisateur choisi l'option **1**, il devra sélectionner **la catégorie** puis **l'aliment** qu'il désire remplacer.
-> Le programme propose un substitut, **sa description, un magasin où l'acheter, et un lien vers la page Open Food Facts**
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

________________________________

```
Installer SQLAlchemy, requests par le fichier requirements.txt
-> installer pip install -r requirements.txt
Pour créer la base de Données -> python -m off.importer_off_db
Méthode Agile -> Users Stories / Tableau de tâches et sous tâches sur Trello
Schéma de la Base de Données -> MPD réaliser sur Indesign
Maquette réalisé sur Indesign
Base de Données sur PostgreSql, Postico (visualiser les tables, effectuer des queries)
Script Python
```

