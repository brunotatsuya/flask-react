from flask import send_from_directory

def init(app):

    @app.route("/", defaults={'path':''})
    def serve(path):
        return send_from_directory(app.static_folder,'index.html')