import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, mode="r") as loaded_file:
        reader = csv.DictReader(loaded_file)
        data = {}

        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n):
        min_idx = i
        for num_idx in range(i + 1, n):
            if list_of_numbers[num_idx] < list_of_numbers[min_idx]:
                min_idx = num_idx
        list_of_numbers[i], list_of_numbers[min_idx] = list_of_numbers[min_idx], list_of_numbers[i]
    return list_of_numbers


def bubble_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n-1):
        for idx in range(n - i - 1):
            if list_of_numbers[idx + 1] < list_of_numbers[idx]:
                list_of_numbers[idx + 1], list_of_numbers[idx] = list_of_numbers[idx], list_of_numbers[idx + 1]
    return list_of_numbers


def main():
    my_data = read_data("numbers.csv")
    print(my_data)

    sort_method = selection_sort()
    # sort_method = bubble_sort()

    sorted_select = sort_method(my_data["series_3"])
    print(sorted_select)


if __name__ == '__main__':
    main()
