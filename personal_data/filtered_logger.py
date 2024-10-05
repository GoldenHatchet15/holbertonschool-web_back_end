import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in the log message."""
    pattern = f"({'|'.join([re.escape(field)
                            for field in fields])})=([^'{separator}']+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
