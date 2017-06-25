"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

    # It is a class object.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

    # An association table represents a connection between two other tables. 
    # It's a tool to create relationships between the other two tables. 
    # It manages a many to many relationship. 




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id=='ram').one()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = db.session.query(Model).filter(Model.name=='Corvette', Brand.brand_id=='che').all()
    or Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None)|(Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(db.not_(Model.brand_id.in_('for'))).all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_list = Model.query.filter(Model.year == year).all()

    for model in model_list

        print model.name, model.brand.name, model.brand.headquarters

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    db.session.query(Brand.name, Model.name, Model.year).join(Model).group_by(Brand.name)
    # The query above worked but returned the Query itself, which I wasn't able
    # to print correctly. 

    # I tried numerous queries, but failed on having the group_by work and print
    # information correctly. 
    # This was the closest that I got, but it still prints the brand numerous time. 

    brands = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()

    for name, model_name, model_year in brands:
        print name, model_name, model_year

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brands = Brand.query.filter(Brand.name.like(%mystr%)).all()

        print brands

    # to iterate through the list and print each item on its own line:
    # for brand in brands:
    #     print brand

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter((Model.year >= start_year) & (Model.year <= end_year)).all()

    # to iterate through the list and print each item on its own line:
    # for model in models:
    #     print model



