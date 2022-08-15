def format_name(f_name, l_name):
    """ Take a first and last name and format it to return the title case version of the name

    Args:
        f_name (string): first name
        l_name (string): last name

    Returns:
        string : title case version of combined first and last name
    """
    return f'{f_name.title()} {l_name.title()}'

print(format_name("thomas", "anderson"))