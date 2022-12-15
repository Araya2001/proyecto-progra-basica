import service.csv_proxy

SALES_CSV_FILE = "./sales.csv"
sales_rows = []
service.csv_proxy.read(SALES_CSV_FILE, sales_rows)
ID_COL = 0
SALES_TOTAL_COL = 1
SALES_PRODUCTOS_ADQUIRIDOS_COL = 2
SALES_METODO_PAGO_COL = 3
SALES_INFO_COMPRADOR_COL = 4
SALES_INFO_VENDEDOR_COL = 5
SALES_FECHA_VENTA_COL = 6


def find_all():
    return sales_rows


def find_by_id(id_sales):
    try:
        for row in find_all():
            if row[ID_COL] == id_sales:
                return row
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return None


def update(id_sales, sales_total,
           productos_adquiridos,
           metodo_pago,
           info_comprador,
           info_vendedor,
           fecha_venta):
    is_valid = False
    try:
        for row in find_all():
            if row[ID_COL] == id_sales:
                is_valid = True
                find_all().remove(row)
        if is_valid:
            find_all().append([id_sales, sales_total,
                               productos_adquiridos,
                               metodo_pago,
                               info_comprador,
                               info_vendedor,
                               fecha_venta])

            service.csv_proxy.write(SALES_CSV_FILE, find_all())
            return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def save(sales_total,
         productos_adquiridos,
         metodo_pago,
         info_comprador,
         info_vendedor,
         fecha_venta):
    try:
        last_id = service.csv_proxy.get_last_id(find_all()) + 1
        service.csv_proxy.write_append(SALES_CSV_FILE, [[last_id, sales_total,
                                                         productos_adquiridos,
                                                         metodo_pago,
                                                         info_comprador,
                                                         info_vendedor,
                                                         fecha_venta]])
        find_all().append([last_id, sales_total,
                           productos_adquiridos,
                           metodo_pago,
                           info_comprador,
                           info_vendedor,
                           fecha_venta])
        return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def delete(id_sales):
    try:
        for row in find_all():
            if row[ID_COL] == id_sales:
                find_all().remove(row)
                service.csv_proxy.write(SALES_CSV_FILE, find_all())
                return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def SALES_NAME_COL():
    return None
