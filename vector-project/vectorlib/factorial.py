import math

n = 1_000_000_000
filename = "factorial_1b.txt"

# Вычисляем логарифм факториала
ln_fact = math.lgamma(n + 1)
log10_fact = ln_fact / math.log(10)

exponent = int(log10_fact)
mantissa = 10 ** (log10_fact - exponent)

# Формируем текст для записи
output_text = (
    f"Приближенное значение {n:,}!:\n"
    f"{mantissa:.15f} * 10^{exponent}\n"
    f"Всего цифр в числе: {exponent + 1:,}\n"
)

# Записываем в файл
with open(filename, "w", encoding="utf-8") as file:
    file.write(output_text)

print(f"Готово! Результат сохранен в файл {filename}")
