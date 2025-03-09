CREATE TABLE bookings.amenities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    flat_number VARCHAR(5) NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    amenity VARCHAR(50) NOT NULL
);

CREATE TABLE bookings.PartyHall (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    flat_number VARCHAR(5) NOT NULL,
    date DATE NOT NULL,
    TimeDuration VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(11),
    UPI VARCHAR(50) NOT NULL
);

INSERT INTO bookings.amenities (name, flat_number, date, start_time, end_time, amenity)
VALUES ('John Doe', 'E0101', '2024-01-15', '10:00:00', '11:00:00', 'basketball'),
       ('Jane Smith', 'A1205', '2024-01-16', '14:00:00', '16:00:00', 'Swimming Pool'),
       ('Mike Johnson', 'D0312', '2024-01-20', '18:30:00', '20:00:00', 'Tennis Court');

INSERT INTO bookings.PartyHall (name, flat_number, date, TimeDuration, PhoneNumber, UPI)
VALUES 
    ('John Doe', 'E0101', '2024-01-15', 'Half-day(9am-2pm)', '12345678901', 'john.doe@upi'),
    ('Jane Smith', 'A1205', '2024-01-16', 'Half-day(2pm-8pm)', '98765432109', 'jane.smith@upi'),
    ('Mike Johnson', 'D0312', '2024-01-20', 'Full Day(9am-9pm)', '45678901234', 'mike.johnson@upi');


