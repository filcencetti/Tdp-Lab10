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
        query = """SELECT *
                   FROM country"""
        cursor.execute(query,)

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountries(year):
        conn = DBConnect.get_connection()

        result = []
        edges = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct c.state1ab as AB1, c.state2ab as AB2, c.state1no as Code1, c.state2no as Code2, c2.StateNme as Name1, c3.StateNme as Name2
                FROM contiguity c
                left join country c2 on state1no = c2.CCode
                left join country c3 on state2no = c3.CCode
                where year < %s"""
        cursor.execute(query,(int(year),))

        for row in cursor:
            result.append(Country(row["AB1"],row["Code1"],row["Name1"]))
            edges.append((Country(row["AB1"],row["Code1"],row["Name1"]),Country(row["AB2"],row["Code2"],row["Name2"])))


        cursor.close()
        conn.close()
        return list(set(result)), edges