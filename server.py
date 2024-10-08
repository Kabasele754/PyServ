import cgi
import sqlite3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os


class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        root = os.path.join(os.getcwd(), "templates")
        if path == "/" or path == "/index.html":
            return os.path.join(root, "index.html")
        elif path == "/about":
            return os.path.join(root, "about.html")
        elif path == "/contact":
            return os.path.join(root, "contact.html")
        elif path.startswith("/static"):
            root = os.path.join(os.getcwd(), "static")
            path = path[len("/static"):]
        return os.path.join(root, path.lstrip('/'))


    def do_POST(self):
        if self.path == '/submit_contact':
            # Utiliser cgi.FieldStorage pour parser les données multipart/form-data
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })

            # Extraire les données du formulaire
            name = form.getvalue('name', '')
            email = form.getvalue('email', '')
            message = form.getvalue('message', '')

            print("Données reçues:")
            print(f"Nom: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")

            # Enregistrer dans la base de données SQLite
            conn = sqlite3.connect('contact.db')
            cursor = conn.cursor()

            # Créer la table si elle n'existe pas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT, 
                email TEXT, 
                message TEXT)
            ''')

            # Insérer les données
            cursor.execute('''
                INSERT INTO contacts (name, email, message) 
                VALUES (?, ?, ?)
            ''', (name, email, message))

            conn.commit()
            conn.close()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Message enregistré avec succès dans la base de données".encode('utf-8'))
        else:
            super().do_POST()


def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('localhost', 8080)
    httpd = server_class(server_address, handler_class)
    print("Serveur démarré sur http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()