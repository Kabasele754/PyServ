import os
from http.server import SimpleHTTPRequestHandler, HTTPServer


class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Définir le chemin de base pour les fichiers HTML dans "templates"
        root = os.path.join(os.getcwd(), "templates")

        # Si la racine est demandée, renvoyer le fichier index.html
        if path == "/":
            path = "/index.html"

        # Si le chemin commence par /static, utiliser le dossier static/
        if path.startswith("/static"):
            root = os.path.join(os.getcwd(), "static")
            path = path[len("/static"):]

        # Retourner le chemin complet du fichier
        return os.path.join(root, path.lstrip('/'))


def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('localhost', 8080)
    httpd = server_class(server_address, handler_class)
    print("Serveur démarré sur http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()



