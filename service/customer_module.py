import service.csv_proxy

CUSTOMER_CSV_FILE = "./customer.csv"
customer_rows = []
service.csv_proxy.read(CUSTOMER_CSV_FILE, customer_rows)
ID_COL = 0
CUSTOMER_NAME_COL = 1
CUSTOMER_ID_COL = 2
CUSTOMER_PHONE_NUMBER_COL = 3
CUSTOMER_ADDRESS_COL = 4


def find_all():
    return customer_rows


def find_by_id(id_customer):
    try:
        for row in find_all():
            if int(row[ID_COL]) == int(id_customer):
                return row
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return None


def update(id_customer, customer_name, customer_id, customer_phone_number, customer_address):
    is_valid = False
    try:
        for row in find_all():
            if int(row[ID_COL]) == int(id_customer):
                is_valid = True
                find_all().remove(row)
        if is_valid:
            find_all().append(
                [id_customer, customer_name, customer_id, customer_phone_number, customer_address])
            service.csv_proxy.write(CUSTOMER_CSV_FILE, find_all())
            return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def save(customer_name, customer_id, customer_phone_number, customer_address):
    try:
        last_id = int(service.csv_proxy.get_last_id(find_all())) + 1
        service.csv_proxy.write_append(CUSTOMER_CSV_FILE, [[last_id, customer_name,
                                                           customer_id,
                                                           customer_phone_number,
                                                           customer_address]])
        find_all().append([last_id, customer_name,
                           customer_id,
                           customer_phone_number,
                           customer_address])
        return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def delete(id_customer):
    try:
        for row in find_all():
            if int(row[ID_COL]) == int(id_customer):
                find_all().remove(row)
                service.csv_proxy.write(CUSTOMER_CSV_FILE, find_all())
                return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False
