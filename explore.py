from functools import partial
from glob import glob
import random
import sys
import os

from pynput import keyboard

try:
    from rich import print
except ImportError:
    pass
import typer


app = typer.Typer()


def split_document(document, snippet_length):
    snippets = [
        document[i : i + snippet_length]
        for i in range(0, len(document), snippet_length)
    ]
    return snippets


def get_snippet(dir_path, snippet_length, split):
    filepaths = glob(dir_path + "**/*.*", recursive=True)
    random.shuffle(filepaths)
    filepath = filepaths[0]

    with open(filepath) as f:
        document = f.read()

    if split:
        snippets = split_document(document, snippet_length)
        random.shuffle(snippets)
        return snippets[0]
    else:
        return document


def on_press(key, dir_path, snippet_length, split):
    if key == keyboard.Key.space:
        os.system("clear")
        snippet = get_snippet(dir_path, snippet_length, split)
        print(snippet)


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.KeyCode(char="q"):
        return False


@app.command()
def explore(dir_path, snippet_length: int = 2000, split: bool = True):
    snippet = get_snippet(dir_path, snippet_length, split)
    print(snippet)

    with keyboard.Listener(
        on_press=partial(
            on_press, dir_path=dir_path, snippet_length=snippet_length, split=split
        ),
        on_release=on_release,
    ) as listener:
        listener.join()


if __name__ == "__main__":
    app()
