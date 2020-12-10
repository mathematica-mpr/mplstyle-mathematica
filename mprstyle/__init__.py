import matplotlib as mpl
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import seaborn as sns

MPR_COLORS = {
    "green": "#046B5C",
    "blue": "#0B2949",
    "teal": "#189394",
    "cyan": "#189394",
    "gold": "#F1B51C",
    "yellow": "#F1B51C",
    "red": "#D02B27",
    "lime": "#17A673",
    "light green": "#17A673",
    "beige": "#E0D4B5",
    "grey": "#5B6771",
    "gray": "#5B6771",
    "black": "#000000",
    "white": "#ffffff",
}

MPR_COLORS_75 = {
    "green": "#488378",
    "blue": "#414b66",
    "teal": "#65a7a9",
    "cyan": "#65a7a9",
    "gold": "#f4c55c",
    "yellow": "#f4c55c",
    "red": "#d9654a",
    "lime": "#6ab790",
    "light green": "#6ab790",
    "beige": "#e7ddc6",
    "grey": "#7b818a",
    "gray": "#7b818a",
    "black": "#bdbdbd",
    "white": "#ffffff",
}

MPR_COLORS_50 = {
    "green": "#7fa29a",
    "blue": "#72748b",
    "teal": "#96bec1",
    "cyan": "#96bec1",
    "gold": "#f8d690",
    "yellow": "#f8d690",
    "red": "#e39378",
    "lime": "#9ccab0",
    "light green": "#9ccab0",
    "beige": "#eee7d6",
    "grey": "#9fa2a9",
    "gray": "#9fa2a9",
    "black": "#7e7e7e",
    "white": "#ffffff",
}

MPR_COLORS_25 = {
    "green": "#b8c8c4",
    "blue": "#acacba",
    "teal": "#c8dadb",
    "cyan": "#c8dadb",
    "gold": "#fbe8c4",
    "yellow": "#fbe8c4",
    "red": "#efc4b3",
    "lime": "#cbe2d3",
    "light green": "#cbe2d3",
    "beige": "#f5f1e8",
    "grey": "#c8c9cc",
    "gray": "#c8c9cc",
    "black": "#3f3f3f",
    "white": "#ffffff",
}

def apply(style="default"):
    sns.set(font="Montserrat", palette=[MPR_COLORS[x] for x in ["green", "gold", "blue", "red", "teal", "lime", "beige", "grey", "black"]])  # , style="ticks")

    mpl.rc("text", color=MPR_COLORS["grey"])
    mpl.rc("figure", facecolor=MPR_COLORS_25["beige"], edgecolor="none", dpi=300)
    mpl.rc("grid", color=MPR_COLORS_50["grey"], linestyle=":", linewidth=1.0)
    mpl.rc("axes", facecolor=MPR_COLORS_25["beige"], edgecolor="none", labelcolor=MPR_COLORS["grey"])
    mpl.rc("xtick", color=MPR_COLORS["grey"], labelsize="small")
    mpl.rc("ytick", color=MPR_COLORS["grey"], labelsize="small")
    mpl.rc("legend", framealpha=1.0, fontsize="small")

# AXIS_FONT = {"fontname": "Montserrat"}
# TITLE_FONT = {"fontname": "Zilla Slab Medium"}

# register_matplotlib_converters()

PCT_FORMATTER = mtick.FuncFormatter(lambda x, pos: "{:.0f}%".format(x * 100))
DATE_FORMATTER = mdates.ConciseDateFormatter(mdates.AutoDateLocator())
DOLLAR_FORMATTER = mtick.FuncFormatter(lambda x, pos: "${:,.0f}".format(x))