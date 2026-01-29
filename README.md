# QR Code Utility

A Python utility to create and read QR codes.

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Installed libraries:**
   - `qrcode[pil]` - For creating QR codes
   - `opencv-python` - For reading/decoding QR codes and image processing
   - `pillow` - Image handling

## Usage

### Create a QR Code

```bash
python qr_utility.py create <text_or_url> [output_file]
```

**Examples:**
```bash
# Create QR code with default name (qrcode.png)
python qr_utility.py create https://www.github.com

# Create QR code with custom name
python qr_utility.py create https://www.example.com my_qr.png

# Create QR code with text
python qr_utility.py create "Hello, World!" greeting.png
```

### Read a QR Code

```bash
python qr_utility.py read <image_file>
```

**Examples:**
```bash
# Read QR code from image
python qr_utility.py read qrcode.png

# Read QR code from custom file
python qr_utility.py read my_qr.png
```

## Features

- ✅ Generate QR codes from URLs or text
- ✅ Save QR codes as PNG images
- ✅ Read and decode QR codes from images
- ✅ Automatically detect URLs in QR codes
- ✅ Support for multiple QR codes in a single image

## Requirements

- Python 3.14
- Virtual environment (venv)
