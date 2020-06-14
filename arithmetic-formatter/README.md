# [Arithmetic Formatter](https://repl.it/@borntofrappe/fcc-arithmetic-arranger)

> First project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

At the time of writing, the freeCodeCamp team is working on the certification, and the projects are not publicly available yet.

Since the curriculum is actively being developed, this folder also includes more than one script:

- `main` imports the formatting function(s) and runs them with a variety of input options

- `arithmetic_arranger_previous` formats arithmetic operations. This is however a script created in January 2020, and for a previous version of the freeCodeCamp curriculum.

- `arithmetic_arranger` formats arithmetic operations. This is meant to describe the code submitted to the freeCodeCamp platform.

It is teaching to see not only how the project has evolved, but also my approach to the problem at hand.

_Please note_: `arithmetic_arranger_previous` is not equipped to consider the optional second argument. This feature was not present in the original project.

## Assignment

The project describes a series of requirements, but in the simplest terms, it can summed up in terms of input and output values:

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

## Formatting

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

## Error handling

Following the project guidelines, the function needs to return a string with an error message in the following instances:

- the list contains more than five problems. This check is performed with an `if` statement and the `len` function

- the operator describes a multiplication or division operation. Use an `if` statement checking the necessary characters

- the operand contains characters other than numbers. You can achieve this in more than one way, but personally, I opted to import the `re` module and checked the strings with a regular expression

- the operand have more than four characters. I checked the length of the strings describing the operands, but you can very well parse the strings to integer, and then check the values are less than `9999`

The first condition can be tested immediately, while the others are included in the for loop considering the individual operations.

## Good to know

- check if a dictionary has a particular key

  ```py
  if "key" in dictionary:
  ```

  With the `not` operator you can also check if a dictionary has not a key. This comes in handy to add the field for the fourth row if one is not already available

  ```py
  if "fourth" not in rows:
  ```

- join a list to make a string

  This required a bit of an adjustment coming from JavaScript. Instead of using the `.join()` method on the collection, you apply the function to the string used as a connector between the items.

  In most practical terms:

  ```py
  names_list = ["George", "Timothy", "Ella"]
  names_string = ", ".join(names_list) # "George, Timothy, Ella"
  ```

  Join together the items with the string `,`

- get the values of a dictionary

  This is actually a one liner

  ```py
  rows_values = rows.values()
  ```

  In a previous version I considered the rows individually, accessing the lists with `rows["first"]`, `rows["second"]` and so forth, but this solution is preferable. It allows to have a list of three or four lists depending on the structure of the dictionary. No need to further check if the dictionary has a fourth row

- remove the last character from a string

  This comes in the larger topic of _slices_, and is rapidly achieved by considering every letter from the first up to the penultimate character.

  ```py
  return output[:-1]
  ```

  It is handy to remove the `\n` new line. This is added after each row, but is superfluous for the last row..
