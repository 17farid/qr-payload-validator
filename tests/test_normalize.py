import unittest
from src.normalize import normalize


class TestNormalize(unittest.TestCase):

    # TEXT

    def test_text(self):
        self.assertEqual(
            normalize("Hello World", "text"),
            "Hello World"
        )

    # URL

    def test_url_without_protocol(self):
        self.assertEqual(
            normalize("google.com", "url"),
            "https://google.com"
        )

    def test_url_with_https(self):
        self.assertEqual(
            normalize("https://google.com", "url"),
            "https://google.com"
        )

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            normalize("abc", "url")

    # EMAIL

    def test_email(self):
        self.assertEqual(
            normalize("john@example.com", "email"),
            "mailto:john@example.com"
        )

    def test_email_already_prefixed(self):
        self.assertEqual(
            normalize("mailto:john@example.com", "email"),
            "mailto:john@example.com"
        )

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            normalize("johnexample.com", "email")

    # PHONE

    def test_phone(self):
        self.assertEqual(
            normalize("+994 50 123 45 67", "phone"),
            "tel:+994501234567"
        )

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            normalize("abc123", "phone")

    # WIFI

    def test_wifi(self):
        wifi = {
            "ssid": "Home",
            "password": "12345678",
            "encryption": "WPA"
        }

        self.assertEqual(
            normalize(wifi, "wifi"),
            "WIFI:T:WPA;S:Home;P:12345678;;"
        )

    def test_wifi_nopass(self):
        wifi = {
            "ssid": "Cafe",
            "encryption": "nopass"
        }

        self.assertEqual(
            normalize(wifi, "wifi"),
            "WIFI:T:nopass;S:Cafe;P:;;"
        )

    def test_wifi_missing_ssid(self):
        with self.assertRaises(ValueError):
            normalize(
                {
                    "password": "12345678",
                    "encryption": "WPA"
                },
                "wifi"
            )

    # EDGE CASES

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            normalize("", "text")

    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            normalize(123, "text")

    def test_unsupported_payload(self):
        with self.assertRaises(ValueError):
            normalize("hello", "pdf")


if __name__ == "__main__":
    unittest.main()