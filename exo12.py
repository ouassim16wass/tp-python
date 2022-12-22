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

@app.route('/formAdd', methods=["GET"])
def doFormAdd():
    return render_template('formAdd.html')

@app.route('/formUpdate', methods=["GET"])
def doFormUpdate():
    return render_template('formUpdate.html')


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

    # cursor.execute("INSERT INTO person" 'VALUES ('+str(new_ID)+', "'+nom+'", "'+prenom+'", '+points+')')
    cursor.execute("INSERT INTO person VALUES (" +str(new_ID)+ ",'" +nom+ "', '" +prenom+ "' , '" +points+ "') ")


    conn.commit()
    cursor.close()
    
    return redirect('formAdd')



if __name__ == "__main__":
	app.run(debug=True, port=5000) 