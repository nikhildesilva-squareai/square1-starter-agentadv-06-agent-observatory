"""Distributed tracing with nested span support for agent workflows."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Span:
    """A single trace span representing one operation."""
    span_id: str
    name: str
    parent_id: str | None
    start_time: str
    end_time: str | None = None
    metadata: dict = field(default_factory=dict)
    children: list["Span"] = field(default_factory=list)


class AgentTracer:
    """Creates and manages nested trace spans for agent operations."""

    def __init__(self):
        """Initialise the tracer with an empty span store."""
        self._spans: dict[str, Span] = {}

    def start_span(self, name: str, *, parent_id: str | None = None) -> Span:
        """Start a new trace span.

        Creates a span representing an operation, optionally nested
        under a parent span to build a trace tree.

        Args:
            name: Human-readable name for this operation.
            parent_id: Optional parent span ID for nesting.

        Returns:
            The newly created Span.
        """
        raise NotImplementedError("TODO: implement span creation with nesting")

    def end_span(self, span_id: str) -> Span:
        """End an active span and record its duration.

        Args:
            span_id: The ID of the span to close.

        Returns:
            The completed Span with end_time set.
        """
        raise NotImplementedError("TODO: implement span completion")
