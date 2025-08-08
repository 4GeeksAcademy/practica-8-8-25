from flask import Flask
from flask_cors import CORS
from Routes.animal_routes import animal_bp


app = Flask(__name__)
app.register_blueprint(animal_bp)

CORS(app)








if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0', port= 5000)