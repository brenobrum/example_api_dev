from __future__ import annotations

from pathlib import Path


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
APP_DIR: Path = PROJECT_ROOT / "app"


def snake_to_pascal(value: str) -> str:
    return "".join(part.capitalize() for part in value.split("_") if part)


def singularize(word: str) -> str:
    if word.endswith("ies"):
        return f"{word[:-3]}y"
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content)


def write_or_update(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def ensure_init(path: Path) -> None:
    write_if_missing(path / "__init__.py", "")


def append_if_missing(path: Path, block: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    current: str = path.read_text() if path.exists() else ""
    if block not in current:
        separator: str = "\n" if current and not current.endswith("\n") else ""
        path.write_text(f"{current}{separator}{block}")
