#!/usr/bin/env python3
"""
Filtering module
"""
import logging
import re
from typing import List

# Define PII fields to be obfuscated in the logs
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class for filtering PII data """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the formatter with a list of fields to redact """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log message by redacting sensitive information """
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)

def get_logger() -> logging.Logger:
    """
    Creates and returns a logger object with specified settings.
    
    The logger will obfuscate PII and log up to INFO level.
    """
    # Create a logger named "user_data"
    logger = logging.getLogger("user_data")
    
    # Set log level to INFO
    logger.setLevel(logging.INFO)
    
    # Prevent propagation to parent loggers
    logger.propagate = False

    # Create a StreamHandler
    stream_handler = logging.StreamHandler()

    # Use RedactingFormatter with PII_FIELDS
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stream_handler)

    return logger