import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): List of fields to be obfuscated.
        redaction (str): The string to replace the field values with.
        message (str): The log message containing the fields.
        separator (str): The separator string between fields in the log message.

    Returns:
        str: The log message with obfuscated fields.
    """
    # Create a regex pattern that matches fields to be obfuscated
    pattern = f"({'|'.join(fields)})=.*?{separator}"

    # Substitute the matched field values with the redaction string
    return re.sub(pattern, lambda m: m.group(0).split(
        '=')[0] + f'={redaction}{separator}', message)
