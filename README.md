# Production Agent Observatory — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect Advanced · Project 6.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P6: Production Agent Observatory

Build an observability platform for production LLM agents with distributed tracing, cost/latency/token metrics, anomaly detection, and a dashboard API.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.cli --dashboard
```

## Running Tests

```bash
pytest tests/ -v
```

## Project Structure

```
src/
  tracer.py      — Distributed tracing with nested spans
  metrics.py     — Cost, latency, and token metrics collection
  alerter.py     — Anomaly detection and alerting
  dashboard.py   — Dashboard API
  cli.py         — Command-line interface
tests/
  test_observatory.py — Contract tests
```
