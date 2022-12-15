import service.csv_proxy

PROVIDER_CSV_FILE = "./provider.csv"
provider_rows = []
service.csv_proxy.read(PROVIDER_CSV_FILE, provider_rows)
ID_COL = 0
PROVIDER_NAME_COL = 1
PROVIDER_TYPE_COL = 2
PROVIDER_ROUTE_START_COL = 3
PROVIDER_ROUTE_END_COL = 4
PROVIDER_IS_CONTINENTAL_COL = 5


def find_all():
    return provider_rows


def find_by_id(id_provider):
    try:
        for row in find_all():
            if row[ID_COL] == id_provider:
                return row
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return None


def update(id_provider, provider_name, provider_type, provider_route_start, provider_route_end,
           provider_is_continental):
    is_valid = False
    try:
        for row in find_all():
            if row[ID_COL] == id_provider:
                is_valid = True
                find_all().remove(row)
        if is_valid:
            find_all().append(
                [id_provider, provider_name, provider_type, provider_route_start, provider_route_end,
                 provider_is_continental])
            service.csv_proxy.write(PROVIDER_CSV_FILE, find_all())
            return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def save(provider_name, provider_type, provider_route_start, provider_route_end,
         provider_is_continental):
    try:
        last_id = service.csv_proxy.get_last_id(find_all()) + 1

        service.csv_proxy.write_append(PROVIDER_CSV_FILE, [[last_id, provider_name,
                                                           provider_type,
                                                           provider_route_start,
                                                           provider_route_end,
                                                           provider_is_continental]])
        find_all().append([last_id, provider_name,
                           provider_type,
                           provider_route_start,
                           provider_route_end,
                           provider_is_continental])
        return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False


def delete(id_provider):
    try:
        for row in find_all():
            if row[ID_COL] == id_provider:
                find_all().remove(row)
                service.csv_proxy.write(PROVIDER_CSV_FILE, find_all())
                return True
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
    return False
