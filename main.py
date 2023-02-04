import unittest
import requests
import json

class BookingTestCase(unittest.TestCase):
    def test_bookings(self):
        url = "https://restful-booker.herokuapp.com/booking"

        response = requests.get(url)

        # Parse the JSON response
        bookings = json.loads(response.text)

        # Validate that there is at least one booking
        self.assertGreaterEqual(len(bookings), 1, "No bookings were found")

    def test_response_status(self):
        url = "https://restful-booker.herokuapp.com/booking"

        response = requests.get(url)

        # Validate that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200, "Response status code is not 200 (OK)")

if __name__ == '__main__':
    unittest.main()