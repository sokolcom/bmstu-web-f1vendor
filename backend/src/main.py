import argparse

from app import run_app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_port', type=int, default=8888)
    parser.add_argument('--db_port', type=str, default=5432)
    parser.add_argument('--readonly', type=str, default="true")
    args = parser.parse_args()

    run_app(args)
    