import re


def normalize(raw_input, payload_type):
    """
    Normalize different payload types into QR-ready strings.

    Supported types:
    - text
    - url
    - email
    - phone
    - wifi
    """

    if payload_type == "wifi":
        if not isinstance(raw_input, dict):
            raise TypeError("WiFi input must be a dictionary.")

        ssid = raw_input.get("ssid")
        password = raw_input.get("password", "")
        encryption = raw_input.get("encryption", "WPA")

        if not ssid:
            raise ValueError("SSID is required.")

        if encryption not in ("WPA", "WEP", "nopass"):
            raise ValueError("Invalid encryption type.")

        if encryption == "nopass":
            password = ""

        return f"WIFI:T:{encryption};S:{ssid};P:{password};;"

    if not isinstance(raw_input, str):
        raise TypeError("Input must be a string.")

    raw_input = raw_input.strip()

    if raw_input == "":
        raise ValueError("Input cannot be empty.")

    payload_type = payload_type.lower()

    if payload_type == "text":
        return raw_input

    elif payload_type == "url":

        if not raw_input.startswith(("http://", "https://")):
            raw_input = "https://" + raw_input

        pattern = re.compile(
            r"^https?://([A-Za-z0-9-]+\.)+[A-Za-z]{2,}(/.*)?$"
        )

        if not pattern.match(raw_input):
            raise ValueError("Invalid URL.")

        return raw_input

    elif payload_type == "email":

        if raw_input.startswith("mailto:"):
            email = raw_input
        else:
            email = "mailto:" + raw_input

        if not re.match(r"^mailto:[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise ValueError("Invalid email.")

        return email

    elif payload_type == "phone":

        phone = raw_input.replace(" ", "")

        if not re.fullmatch(r"\+?\d+", phone):
            raise ValueError("Invalid phone number.")

        return "tel:" + phone

    else:
        raise ValueError("Unsupported payload type.")