# Wrong function: This function checks for an exact match instead of a substring
def find_tests_with_keyword_wrong(test_list, keyword):
    matched_tests = []
    for test in test_list:
        # Mistake: Exact match instead of substring search
        if test == keyword:
            matched_tests.append(test)
    return matched_tests

# Using the wrong function
matched_tests_wrong = find_tests_with_keyword_wrong(test_names, keyword_to_search)
print(f"Tests matching '{keyword_to_search}' (wrong function): {matched_tests_wrong}")


