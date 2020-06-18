# [NumPy Stats](https://repl.it/@borntofrappe/fcc-mean-var-std)

> First project of five to earn the **Data Analysis with Python** certification on freeCodeCamp.

The note introducing other projects for the freeCodeCamp certification is repeated here to be exhaustive:

- the freeCodeCamp curriculum is under development

- a link to the assignment will be included when the certification will be live

- there are actually two scripts. One created in the end of January 2020, one in June 2020 as I reviewed the project. The two differ since the project was updated with additional requirements, and since I've learned more about the Python language

## Assignment

In its revised version, the project asks to compute the following information for a 3x3 matrix:

- mean
- variance
- standard deviation
- max
- min

It also asks to calculate the sum of the rows, of the columns, and the items themselves.

## Lessons learned

- convert a numpy array to a list

  ```py
  a = np.array([1, 2, 4])
  list = a.tolist()
  ```

  Trivial example, but it illustrates the point. The function is exceedingly useful in the project, where the output must be a list and not a numpy array.

- raise an exception to highlight an issue in the terminal

  ```py
  raise ValueError("List must contain nine numbers.")
  ```

  In the specific project I raise the exception when the reshaping of the flattened array fails.

## Standard deviation

It is actually possible to compute the standard deviation on the basis of the variance, making use of the element-wise operations allowed by numpy.

```py
standard_deviation = [(np.array(variance[0]) ** 0.5).tolist(), ...]
```

This since the standard deviation is the square root of the variance.

I decided to use the relation within a for loop:

```py
standard_deviation = []
        for v in variance:
            standard_deviation.append((np.array(v) ** 0.5).tolist())
```

And finally updated the syntax to use a list comprehension.

```py
standard_deviation = [(np.array(v) ** 0.5).tolist() for v in variance]
```
