import service.csv_proxy

EMPLOYEE_CSV_FILE = "./employee.csv"
employee_rows = []
service.csv_proxy.read(EMPLOYEE_CSV_FILE, employee_rows)
ID_COL = 0
EMPLOYEE_NAME_COL = 1
EMPLOYEE_LASTNAME_COL = 2
EMPLOYEE_ID_COL = 3
EMPLOYEE_SALARY_COL = 4
EMPLOYEE_POSITION_COL = 5


def find_all():
    return employee_rows


def find_by_id(id_provider):
    try:
        for row in find_all():
            if row[ID_COL] == id_provider:
                return row
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return None


def update(id_employee, employee_name,
           employee_lastname,
           employee_id,
           employee_salary,
           employee_position):
    is_valid = False
    try:
        for row in find_all():
            if row[ID_COL] == id_employee:
                is_valid = True
                find_all().remove(row)
        if is_valid:
            find_all().append(
                [id_employee, employee_name, employee_lastname, employee_id, employee_salary,
                 employee_position])
            service.csv_proxy.write(EMPLOYEE_CSV_FILE, find_all())
            return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def save(employee_name,
         employee_lastname,
         employee_id,
         employee_salary,
         employee_position):
    try:
        last_id = service.csv_proxy.get_last_id(find_all()) + 1
        data = [last_id, employee_name,
                employee_lastname,
                employee_id,
                employee_salary,
                employee_position]
        service.csv_proxy.write_append(EMPLOYEE_CSV_FILE, data)
        find_all().append(data)
        return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def delete(id_employee):
    try:
        for row in find_all():
            if row[ID_COL] == id_employee:
                find_all().remove(row)
                service.csv_proxy.write(EMPLOYEE_CSV_FILE, find_all())
                return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False
