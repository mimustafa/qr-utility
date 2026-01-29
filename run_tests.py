#!/usr/bin/env python3
"""
Comprehensive test suite for QR code utility
Tests both QR code creation and reading functionality
"""

import sys
import os
import subprocess
import tempfile

# Test results tracking
tests_passed = 0
tests_failed = 0
test_results = []

def run_command(cmd):
    """Run a command and return output and exit code."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr, result.returncode

def test_create_qr_url():
    """Test creating a QR code with a URL."""
    global tests_passed, tests_failed
    
    print("Test 1: Creating QR code with URL...")
    output, exit_code = run_command("python qr_utility.py create https://www.github.com test_github.png")
    
    if exit_code == 0 and os.path.exists("test_github.png") and "✓" in output:
        print("  ✓ PASSED: QR code created successfully")
        tests_passed += 1
        test_results.append(("Create QR with URL", "PASSED"))
        return True
    else:
        print("  ✗ FAILED: QR code creation failed")
        tests_failed += 1
        test_results.append(("Create QR with URL", "FAILED"))
        return False

def test_create_qr_text():
    """Test creating a QR code with plain text."""
    global tests_passed, tests_failed
    
    print("\nTest 2: Creating QR code with plain text...")
    output, exit_code = run_command('python qr_utility.py create "Hello World" test_text.png')
    
    if exit_code == 0 and os.path.exists("test_text.png") and "✓" in output:
        print("  ✓ PASSED: QR code with text created successfully")
        tests_passed += 1
        test_results.append(("Create QR with text", "PASSED"))
        return True
    else:
        print("  ✗ FAILED: QR code with text creation failed")
        tests_failed += 1
        test_results.append(("Create QR with text", "FAILED"))
        return False

def test_read_generated_qr_url():
    """Test reading a generated QR code with URL."""
    global tests_passed, tests_failed
    
    print("\nTest 3: Reading generated QR code (URL)...")
    output, exit_code = run_command("python qr_utility.py read test_github.png")
    
    if exit_code == 0 and "https://www.github.com" in output and "✓" in output:
        print("  ✓ PASSED: QR code read successfully")
        tests_passed += 1
        test_results.append(("Read QR with URL", "PASSED"))
        return True
    else:
        print("  ✗ FAILED: QR code reading failed")
        print(f"    Output: {output}")
        tests_failed += 1
        test_results.append(("Read QR with URL", "FAILED"))
        return False

def test_read_generated_qr_text():
    """Test reading a generated QR code with text."""
    global tests_passed, tests_failed
    
    print("\nTest 4: Reading generated QR code (text)...")
    output, exit_code = run_command("python qr_utility.py read test_text.png")
    
    if exit_code == 0 and "Hello World" in output and "✓" in output:
        print("  ✓ PASSED: QR code with text read successfully")
        tests_passed += 1
        test_results.append(("Read QR with text", "PASSED"))
        return True
    else:
        print("  ✗ FAILED: QR code with text reading failed")
        print(f"    Output: {output}")
        tests_failed += 1
        test_results.append(("Read QR with text", "FAILED"))
        return False

def test_read_photo_qr():
    """Test reading QR codes from photos (if available)."""
    global tests_passed, tests_failed
    
    print("\nTest 5: Reading QR codes from photos...")
    
    # Check if photo QR codes exist
    photo_files = []
    if os.path.exists("qr-1.jpeg"):
        photo_files.append("qr-1.jpeg")
    if os.path.exists("qr-2.jpg"):
        photo_files.append("qr-2.jpg")
    
    if not photo_files:
        print("  ⊘ SKIPPED: No photo QR codes found (qr-1.jpeg, qr-2.jpg)")
        test_results.append(("Read photo QR codes", "SKIPPED"))
        return None
    
    passed = True
    for photo in photo_files:
        output, exit_code = run_command(f"python qr_utility.py read {photo}")
        if exit_code == 0 and "✓" in output and "https://" in output:
            print(f"  ✓ {photo}: Read successfully")
        else:
            print(f"  ✗ {photo}: Failed to read")
            passed = False
    
    if passed:
        tests_passed += 1
        test_results.append(("Read photo QR codes", "PASSED"))
        return True
    else:
        tests_failed += 1
        test_results.append(("Read photo QR codes", "FAILED"))
        return False

def test_read_nonexistent_file():
    """Test error handling for non-existent file."""
    global tests_passed, tests_failed
    
    print("\nTest 6: Error handling for non-existent file...")
    output, exit_code = run_command("python qr_utility.py read nonexistent_file.png")
    
    if "✗" in output and "not found" in output.lower():
        print("  ✓ PASSED: Error handled correctly")
        tests_passed += 1
        test_results.append(("Error handling", "PASSED"))
        return True
    else:
        print("  ✗ FAILED: Error not handled properly")
        tests_failed += 1
        test_results.append(("Error handling", "FAILED"))
        return False

def test_backwards_compatibility():
    """Test backwards compatibility with existing QR codes."""
    global tests_passed, tests_failed
    
    print("\nTest 7: Backwards compatibility with existing QR codes...")
    
    # Check if old QR codes exist
    old_qr_files = []
    for f in ["github_qr.png", "python_qr.png", "text_qr.png"]:
        if os.path.exists(f):
            old_qr_files.append(f)
    
    if not old_qr_files:
        print("  ⊘ SKIPPED: No existing QR codes found")
        test_results.append(("Backwards compatibility", "SKIPPED"))
        return None
    
    passed = True
    for qr_file in old_qr_files:
        output, exit_code = run_command(f"python qr_utility.py read {qr_file}")
        if exit_code == 0 and "✓" in output:
            print(f"  ✓ {qr_file}: Still readable")
        else:
            print(f"  ✗ {qr_file}: Failed to read")
            passed = False
    
    if passed:
        tests_passed += 1
        test_results.append(("Backwards compatibility", "PASSED"))
        return True
    else:
        tests_failed += 1
        test_results.append(("Backwards compatibility", "FAILED"))
        return False

def cleanup_test_files():
    """Clean up test files."""
    print("\nCleaning up test files...")
    test_files = ["test_github.png", "test_text.png"]
    for f in test_files:
        if os.path.exists(f):
            os.remove(f)
            print(f"  Removed {f}")

def print_summary():
    """Print test summary."""
    total_tests = tests_passed + tests_failed
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in test_results:
        status_symbol = "✓" if result == "PASSED" else "✗" if result == "FAILED" else "⊘"
        print(f"{status_symbol} {test_name}: {result}")
    
    print("\n" + "-" * 60)
    print(f"Total tests run: {total_tests}")
    print(f"Passed: {tests_passed}")
    print(f"Failed: {tests_failed}")
    
    if tests_failed == 0:
        print("\n🎉 ALL TESTS PASSED! Safe to commit.")
        print("=" * 60)
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED! Review before committing.")
        print("=" * 60)
        return 1

def main():
    """Run all tests."""
    print("=" * 60)
    print("QR UTILITY TEST SUITE")
    print("=" * 60)
    print()
    
    # Run all tests
    test_create_qr_url()
    test_create_qr_text()
    test_read_generated_qr_url()
    test_read_generated_qr_text()
    test_read_photo_qr()
    test_read_nonexistent_file()
    test_backwards_compatibility()
    
    # Cleanup
    cleanup_test_files()
    
    # Print summary and exit
    exit_code = print_summary()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
