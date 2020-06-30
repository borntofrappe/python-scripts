# Sea level predictor

> Fifth project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

## Assignment

The project asks to take the data from `data.csv`, which describes the level of sea rise between 1880 and 2013, plot a few visualizations and predict the change occurring between 2013 and 2050.

This using the following libraries:

- pandas, to read and manipulate the data

- matplotlib, to plot the data

- scipy, to predict the level within an error margin

## Development

`main.py` is the entry point for the script. Once run, it will take the code from `predictor.py` and run the functions to produce the desired visualization in the form of `.png` images.

`min.py` is a file I personally added to explore the libraries and build the project in increments.

<!-- ## Notes

A few things I've learned developing the script. -->

---

<!--

### Assignment

You will anaylize a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:
* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
* Use the `linregress` function from `scipi.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the "run" button and `main.py` will run.

### Testing

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

### Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise

-->
