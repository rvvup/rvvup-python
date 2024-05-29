from enum import Enum


class PaymentDeclineReason(str, Enum):
    ACCOUNT_CLOSED = "ACCOUNT_CLOSED"
    AMOUNT_LIMITS_EXCEEDED = "AMOUNT_LIMITS_EXCEEDED"
    CONSENT_MISSING = "CONSENT_MISSING"
    CVV2_FAILURE = "CVV2_FAILURE"
    FUNDING_INSTRUMENT_DECLINED = "FUNDING_INSTRUMENT_DECLINED"
    FUNDING_INSTRUMENT_EXPIRED = "FUNDING_INSTRUMENT_EXPIRED"
    FUNDING_INSTRUMENT_INVALID = "FUNDING_INSTRUMENT_INVALID"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    SUSPECTED_FRAUD = "SUSPECTED_FRAUD"

    def __str__(self) -> str:
        return str(self.value)
