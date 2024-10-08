import sqlite3

# Connexion à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('contact.db')
    return conn

# Créer une table pour stocker les soumissions du formulaire de contact
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ajouter une nouvelle soumission
def add_contact(name, email, message):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, email, message) 
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

# Récupérer toutes les soumissions de contact
def get_contacts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Appel initial pour créer la table si elle n'existe pas
create_table()
