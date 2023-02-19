#!/usr/bin/python

import json
import os, sys
import pathlib
from glob import glob


def get_json_object(folder):

    f = open(folder+'/info.json')
    obj = json.load(f)
    f.close()
    obj["bild"] = f'{folder}/bild.jpg'

    with open(folder+'/url.url', encoding='utf-8') as f2:
        lines = f2.readlines()
        for line in lines:
            if line.startswith('URL='):
                obj["url"] = line[4:].rstrip()
    return obj


def start():
    print(f"{pathlib.Path().resolve()}sorter/*/")
    folders = glob(f"{pathlib.Path().resolve()}/sorter/*/", recursive=True)
    list = []

    for folder in folders:
        list.append(get_json_object(folder))

    with open(f'{pathlib.Path().resolve()}\\sorter.json', 'w', encoding='utf-8') as wd:
        json.dump(list, wd, ensure_ascii=False)


start()

