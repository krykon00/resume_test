"""Utility functions"""
import json
from pathlib import Path
from typing import Any

from PIL import Image


FILE_PATH = Path(__file__).parent.resolve()
LANGUAGES_PATH = f"{FILE_PATH}/languages"


def get_langs_names() -> dict[str, str]:
    """"Get dict of all aviable languages with their flags icons"""
    langs: dict[str, str] = dict()
    for item in Path(LANGUAGES_PATH).iterdir():
        if item.is_file():
            lang = str(item).split("/")[-1]
            lang = str(lang).split(".")[0]
            langs[lang.upper()] = item

    return langs


def read_json(file_path: str) -> dict[str, Any]:
    """Read json file"""
    with open(file_path) as f:
        return json.load(f)

def get_profile_pic() -> Image:
    """Load profle picture image"""

