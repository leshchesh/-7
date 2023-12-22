def count_digits(number, count=0, even_count=0):
    if number == 0:
        return count, even_count
    else:
        digit = number % 10
        if digit % 2 == 0:
            even_count += 1
        return count_digits(number // 10, count+1, even_count)
number = int(input("Введите число:"))
digit_count, even_digit_count = count_digits(number)
print("Количество цифр:", digit_count)
print("Количество чётных цифр:", even_digit_count)
