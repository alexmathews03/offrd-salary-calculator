"""
Unit Tests for Offrd Salary Breakdown Calculator
Covers multiple salary levels, ESI thresholds, statutory caps, and edge cases.
"""

import pytest
from salary_calculator import calculate_monthly_salary


def test_standard_mid_level_ctc():
    """
    Test 1: Standard Mid-Level CTC (Rs 6,00,000 / annum = Rs 50,000 / month)
    - Basic: 50% = Rs 25,000
    - HRA: 50% of Basic = Rs 12,500
    - EPF: Basic > Rs 15,000 ceiling, so EPF is capped at 12% of Rs 15,000 = Rs 1,800
    - ESI: Gross > Rs 21,000, so ESI must be Rs 0.0
    - PT: Rs 200.0
    """
    res = calculate_monthly_salary(600000.0)

    assert res["annual_ctc"] == 600000.0
    assert res["monthly_ctc"] == 50000.0
    assert res["basic"] == 25000.0
    assert res["hra"] == 12500.0
    assert res["employer_epf"] == 1800.0
    assert res["employee_epf"] == 1800.0
    assert res["employer_esi"] == 0.0
    assert res["employee_esi"] == 0.0
    assert res["professional_tax"] == 200.0
    assert res["net_take_home"] == 46200.0


def test_esi_eligible_low_ctc():
    """
    Test 2: Low CTC under ESI threshold (Rs 1,80,000 / annum = Rs 15,000 / month)
    - Monthly CTC: Rs 15,000
    - Basic: Rs 7,500
    - HRA: Rs 3,750
    - EPF: 12% of Rs 7,500 = Rs 900.0
    - Gross estimate: 15,000 - 900 = Rs 14,100 <= Rs 21,000, so ESI is triggered!
    - Employer ESI: 3.25% of Rs 14,100 = Rs 458.25
    - Employee ESI: 0.75% of Rs 14,100 = Rs 105.75
    """
    res = calculate_monthly_salary(180000.0)

    assert res["monthly_ctc"] == 15000.0
    assert res["basic"] == 7500.0
    assert res["hra"] == 3750.0
    assert res["employer_epf"] == 900.0
    assert res["employee_epf"] == 900.0
    assert res["employer_esi"] == 458.25
    assert res["employee_esi"] == 105.75
    # Gross salary under Rs 15,000 -> PT is Rs 0
    assert res["professional_tax"] == 0.0
    assert res["net_take_home"] > 0


def test_high_executive_ctc():
    """
    Test 3: High Executive CTC (Rs 24,00,000 / annum = Rs 2,00,000 / month)
    - Basic: Rs 1,00,000
    - HRA: Rs 50,000
    - EPF: Must strictly remain capped at Rs 1,800 (not 12% of Rs 1,00,000)
    - ESI: Rs 0.0
    """
    res = calculate_monthly_salary(2400000.0)

    assert res["monthly_ctc"] == 200000.0
    assert res["basic"] == 100000.0
    assert res["hra"] == 50000.0
    assert res["employer_epf"] == 1800.0
    assert res["employee_epf"] == 1800.0
    assert res["employer_esi"] == 0.0
    assert res["employee_esi"] == 0.0
    assert res["professional_tax"] == 200.0
    assert res["net_take_home"] == 196200.0


def test_edge_case_very_low_ctc():
    """
    Test 4: Edge Case - Very Low CTC (Rs 60,000 / annum = Rs 5,000 / month)
    Ensures special allowance does not become negative and net pay remains valid.
    """
    res = calculate_monthly_salary(60000.0)

    assert res["monthly_ctc"] == 5000.0
    assert res["special_allowance"] >= 0.0
    assert res["net_take_home"] > 0.0


def test_invalid_negative_or_zero_ctc():
    """
    Test 5: Edge Case - Negative or zero CTC raises ValueError
    """
    with pytest.raises(ValueError):
        calculate_monthly_salary(0.0)

    with pytest.raises(ValueError):
        calculate_monthly_salary(-50000.0)
