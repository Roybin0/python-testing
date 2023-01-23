import unittest
from students import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.student = Student("Fuck", "CodeInstitute")

    def tearDown(self):
        print("tearDownSelf")

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "Fuck CodeInstitute")

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email_address(self):
        self.assertEqual(self.student.email_address,
                         "fuck.codeinstitute@email.com")

    def test_apply_extension(self):
        old_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_date + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("students.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("students.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(
                schedule, "Something went wrong with the request.")


if __name__ == "__main__":
    unittest.main()
