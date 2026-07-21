import re


def normalize(raw_input, payload_type):
   if payload_type == "wifi":
    if not isinstance(raw_input, dict):
        raise TypeError("WiFi payload must be a dictionary")
else:
    if not isinstance(raw_input, str):
        raise TypeError("Input must be a string")

    raw_input = raw_input.strip()

    if not raw_input:
        raise ValueError("Input cannot be empty")

    payload_type = payload_type.lower()

    if payload_type == "text":
        return raw_input

    elif payload_type == "url":
        if not raw_input.startswith(("http://", "https://")):
            raw_input = "https://" + raw_input

        url_pattern = re.compile(
            r"^https?://([A-Za-z0-9-]+\.)+[A-Za-z]{2,}(/.*)?$"
        )

        if not url_pattern.match(raw_input):
            raise ValueError("Invalid URL")

        return raw_input

    elif payload_type == "email":
        if raw_input.startswith("mailto:"):
            email = raw_input[7:]
        else:
            email = raw_input

        email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

        if not email_pattern.match(email):
            raise ValueError("Invalid email")

        return "mailto:" + email

    elif payload_type == "phone":
        phone = raw_input.replace(" ", "")

        if not re.fullmatch(r"\+?\d+", phone):
            raise ValueError("Invalid phone number")

        return "tel:" + phone

    elif payload_type == "wifi":
        raise NotImplementedError(
            "WiFi payload expects a dictionary/object, not a string."
        )

    else:
        raise ValueError("Unsupported payload type")
