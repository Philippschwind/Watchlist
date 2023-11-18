"""
Project Name: Watchlist
Description: Monitors your browser and creates a List of all the shows you watched
Author: Philipp Schwind
Creation Date: 15.11.23
"""
import server
from Show import Show
from Episode import Episode
from db_connection import Database

if __name__ == '__main__':
    server.app.run(debug=True)
