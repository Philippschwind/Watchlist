import sqlite3
from Show import Show
from Episode import Episode
class Database:
    def __init__(self, db_name):
        self.connect(db_name)

    sqliteConnection = None
    cursor = None

    def connect(self, db_name):
        try:
            if not self.sqliteConnection:
                self.sqliteConnection = sqlite3.connect(db_name)
                self.cursor = self.sqliteConnection.cursor()
                print('DB Init')
        except sqlite3.Error as error:
            print('Error occurred - ', error)

    def disconnect(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
            print('SQLite Connection closed')

    def create_tables(self):
        if not self.sqliteConnection:
            self.connect("Watchlist.db")
        SQL_statement = ""  # Copy and paste SQL statement from SQL_Query file.
        # Every statement must be executed separately
        if SQL_statement is "":
            return

        self.cursor.execute(SQL_statement)

    def add_episode(self, ep_nr, show_title):
        show = self.query_show(show_title)
        print(show)
        if not show:
            show_id = self.add_show(show_title)
        else:
            show_id = show[0]

        if self.check_duplicates(ep_nr, show_id):
            print("Epsiode already saved")
            return

        query = """INSERT INTO Episodes (ep_nr, show_id)
                VALUES ({},{})""".format(ep_nr, show_id)

        self.cursor.execute(query)
        self.sqliteConnection.commit()
        print("Episode saved")

    def add_show(self, show_title):
        query = """INSERT INTO Shows (title)
                VALUES (\"{}\")""".format(show_title)
        self.cursor.execute(query)
        self.sqliteConnection.commit()
        print("Show saved")
        return self.cursor.lastrowid

    def query_show(self, show):
        query = "SELECT * FROM Shows WHERE title=\""+show+"\""

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if rows:
            return rows[0]

    def check_duplicates(self, ep_nr, show_id):
        query = """SELECT * FROM Episodes WHERE ep_nr={} AND show_id={}""".format(ep_nr, show_id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if rows:
            return True
        return False

    def get_all_shows(self):
        self.cursor.execute('SELECT * FROM shows')
        rows = self.cursor.fetchall()
        shows = []
        for row in rows:
            show = Show(show_id=row[0], title=row[1], ep_count=row[2], completed=False)
            shows.append(show)
        return shows

    def search_shows(self, title):
        self.cursor.execute('SELECT * FROM shows WHERE title LIKE ?', ('%' + title + '%',))
        rows = self.cursor.fetchall()
        shows = []
        for row in rows:
            show = Show(show_id=row[0], title=row[1], ep_count=row[2], completed=False)
            shows.append(show)
        return shows

    def get_show_by_id(self, show_id):
        self.cursor.execute('SELECT * FROM shows WHERE show_id = ?', (show_id,))
        rows = self.cursor.fetchall()
        shows = []
        for row in rows:
            show = Show(show_id=row[0], title=row[1], ep_count=row[2], completed=False)
            shows.append(show)
        return shows[0]

    def get_episodes_for_show(self, show):
        self.cursor.execute('SELECT * FROM episodes WHERE show_id = ?', (show.show_id,))
        rows = self.cursor.fetchall()
        episodes = []
        for row in rows:
            episode = Episode(row[2], show)
            episodes.append(episode)
        return episodes
