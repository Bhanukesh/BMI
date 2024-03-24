from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_yoga_and_nutrition(bmi):
    if bmi < 18.5:
        return "Surya Namaskar, Vrikshasana", "Increase intake of proteins and healthy fats, and consume more calories."
    elif 18.5 <= bmi < 25:
        return "Tadasana, Trikonasana", "Maintain a balanced diet with a good mix of fruits, vegetables, whole grains, and lean proteins."
    elif 25 <= bmi < 30:
        return "Bhujangasana, Dhanurasana", "Focus on a diet rich in fiber, reduce sugar intake, and increase physical activity."
    else:
        return "Balasana, Savasana", "Adopt a low-calorie diet, increase water intake, and consult a nutritionist for a personalized plan."

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        yoga, nutrition = recommend_yoga_and_nutrition(bmi)
        return render_template('results.html', bmi=bmi, yoga=yoga, nutrition=nutrition)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
