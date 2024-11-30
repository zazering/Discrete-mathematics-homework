def hamming_encode(data):
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    result = ['0'] * (m + r)
    control_bits = []

    j = 0
    for i in range(1, len(result) + 1):
        if i & (i - 1) == 0:
            continue
        result[i - 1] = data[j]
        j += 1

    for i in range(r):
        pos = 2 ** i - 1
        xor_sum = 0

        for j in range(1, len(result) + 1):
            if j & (2 ** i) != 0:
                xor_sum ^= int(result[j - 1])
        result[pos] = str(xor_sum)
        control_bits.append((2 ** i, xor_sum))

    return ''.join(result), control_bits


data = "001010001100111000001001011110101110101000000100110101000000000000"
enc = "1000010110001101011100000100101011101011101010000001001101010000000000000"
encoded_data, control_bits = hamming_encode(data)

print("Закодированная строка (по Хэммингу):", encoded_data)

print("\nКонтрольные биты (позиция, значение):")
for pos, bit in control_bits:
    print(f"Позиция: {pos}, Контрольный бит: {bit}")


print(f"длина исходной: {len(data)}, длина закодированного сообщения: {len(encoded_data)}")
