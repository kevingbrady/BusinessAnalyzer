def get_keys_at_indent(json_data, target_indent, current_indent=0):
    """
    Recursively finds keys at a specific indent level in JSON data.

    Args:
        json_data: The JSON data (dict or list).
        target_indent: The target indentation level (integer).
        current_indent: The current indentation level (internal use).

    Returns:
        A list of keys at the target indent level.
    """
    keys = []

    if isinstance(json_data, dict):
        if current_indent == target_indent:
            keys.extend(json_data.keys())
        else:
            for value in json_data.values():
                keys.extend(get_keys_at_indent(value, target_indent, current_indent + 1))
    elif isinstance(json_data, list):
        for item in json_data:
            keys.extend(get_keys_at_indent(item, target_indent, current_indent + 1))

    return keys

