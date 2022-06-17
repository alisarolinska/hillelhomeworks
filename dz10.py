import sqlite3
import time
now = time.strftime('%Y-%m-%d')

connection = sqlite3.connect('test.db')
cursor = connection.cursor()


def create_table():
	query = """
	CREATE TABLE IF NOT EXISTS articles (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title varchar(12) DEFAULT 'NONE',
		created_at now,
		text VARCHAR(40) DEFAULT "None"
	)
	"""
	cursor.execute(query)
	connection.commit()

create_table()
keys = ['id', 'text', 'created_at', 'title']
cursor.execute('select * from articles order by id text')
article = cursor.fetchone()

print(article)


def create_article(text, created_at, title):
	cursor.execute(f'insert into articles (text, title) values ("{text}", "{created_at()}", "{title}")')
	connection.commit()

def delete_article(id):
	cursor.execute(f'delete from articles where id = {id}')
	connection.commit()

def update_article(id, title, text):
	cursor.execute(f'Update articles set title = {title}, text = {text} where id = {id}')
	connection.commit()

def get_article(title, text):
	cursor.execute(f'select * from articles where text = {text} or title = {title}')
	connection.commit()