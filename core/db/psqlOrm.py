from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.conf import APP_CONFIG

class PsqlORM:
    engine = None 
    @classmethod
    def init(cls):
        if cls.engine == None:
            cls.engine = create_engine('postgresql://{}:{}@{}:5432/{}'.format(
                APP_CONFIG["PSQL_USER"],
                APP_CONFIG["PSQL_PWD"],
                APP_CONFIG["PSQL_HOST"],
                APP_CONFIG["PSQL_DB"]

            )) 
    @classmethod
    def get_engine(cls):
        return cls.engine

    @classmethod
    def get_session(cls):
        return sessionmaker(bind=cls.engine)
    
    @classmethod
    def get_Base(cls):
        return declarative_base()

    @classmethod
    def get_db(cls):
        session = cls.get_session()
        return session()


    @classmethod
    def create_all(cls):
        base = cls.get_Base()
        base.metadata.create_all(cls.engine)

base = PsqlORM.get_Base()
print(base)