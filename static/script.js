function handleSportsAmenitiesFormSubmission() {
  const form = document.getElementById('sports-amenities-form');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Get user inputs
    const amenity = document.getElementById('amenity').value;
    const date = document.getElementById('date').value;
    const startTime = document.getElementById('start-time').value;
    const endTime = document.getElementById('end-time').value;

    // Perform client-side validation
    if (!amenity || !date || !startTime || !endTime) {
      alert('Please fill in all fields.');
      return;
    }

    if (startTime >= endTime) {
      alert('End time must be after start time.');
      return;
    }

    // Display booking details
    alert(`Booking Details:
Amenity: ${amenity}
Date: ${date}
Start Time: ${startTime}
End Time: ${endTime}`);

    // To redirect to payment page
    window.location.href = 'payment.html';
  });
}

function handlePartyHallFormSubmission() {
  const form = document.getElementById('party-hall-form');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Get user inputs
    const name = document.getElementById('name').value;
    const flat_number = document.getElementById('flat_number').value;
    const date = document.getElementById('date').value;
    const booking_duration = document.getElementById('booking_duration').value;
    const phone = document.getElementById('phone').value;

    // Perform client-side validation
    if (!name || !flat_number || !date || !booking_duration || !phone) {
      alert('Please fill in all fields.');
      return;
    }

    // Display booking details
    alert(`Booking Details:
Amenity: ${amenity}
Name: ${name}
booking_duration: ${booking_duration}
phone: ${phone}
Date: ${date}`);

    // To redirect to payment page
    window.location.href = 'payment.html';
  });
}


function UPISubmission() {
  const form = document.getElementById('payment-form');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Get user inputs
    const upi = document.getElementById('upi').value;

    // // Perform client-side validation
    // if (!name || !flat_number || !date || !booking_duration || !phone) {
    //   alert('Please fill in all fields.');
    //   return;
    // }

    // Display booking details
    alert(`Booking Details:
Amenity: ${amenity}
Name: ${name}
booking_duration: ${booking_duration}
phone: ${phone}
Date: ${date}`);

    // To redirect to payment page
    window.location.href = 'payment.html';
  });
}
