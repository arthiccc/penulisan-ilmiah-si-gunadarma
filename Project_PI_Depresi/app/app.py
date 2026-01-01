from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model and vectorizer
MODEL_PATH = 'model_assets/sentiment_model.pkl'
VECTORIZER_PATH = 'model_assets/vectorizer.pkl'

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    model = None
    vectorizer = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model not loaded properly.'}), 500
    
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided.'}), 400
    
    # Vectorize and Predict
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    
    # 0: Normal, 1: Indikasi Depresi
    result = "Indikasi Depresi" if prediction == 1 else "Normal"
    color = "danger" if prediction == 1 else "success"
    
    return jsonify({
        'result': result,
        'color': color,
        'original_text': text
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
