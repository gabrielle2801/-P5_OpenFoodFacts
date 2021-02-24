from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = MetaData()

product_category = Table('product_category', Base.metadata,
                         Column('product_id', Integer,
                                ForeignKey('product.id')),
                         Column('category_id', Integer,
                                ForeignKey('category.id'))
                         )

product_store = Table('product_store', Base.metadata,
                      Column('product_id', Integer, ForeignKey('product.id')),
                      Column('store_id', Integer,
                             ForeignKey('store.id'))
                      )


class Product(Base):

    """Table Product

    Attributes:
        barcode (int): barcode of product
        brand (TYPE): Relationship between Product and Brand (many to one)
        brand_id (INT): id of product refered
        categories (TYPE): Relationship between Product and category
            (many to many)
        description (STR): Details of ingredients
        id (TINT): identifiant
        name (STR): name of product
        nova (INT): nova score 1 to 4 highlight the degree of processing
            of foods
        nutriscore (STR): nutrsiscore A to E quality of food products
        stores (TYPE): Relationship between Product and Store (many to many)
        url (STR): Web link to product information
    """

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nutriscore = Column(String)
    nova = Column(Integer)
    url = Column(String)
    barcode = Column(String)
    description = Column(String)
    brand_id = Column(Integer, ForeignKey(
        'brand.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    brand = relationship("Brand", backref="brands", lazy=True)

    categories = relationship(
        "Category",
        secondary=product_category, backref="products")
    stores = relationship(
        "Store",
        secondary=product_store,
        backref="products")

    def __repr__(self):
        """Representation of values

        Returns:
            STR: name, nustriscore and nova
        """
        return " %s, nutriscore:%s, nova:%s"\
            % (self.name, self.nutriscore.upper(), self.nova)


class Substitute(Base):

    """Table Substitute

    Attributes:
        id (INT): Identifiant
        product (INT): Id of product
        product_id (INT): Relationship between Product and Subtitute
            (many to many)
        substitute (INT): Id of substitutes
        substitute_id (INT): Relationship between Product and Subtitute
            (many to many)
    """

    __tablename__ = 'substitute'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), unique=True)
    substitute_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', lazy=True, foreign_keys=[product_id])
    substitute = relationship('Product', lazy=True,
                              foreign_keys=[substitute_id])

    def __repr__(self):
        """ Reprensation of values

        Returns:
            TYPE: Description
        """
        return '<Substitute : {}>'.format(self.id)


class Brand(Base):

    """ Table Brand

    Attributes:
        id (INT): Identifiant
        label (STR): detail of label ("bio, veagn....")
        name (STR): nname of brand
    """

    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    label = Column(String)

    def __repr__(self):
        """Representation of values

        Returns:
            TYPE: <Brand = name >
        """
        return "<Brand(name='%s', label='%s')>" % (self.name,
                                                   self.label)


class Category(Base):

    """Table Category

    Attributes:
        id (int): Identifiant
        name (str): name of category
    """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        """Representation of values

        Returns:
            TYPE: <Category = name >
        """
        return "<Category(name='%s')>" % (self.name)


class Store(Base):

    """Table Store

    Attributes:
        id (INT): Identifiant
        name (STR): name of store
    """

    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        """Representation of values

        Returns:
            TYPE: <Store = name >
        """
        return "<Store(name='%s'))>" % (self.name)
