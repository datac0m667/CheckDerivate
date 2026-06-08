import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

STRATEGY_DIR = BASE_DIR / "strategies"

def load_strategy_names():

    files = STRATEGY_DIR.glob("*.json")

    return sorted([
        f.stem for f in files
    ])

def load_strategy(name):

    strategy_file = STRATEGY_DIR / f"{name}.json"

    if not strategy_file.exists():
        raise FileNotFoundError(
            f"Strategie-Datei nicht gefunden: {strategy_file}"
        )

    with open(
        strategy_file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)