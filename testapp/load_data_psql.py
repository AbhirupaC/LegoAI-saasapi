from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


engine = create_engine('postgresql://postgres:pwd@appdev:5432/legoai_apiservice')
Session = sessionmaker(bind=engine)

Base = declarative_base()
# from core.db.psqlOrm import Base, Session
from sqlalchemy import Column, String, Integer, Date, Boolean

class Wrangler_Transformation(Base):
    __tablename__ = 'lai_wrangler_transformations'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    expanded = Column(Boolean)
    data = Column(String)

    def __init__(self, category, expanded, data):
        self.category = category
        self.expanded = expanded
        self.data = data

class Data_Domain(Base):
    __tablename__ = "data_domain"
    domain_id = Column(Integer, primary_key=True)
    domain_name = Column(String)
    color = Column(String)
    icon = Column(String)
    invisibleNode = Column(String)
    size = Column(String)
    shape = Column(String)
    labelColor = Column(String)
    importance = Column(String)
    labelBgColor = Column(String) 
    dataQuality = Column(String)
    # data_sources = relationship("Data_Sources", back_populates="data_domain")


class Data_Sources(Base):
    __tablename__ = 'data_sources'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)
    meta = Column(String)
    # domain_id= Column(Integer)
    data_domain = Column(Integer, ForeignKey("data_domain.domain_id"))

    def __init__(self, name, data, meta, data_domain):
        self.name = name
        self.data = data
        self.meta = meta
        self.data_domain = data_domain


class Data_Columns(Base):
    __tablename__ = 'data_columns'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)
    meta = Column(String)
    data_id =  Column(Integer)
    
    def __init__(self, name, data, meta , data_id):
        self.name = name
        self.data = data
        self.meta = meta
        self.data_id = data_id



class Data_lineage(Base):
    __tablename__ = 'data_lineage'

    id = Column(Integer, primary_key=True)
    source = Column(String)
    target = Column(String)
    linkType = Column(String)
    color = Column(String)
    progress = Column(String)
    labelColor = Column(String)

    def __init__(self, source, target, linkType="Dashed", color="white", progress="0", labelColor="white"):
        self.source = source
        self.target = target
        self.linkType = linkType
        self.color = color
        self.progress = progress
        self.labelColor = labelColor

class Wrangler_Expressions(Base):
    __tablename__ = 'wrangler_expressions'
    id = Column(Integer, primary_key = True)
    category = Column(String)
    expanded = Column(Boolean)
    data = Column(String)

    def __init__(self, category, expanded, data):
        self.category = category
        self.expanded = expanded
        self.data = data



class Graph_config(Base):
    __tablename__="graph_config"
    id = Column(Integer, primary_key = True)
    category = Column(String)
    data = Column(String) 

    def __init__(self, category, data):
        self.category = category
        self.data = data



class Gov_Transformations(Base):
    __tablename__ = 'gov_transformations'
    id = Column(Integer, primary_key = True)
    recipe_id = Column(String)
    category = Column(String)
    execution_status = Column(String)
    spark_query = Column(String)
    domain = Column(String)
    nodes = Column(String)
    functions = Column(String)
    details = Column(String)
    

    def __init__(self, recipe_id, category, execution_status, spark_query, domain, nodes, functions, details):
        self.recipe_id = recipe_id
        self.category = category
        self.execution_status = execution_status
        self.spark_query = spark_query
        self.domain = domain
        self.nodes = nodes
        self.functions = functions
        self.details = details



class Gov_Useraccess(Base):
    __tablename__ = "gov_useraccess"
    id = Column(Integer, primary_key = True)
    account= Column(String)
    role = Column(String)
    marketplace_view = Column(String)
    marketplace_edit = Column(String)
    marketplace_delete = Column(String)
    ontology_filter = Column(String)
    ontology_cart = Column(String)
    wrangler_download = Column(String)
    wrangler_settings = Column(String)
    wrangler_tag = Column(String)
    cart_union = Column(String)
    cart_tune = Column(String)
    cart_lock = Column(String)
    data_upload = Column(String)
    data_delete = Column(String)


    def __init__(self, account, role, marketplace_view,   marketplace_edit,   marketplace_delete,   ontology_filter,   ontology_cart,   wrangler_download,   wrangler_settings,   wrangler_tag,   cart_union,   cart_tune,   cart_lock,   data_upload,   data_delete):
        self.account = account
        self.role = role
        self.marketplace_view = marketplace_view 
        self.marketplace_edit = marketplace_edit 
        self.marketplace_delete = marketplace_delete 
        self.ontology_filter = ontology_filter 
        self.ontology_cart = ontology_cart 
        self.wrangler_download = wrangler_download 
        self.wrangler_settings = wrangler_settings 
        self.wrangler_tag = wrangler_tag 
        self.cart_union = cart_union 
        self.cart_tune = cart_tune 
        self.cart_lock = cart_lock 
        self.data_upload = data_upload 
        self.data_delete = data_delete 



# Base.metadata.create_all(engine)



# exit()
from test_data import *
import json
db = Session()


for src in data_sources:
    row = Data_Sources(src["table_name"], src["icon"], json.dumps(src.get("meta")) , None)
    db.add(row)
    db.commit()

# # exit()
# for _key in metadata_customers_cols:
#     _row = metadata_customers_cols[_key]
#     db.add(Data_Columns(_key, "customers", json.dumps(_row), 1))
#     db.commit()

# # exit()
# with open("../data/expressions.json", 'r') as _f:
#     for _row in json.loads(_f.read()):
#         db.add(Wrangler_Expressions(_row["key"], _row["expanded"], json.dumps(_row["data"])))
#         db.commit()


# # exit()
with open("../data/canvas-data.json", 'r') as _f:
    for _row in json.loads(_f.read())["links"]:
        # db.add(Data_lineage(_row["source"], _row["target"], _row.get("linkType"), _row.get("color"), _row.get("progress"), _row.get("labelColor")  ))
        db.add(Data_lineage(_row["source"], _row["target"]) )
        db.commit()


for row in Gov_Transformations_data:
    db.add(Gov_Transformations( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7] ) )
    db.commit()



# # for row in gov_access_data:
# #     db.add(Gov_Useraccess( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14] ) )
# #     db.commit()

# # for row in graph_config_data:
# #     db.add(Graph_config(row) )