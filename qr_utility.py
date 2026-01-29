#!/usr/bin/env python3
"""
QR Code Utility
This utility provides functions to:
1. Generate QR codes from URLs or text
2. Read QR codes from images and display their content
"""

import qrcode
from PIL import Image
import cv2
import sys
import os
import numpy as np


def create_qr_code(data, filename="qrcode.png", box_size=10, border=4):
    """
    Create a QR code from the given data and save it as an image.
    
    Args:
        data (str): The data/URL to encode in the QR code
        filename (str): Output filename for the QR code image
        box_size (int): Size of each box in the QR code grid
        border (int): Border size (minimum is 4)
    
    Returns:
        str: Path to the saved QR code image
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"✓ QR code created successfully: {filename}")
    print(f"  Content: {data}")
    
    return filename


def read_qr_code(image_path):
    """
    Read a QR code from an image file and display its content.
    
    Args:
        image_path (str): Path to the image file containing the QR code
    
    Returns:
        list: List of decoded data from the QR code(s) in the image
    """
    if not os.path.exists(image_path):
        print(f"✗ Error: File not found: {image_path}")
        return []
    
    try:
        # Load the image using OpenCV
        img = cv2.imread(image_path)
        
        if img is None:
            print(f"✗ Error: Could not load image: {image_path}")
            return []
        
        # Initialize QR code detector
        qr_detector = cv2.QRCodeDetector()
        
        # Try multiple preprocessing approaches
        images_to_try = [
            ("Original", img),
            ("Grayscale", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)),
        ]
        
        # Add preprocessed versions for photos
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        images_to_try.extend([
            ("Enhanced contrast", cv2.equalizeHist(gray)),
            ("Thresholded", cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)),
            ("Binary", cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]),
        ])
        
        # Try detecting with different preprocessing
        for method_name, processed_img in images_to_try:
            data, bbox, _ = qr_detector.detectAndDecode(processed_img)
            
            if data:
                # Display the decoded data
                results = [data]
                
                print(f"\n✓ QR Code detected! (using {method_name})")
                print(f"  Content: {data}")
                
                # Check if it's a URL
                if data.startswith(('http://', 'https://', 'www.')):
                    print(f"  → This appears to be a URL")
                
                return results
        
        print(f"✗ No QR code found in: {image_path}")
        return []
        
    except Exception as e:
        print(f"✗ Error reading image: {e}")
        return []


def main():
    """Main function to demonstrate the QR code utility."""
    if len(sys.argv) < 2:
        print("QR Code Utility")
        print("=" * 50)
        print("\nUsage:")
        print("  Create QR code:")
        print("    python qr_utility.py create <text_or_url> [output_file]")
        print("    Example: python qr_utility.py create https://github.com myqr.png")
        print("\n  Read QR code:")
        print("    python qr_utility.py read <image_file>")
        print("    Example: python qr_utility.py read qrcode.png")
        print("\nTry it out:")
        print("  python qr_utility.py create https://www.example.com")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "create":
        if len(sys.argv) < 3:
            print("✗ Error: Please provide text or URL to encode")
            print("  Usage: python qr_utility.py create <text_or_url> [output_file]")
            sys.exit(1)
        
        data = sys.argv[2]
        filename = sys.argv[3] if len(sys.argv) > 3 else "qrcode.png"
        create_qr_code(data, filename)
        
    elif command == "read":
        if len(sys.argv) < 3:
            print("✗ Error: Please provide image file path")
            print("  Usage: python qr_utility.py read <image_file>")
            sys.exit(1)
        
        image_path = sys.argv[2]
        read_qr_code(image_path)
        
    else:
        print(f"✗ Error: Unknown command '{command}'")
        print("  Valid commands: create, read")
        sys.exit(1)


if __name__ == "__main__":
    main()
