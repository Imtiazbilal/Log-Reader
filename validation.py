def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-INPUT-']) == 0:
        values_invalid.append('File name not given')
        is_valid = False

    result = {"is_valid": is_valid, "values_invalid": values_invalid}
    return result


def validate1(values):
    is_valid = True
    values_invalid = []

    if len(values['-OUTPUT-']) == 4:
        values_invalid.append('csv file not given')
        is_valid = False

    result = {"is_valid": is_valid, "values_invalid": values_invalid}
    return result


def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += (' ' + value_invalid)

    return error_message
