import string
import os

snake_directory = os.path.dirname(os.path.abspath(__file__))

high_score_path = os.path.join(snake_directory, "high_score.txt")

font_path = os.path.join(snake_directory, "Pixolletta8px.ttf")

hh_closed_path = os.path.join(snake_directory, "hi-hat-closed.mp3")
hh_open_path = os.path.join(snake_directory, "hi-hat-open.mp3")


def file_create():
    with open(high_score_path, "w") as file:
        DEFAULT_STRING = "0"
        file.write(DEFAULT_STRING)
        return DEFAULT_STRING


def file_load():
    file_content = ""
    if not os.path.exists(high_score_path):
        file_content = file_create()
    with open(high_score_path, "r") as file:
        file_content = file.read()
        if not file_content.isdigit():
            file_create()
            file_content = file.read()
    return file_content


high_score = file_load()


def new_high_score(score):
    if score > int(high_score):
        with open(high_score_path, "w") as file:
            file.write(str(score))
