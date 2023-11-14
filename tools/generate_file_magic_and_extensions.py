#!/usr/bin/python3

import os
import json
import binascii
from itertools import chain
from collections import namedtuple
import sys
from typing import Union, Tuple, List

here = os.path.abspath(os.path.dirname(__file__))

PureMagic = namedtuple(
    "PureMagic",
    (
        "magic",
        "byte_match",
        "offset",
        "extension",
        "mime_type",
        "name",
    ),
)

def _create_puremagic(x: List) -> PureMagic:
    return PureMagic(
        magic=x[0], byte_match=binascii.unhexlify(x[0].encode("ascii")), offset=x[1], extension=x[2], mime_type=x[3], name=x[4]
    )

def _magic_data(
    filename: Union[os.PathLike, str] = os.path.join(here, "magic_data.json"),
) -> Tuple[List[PureMagic], List[PureMagic], List[PureMagic]]:
    """Read the magic file"""
    with open(filename) as f:
        data = json.load(f)
    headers = sorted((_create_puremagic(x) for x in data["headers"]), key=lambda x: x.byte_match)
    footers = sorted((_create_puremagic(x) for x in data["footers"]), key=lambda x: x.byte_match)
    extensions = [_create_puremagic(x) for x in data["extension_only"]]
    return headers, footers, extensions

if __name__ == "__main__":
    headers, footers, extensions = _magic_data()

    print(sys.argv[1])
    os.chdir(sys.argv[1])
    if not os.path.exists("./magic_and_extensions"):
        os.mkdir("./magic_and_extensions")
    os.chdir("./magic_and_extensions")
    no_extension = 0
    for i in headers:
        print(i.magic)
        if os.path.exists(i.magic):
            continue
        os.mkdir(i.magic)

    for i in footers:
        print(i.magic)
        if os.path.exists(i.magic):
            continue
        os.mkdir(i.magic)

    for i in extensions:
        print(i.extension)
        if os.path.exists(i.extension[1:]):
            continue
        os.mkdir(i.extension[1:])