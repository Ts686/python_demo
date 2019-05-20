import cx_Oracle
import traceback
import re


class oracleHandle:
    def connect(username, password, url):
        conn = cx_Oracle.connect(username, password, url)
        return conn

    def insert(connection, data, tableName):
        # connect oracle database
        # connect oracle database
        cursor = connection.cursor()
        fields = data.pop(0)
        fields_str = ",".join(fields)
        execute_sql = ""
        execute_sql += "insert into %s ( %s) values (" % (tableName, fields_str)
        count = 1
        for field in fields:
            if count < len(fields):
                if re.search("date", field, re.IGNORECASE):
                    execute_sql += ",to_date(:" + str(count) + ",'yyyy-mm-dd hh24:mi:ss')"
                elif count != 1:
                    execute_sql += ",:" + str(count)
                elif count == 1:
                    execute_sql += ":" + str(count)
            elif count == len(fields):
                execute_sql += ",:" + str(count) + ")"
            count += 1
        print(execute_sql)
        cursor.prepare(execute_sql)
        try:
            cursor.executemany(None, data)
        except Exception:
            print(traceback.print_exc())
        connection.commit()
        cursor.close()
        connection.close()
