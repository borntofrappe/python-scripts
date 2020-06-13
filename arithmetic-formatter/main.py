from arithmetic_formatter import arithmetic_formatter

print(arithmetic_formatter(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_formatter(
    ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_formatter(["44 + 815", "909 - 2",
                            "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_formatter(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_formatter(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_formatter(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_formatter(
    ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
