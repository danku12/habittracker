import json

FAIL="data.json"


def lae_andmed():
    """Lae andmed failist."""
    try:
        with open(FAIL, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}


def salvesta_andmed(andmed):
    """Salvesta andmed faili."""
    with open(FAIL, "w", encoding="utf-8") as f:
        json.dump(andmed, f, indent=4, ensure_ascii=False)
