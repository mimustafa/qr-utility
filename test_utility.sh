#!/bin/bash

# Activate virtual environment
source venv/bin/activate

echo "=== QR Code Utility Test ==="
echo ""

# Test 1: Create QR code with URL
echo "Test 1: Creating QR code with GitHub URL..."
python qr_utility.py create https://www.github.com github_qr.png
echo ""

# Test 2: Read the QR code
echo "Test 2: Reading the QR code..."
python qr_utility.py read github_qr.png
echo ""

# Test 3: Create QR code with text
echo "Test 3: Creating QR code with text message..."
python qr_utility.py create "Hello from QR Utility!" text_qr.png
echo ""

# Test 4: Read the text QR code
echo "Test 4: Reading the text QR code..."
python qr_utility.py read text_qr.png
echo ""

echo "=== All tests completed! ==="
