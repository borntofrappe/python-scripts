# [Time Calculator](https://repl.it/@borntofrappe/fcc-time-calculator)

> Second project of five to earn the **Scientific Computing with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Assignment

The goal of the project is create a function `add_time`, which takes as input a start time and a duration, in order to return the end time. This following a 12-hour clock format, and a series of rules regarding the proper format.

The function also includes an optional parameter in the day of the week. If one is specified, the idea is to provide the day of the end time.

## Examples

There are a few rules regarding the format, but instead of repeating the assignment, here a few examples to highlight how the function is supposed to work.

```py
add_time("3:00 PM", "3:10")
# 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# 12:03 PM

add_time("10:10 PM", "3:30")
# 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# 7:42 AM (9 days later)
```

## Lessons learned

- compute integer division with two backslash character: `//`.

  ```py
  15 // 6 # 2
  ```

  In the project this is handy to consider the number of hours obtained by having a `minute` value greater than `60`

- find the position of an item in a list

  ```py
  names = ['Timothy', 'Geoffrey', 'Elizabeth']
  index = names.index('Timothy') # 0
  ```
