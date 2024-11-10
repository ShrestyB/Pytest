test_names = [
    "TestLoginFunctionality",
    "TestLogoutProcess",
    "TestSignupWorkflow",
    "TestPasswordReset",
    "TestEmailVerification",
    "TestDashboardLoad",
    "TestDataAnalysis",
]

def find_tests_with_keyword(test_list, keyword):
    matched_tests = []
    for test in test_list:
        if keyword in test:
            matched_tests.append(test)
    return matched_tests


keyword_to_search = "Login"
matched_tests = find_tests_with_keyword(test_names, keyword_to_search)
print(f"Tests matching '{keyword_to_search}': {matched_tests}")
