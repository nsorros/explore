from functools import partial
from glob import glob
import importlib.util
import random
import sys
import os

from pynput import keyboard

try:
    from rich import print
except ImportError:
    pass
import catalogue
import typer


document_processors = catalogue.create("explore", "document_processors")
app = typer.Typer()


@document_processors.register("txt")
def txt_document_processor(document):
    return document


def split_document(document, snippet_length):
    snippets = [
        document[i : i + snippet_length]
        for i in range(0, len(document), snippet_length)
    ]
    return snippets


def get_snippet(dir_path, snippet_length, split, document_processor_name):
    filepaths = glob(dir_path + "**/*.*", recursive=True)
    random.shuffle(filepaths)
    filepath = filepaths[0]

    with open(filepath) as f:
        document = f.read()

    process_document = document_processors.get(document_processor_name)
    document = process_document(document)
    if split:
        snippets = split_document(document, snippet_length)
        random.shuffle(snippets)
        return snippets[0]
    else:
        return document


def on_press(key, dir_path, snippet_length, split, document_processor_name):
    if key == keyboard.Key.space:
        os.system("clear")
        snippet = get_snippet(dir_path, snippet_length, split, document_processor_name)
        print(snippet)


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.KeyCode(char="q"):
        return False


@app.command()
def explore(
    dir_path,
    snippet_length: int = 2000,
    split: bool = True,
    code_path=None,
    document_processor_name="txt",
):
    if code_path:
        spec = importlib.util.spec_from_file_location("python", code_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    snippet = get_snippet(dir_path, snippet_length, split, document_processor_name)
    print(snippet)

    with keyboard.Listener(
        on_press=partial(
            on_press,
            dir_path=dir_path,
            snippet_length=snippet_length,
            split=split,
            document_processor_name=document_processor_name,
        ),
        on_release=on_release,
    ) as listener:
        listener.join()


if __name__ == "__main__":
    app()
