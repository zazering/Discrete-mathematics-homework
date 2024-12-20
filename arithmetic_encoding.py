def arithmetic(text, probabilities):
    sorted_probs = dict(sorted(probabilities.items()))
    intervals = {}
    low = 0.0
    for char, prob in sorted_probs.items():
        high = low + prob
        intervals[char] = (low, high)
        low = high

    low, high = 0.0, 1.0
    bounds = []

    for char in text:
        char_low, char_high = intervals[char]
        range_width = high - low
        new_high = low + range_width * char_high
        new_low = low + range_width * char_low
        bounds.append((new_low, new_high))
        low, high = new_low, new_high

    encoded_value = (low + high) / 2
    return encoded_value, intervals, bounds


def to_bin(value, precision=64):
    """Преобразует число в двоичное представление с заданной точностью."""
    result = []
    for _ in range(precision):
        value *= 2
        if value >= 1:
            result.append('1')
            value -= 1
        else:
            result.append('0')
    return ''.join(result)


text = "никулинмарккириллович"
probabilities = {
    'а': 0.0476190476190, 'в': 0.0476190476190, 'и': 0.238095238095238095,
    'к': 0.095238095238095238, 'л': 0.142857242857142857, 'м': 0.0476190476190,
    'н': 0.095238095238095238, 'о': 0.0476190476190, 'р': 0.095238095238095238,
    'у': 0.0476190476190, 'ч': 0.0476190476190
}

encoded_value, intervals, bounds = arithmetic(text, probabilities)

print("\nГраницы интервалов на каждом шаге:")
for step, (low, high) in enumerate(bounds, 1):
    print(f"Шаг {step}: [{low:.10f}, {high:.10f})")

binary_code = to_bin(encoded_value)
print(f"\nЗакодированное значение: {encoded_value:.10f}")
print(f"Бинарное представление: {binary_code}")


print(len("1010001100111000001001011110101110101000000100110101000000000000"))
