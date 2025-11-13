# app.py
"""
Flask backend for Book Finder with modal Add-Book UI.
Run: python app.py
"""

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change for production

# SQLite DB in project folder
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "books.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -------------------------
# DATABASE MODEL
# -------------------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    publisher = db.Column(db.String(200), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    shelf = db.Column(db.String(50), nullable=True)
    copies = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "isbn": self.isbn,
            "name": self.name,
            "author": self.author,
            "publisher": self.publisher,
            "year": self.year,
            "genre": self.genre,
            "shelf": self.shelf,
            "copies": self.copies,
        }

# -------------------------
# ROUTES
# -------------------------
@app.route("/", methods=["GET"])
def home():
    q = request.args.get("search", "").strip()
    books = []
    if q:
        like = f"%{q}%"
        books = Book.query.filter(
            db.or_(
                Book.name.ilike(like),
                Book.author.ilike(like),
                Book.isbn.ilike(like)
            )
        ).order_by(Book.name).all()

    return render_template("index.html", books=books, query=q)


@app.route("/add", methods=["POST"])
def add_book():
    isbn = request.form.get("isbn", "").strip() or None
    name = request.form.get("name", "").strip()
    author = request.form.get("author", "").strip()
    publisher = request.form.get("publisher", "").strip() or None
    year = request.form.get("year", "").strip()
    genre = request.form.get("genre", "").strip() or None
    shelf = request.form.get("shelf", "").strip() or None
    copies = request.form.get("copies", "").strip()

    if not name or not author:
        flash("Please provide at least Book Name and Author.", "danger")
        return redirect(url_for("home"))

    try:
        year_i = int(year) if year else None
    except ValueError:
        year_i = None

    try:
        copies_i = int(copies) if copies else None
    except ValueError:
        copies_i = None

    new = Book(
        isbn=isbn,
        name=name,
        author=author,
        publisher=publisher,
        year=year_i,
        genre=genre,
        shelf=shelf,
        copies=copies_i,
    )

    db.session.add(new)
    db.session.commit()

    flash(f'Book "{name}" added.', "success")
    return redirect(url_for("home", search=name))


@app.route("/api/books")
def api_books():
    q = request.args.get("search", "").strip()
    if not q:
        return {"books": []}

    like = f"%{q}%"
    books = Book.query.filter(
        db.or_(
            Book.name.ilike(like),
            Book.author.ilike(like),
            Book.isbn.ilike(like)
        )
    ).all()

    return {"books": [b.to_dict() for b in books]}

# -------------------------
# STARTUP: create tables if they don't exist
# -------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
