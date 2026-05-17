#!/usr/bin/env python3

from argparse import ArgumentParser
from os.path import basename, exists
from shutil import move
from tempfile import TemporaryDirectory
from urllib import request
from zipfile import ZipFile

from settings import NERD_PATCHER, SRC_FILES

# FRCD_URL = "https://github.com/tonsky/FiraCode/releases/download/6.2/Fira_Code_v6.2.zip"
JBMN_URL = "https://github.com/JetBrains/JetBrainsMono/releases/download/v2.304/JetBrainsMono-2.304.zip"
PLEX_URL = "https://github.com/IBM/plex/releases/download/%40ibm%2Fplex-sans-jp%403.0.0/ibm-plex-sans-jp.zip"
NERD_URL = (
    "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FontPatcher.zip"
)


def main():
    parser = ArgumentParser(description="File downloader for Firple Generator")
    parser.add_argument(
        "-a", "--all", action="store_true", help="download all files (default)"
    )
    parser.add_argument(
        "--jb-mono", action="store_true", help="download jetbrains mono"
    )
    parser.add_argument("--plex-sans", action="store_true", help="download plex sans")
    parser.add_argument(
        "--font-patcher", action="store_true", help="download nerd font patcher"
    )
    args = parser.parse_args()

    if not (args.jb_mono or args.plex_sans or args.font_patcher):
        args.all = True

    if args.all or args.jb_mono:
        print("JetBrains Mono...")
        jb_mono()
    if args.all or args.plex_sans:
        print("Plex Sans...")
        plex_sans()
    if args.all or args.font_patcher:
        print("Font Patcher...")
        font_patcher()


def jb_mono():
    with TemporaryDirectory() as tmpdir:
        # download
        path = f"{tmpdir}/JetBransMono.zip"
        request.urlretrieve(JBMN_URL, path)
        # extract
        with ZipFile(path) as zf:
            for weight in ["Regular", "Bold", "Italic", "BoldItalic"]:
                outpath = SRC_FILES[weight][0]
                name = basename(outpath)
                tmppath = zf.extract(f"fonts/ttf/{name}", tmpdir)
                move(tmppath, outpath)


def plex_sans():
    with TemporaryDirectory() as tmpdir:
        # download
        path = f"{tmpdir}/PlexSans.zip"
        request.urlretrieve(PLEX_URL, path)
        # extract
        with ZipFile(path) as zf:
            for weight in ["Regular", "Bold"]:
                outpath = SRC_FILES[weight][1]
                name = basename(outpath)
                tmppath = zf.extract(
                    f"ibm-plex-sans-jp/fonts/complete/ttf/hinted/{name}",
                    tmpdir,
                )
                move(tmppath, outpath)


def font_patcher():
    with TemporaryDirectory() as tmpdir:
        # download
        path = f"{tmpdir}/FontPacher.zip"
        request.urlretrieve(NERD_URL, path)
        # extract
        with ZipFile(path) as zf:
            zf.extractall(NERD_PATCHER.rpartition("/")[0])
        assert exists(NERD_PATCHER)


if __name__ == "__main__":
    main()
