# utils.py

import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from typing import Dict, List, Optional

from payment_processor.config import Config
from payment_processor.exceptions import (
    PaymentProcessorError,
    PaymentProcessorException,
)
from payment_processor.models import (
    Payment,
    PaymentMethod,
    PaymentStatus,
    User,
)

logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user."""
    return hmac.compare_digest(stored_password, hash_password(provided_password))

def generate_token() -> str:
    """Generate a random token."""
    return secrets.token_urlsafe(32)

def is_valid_email(email: str) -> bool:
    """Check if email is valid."""
    try:
        from email.utils import parseaddr
        name, email = parseaddr(email)
        return "@" in email
    except Exception as e:
        logger.error(f"Error validating email: {e}")
        return False

def validate_payment(payment: Payment) -> bool:
    """Validate a payment."""
    if payment.status!= PaymentStatus.pending:
        return False
    if not payment.method:
        return False
    if not payment.method.user_id:
        return False
    return True

def validate_payment_method(payment_method: PaymentMethod) -> bool:
    """Validate a payment method."""
    if not payment_method.user_id:
        return False
    if not payment_method.method:
        return False
    return True

def validate_user(user: User) -> bool:
    """Validate a user."""
    if not user.id:
        return False
    if not user.email:
        return False
    if not is_valid_email(user.email):
        return False
    return True

def get_config_value(key: str, default: Optional[str] = None) -> str:
    """Get a config value."""
    return Config.get(key, default)

def get_config_values(keys: List[str]) -> Dict[str, str]:
    """Get multiple config values."""
    return {key: Config.get(key) for key in keys}