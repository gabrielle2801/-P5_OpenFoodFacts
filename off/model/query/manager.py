from off.model.db.models import Product, Category, Store, Substitute, Brand
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from off.constants import DB_ENGINE_URL
from sqlalchemy import asc
global Session
engine = create_engine(DB_ENGINE_URL)
Session = sessionmaker(bind=engine)


class DBManager():
    '''This class returns queries response.
    Methods get_or_create return one element of category, product, store and
    brand OR create it.
    Methods get_, return the result of queries.

    Attributes:
        session (TYPE): open a session to database
    '''

    def __init__(self):

        self.session = Session()

    def get_or_create_category(self, category_name):
        """ first found element

        Parameters:
            category_name (STR): name of category

        Returns:
            STR: Reseach the category on parameter and return one element
            if element doesn't exist create it on database
        """
        category = self.session.query(Category).filter(
            Category.name == category_name).first()
        if not category:
            category = Category(name=category_name)
            self.session.add(category)
        return category

    def get_or_create_brand(self, brand_name, label):
        """first found element

        Parameters:
            brand_name (STR): name of brand
            label (STR): description of information of brand

        Returns:
            STR : Reseach the brand on parameter and return one element
            if element doesn't exist create it on database
        """
        brand = self.session.query(Brand).filter(
            Brand.name == brand_name).first()
        if not brand or brand == "":
            brand = Brand(name=brand_name, label=label)
            self.session.add(brand)
        return brand

    def get_or_create_store(self, store_name):
        """first element found

        Parameters:
            store_name (STR): name of store

        Returns:
            STR: Reseach the store on parameter and return one element
            if element doesn't exist create it on database
        """
        store = self.session.query(Store).filter(
            Store.name == store_name).first()
        if not store or store == "":
            store = Store(name=store_name)
            self.session.add(store)
        return store

    def get_categories(self):
        """reseach categories order by alphabetical

        Returns:
            LIST: list of categories
        """
        return self.session.query(Category).select_from(Category).order_by(
            asc(Category.name)).all()

    def get_products_for_category(self, category_id):
        """Get products from number of selected category

        Parameters:
            category_id (INT): value selected by user

        Returns:
            TLIST: list of products
        """
        return self.session.query(Product).select_from(Product)\
            .join(Product.categories).filter(Category.id == category_id).all()

    def get_substitutes(self, product_id, category_id=None):
        """Get products where the nutrition grades is better than the selected
            product

        Parameters:
            product_id (INT): product id
            category_id (None, optional): category id or None

        Returns:
            LIST: list of products where nova and nutriscore is better
        """
        product = self.get_products(product_id)
        if not category_id:
            category_id = product.categories[0].id
        result = []

        product_search = self.session.query(Product).\
            select_from(Category).join(Product.categories).\
            filter(Category.id == category_id,
                   Product.nutriscore < product.nutriscore,
                   Product.nova < product.nova).all()
        if not product_search:
            product_search = self.session.query(Product).\
                select_from(Category).join(Product.categories).\
                filter(Category.id == category_id,
                       Product.nutriscore < product.nutriscore).all()
        result.extend(product_search)
        if len(result) < 3:
            return result
        else:
            return result[0:2]

    def get_stores_for_product(self, product_id):
        """get stores for product search by categorie

        Parameters:
            product_id (INT): product id

        Returns:
            LIST: list of stores for selcted product
        """
        stores_product = self.session.query(Store).select_from(Product)\
            .join(Product.stores).filter(Product.id == product_id).all()
        store_result = ""
        for store in stores_product:
            store_result = store.name + " - " + store_result
        return store_result

    def get_stores_for_substituts(self, substitut_list):
        """get stores for substituts

        Parameters:
            substitut_list (LIST): substitites proposed by get_substitutes

        Returns:
            LIST: stores list of subtitut list
        """
        list_stores = []
        store_result = ''
        for substitut in substitut_list:
            stores_substitut = self.session.query(Store).select_from(Product)\
                .join(Product.stores).filter(Product.id == substitut.id).all()
            for stores in stores_substitut:
                store_result = stores.name + " - " + store_result
            list_stores.extend([store_result])
            store_result = ""
        return list_stores

    def get_products(self, product_id):
        """get products

        Parameters:
            product_id (INT): product id

        Returns:
            INT: Reseach the product id on parameter and return one element
        """
        return self.session.query(Product).select_from(Product).filter(
            Product.id == product_id).first()

    def search_product(self, product_name):
        """Research product by name

        Parameters:
            product_name (STR): product name

        Returns:
            LIST: list of product
        """
        return self.session.query(Product).select_from(Product).filter(
            Product.name.like('%' + product_name + '%')).all()

    # List of subtitutes saved
    def create_substitute(self, product_id, substitut_id):
        """List of subtitutes saved on database

        Parameters:
            product_id (INT): product id
            substitut_id (INT): substitut id
        """
        subtitute = self.session.query(Substitute).filter(
            Substitute.product_id == product_id).first()
        if not subtitute:
            substitute = Substitute(substitute_id=substitut_id,
                                    product_id=product_id)
            self.session.add(substitute)
            print("Le produit et son substitut ont bien été enregistré")
        else:
            print("Le produit a déja été sauvegardé dans la liste")
        self.session.commit()

    def get_substitute_saved(self):

        return self.session.query(Substitute).all()
