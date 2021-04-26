import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')
        for row in reader:
            data = []
            for item in row:
                 data.append(int(item))
    return data






def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = []
        i = 0
        for row in reader:
            if i == row_number:
                for item in row:
                    data.append(int(item))
            i = i + 1
    return data




def selection_sort(number_array, direction='ascending'):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    if direction == "ascending":
        for i in range(len(number_array)):
            minimum = i
            for j in range(i+1, len(number_array)):
                if number_array[minimum] > number_array[j]:
                    minimum = j
            number_array[i], number_array[minimum] = number_array[minimum], number_array[i]
        return number_array

    elif direction == "descending":
        for i in range(len(number_array)):
            maximum = i
            for j in range(i+1, len(number_array)):
                if number_array[maximum] < number_array[j]:
                    maximum = j
            number_array[maximum], number_array[i] = number_array[i], number_array[maximum]
        return number_array



def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    for number in range(len(number_array)-1):
        for i in range(len(number_array)-1):
            if number_array[i] > number_array[i+1]:
                number_array[i], number_array[i+1] = number_array[i+1], number_array[i]

    return number_array






def main():
    data = read_row('numbers_one.csv')
    sorted_numbers = selection_sort(data)
    print(sorted_numbers)

    # Ukol: Selection Sort


    # Ukol: Selection Sort - se smerem razeni
    sorted_numbers = selection_sort(data, 'descending')
    print(sorted_numbers)

    random_number = random.randint(0,2)
    row = read_rows('numbers_two.csv', random_number)
    print(row)
    # Ukol: Bubble Sort
    bubble = bubble_sort(row)
    print("Bubble sort ")
    print(bubble)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

