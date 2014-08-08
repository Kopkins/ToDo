# todo setup.py
from distutils.core import setup
setup(
    name = "todo-gtk",
    packages = ["todo"],
    version = "0.1",
    description = "A simple to do list application written in python and gtk+3",
    author = "Kyle Hopkins",
    author_email = "kylehopkins1215@gmail.com",
    url = "https://github.com/Kopkins/ToDo",
    keywords = ["todo", "to", "do", "task", "list"],
    classifiers = [
        "Programming Language :: Python :: 3.4",
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Unix",
        "Topic :: Office/Business",
        "Topic :: Utilities"
        ]
    )
