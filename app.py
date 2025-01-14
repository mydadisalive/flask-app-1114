from flask import Flask, render_template
import os
import random
import mysql.connector

# Create Flask app
app = Flask(__name__)

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"), # Use the DB_HOST variable from the docker-compose file
        user=os.getenv("DB_USER"), # Use the DB_USER variable from the docker-compose file
        password=os.getenv("DB_PASSWORD"), # Use the DB_PASSWORD variable from the docker-compose file
        database=os.getenv("DB_NAME") # Use the DB_NAME variable from the docker-compose file
    )

@app.route("/")
def index():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT url FROM gifs")
        gifs = [row[0] for row in cursor.fetchall()]
        db.close()
        url = random.choice(gifs) if gifs else None
    except Exception:
        url = None
    
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
