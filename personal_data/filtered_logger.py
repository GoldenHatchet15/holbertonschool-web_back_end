#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Function to hide personal data.

    Args:
        fields (List[str]): Fields to be obfuscated.
        redaction (str): String used to replace field values.
        message (str): Log message containing fields.
        separator (str): Character separating fields in the log message.

    Returns:
        str: The log message with obfuscated fields.
    """
    for field in fields:
        message = re.sub(rf"{re.escape(field)}=(.*?){re.escape(separator)}",
                         f'{field}={redaction}{separator}', message)
    return message
