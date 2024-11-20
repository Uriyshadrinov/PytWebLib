from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'books.db'

# Инициализация базы данных
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            pages INTEGER NOT NULL
                        )''')

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# API: Получение всех книг
@app.route('/api/books', methods=['GET'])
def get_books():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
    return jsonify(books)

# API: Добавление книги
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, pages) VALUES (?, ?, ?)",
                       (data['title'], data['author'], data['pages']))
        conn.commit()
    return jsonify({"message": "Book added!"}), 201

# API: Удаление книги
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
    return jsonify({"message": "Book deleted!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
