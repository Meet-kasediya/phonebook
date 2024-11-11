from flask import Flask, render_template,url_for,request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/CreateContact",methods=["POST","GET"])
def CreateContact():
    if request.method == "POST":
        firstname = request.form["Firstname"]
        lastname = request.form["Lastname"]
        Email = request.form["Email"]
        No = request.form["No"]
        Address = request.form["Address"]
        organisation = request.form["Organisation"]
        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        cursor.execute('''INSERT INTO contact (contact_firstname, contact_lastname, contact_email, contact_No, contact_address, contact_organisation) values (?,?,?,?,?,?)''',(firstname,lastname,Email,No,Address,organisation))
        cursor.close()
        myconn.commit()

        return render_template("home.html",msg="Record added successfully")

    return render_template("CreateContact.html")

@app.route("/SearchContact")
def SearchContact():
    return render_template("SearchContact.html")

@app.route("/results",methods=["POST","GET"])
def results():
    if request.method == "POST":
        search_term = request.form["searchfor"]

        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        params = [f'%{search_term}%' for _ in range(6)]
        query = '''SELECT * FROM contact WHERE contact_firstname LIKE ? OR contact_lastname LIKE ? OR contact_email LIKE ? OR contact_no LIKE ? OR contact_address LIKE ? OR contact_organisation LIKE ?;'''
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return render_template("results.html",rows=rows)


@app.route("/UpdateContact",methods=["POST","GET"])
def UpdateContact():
    if request.method == "POST":
        contact_id = request.form["id"]
        index = request.form.get('replace')
        update = request.form["by"]
        columns = ['contact_firstname', 'contact_lastname', 'contact_email', 'contact_no', 'contact_address', 'contact_organisation']
        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        query = f'''UPDATE contact SET { columns[int(index)] }=? WHERE contact_id=?'''
        cursor.execute(query, (update, contact_id))  
        cursor.close()
        myconn.commit()

        return render_template("home.html",)
    return render_template("UpdateContact.html")

@app.route("/gatherID",methods=["POST","GET"])
def gatherID():
    contact_id = request.form["id"]
    return render_template("UpdateContact.html",contact_id=contact_id)

@app.route("/deleteID",methods=["POST","GET"])
def deleteID():
    contact_id = request.form["id"]
    myconn = sqlite3.connect('database.db')
    cursor = myconn.cursor()
    cursor.execute('''DELETE FROM contact WHERE contact_id = ?''',(int(contact_id),))
    cursor.close()
    myconn.commit()
    return render_template("home.html")


@app.route('/contactcategory')
def contactcategory():
    myconn = sqlite3.connect('database.db')
    cursor = myconn.cursor()

    query = '''
    SELECT c.contact_id, c.contact_firstname, c.contact_lastname, c.contact_email, 
           c.contact_no, c.contact_address, c.contact_organisation, cat.category_name
    FROM contact c
    JOIN contact_category cc ON c.contact_id = cc.contact_id
    JOIN category cat ON cc.category_id = cat.category_id
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    myconn.close()

    contacts = {}
    for row in rows:
        category_name = row[-1]
        if category_name not in contacts:
            contacts[category_name] = []
        contacts[category_name].append(row)

    return render_template('contactcategory.html', contacts=contacts)

@app.route("/addcategory",methods=["POST","GET"])
def addcategory():
    if request.method == "POST":
        category_name = request.form["categoryname"]
        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        cursor.execute('''INSERT INTO category (category_name) values (?)''',(category_name,))
        cursor.close()
        myconn.commit()

        return render_template('home.html')

    return render_template('addcategory.html')

@app.route("/gathercategory",methods=["POST","GET"])
def gathercategory():
    category_name = request.form["id"]
    return render_template("updatecategory.html",category_name=category_name)


@app.route("/updatecategory",methods=["POST","GET"])
def updatecategory():
    if request.method == "POST":
        c_name = request.form["id"]
        update = request.form["by"]
        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        cursor.execute('''UPDATE category SET category_name=? WHERE category_name=?''',(update,c_name))  # Assuming the last element is an identifier for the contact
        cursor.close()
        myconn.commit()

        return render_template("home.html",)
    return render_template("updatecategory.html")

@app.route("/deletecategory",methods=["POST","GET"])
def deletecategory():
    c_name = request.form["id"]
    myconn = sqlite3.connect('database.db')
    cursor = myconn.cursor()
    cursor.execute('''DELETE FROM category WHERE category_name = ?''',(c_name,))
    cursor.close()
    myconn.commit()
    return render_template("home.html")

@app.route("/gatheridforcategory",methods=["POST","GET"])
def gatheridforcategory():
    contact_id = request.form["id"]
    myconn = sqlite3.connect('database.db')
    cursor = myconn.cursor()
    cursor.execute('''SELECT * FROM category''')
    rows = cursor.fetchall()
    return render_template("addtocategory.html",contact_id=contact_id,rows=rows)

@app.route("/",methods=["POST","GET"])  
def addtocategory():
    if request.method == "POST":
        c_id = request.form["c_id"]
        cat_id = request.form.get('select_category')
        myconn = sqlite3.connect('database.db')
        cursor = myconn.cursor()
        cursor.execute('''INSERT INTO contact_category (contact_id,category_id)values (?,?)''',(c_id,cat_id))
        cursor.close()
        myconn.commit()
        return render_template("home.html")

def create_db():
    myconn = sqlite3.connect('database.db')
    cursor = myconn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contact (
        contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_firstname TEXT,
        contact_lastname TEXT,
        contact_email TEXT,
        contact_no TEXT,
        contact_address TEXT,
        contact_organisation TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS category (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT UNIQUE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS contact_category (
        contact_id INTEGER,
        category_id INTEGER,
        FOREIGN KEY(contact_id) REFERENCES contact(contact_id),
        FOREIGN KEY(category_id) REFERENCES category(category_id)
    )''')

    myconn.commit()
    cursor.close()
    myconn.close()


create_db()

if __name__ == "__main__":
	app.run(debug=True)


# pip freeze > requirements.txt
# pip install -r requirements.txt
