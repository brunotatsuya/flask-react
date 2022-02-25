from flask import jsonify

def init(app):

    @app.route('/api/route1', methods=['GET'])
    def route1():
        return jsonify({"message": 'You have accessed a protected route.', "status": 200}), 200