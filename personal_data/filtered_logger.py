#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): Fields to be obfuscated.
        redaction (str): String used to replace field values.
        message (str): Log message containing fields.
        separator (str): Character separating fields in the log message.

    Returns:
        str: The log message with obfuscated fields.
    """
    # Join the fields into a single regex pattern
    pattern = f"({'|'.join(re.escape(field)
                           for field in fields)})=(.*?){re.escape(separator)}"

    # Use re.sub to replace the matched field values with the redaction
    return re.sub(pattern, lambda m: f"{m.group(1)}={
                  redaction}{separator}", message)
