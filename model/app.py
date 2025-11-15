from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("mood_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
le = joblib.load("label_encoder.pkl")

mood_to_dishes = {
    "happy": ["Ice Cream", "Chocolate Cake", "Mango Smoothie"],
    "sad": ["Mac and Cheese", "Chicken Soup", "Chocolate Brownie"],
    "angry": ["Spicy Ramen", "Pepper Pizza", "Buffalo Wings"],
    "excited": ["Sushi", "Cupcakes", "Energy Bars"],
    "tired": ["Oatmeal", "Banana Smoothie", "Herbal Tea"],
    "stressed": ["Dark Chocolate", "Avocado Toast", "Green Tea"],
    "bored": ["Popcorn", "Nachos", "Fruit Salad"]
}

def predict_mood_and_dishes(text):
    text_vec = vectorizer.transform([text])
    encoded_mood = model.predict(text_vec)[0]
    mood = le.inverse_transform([encoded_mood])[0]
    return mood, mood_to_dishes[mood]

@app.route("/", methods=["GET"])
def home():
    return render_template("mood.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form["mood_input"]
    mood, dishes = predict_mood_and_dishes(user_input)
    return render_template("mood.html", mood=mood, dishes=dishes)

if __name__ == "__main__":
    app.run(debug=True)
