from flask import Flask, jsonify, request, render_template
import csv

app = Flask(__name__)

def load_food_data() -> dict:
    """
    Load food data from a CSV file.

    Returns:
        dict: A dictionary of food data.
    """
    food_data = {}
    with open('test.csv', mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            food_name = row['Food (100g)']
            food_data[food_name] = {
                "Calories (kCal)": float(row['Calories (kCal)']),
                "Carbohydrates (g)": float(row['Carbohydrates (g)']),
                "Fiber (g)": float(row['Fiber (g)']),
                "Net Carbs (g)": float(row['Net Carbs (g)']),
                "Fats (g)": float(row['Fats (g)']),
                "Protein (g)": float(row['Protein (g)']),
                "food_name": food_name
            }
    return food_data

food_data = load_food_data()

@app.route('/', methods=['GET'])
def welcome_page():
    return render_template('index.html')

@app.route('/get_nutrition', methods=['GET'])
def get_nutrition():
    """
    Get nutritional information for a list of food items.

    Returns:
        list: A list of dictionaries containing nutritional information for each food item.
    """
    data = request.args.getlist('food')

    if not data:
        return jsonify({'error': 'Invalid request, please provide a list of food names'}), 422

    result = []
    for food_name in data:
        if food_name in food_data:
            result.append(food_data[food_name])
        else:
            result.append({'error': f'Nutritional information not found for {food_name}'})

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)