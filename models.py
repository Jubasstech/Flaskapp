from your_app import mysql

class Tag:
    @staticmethod
    def get_all_tags():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tags")
        tags = cur.fetchall()
        cur.close()
        return tags

    @staticmethod
    def create_tag(name):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tags (name) VALUES (%s)", (name,))
        mysql.connection.commit()
        cur.close()

class Category:
    @staticmethod
    def get_all_categories():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM categories")
        categories = cur.fetchall()
        cur.close()
        return categories

    @staticmethod
    def create_category(name):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
        mysql.connection.commit()
        cur.close()
