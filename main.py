"""
Project Name: Watchlist
Description: Monitors your browser and creates a List of all the shows you watched
Author: Philipp Schwind
Creation Date: 15.11.23
"""

import server
from db_connection import Database

if __name__ == '__main__':

    #db = Database()
    #db.create_tables()
    #db.disconnect()

    server.app.run()

