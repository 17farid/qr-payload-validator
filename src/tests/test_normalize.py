import unittest
from src.normalize import normalize


class TestNormalize(unittest.TestCase):

    def test_text(self):
        self.assertEqual(normalize("Hello", "text"), "Hello")

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

    def test_email(self):
        self.assertEqual(
            normalize("test@example.com", "email"),
            "mailto:test@example.com"
        )

    def test_phone(self):
        self.assertEqual(
            normalize("+994 50 211 09 09", "phone"),
            "tel:+994502110909"
        )

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            normalize("", "text")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            normalize("abc", "email")

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            normalize("abc", "url")

    def test_wrong_input_type(self):
        with self.assertRaises(TypeError):
            normalize(123, "text")

    def test_unsupported_type(self):
        with self.assertRaises(ValueError):
            normalize("hello", "pdf")


if __name__ == "__main__":
    unittest.main()

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


def test_wifi_missing_ssid(self):
    with self.assertRaises(ValueError):
        normalize(
            {
                "password": "12345678",
                "encryption": "WPA"
            },
            "wifi"
        )
