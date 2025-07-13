import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    dbname = "mealplanner",
    user="eng",
    host="localhost",
    port="5432"
)

@app.route("/")
def home():
    return "Meal Planner API is running!"

@app.route("/preferences", methods=["POST"])
def save_preferences():
    data = request.get_json()
    diet = data.get("diet")
    restrictions = data.get("restrictions")
    plan_length = data.get("plan_length")

    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            """
            INSERT INTO preferences (diet, restrictions, plan_length)
            VALUES (%s, %s, %s)
            RETURNING *;
            """,
            (diet, restrictions, plan_length)
        )
        conn.commit()
        new_pref = cur.fetchone()
    
    return jsonify(new_pref)

@app.route("/testpost", methods=["POST"])
def test_post():
    return {"message": "POST received"}, 200

if __name__ == "__main__":
    app.run(debug=True)