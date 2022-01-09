import json

try:
    from app import app
    import unittest
except Exception as e:
    print("Some Module Error".format(e))


class FlaskTestCase(unittest.TestCase):
    # Test Main home Page
    def test_main_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_auth_index(self):
        tester = app.test_client(self)
        response = tester.get("/auth")
        self.assertTrue(b"message" in response.data)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.post("/auth/login", json={"email": "admin@gmail.com", "password": "admin@123"})
        self.assertEqual(response.status_code, 200)

    def test_info(self):
        tester = app.test_client(self)
        response = tester.post("/auth/login", json={"email": "admin@gmail.com", "password": "admin@123"})
        token = json.loads(response.data)["token"]
        headers = {
            'Bearer': token
        }
        info_response = tester.get("/auth", headers=headers)
        self.assertEqual(info_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
