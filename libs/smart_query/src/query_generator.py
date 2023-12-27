from .transformation import Transformations
from .operators import Operators


class QueryGenerator():

    @classmethod
    def get_select_fields(cls, selectFields):
        # Extracting Select Columns 
        selectedFields = []

        if len(selectFields) == 0:
            selectedFieldsExpr = " * "
        else:
            for field in selectFields:  
                
                if field["isFunction"] == "True":
            #         func = functions[field["function"][0]["funName"]]
                    func = getattr(Transformations, field["function"][0]["funName"])
                    expr = func(**field["function"][0]["params"])
                else:
                    expr = field["datasetName"] + "." + field["fieldName"]
                if field["renameCol"] == "True":
                    expr = expr + " as " + field["renameColName"]
                
                selectedFields.append(expr)
            selectedFieldsExpr = ",".join(selectedFields)

        return selectedFieldsExpr

    @classmethod
    def get_join_expr(cls, joinFields, fromTable):
        # Join Expression
        join_query = ""
        if joinFields != {}:
            tbl_cnt = len(joinFields)
            for i in range(0,tbl_cnt):
                if i==0:
                    if joinFields[str(i)]["table_name"] != fromTable:
                        print("Starting with Invalid Table Name")
                        break
        #             join_query += query["join"][str(i)]["table_name"]
                else:
                    joining_cndn = " AND ".join(["`" + join_col["left_tbl"] + "`" + "." + join_col["left_column"] + " = " + "`" + join_col["right_table"] + "`" + "." + join_col["right_column"] for join_col in joinFields[str(i)]["columns"]])
                    join_query += " " + joinFields[str(i)]["join_type"].upper() + " JOIN " + joinFields[str(i)]["table_name"] + " on " + str(joining_cndn)
            
        return join_query

    @classmethod
    def get_filter_expr(cls, filterFields):
        # Filter Expression
        filterExpr = ""
        if filterFields != {}:
            filterExpr = " WHERE "
            filterCols = []
            for filterField in filterFields["fields"]:
                func = getattr(Operators, "_" + filterField["operator"])
                expr = func(filterField["datasetName"], filterField["fieldName"], **filterField["params"])
                filterCols.append(expr)
                
            filterExpr = filterExpr + " {} ".format(filterFields["condition"].upper()).join(filterCols)
            
            
        return filterExpr 
    
    @classmethod
    def get_groupby_expr(cls, groupbyFields):
        groupbyExpr = ""
        if groupbyFields != {} and len(groupbyFields["keys"]) != 0:
            groupbyCols = []
            for field in groupbyFields["keys"]:
                groupbyCols.append(field['datasetName'] + "." + field["fieldName"])

            groupbyExpr = " GROUP BY " + " , ".join(groupbyCols)
            
            if "having" in groupbyFields and len(groupbyFields["having"]) !=0:
                groupbyExpr += cls.get_filter_expr(groupbyFields["having"]).replace(" WHERE ", " HAVING ", 1)
        return groupbyExpr

    @classmethod
    def get_sort_expr(cls, sortFields):
        # Sort Expression
        sortExpr = ""
        if sortFields != {}:
            sortExpr = " ORDER BY "
            sortCols = []
            for sortField in sortFields:
                sortCol = sortField["datasetName"] + "." + sortField["field"]
                if sortField["dir"] == "asc":
                    sortOp = "ASC"
                elif sortField["dir"] == "desc":
                    sortOp = "DESC"
                else:
                    sortOp = ""
                sortCols.append(sortCol + " " + sortOp)
            sortExpr = sortExpr + " , ".join(sortCols)
        return sortExpr
        
    @classmethod
    def get_limit_expr(cls, limit):
        return " LIMIT {}".format(limit)
    
    @classmethod
    def getQuery(cls, config):
        sqlQuery = ""
        
        if sqlQuery == "" and "selectedFields" in config:
            sqlQuery += "SELECT "
            sqlQuery += cls.get_select_fields(config["selectedFields"])
        else:
            print("No Selected Fields Passed")
            return sqlQuery

        # From Table    
        if "from" in config:
            sqlQuery = sqlQuery + " FROM " + config["from"]

        if "join" in config and config["join"] != {}:
            sqlQuery += cls.get_join_expr(config["join"], config["from"])

        if "filters" in config and config["filters"] != {}:
            sqlQuery += cls.get_filter_expr(config["filters"])
        
        if "groupBy" in config and config["groupBy"] != {}:
            sqlQuery += cls.get_groupby_expr(config["groupBy"])

        if "sortField" in config and config["sortField"] != []:
            sqlQuery += cls.get_sort_expr(config["sortField"])
            
        if "limit" in config and config["limit"] != 0:
            sqlQuery += cls.get_limit_expr(config["limit"])

        return sqlQuery

