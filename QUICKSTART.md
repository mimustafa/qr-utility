# Quick Start Guide

## Setup (One-time)

```bash
# Activate the virtual environment
source venv/bin/activate
```

## Common Commands

### Create QR Codes

```bash
# Create QR code for a URL
python qr_utility.py create https://www.github.com

# Create QR code with custom filename
python qr_utility.py create https://www.example.com my_site.png

# Create QR code with text
python qr_utility.py create "Contact: john@example.com" contact.png
```

### Read QR Codes

```bash
# Read any QR code image
python qr_utility.py read qrcode.png

# Read QR code with custom filename
python qr_utility.py read my_qr.png
```

## Examples

```bash
# Create and verify a QR code in one go
python qr_utility.py create https://www.python.org py.png && python qr_utility.py read py.png
```

## Testing

Run the included test script:
```bash
./test_utility.sh
```

## What Gets Created

- `venv/` - Python virtual environment (Python 3.14)
- `*.png` - QR code images you create
- Generated QR codes can be scanned with any QR code reader app

## Files in this Project

- `qr_utility.py` - Main utility script
- `test_utility.sh` - Automated test script
- `README.md` - Full documentation
- `QUICKSTART.md` - This file
