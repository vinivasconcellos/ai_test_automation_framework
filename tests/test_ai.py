from ai.testcase_generator import generate_test_cases
from ai.failure_analysis import analyze_failure


def test_generate_test_cases():
    feature = "Bluetooth connection for infotainment system"

    result = generate_test_cases(feature)

    assert result is not None
    assert len(result) > 50


def test_failure_analysis():
    feature = "Bluetooth connection"
    error = "No audio after connection"

    result = analyze_failure(feature, error)

    assert result is not None
    assert "Root cause" or "Root Cause" in result