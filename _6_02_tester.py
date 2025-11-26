def tester():
    # Liệt kê các trường hợp đầu vào và kết quả dự kiến
    # 1 2
    test_cases = [
        (input_1, expected_1, description_1),
        (input_2, expected_2, description_2)
    ]
    
    print("Validation Test:")
    print("=" * 70)
    
    passed = 0
    total = len(test_cases)
    
    # Kích hoạt hàm với các test_case đã chuẩn bị rồi in kết quả và so sánh
    # 3 4 5
    for i, (input, expected, description) in enumerate(test_cases):
        result = function_to_test(input)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        
        print(f"Test {i+1:2d}: {status}")
        print(f"  Input: '{input}'")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  {description}")
        
        if result != expected:
            print(f"  >>> MISMATCH! <<<")
        print()
    
    # Hiển thị kết quả kiểm tra và kết luận
    # 6
    print("=" * 70)
    print(f"Results: {passed}/{total} tests passed")
    if passed == total:
        print("All tests passed!")
    else:
        print(f"❌ {total - passed} tests failed. Please review the logic.")
