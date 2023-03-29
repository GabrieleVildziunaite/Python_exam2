from app import app
from flask import render_template, request, redirect, flash, url_for


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app.config['SECRET_KEY'] = 'fhadkjhakjfdh'


engine = create_engine('sqlite:///billsDB.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Bills(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    name = Column("title", String)
    description = Column("D=description", String)
    number = Column("participants", String)
    amount = Column("amount", String)
    author = Column("responsible", String)
    date = Column("date", String)     
    
    def __init__(self, name, description, number, amount, author, date):
        self.name = name
        self.description = description
        self.number = number
        self.amount = amount
        self.author = author
        self.date = date

    def __repr__(self):
        return f"{self.id} {self.name} {self.description} {self.number} {self.amount} {self.author} {self.date}"
    
Base.metadata.create_all(engine)

menu = [{"name": "Split Bill", "url": "/"},
        {"name": "Login", "url": "login"},
        {"name": "Group entries", "url": "groups"},
        {"name": "All bills", "url": "bills"}]


@app.route('/bills')
def bills():
    allData = session.query(Bills).all()
    return render_template('admin/bills.html', title="Bills", title2="All of your bills", menu=menu, allData=allData) 


@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        number = request.form['number']
        amount = request.form['amount']
        author = request.form['author']
        date = request.form['date']
        
        my_data = Bills(name, description, number, amount, author, date)

        session.add(my_data)
        session.commit()
        
        return redirect(url_for('bills'))
 

@app.route("/<string:title>", methods=['GET', 'POST']) 
def article(title):
    allData = session.query(Bills).all()
    return render_template("admin/article.html", title=title, menu=menu, allData=allData)


@app.route("/groups") 
def groups():
    allData = session.query(Bills).all()
    return render_template("admin/groups.html", menu=menu, title="Your Split Bill Entries", title2="Bills", allData=allData)


