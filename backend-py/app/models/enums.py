"""String enums mirroring the Prisma/Postgres enums exactly (value == name)."""

from __future__ import annotations

import enum


class TenantType(str, enum.Enum):
    INSURER = "INSURER"
    HOSPITAL = "HOSPITAL"


class Role(str, enum.Enum):
    PLATFORM_ADMIN = "PLATFORM_ADMIN"
    HOSPITAL_ADMIN = "HOSPITAL_ADMIN"
    INSURER_ADMIN = "INSURER_ADMIN"
    HOSPITAL_STAFF = "HOSPITAL_STAFF"
    INSURER_ADJUDICATOR = "INSURER_ADJUDICATOR"
    PATIENT = "PATIENT"


class UserStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"


class ClaimType(str, enum.Enum):
    CASHLESS = "CASHLESS"
    REIMBURSEMENT = "REIMBURSEMENT"


class Verdict(str, enum.Enum):
    APPROVE = "APPROVE"
    DENY = "DENY"
    QUERY = "QUERY"


class ClaimStatus(str, enum.Enum):
    SUBMITTED = "SUBMITTED"
    PROCESSING = "PROCESSING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    QUERIED = "QUERIED"
    UNDER_REVIEW = "UNDER_REVIEW"
    SETTLED = "SETTLED"


class FraudSeverity(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class BedStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    MAINTENANCE = "MAINTENANCE"


class AdmissionStatus(str, enum.Enum):
    ADMITTED = "ADMITTED"
    DISCHARGED = "DISCHARGED"


class ClaimEventType(str, enum.Enum):
    SUBMITTED = "SUBMITTED"
    AI_STARTED = "AI_STARTED"
    AI_DECISION = "AI_DECISION"
    FRAUD_FLAGGED = "FRAUD_FLAGGED"
    QUERY_RAISED = "QUERY_RAISED"
    OVERRIDDEN = "OVERRIDDEN"
    SETTLED = "SETTLED"
    NOTE = "NOTE"
