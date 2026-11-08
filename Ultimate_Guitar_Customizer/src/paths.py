import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONTS = ROOT / "fonts"
STYLES = ROOT / "styles"


def slugify(text: str) -> str:
    """'B.C. Rich' -> 'bc_rich', "Filter'Tron" -> 'filtertron'."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace(".", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "_", text).strip("_")