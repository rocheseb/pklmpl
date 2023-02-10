import os
import pickle
import argparse
from matplotlib.figure import Figure
from matplotlib import pylab


def pickle_mpl_figure(fig: Figure, path: str) -> None:
    """
    Save an mpl figure using pickle
    """
    with open(path, "wb") as outfile:
        pickle.dump(fig, outfile)


def open_pickled_mpl_figure(path: str) -> None:
    """
    Open a pickled matplotlib figure
    path (str): full path to the pickle file
    """
    with open(path, "rb") as infile:
        fig = pylab.figure(pickle.load(infile))

    pylab.show(block=True)


def pickle_to_png(path: str, outfile: str = "") -> None:
    """
    Open a pickled matplotlib figure and save it as a .png
    path (str): full path to the pickle file
    outfile (str): full path to the png file, if left as empty string, just use "path" with a png extension
    """

    with open(path, "rb") as infile:
        fig = pylab.figure(pickle.load(infile))

    if not outfile:
        outfile = path.replace(".pickle", ".png")
    fig.savefig(outfile)


def main():
    parser = argparse.ArgumentParser(description="Open a pickled matplotlib figure")
    parser.add_argument("path", help="full path to the pickle file")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["open", "png"],
        default="open",
        help="one of [open,png], use to either open up the figure or save it to a png",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        default="",
        help="Only used with the png mode, full path to the file of the output png file, if not given it will just replace '.pickle' with '.png' in the path argument",
    )
    args = parser.parse_args()

    if not os.path.exists(args.path):
        raise Exception(f"Wong path: {args.path}")

    if args.mode == "open":
        open_pickled_mpl_figure(args.path)
    elif args.mode == "png":
        pickle_to_png(args.path, args.outfile)


if __name__ == "__main__":
    main()
