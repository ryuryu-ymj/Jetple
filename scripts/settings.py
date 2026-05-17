FAMILY = "Jetple"
VERSION = "6.400"
COPYRIGHT = "Copyright 2021 negset\nCopyright 2026 ryuryu-ymj"

SRC_DIR = "src"
OUT_DIR = "out"
TMP_DIR = "tmp"
SRC_FILES = {
    "Regular": [
        f"{SRC_DIR}/JetBrainsMono-Regular.ttf",
        f"{SRC_DIR}/IBMPlexSansJP-Text.ttf",
    ],
    "Bold": [
        f"{SRC_DIR}/JetBrainsMono-Bold.ttf",
        f"{SRC_DIR}/IBMPlexSansJP-Bold.ttf",
    ],
    "Italic": [
        f"{SRC_DIR}/JetBrainsMono-Italic.ttf",
    ],
    "BoldItalic": [
        f"{SRC_DIR}/JetBrainsMono-BoldItalic.ttf",
    ],
}
NERD_PATCHER = f"{SRC_DIR}/FontPatcher/font-patcher"

PLEX_SCALE = 1.0
ITALIC_SKEW = 9
ITALIC_OFFSET = -100
SLIM_SCALE = 0.85

ITALIC_GLYPH_NAMES = []  # ["a", "b", "e", "f", "g", "k", "q"]
OVERWRITE_GLYPH_NAMES = []  # ["uni300C", "uni300D"]  # "「", "」"
FEATURE_GLYPH_NAMES = {
    "cv33": ["uni3000"],
    "ss11": [
        "uni3071",  # "ぱ"
        "uni3074",  # "ぴ"
        "uni3077",  # "ぷ"
        "uni307A",  # "ぺ"
        "uni307D",  # "ぽ"
        "uni309C",  # "゜"
        "uni30D1",  # "パ"
        "uni30D4",  # "ピ"
        "uni30D7",  # "プ"
        "uni30DA",  # "ペ"
        "uni30DD",  # "ポ"
        "uniFF9F",  # "ﾟ"
    ],
}
