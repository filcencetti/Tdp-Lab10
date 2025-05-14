from database.DB_connect import DBConnect
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries(year):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct CCode, StateAbb, StateNme 
                    FROM contiguity c
                    LEFT JOIN country c2 ON state1no = c2.CCode
                    WHERE year < %s"""
        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getBorders(year):
        conn = DBConnect.get_connection()

        edges = []

        query = """SELECT distinct c.state1ab as AB1, c.state2ab as AB2, c.state1no as Code1, c.state2no as Code2, c2.StateNme as Name1, c3.StateNme as Name2
                FROM contiguity c
                left join country c2 on state1no = c2.CCode
                left join country c3 on state2no = c3.CCode
                where year < %s and c.conttype = 1 """

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query,(int(year),))

        for row in cursor:
            edges.append((Country(row["AB1"],row["Code1"],row["Name1"]),Country(row["AB2"],row["Code2"],row["Name2"])))


        cursor.close()
        conn.close()
        return edges