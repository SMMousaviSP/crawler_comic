def normalize_string(raw_string):
    """ Normalize string by replacing all spaces with '_' and change all
    characters to lower case.

    :param raw_string: Input string to be normalized.
    :returns: Normalized string without uppercase or space.

    """
    return raw_string.strip().lower().replace(' ', '_').replace('/', '_').replace('\\', '_')
