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


@app.route('/formDelete', methods=["GET"])
def doFormAdd():
    return render_template('formDelete.html')


@app.route('/deletePerson', methods=["POST"])
def doDeletePerson() :
    id = request.form["valId"]

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT max(id) from PERSON")

    max_ID = cursor.fetchall()[0][0]
    new_ID = max_ID + 1

    cursor.execute("DELETE FROM person where id="+id)

    conn.commit()
    cursor.close()
    
    return redirect('formDelete')

@app.route('/updatePerson', methods=["POST"])
def doUpdatePerson() :
    id = request.form["valId"]
    nom = request.form["valNom"]
    prenom = request.form["valPrenom"]
    points = request.form["valPoints"]

    conn = mysql.connect()
    cursor = conn.cursor()

    # cursor.execute("UPDATE  person set "  + 
    #         "nom= '"+nom+"'" + 
    #         ",prenom= '"+prenom+"'" + 
    #         ",points= '"+points+"'" + 
    #         ",where id= "+id)

    # cursor.execute("UPDATE  person set nom= 'changed' , prenom= 'changed' , points= 11 where id= 1")
    cursor.execute("UPDATE  person set nom='" +nom+ "' , prenom='" +prenom+ "', points='" +points+ "'where id=" +id)



    conn.commit()
    cursor.close()
    
    return redirect('formAdd')

if __name__ == "__main__":
	app.run(debug=True, port=5000) 