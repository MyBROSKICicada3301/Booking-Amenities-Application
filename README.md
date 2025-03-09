# Booking System

## Overview

- This is a Flask-based web application that facilitates booking of party halls and sports amenities.
- The system allows users to book amenities, make payments, and view existing bookings.

## Features

- Booking system for party halls and sports amenities
- Payment processing using QR code
- MySQL database integration with SQLAlchemy
- Session management for storing booking details temporarily
- Web interface using HTML templates

## Technologies Used

- **Python** (Flask)
- **MySQL**
- **Flask-SQL Alchemy**
- **HTML/CSS** (for frontend templates)

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3
- MySQL
- Flask and required dependencies

### Setup Instructions

```sh
# Clone the repository
git clone https://github.com/MyBROSKICicada3301/Booking-Amenities-Application.git

# Navigate to the project directory
cd yourrepository

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

#### Configure MySQL Database

Update the database connection details in `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/Bookings'
```

Ensure your MySQL server is running and the `Bookings` database exists.

```sh
# Run the application
python app.py

# Open your browser and visit
http://127.0.0.1:5000/
```

## API Endpoints

- `/` (GET) - Homepage
- `/hall` (GET) - View all hall bookings
- `/amenities` (GET) - View all sports amenities bookings
- `/process-party-hall-booking` (POST) - Process party hall booking
- `/process-sports-amenities-booking` (POST) - Process sports amenities booking
- `/payment` (POST) - Process payment via UPI

## Database Models

### Amenities Table

- **id** - Integer (Primary Key)
- **name** - String(100)
- **flat_number** - String(50)
- **amenity** - String(50)
- **date** - String(20)
- **start_time** - String(10)
- **end_time** - String(10)

### Party Hall Table

- **id** - Integer (Primary Key)
- **name** - String(100)
- **flat_number** - String(50)
- **date** - String(20)
- **TimeDuration** - String(50)
- **PhoneNumber** - String(11)
- **UPI** - String(50)

