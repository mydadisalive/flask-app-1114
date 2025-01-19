from flask import Flask, render_template
import os
import random
import mysql.connector

# Create Flask app
app = Flask(__name__)

# Function to connect to MySQL database
def get_db_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),  # Default to "mysql" for Kubernetes service
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "rootpassword"),
            database=os.getenv("DB_NAME", "catgifs")
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route("/")
def index():
    url = None  # Default value in case of failure
    gifs = []
    
    # Connect to the database and fetch GIF URLs
    db = get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT url FROM gifs")  # Fetch URLs from database
            gifs = [row[0] for row in cursor.fetchall()]
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        finally:
            cursor.close()
            db.close()

    # Choose a random GIF from the database if available
    if gifs:
        url = random.choice(gifs)
    
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
