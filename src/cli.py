"""Command-line interface for the Production Agent Observatory."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Production Agent Observatory")
    parser.add_argument("--dashboard", action="store_true", help="Launch the dashboard server")
    parser.add_argument("--port", type=int, default=8000, help="Dashboard port")
    args = parser.parse_args()

    if args.dashboard:
        from .dashboard import DashboardAPI
        api = DashboardAPI()
        app = api.create_app()
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=args.port)
    else:
        print("Use --dashboard to launch the observatory server.")


if __name__ == "__main__":
    main()
