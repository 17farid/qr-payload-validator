# QR Payload Validator

A Python module that validates and normalizes QR payloads into QR-ready strings.

## Installation

```bash
git clone https://github.com/17farid/qr-payload-validator.git
cd qr-payload-validator
```

## Run tests

```bash
python -m unittest discover tests
```

## Usage

```python
from src.normalize import normalize

print(normalize("google.com", "url"))
# https://google.com

print(normalize("faridalakbarov@gmail.com", "email"))
# mailto:faridalakbarov@gmail.com
```

## Design Decisions

- URLs without a protocol are normalized by prepending `https://`.
- Existing `http://` and `https://` URLs are preserved.
- Phone numbers have whitespace removed and are prefixed with `tel:`.
- Email addresses are prefixed with `mailto:` if not already present.
- Supported Wi-Fi encryption types are `WPA`, `WEP`, and `nopass`.
- Empty inputs, malformed values, unsupported types, and invalid input types raise descriptive exceptions.

## Testing

The test suite covers:

- URL
- Text
- Email
- Phone
- Wi-Fi
- Empty input
- Wrong input type
- Malformed input
