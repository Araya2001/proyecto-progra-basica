import service.csv_proxy

PRODUCT_CSV_FILE = "./productos.csv"
product_rows = []
service.csv_proxy.read(PRODUCT_CSV_FILE, product_rows)
ID_COL = 0
PRODUCT_NAME_COL = 1
PRODUCT_TYPE_COL = 2
PRODUCT_DESCRIPTION_COL = 3
PRODUCT_SCHEDULE_COL = 4
PRODUCT_PRICE_COL = 5


def find_all():
    return product_rows


def find_by_id(productos_id):
    try:
        for row in find_all():
            if row[ID_COL] == productos_id:
                return row
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuenta con el tipo de dato esperado!!")
    return None


def update(productos_id, productos_name,
           productos_type,
           productos_description,
           productos_schedule,
           productos_price):
    is_valid = False
    try:
        for row in find_all():
            if row[ID_COL] == productos_id:
                is_valid = True
                find_all().remove(row)
        if is_valid:
            find_all().append([productos_id, productos_name, productos_type, productos_description,
                               productos_schedule, productos_price])
            service.csv_proxy.write(PRODUCT_CSV_FILE, find_all())
            return True
    except(AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!")
    return False


def save(productos_name,
         productos_type,
         productos_description,
         productos_schedule,
         productos_price):
    try:
        last_id = service.csv_proxy.get_last_id(find_all()) + 1
        service.csv_proxy.write_append(PRODUCT_CSV_FILE, [[last_id,
                                                          productos_name,
                                                          productos_type,
                                                          productos_description,
                                                          productos_schedule,
                                                          productos_price]])
        find_all().append([last_id,
                           productos_name,
                           productos_type,
                           productos_description,
                           productos_schedule,
                           productos_price])
        return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!")
    return False


def delete(productos_id):
    try:
        for row in find_all():
            if row[ID_COL] == productos_id:
                find_all().remove(row)
                service.csv_proxy.write(PRODUCT_CSV_FILE, find_all())
                return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False
