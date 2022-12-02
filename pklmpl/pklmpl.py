import os
import pickle
import argparse
from matplotlib.figure import Figure
from matplotlib import pylab


def pickle_mpl_figure(fig: Figure, path: str):
    """
    Save an mpl figure using pickle
    """
    with open(path, "wb") as outfile:
        pickle.dump(fig, outfile)


def open_pickled_mpl_figure(path: str):
    """
    Open a pickled matplotlib figure
    path (str): full path to the pickle file
    """
    with open(path, "rb") as infile:
        fig = pylab.figure(pickle.load(infile))

    pylab.show(block=True)


def main():
    parser = argparse.ArgumentParser(description="Open a pickled matplotlib figure")
    parser.add_argument("path", help="full path to the pickle file")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        raise Exception(f"Wong path: {args.path}")

    open_pickled_mpl_figure(args.path)


if __name__ == "__main__":
    main()
