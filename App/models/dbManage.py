"""
Models: Operacions amb la base de dades
"""

import psycopg2, os

database = os.environ.get("POSTGRES_DB")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")


class PostgresSql:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="db", port=5432, database=database, user=user, password=password
        )

        self.cursor = self.connection.cursor()

    def create(self, data):
        sql = """
        INSERT INTO test (ip_address, user_agent, accept_languages, resolution, ppi, local_time)
        VALUES (%(ip_address)s, %(user_agent)s, %(accept_languages)s, %(resolution)s, %(ppi)s, %(local_time)s)
        """
        self.cursor.execute(sql, data)
        self.connection.commit()
