from flask import Flask, render_template, request

app = Flask(__name__)

def convert_units(weight, weight_unit, height, height_unit):
    if weight_unit == 'lbs':
        weight *= 0.453592
    if height_unit == 'in':
        height *= 0.0254
    elif height_unit == 'cm':
        height /= 100  # Convert cm to meters
    return weight, height

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def recommend_yoga_and_nutrition(bmi):
    # Your existing function
    pass

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        weight_unit = request.form['weight_unit']
        height_unit = request.form['height_unit']

        weight, height = convert_units(weight, weight_unit, height, height_unit)
        bmi = calculate_bmi(weight, height)
        status = health_status(bmi)
        yoga, nutrition = recommend_yoga_and_nutrition(bmi)

        # Debugging prints
        print(f"Weight: {weight}, Height: {height}")
        print(f"BMI: {bmi}, Status: {status}")
        print(f"Yoga: {yoga}, Nutrition: {nutrition}")

        return render_template('results.html', bmi=round(bmi, 2), status=status, yoga=yoga, nutrition=nutrition)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
