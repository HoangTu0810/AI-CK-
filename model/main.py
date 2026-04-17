import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import tkinter as tk

from data import train_model
from gui.app import BlockerApp


def run_gui():
    root = tk.Tk()
    app = BlockerApp(root)
    root.mainloop()


def run_train():
    train_model.train_and_save()


def main():
    parser = argparse.ArgumentParser(description="Website Blocker AI")
    parser.add_argument("--train", action="store_true", help="Train the model using data/malicious_phish.csv")
    parser.add_argument("--gui", action="store_true", help="Run the desktop GUI")
    args = parser.parse_args()

    if args.train:
        run_train()
    elif args.gui:
        run_gui()
    else:
        parser.print_help()


if __name__ == "__main__":
    if os.path.abspath(os.getcwd()) != os.path.abspath(os.path.dirname(__file__)):
        sys.path.insert(0, os.path.dirname(__file__))
    main()
