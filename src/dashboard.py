"""Dashboard API for the Agent Observatory."""


class DashboardAPI:
    """Serves observatory data through a REST API."""

    def __init__(self, metrics_collector=None, tracer=None, alerter=None):
        """Initialise the dashboard API.

        Args:
            metrics_collector: MetricsCollector instance.
            tracer: AgentTracer instance.
            alerter: AnomalyAlerter instance.
        """
        self.metrics_collector = metrics_collector
        self.tracer = tracer
        self.alerter = alerter

    def create_app(self):
        """Create and return a FastAPI application.

        Returns:
            A configured FastAPI app with observatory endpoints.
        """
        raise NotImplementedError("TODO: implement FastAPI dashboard application")
