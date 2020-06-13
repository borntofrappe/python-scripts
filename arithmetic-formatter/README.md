# Arithmetic Formatter

> First project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

At the time of writing, the curriculum is not public yet, but I'll add a link as soon as it's made avaulalble.

Since the curriculum is actively being developed, the project also includes more than one script:

- `main` imports the formatting function(s) and runs them with a variety of input options

- `arithmetic_arranger` provides a first function to format arithmetic operations in the desired structure. This is however a script created in January 2020, and for a previous version of the freeCodeCamp curriculum.

- `arithmetic_formatter` formats arithmetic operations, and is meant to describe the code submitted to the freeCodeCamp platform.

## Assignment

The project describes a series of requirements, but in the simplest terms, the project can be described in terms of the input and output values of the would-be function:

- input: a list of strings describing a series of arithmetic operations

- output: a string formatting the operations vertically and side by side

Visually, going from this input:

```code
32 + 698
```

To this output:

```code
   32
+ 698
-----
```

Again, there are serveral requirements the project needs to satisfy, but that is the core of the project.

### Formatting

To format the arithmetic operations, I decided to follow this rough plan:

- create a dictionary describing the rows with three empty lists. Four if the function is instructed to show the solutions

- loop through the list of problems

- for each problem split the string to consider the operands and operator

- find the largest operand (since they are strings, the longest operand)

- append to the necessary strings to the rows:

  - first operand to the first row

  - operator and second operand to the second row

  - a string of `-` dash characters to the third row

  - optionally, the solution to the fourth row

- following the loop, join the lists nested in each row to provide a string

- join the strings describing the rows, including a `\n` new line character to have the rows visually on top of one another

### Error handling

Following the project guidelines, the function needs to return a string with an error message in the following instances:

- the list contains more than five problems. This check is performed with an `if` statement and the `len` function

- the operator describes a multiplication or division operation. Use an `if` statement checking the necessary characters

- the operand contains characters other than numbers. You can achieve this in more than one way, but personally, I opted to import the `re` module and checked the strings with a regular expression

- the operand have more than four characters. I checked the length of the strings describing the operands, but you can very well parse the strings to integer, and then check the values are less than `9999`
