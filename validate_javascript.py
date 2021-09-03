def validate_javascript(javascript_code):
    opener_options = '({['
    paired_options = {')': '(', '}': '{', ']': '['}
    openers = []
    for ch in javascript_code:
        if ch in opener_options:
            openers.append(ch)
        elif ch in paired_options:
            if not openers:
                return 0
            opener = openers.pop()
            if opener != paired_options[ch]:
                return 0
    return 1


if __name__ == '__main__':
    test_cases = [('{ [] ( ) }', 1), ('{ [(] ) }', 0), ('{ [ }', 0), ('}}{{', 0),
                  ('adafsd;flkewfa{}asdfasd[fd(dfd)]', 1), ('adafsd;flkewfa{}asdfasd[fd(d)fd)]', 0)]
    for test in test_cases:
        validate_output = validate_javascript(test[0])
        assert validate_output == test[1]
        print(f"{validate_output} {test[1]}")
