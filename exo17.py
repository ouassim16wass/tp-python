from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()



app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass_root'
app.config['MYSQL_DATABASE_DB'] = 'db_persons'


mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id,nom,prenom,points from person")

    data = cursor.fetchall()
    cursor.close()

    return render_template('index.html',data = data)




@app.route('/addPerson', methods=["POST"])
def doAddPerson() :
    nom = request.form["valNom"]
    prenom = request.form["valPrenom"]
    points = request.form["valPoints"]
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT max(id) from PERSON")

    max_ID = cursor.fetchall()[0][0]
    new_ID = max_ID + 1

    cursor.execute("INSERT INTO person VALUES (" +str(new_ID)+ ",'" +nom+ "',' " +prenom+ "','" +points+ "' ) ")


    conn.commit()
    cursor.close()
    
    return redirect('/')

if __name__ == "__main__":
	app.run(debug=True, port=5000) 