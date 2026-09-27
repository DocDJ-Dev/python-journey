lab_tests = {
    "FBC": 0,  # a genuine result of 0 - the test IS done
    "glucose": [],  # empty list sentinel - NOT done yet
    "notes": "",  # empty string sentinel - NOT done yet
}
print(bool(lab_tests["FBC"]))  # False
print(bool(lab_tests["glucose"]))  # False
print(bool(lab_tests["notes"]))  # False


# FBC's False and glucose's False are indistinguishable from the boolean alone, even though one is a completed test with a real zero and the other is genuinely missing.
