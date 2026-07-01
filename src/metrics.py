"""Metrics collection for cost, latency, and token usage."""

from dataclasses import dataclass, field


@dataclass
class MetricsSummary:
    """Aggregated metrics summary."""
    total_requests: int
    total_cost_usd: float
    total_tokens: int
    avg_latency_ms: float
    p95_latency_ms: float


class MetricsCollector:
    """Collects and aggregates operational metrics for agents."""

    def __init__(self):
        """Initialise the metrics collector."""
        self._latencies: list[float] = []
        self._costs: list[float] = []
        self._tokens: list[int] = []

    def record_latency(self, latency_ms: float) -> None:
        """Record a request latency measurement.

        Args:
            latency_ms: Latency in milliseconds.
        """
        raise NotImplementedError("TODO: implement latency recording")

    def record_cost(self, cost_usd: float) -> None:
        """Record an API cost measurement.

        Args:
            cost_usd: Cost in US dollars.
        """
        raise NotImplementedError("TODO: implement cost recording")

    def record_tokens(self, token_count: int) -> None:
        """Record a token usage measurement.

        Args:
            token_count: Number of tokens used.
        """
        raise NotImplementedError("TODO: implement token recording")

    def get_summary(self) -> MetricsSummary:
        """Compute an aggregated metrics summary.

        Returns:
            A MetricsSummary with totals and percentiles.
        """
        raise NotImplementedError("TODO: implement metrics aggregation")
