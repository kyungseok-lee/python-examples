from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from flask import Flask, abort, render_template, url_for


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "examples.json"


def load_examples() -> List[Dict[str, Any]]:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # Normalize and sort
    for item in data:
        item.setdefault("order", 0)
    data.sort(key=lambda x: x.get("order", 0))
    return data


app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

EXAMPLES = load_examples()
EXAMPLES_BY_SLUG = {e["slug"]: e for e in EXAMPLES}


@app.get("/")
def index():
    return render_template("index.html", examples=EXAMPLES)


@app.get("/example/<slug>")
def example(slug: str):
    item = EXAMPLES_BY_SLUG.get(slug)
    if not item:
        abort(404)
    return render_template("example.html", e=item)


@app.errorhandler(404)
def not_found(_):  # type: ignore[override]
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Debug server for local development
    app.run(host="0.0.0.0", port=8000, debug=True)

