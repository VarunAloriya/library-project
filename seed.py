from app import db, Book
from app import app

with app.app_context():

    # OPTIONAL: Clear old data first
    # db.session.query(Book).delete()

    sample_books = [

        # -------------------- ORIGINAL 10 YOU ADDED --------------------
        Book(isbn="9780743273565", name="The Great Gatsby", author="F. Scott Fitzgerald",
             publisher="Scribner", year=1925, genre="Novel", shelf="A1", copies=5),

        Book(isbn="9780061120084", name="To Kill a Mockingbird", author="Harper Lee",
             publisher="J.B. Lippincott & Co.", year=1960, genre="Fiction", shelf="A2", copies=4),

        Book(isbn="9780451524935", name="1984", author="George Orwell",
             publisher="Secker & Warburg", year=1949, genre="Dystopian", shelf="A3", copies=6),

        Book(isbn="9780141439518", name="Pride and Prejudice", author="Jane Austen",
             publisher="T. Egerton", year=1813, genre="Romance", shelf="A4", copies=3),

        Book(isbn="9780345339682", name="The Hobbit", author="J.R.R. Tolkien",
             publisher="George Allen & Unwin", year=1937, genre="Fantasy", shelf="A5", copies=7),

        Book(isbn="9780316769488", name="The Catcher in the Rye", author="J.D. Salinger",
             publisher="Little, Brown and Company", year=1951, genre="Fiction", shelf="B1", copies=4),

        Book(isbn="9780061122415", name="The Alchemist", author="Paulo Coelho",
             publisher="HarperTorch", year=1988, genre="Adventure", shelf="B2", copies=8),

        Book(isbn="9780385504201", name="The Da Vinci Code", author="Dan Brown",
             publisher="Doubleday", year=2003, genre="Thriller", shelf="B3", copies=5),

        Book(isbn="9780747532699", name="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling",
             publisher="Bloomsbury", year=1997, genre="Fantasy", shelf="B4", copies=1),

        Book(isbn="9780618640157", name="The Lord of the Rings", author="J.R.R. Tolkien",
             publisher="George Allen & Unwin", year=1954, genre="Fantasy", shelf="B5", copies=7),


        # -------------------- NEW 50 BOOKS --------------------
        # -------- Programming --------
        Book(isbn="9780132350884", name="Clean Code", author="Robert C. Martin",
             publisher="Prentice Hall", year=2008, genre="Programming",
             shelf="C1", copies=4),

        Book(isbn="9780137081073", name="Clean Architecture", author="Robert C. Martin",
             publisher="Pearson", year=2017, genre="Programming",
             shelf="C2", copies=3),

        Book(isbn="9781491950296", name="Fluent Python", author="Luciano Ramalho",
             publisher="O'Reilly Media", year=2015, genre="Programming",
             shelf="C3", copies=6),

        Book(isbn="9780131103627", name="The C Programming Language", author="Kernighan & Ritchie",
             publisher="Prentice Hall", year=1988, genre="Programming",
             shelf="C4", copies=5),

        Book(isbn="9780201633610", name="Design Patterns", author="Erich Gamma",
             publisher="Addison-Wesley", year=1994, genre="Programming",
             shelf="C5", copies=2),

        Book(isbn="9781617296086", name="Grokking Algorithms", author="Aditya Bhargava",
             publisher="Manning", year=2016, genre="Programming",
             shelf="C6", copies=7),

        Book(isbn="9780134494166", name="Effective Java", author="Joshua Bloch",
             publisher="Addison-Wesley", year=2018, genre="Programming",
             shelf="C7", copies=3),

        Book(isbn="9781492078005", name="Python Crash Course", author="Eric Matthes",
             publisher="No Starch Press", year=2019, genre="Programming",
             shelf="C8", copies=8),

        Book(isbn="9781449355739", name="Learning Python", author="Mark Lutz",
             publisher="O'Reilly Media", year=2013, genre="Programming",
             shelf="C9", copies=4),

        Book(isbn="9780262033848", name="Introduction to Algorithms", author="CLRS",
             publisher="MIT Press", year=2009, genre="Algorithms",
             shelf="C10", copies=5),

        # -------- Science --------
        Book(isbn="9780553380163", name="A Brief History of Time", author="Stephen Hawking",
             publisher="Bantam Books", year=1988, genre="Science",
             shelf="D1", copies=6),

        Book(isbn="9780385537858", name="Astrophysics for People in a Hurry", author="Neil deGrasse Tyson",
             publisher="W. W. Norton", year=2017, genre="Science",
             shelf="D2", copies=4),

        Book(isbn="9780525532172", name="The Order of Time", author="Carlo Rovelli",
             publisher="Riverhead Books", year=2018, genre="Physics",
             shelf="D3", copies=2),

        Book(isbn="9780231173370", name="The Big Picture", author="Sean Carroll",
             publisher="Dutton", year=2016, genre="Science",
             shelf="D4", copies=3),

        Book(isbn="9780553385465", name="The Universe in a Nutshell", author="Stephen Hawking",
             publisher="Bantam", year=2001, genre="Cosmology",
             shelf="D5", copies=5),

        Book(isbn="9780446677455", name="The Elegant Universe", author="Brian Greene",
             publisher="W.W. Norton", year=1999, genre="Physics",
             shelf="D6", copies=4),

        Book(isbn="9780385539432", name="Space Chronicles", author="Neil deGrasse Tyson",
             publisher="W. W. Norton", year=2012, genre="Science",
             shelf="D7", copies=3),

        # -------- Fiction --------
        Book(isbn="9780747532743", name="Harry Potter and the Philosopher's Stone", author="J.K. Rowling",
             publisher="Bloomsbury", year=1997, genre="Fantasy",
             shelf="E1", copies=10),

        Book(isbn="9780553573404", name="A Game of Thrones", author="George R.R. Martin",
             publisher="Bantam", year=1996, genre="Fantasy",
             shelf="E2", copies=4),

        Book(isbn="9780261103573", name="The Hobbit", author="J.R.R. Tolkien",
             publisher="HarperCollins", year=1937, genre="Fantasy",
             shelf="E3", copies=6),

        Book(isbn="9780618640157", name="The Lord of the Rings", author="J.R.R. Tolkien",
             publisher="Houghton Mifflin", year=1954, genre="Fantasy",
             shelf="E4", copies=7),

        Book(isbn="9780307277671", name="The Road", author="Cormac McCarthy",
             publisher="Vintage", year=2006, genre="Fiction",
             shelf="E5", copies=3),

        Book(isbn="9780141439518", name="Pride and Prejudice", author="Jane Austen",
             publisher="Penguin Classics", year=1813, genre="Romance",
             shelf="E6", copies=4),

        Book(isbn="9780525512174", name="The Alchemist", author="Paulo Coelho",
             publisher="HarperOne", year=1988, genre="Fiction",
             shelf="E7", copies=8),

        Book(isbn="9780307949486", name="The Fault in Our Stars", author="John Green",
             publisher="Dutton Books", year=2012, genre="Romance",
             shelf="E8", copies=5),

        # -------- Technology / AI --------
        Book(isbn="9780137903955", name="AI: A Modern Approach", author="Stuart Russell",
             publisher="Pearson", year=2021, genre="Technology",
             shelf="T1", copies=3),

        Book(isbn="9781492045526", name="Hands-On Machine Learning", author="Aurélien Géron",
             publisher="O'Reilly", year=2019, genre="AI",
             shelf="T2", copies=7),

        Book(isbn="9781617294501", name="Deep Learning with Python", author="François Chollet",
             publisher="Manning", year=2021, genre="AI",
             shelf="T3", copies=4),

        Book(isbn="9781492032649", name="Data Science from Scratch", author="Joel Grus",
             publisher="O'Reilly", year=2019, genre="Data Science",
             shelf="T4", copies=6),

        Book(isbn="9781098115784", name="Designing Data-Intensive Applications", author="Martin Kleppmann",
             publisher="O'Reilly", year=2017, genre="Technology",
             shelf="T5", copies=5),

        Book(isbn="9781617293504", name="Grokking Deep Learning", author="Andrew Trask",
             publisher="Manning", year=2019, genre="AI",
             shelf="T6", copies=2),

        # -------- History --------
        Book(isbn="9780679720201", name="The History of the Ancient World", author="Susan Wise Bauer",
             publisher="W.W. Norton", year=2007, genre="History",
             shelf="H1", copies=3),

        Book(isbn="9780307887863", name="Sapiens", author="Yuval Noah Harari",
             publisher="Harper", year=2011, genre="History",
             shelf="H2", copies=6),

        Book(isbn="9780525555379", name="Homo Deus", author="Yuval Noah Harari",
             publisher="Harper", year=2016, genre="History",
             shelf="H3", copies=5),

        Book(isbn="9780307278449", name="Guns, Germs, and Steel", author="Jared Diamond",
             publisher="W.W. Norton", year=1997, genre="History",
             shelf="H4", copies=4),

        Book(isbn="9780143127741", name="The Silk Roads", author="Peter Frankopan",
             publisher="Vintage", year=2015, genre="History",
             shelf="H5", copies=3),

        # -------- Self Help --------
        Book(isbn="9780349413686", name="Subtle Art of Not Giving a F*ck", author="Mark Manson",
             publisher="Harper", year=2016, genre="Self-help",
             shelf="S1", copies=10),

        Book(isbn="9781982137274", name="Atomic Habits", author="James Clear",
             publisher="Avery", year=2018, genre="Self-help",
             shelf="S2", copies=7),

        Book(isbn="9780345816022", name="12 Rules for Life", author="Jordan B. Peterson",
             publisher="Random House", year=2018, genre="Self-help",
             shelf="S3", copies=5),

        Book(isbn="9780307465351", name="The Power of Habit", author="Charles Duhigg",
             publisher="Random House", year=2012, genre="Self-help",
             shelf="S4", copies=4),

        Book(isbn="9780062457714", name="Deep Work", author="Cal Newport",
             publisher="Grand Central", year=2016, genre="Self-help",
             shelf="S5", copies=6),

        # -------- Philosophy --------
        Book(isbn="9780140449334", name="Meditations", author="Marcus Aurelius",
             publisher="Penguin Classics", year=180, genre="Philosophy",
             shelf="P1", copies=7),

        Book(isbn="9780140442106", name="Republic", author="Plato",
             publisher="Penguin Classics", year=-380, genre="Philosophy",
             shelf="P2", copies=3),

        Book(isbn="9780140449273", name="Beyond Good and Evil", author="Friedrich Nietzsche",
             publisher="Vintage", year=1886, genre="Philosophy",
             shelf="P3", copies=4),

        Book(isbn="9780143038412", name="Man's Search for Meaning", author="Viktor E. Frankl",
             publisher="Beacon Press", year=1946, genre="Philosophy",
             shelf="P4", copies=8),
    ]

    db.session.bulk_save_objects(sample_books)
    db.session.commit()

    print("✔ All 60 sample books added successfully!")
