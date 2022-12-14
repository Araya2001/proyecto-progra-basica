import csv


def read(file, csv_rows):
    try:
        with open(file, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            for scoped_row in csv_reader:
                csv_rows.append(scoped_row)
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


def write_append(file, csv_rows):
    try:
        with open(file, mode="a+") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for scoped_row in csv_rows:
                csv_writer.writerow(scoped_row)
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


def write(file, csv_rows):
    try:
        with open(file, mode="w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for scoped_row in csv_rows:
                csv_writer.writerow(scoped_row)
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


def validate_unique_constraint(csv_rows):
    try:
        scoped_id = []
        for scoped_row in csv_rows:
            scoped_id.append(scoped_row[0])
        if len(scoped_id) == len(set(scoped_id)):
            return True
        else:
            return False
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


def get_last_id(csv_rows):
    try:
        if len(csv_rows) != 0:
            return csv_rows[len(csv_rows) - 1][0]
        else:
            return -1
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")

# rows2 = []
# read("./test-file-1.csv", rows2)
# print(get_last_id(rows2))
#
# print(validate_unique_constraint(rows2))
