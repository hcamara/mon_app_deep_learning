from flask import Flask, render_template, request
import face_recognition
import os

# Creation de l'application web Flask
app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/', methods=['GET','POST'])
def index():
    return 'API Face Recognition'

# Compare deux images (interfaces)
@app.route('/compare', methods=['GET','POST'])
def compare():
    return render_template('compare.html')


# Prediction de l'image 2 par rapport à l'image 1
@app.route('/predict', methods=['GET','POST'])
def predict():

    # Suppression de l'ancienne image
    if os.path.exists('image1.jpeg'):
        os.remove('image1.jpeg')

    image1 = request.files['image1']
    image1.save('image1.jpeg')


    # Suppression de l'ancienne image
    if os.path.exists('image2.jpeg'):
        os.remove('image2.jpeg')

    image1 = request.files['image2']
    image1.save('image2.jpeg')


    known_image = face_recognition.load_image_file('image1.jpeg')
    unknown_image = face_recognition.load_image_file('image2.jpeg')

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    return str(results)

# Lancement de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
