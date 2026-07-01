"""Contract tests for the Production Agent Observatory."""

import pytest

from src.tracer import AgentTracer
from src.metrics import MetricsCollector
from src.alerter import AnomalyAlerter, AlertSeverity


class TestAgentTracer:
    """Tracer must create and nest spans correctly."""

    def test_tracer_creates_nested_spans(self):
        tracer = AgentTracer()

        parent = tracer.start_span("agent_run")
        child = tracer.start_span("llm_call", parent_id=parent.span_id)
        completed_child = tracer.end_span(child.span_id)
        completed_parent = tracer.end_span(parent.span_id)

        assert completed_child.end_time is not None, "Child span must have end_time"
        assert completed_parent.end_time is not None, "Parent span must have end_time"
        assert child.parent_id == parent.span_id, "Child must reference parent"


class TestMetricsCollector:
    """Metrics collector must aggregate measurements correctly."""

    def test_metrics_collector_aggregates_correctly(self):
        collector = MetricsCollector()

        collector.record_latency(100.0)
        collector.record_latency(200.0)
        collector.record_latency(300.0)
        collector.record_cost(0.01)
        collector.record_cost(0.02)
        collector.record_tokens(500)
        collector.record_tokens(1000)

        summary = collector.get_summary()

        assert summary.total_requests == 3, "Must count all latency records"
        assert abs(summary.total_cost_usd - 0.03) < 0.001, "Must sum costs"
        assert summary.total_tokens == 1500, "Must sum tokens"
        assert summary.avg_latency_ms == 200.0, "Must average latencies"


class TestAnomalyAlerter:
    """Alerter must trigger alerts when thresholds are breached."""

    def test_alerter_triggers_on_threshold_breach(self):
        alerter = AnomalyAlerter(latency_threshold_ms=1000.0)

        alerts = alerter.check_anomaly(latency_ms=5000.0)

        assert len(alerts) > 0, "Must trigger at least one alert"
        assert alerts[0].current_value == 5000.0, "Must report the current value"
        assert alerts[0].threshold == 1000.0, "Must report the threshold"
        assert alerts[0].severity in AlertSeverity, "Severity must be valid"
