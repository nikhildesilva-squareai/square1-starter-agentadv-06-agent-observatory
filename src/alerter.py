"""Anomaly detection and alerting for agent metrics."""

from dataclasses import dataclass
from enum import Enum


class AlertSeverity(Enum):
    """Alert severity levels."""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class Alert:
    """A triggered alert."""
    metric: str
    severity: AlertSeverity
    current_value: float
    threshold: float
    message: str


class AnomalyAlerter:
    """Monitors metrics and triggers alerts on anomalies."""

    def __init__(
        self,
        *,
        latency_threshold_ms: float = 5000.0,
        cost_threshold_usd: float = 1.0,
        token_threshold: int = 100_000,
    ):
        """Initialise the alerter with configurable thresholds.

        Args:
            latency_threshold_ms: Latency above which to alert.
            cost_threshold_usd: Per-request cost above which to alert.
            token_threshold: Token count above which to alert.
        """
        self.latency_threshold_ms = latency_threshold_ms
        self.cost_threshold_usd = cost_threshold_usd
        self.token_threshold = token_threshold

    def check_anomaly(
        self, *, latency_ms: float | None = None, cost_usd: float | None = None, tokens: int | None = None
    ) -> list[Alert]:
        """Check metric values against thresholds and return any alerts.

        Args:
            latency_ms: Current latency to check.
            cost_usd: Current cost to check.
            tokens: Current token count to check.

        Returns:
            A list of Alert objects for any breached thresholds.
        """
        raise NotImplementedError("TODO: implement anomaly detection against thresholds")
