from flask import Flask, render_template
import os
import psycopg2

db_config = {
    'host': 'db',
    'user': 'luxonis',
    'password': 'luxonis',
    'database': 'luxonis',
}

app = Flask(__name__)

@app.route('/')
def home():
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""
    SELECT id, title, img_url FROM sreality
    """)
    
    rows = cur.fetchall()
    listings = []
    for row in rows:
        listing = {
            'id': row[0],
            'title': row[1],
            'img_url': row[2],
        }
        listings.append(listing)
    
    # Close the database connection and return the template with the listings data
    cur.close()
    conn.close()
    return render_template('index.html', listings=listings)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))