# [Matplotlib line](Plot data from Google Trends with a line chart and matplotlib)

Plot data from Google Trends with a line chart and matplotlib.

## Data

For the data I collected the information from Google Trends, looking at the search results for the words 'python' and 'snake' at a Worldwide level, and in the timeframe `["2020-05-31", "2020-06-24"]`. [Here's a link](https://trends.google.com/trends/explore?date=2020-05-31%202020-06-24&q=python,snake) for reference.

## os

To have the script reference the `data.csv` file, use the `os` module. This one allows to find the path for the current directory as follows:

```
import os
dir = os.path.dirname(os.path.realpath(__file__))
```

## Interface

matplotlib provides two interfaces to plot data. One applying a series of attributes and methods from the `plt` global object, one creating separate objects to then work on the specific entity.

For practice, I've completed the script using both interfaces.

In `script-global`, the data is mapped to a single visualization, describing the line chart in the same panel.

In `script-object`, data is instead plotted in two separate panels, each with a distinct color.

## Write figure

The project creates a `.png` image describing the actual visualization.

```py
fig = plt.figure()

# plot data

fig.savefig(dir + '/plot.png')
```

_Minor note_: I've added a `.gitignore` file to make sure the `.png` images are not picked up by git.
