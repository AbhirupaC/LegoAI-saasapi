from core.db.psql import Pool
import sqlite3

scripts = []
sqldb = None

def get_sqlite():
    if sqldb == None:
        sqldb  = sqlite3.connect("test.db")
    return sqldb





def prepare_table_script(table_res):
        # scripts = []
    global scripts
    for _table in table_res:
        table_name = _table["table_name"]
        table_description = _table["table_description"]

        # script 1: create table {table_name}()
        create_table_script = f"CREATE TABLE {table_name}()"
        scripts.append(create_table_script)

        # script 2: create comment on table  {table_name} is {table_description}
        
        comment_table_script = f"COMMENT ON TABLE {table_name} IS {table_description}"
        scripts.append(comment_table_script)


       
    
def prepare_col_script(col_res):
    global scripts

    for _col in col_res:
        table_description = _col["table_name"]
        col_name = _col["column_name"]
        data_type = _col["dt"]
        is_null = "NULL" if _col["isNull"] else "NOT NULL"
        is_pk = "PRIMARY KEY" if _col["pk"] == 1 else ""
        business_glossary = _col["bg"]

        # script 1: alter table {table_name} add column {col_name} {dt} {nul/notnull} {! pk}
        add_column_script = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {data_type} {is_null} {is_pk};"
        scripts.append(add_column_script)

        # script 2: create comment on column  {table_name}.{column_name} is {business_glossary}
        comment_column_script = f"COMMENT ON COLUMN {table_name}.{col_name} IS '{business_glossary}';"
        scripts.append(comment_column_script)





def prepare_fk_script(fk_res):
    for _fk in fk_res:
        ...





def write_to_db(scripts):
    db = get_sqlite()
    for _script in scripts:
        db.execute(_script)
    db.close()



scripts = [
    "id int  not null Primary key",
    "name  varchar(255) not null"
]
create table test(
    id int  not null Primary key,
    name  varchar(255) not null
)


table_res = Pool.fetch("select distinct table_name, table_description from bg_output_0")
prepare_table_script(table_res["data"])


col_res = Pool.fetch("select  table_name, column_name, bg, dt, pk, isNull  from bg_output_0")
prepare_col_script(col_res["data"])


print(scripts)
exit()


fk_res = Pool.fetch("select  table_name, column_name, joining_col_name  from bg_output_0 where fk = 1")
prepare_fk_script(fk_res["data"])


write_to_db(scripts)    

