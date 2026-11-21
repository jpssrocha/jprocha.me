#!/usr/bin/env python3
"""Generate publications.yml (Quarto listing data) from scientific_papers.bib."""

from __future__ import annotations

import json
import subprocess
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "scientific_papers.bib"
OUT = ROOT / "publications.yml"
MONTHS = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)


def _inline(nodes: list[dict]) -> str:
    parts: list[str] = []
    for node in nodes:
        kind = node["t"]
        value = node.get("c")
        if kind == "Str":
            parts.append(value)
        elif kind in ("Space", "SoftBreak", "LineBreak"):
            parts.append(" ")
        elif kind in ("Emph", "Strong", "Strikeout", "Superscript",
                      "Subscript", "SmallCaps"):
            parts.append(_inline(value))
        elif kind == "Span":
            parts.append(_inline(value[1]))
        elif kind in ("Link", "Image"):
            parts.append(_inline(value[1]))
        elif kind == "Cite":
            parts.append(_inline(value[1]))
        elif kind == "RawInline":
            parts.append(value[1])
        elif kind == "Quoted":
            parts.append(_inline(value[1]))
        elif kind == "Code":
            parts.append(value[1])
        elif kind == "Math":
            parts.append(value[1])
    return "".join(parts)


def _text(value: dict) -> str:
    kind = value["t"]
    if kind == "MetaString":
        return value["c"]
    if kind == "MetaInlines":
        return _inline(value["c"]).strip()
    if kind == "MetaBool":
        return str(value["c"]).lower()
    return ""


def _date_and_label(issued: str) -> tuple[str, str]:
    parts = issued.split("-")
    year = parts[0]
    if len(parts) > 1 and parts[1].isdigit():
        month = int(parts[1])
        if 1 <= month <= 12:
            return issued, f"{MONTHS[month - 1]} {year}"
    return issued, year


def main() -> None:
    result = subprocess.run(
        ["quarto", "pandoc", "--standalone", "--from=bibtex", "--to=json", str(BIB)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    doc = json.loads(result.stdout)
    refs = doc.get("meta", {}).get("references", {}).get("c", [])

    entries = []
    for ref in refs:
        fields = {key: _text(value) for key, value in ref["c"].items()}
        date, label = _date_and_label(fields.get("issued", ""))
        if fields.get("type") == "thesis":
            school = fields.get("school") or fields.get("publisher")
            genre = fields.get("genre")
            venue = ", ".join(part for part in (genre, school) if part)
        elif fields.get("container-title"):
            venue = fields["container-title"]
        elif fields.get("publisher"):
            venue = fields["publisher"]
        elif fields.get("genre"):
            venue = fields["genre"]
        else:
            venue = fields.get("type", "")
        if fields.get("doi"):
            doi = fields["doi"]
            link = (
                f'<a href="{escape(f"https://doi.org/{doi}", quote=True)}">'
                f'{escape(doi).replace("/", "/<wbr>")}</a>'
            )
        elif fields.get("url"):
            url = fields["url"]
            link = f'<a href="{escape(url, quote=True)}">link</a>'
        else:
            link = ""
        entries.append(
            {
                "title": fields.get("title", ""),
                "venue": venue,
                "date": date,
                "when": label,
                "doi": link,
            }
        )

    entries.sort(key=lambda entry: entry["date"], reverse=True)
    OUT.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
