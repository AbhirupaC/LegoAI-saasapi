import psycopg2
from ..logger import log

class Pool:
    r = None
    max_retries = 3 
    @classmethod
    def __attemptConnection__(cls, refresh = False):
        
        from core.conf import APP_CONFIG
        # print(APP_CONFIG["PSQL_HOST"], APP_CONFIG["PSQL_USER"], APP_CONFIG["PSQL_PWD"])
        if cls.r !=None:
            try:
                if cls.r.poll() == 0:
                    return
            except psycopg2.InterfaceError as ie:
                log.error("The existing connection is closed")
        try:
            log.info("initializing psql connection")
            conn = psycopg2.connect(
                database=APP_CONFIG["PSQL_DB"], 
                host=APP_CONFIG["PSQL_HOST"], 
                user=APP_CONFIG["PSQL_USER"], 
                password=APP_CONFIG["PSQL_PWD"], 
                port=5432
            )
            # psycopg2.extra.RealDictCursor
            cls.r = conn
            # import psycopg2
            # from psycopg2.pool import ThreadedConnectionPool
            # con = ThreadedConnectionPool(2, 4, 
            # 	database="postgres", 
            # 	host="localhost", 
            # 	user="postgres", 
            # 	password="pwd", 
            # 	port=5432 
            # )

            log.info("psql connection established")
        except Exception as e:
            cls.r = None
            log.error("Failed to establish connection to psql")
            raise(e)
        

    @classmethod
    def getConnection(cls):
        counter = 0
        while counter <  cls.max_retries:
            
            try:
                cls.__attemptConnection__()
                break
            except Exception as e:
                log.error(e)
                log.warning("retrying to connect to psql: ", counter)
                counter = counter + 1
            continue
        return cls.r

    @classmethod
    def getCursor(cls):
        con = cls.getConnection()
        from psycopg2.extras import RealDictCursor
        try:
            log.info("creating cursor")
            return con.cursor(cursor_factory = RealDictCursor)
        except AttributeError as ae:
            log.error("Cannot establish connection to psql")
            raise(ae)

    
    
    @classmethod
    def fetch(cls, query="", params = (), silent = True):
        try:
            cursor = cls.getCursor()
        except AttributeError as ae:
            log.error("Failed to instantiate cursor for psql connection")
            if silent:
                return {
                    "data":[],
                    "status":"FAILED",
                    "msg":"Cannot fetch data."
                }
            raise ae
        res = []
        try:
            cursor.execute(query, params)
            return {
                    "data":cursor.fetchall(),
                    "status":"SUCCESS",
                    "msg":None
                } 
        
        except psycopg2.errors.SyntaxError as _se:
            log.error("Wrong query supplied:", query)
            cursor.connection.rollback()
            raise _se
        except Exception as e:
            cursor.connection.rollback()
            raise e
        finally:
            cls.closeCursor(cursor)
            # cls.r.close()

    @classmethod
    def execute(cls, query="", params = (), silent = True, returning = None):
        try:
            cursor = cls.getCursor()
        except AttributeError as ae:
            log.error("Failed to instantiate cursor for psql connection")
            if silent:
                return {
                    "data":[],
                    "status":"FAILED",
                    "msg":"Cannot fetch data."
                }
            raise ae
        res = []
        if returning is not None:
            query = "{} returning {}".format(query, returning)
            
        try:
            cursor.execute(query, params)
            cursor.connection.commit()
            if returning is not None:
                res = cursor.fetchall()    
            return {
                    "data":res,
                    "status":"SUCCESS",
                    "msg":None
                } 
        
        except psycopg2.errors.SyntaxError as _se:
            log.error("Wrong query supplied:", query)
            cursor.connection.rollback()
            raise _se
        except Exception as e:
            cursor.connection.rollback()
            raise e
        finally:
            cls.closeCursor(cursor)
            # cls.r.close()

    @classmethod
    def closeCursor(cls, cursor) -> None:
        log.info("closing cursor")
        cursor.close()
        # cursor.connection.close()


    @classmethod
    def releaseConnection(cls, conn) -> None:
        conn.close()
