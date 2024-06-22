from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='test',
            user='root',
            password='FOOD_COMP@123'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
@app.route('/', methods=['GET'])
def welcome_page():
    return "Welcome to Food comparision"

@app.route('/get_nutrition', methods=['GET'])
def get_nutrition():
    food_name = "Basil" 
    if not food_name:
        return jsonify({'error': 'No food specified'}), 400
    
    print(f"Received food name: {food_name}")
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM nutrition_info_new WHERE food = %s"
    cursor.execute(query, (food_name,))
    result = cursor.fetchone()
    
    print(f"SQL Query: {query}")
    print(f"Query Result: {result}")
    
    cursor.close()
    connection.close()
    
    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'Food not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
