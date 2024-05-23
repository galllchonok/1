def find_min_column(matrix, col_num):
    column = [row[col_num] for row in matrix]
    return min(column)
def find_nonzero_product(row):
    product = 1
    for num in row:
        if num != 0:
            product *= num
    return product
def main():
    with open('какая-томатрица.txt', 'r') as file:
        matrix = [[int(num) for num in line.split()] for line in file]

    k = int(input("Введите номер столбца (k): "))

    if k < 0 or k >= len(matrix[0]):
        print("Неверное значение для k")
        return
    min_element = find_min_column(matrix, k)
    for i, row in enumerate(matrix):
        if min_element in row:
            product = find_nonzero_product(row)
            print(f"В строке с минимальным элементом в столбце {k} произведение отличных от нуля элементов: {product}")
            break
if __name__ == "__main__":
    main()
