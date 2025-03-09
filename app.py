from flask import Flask, render_template, request, jsonify,session
from flask_sqlalchemy import SQLAlchemy

import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='admin',database='Bookings') 
my_cursor=conn.cursor()                    

conn.commit()
conn.close()

print("connection successfully")
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/Bookings'  # Connect to MySQLWorkbench
db = SQLAlchemy(app)

class amenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    flat_number = db.Column(db.String(50), nullable=False)
    amenity = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
   
class partyhall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    flat_number = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    TimeDuration = db.Column(db.String(50), nullable=True)  
    PhoneNumber = db.Column(db.String(11), nullable=True)
    UPI = db.Column(db.String(50), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hall')
def hallBookings_made():
    bookings = partyhall.query.all()
    print(bookings)
    return render_template('hall.html', bookings=bookings)


@app.route('/amenities')
def SportsBookings_made():
    bookings = amenities.query.all()
    print(bookings)
    return render_template('amenities.html', bookings=bookings)

@app.route('/party-hall')
def party_hall():
    return render_template('party-hall.html')

@app.route('/sports-amenities')
def sports_amenities():
    return render_template('sports-amenities.html')

@app.route('/bookings-made')
def bookings_made():
    return render_template('bookings-made.html')

@app.route('/booking-confirmation.html')
def booking_confirmation():
    return render_template('booking-confirmation.html')

@app.route('/payment.html')
def payment_page():
    return render_template('payment.html')



@app.route('/process-party-hall-booking', methods=['POST'])
def process_party_hall_booking():
    data = request.json
    name=data['name']
    print(data)
    flatNumber = data['flat_number']
    date = data['date']
    bookingDuration = data['booking_duration']
    phone = data['phone']
    session['name']=name
    session['flatNumber']=flatNumber
    session['date']=date
    session['bookingDuration']=bookingDuration
    session['phone']=phone
    return jsonify({'status': 'success'})

@app.route('/payment', methods=['POST'])
def getUPI():
    data = request.json
    print(data)
    name=session['name']
    flatNumber=session['flatNumber']
    date=session['date']
    bookingDuration=session['bookingDuration']
    phone=session['phone']
    upi=data['UPI']
    #print(name) // used for testing
    new_booking = partyhall(
        UPI=upi,
        name=name,
        flat_number=flatNumber,
        date=date,
        TimeDuration=bookingDuration,
        PhoneNumber=phone,
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'status': 'success'})


@app.route('/process-sports-amenities-booking', methods=['POST'])
def process_sports_amenities_booking():
    data = request.json
    name = data['name']
    flatNumber = data['flatNumber']
    date = data['date']
    startTime = data['startTime']
    endTime = data['endTime']
    amenity = data['amenity']
    
    new_booking = amenities(
        name=name,
        flat_number=flatNumber,
        amenity=amenity,
        date=date,
        start_time=startTime,
        end_time=endTime        
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)