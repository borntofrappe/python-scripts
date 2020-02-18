# [Binary Tree](https://repl.it/@borntofrappe/binarytree)

> Use the binary tree algorithm to create a maze.

## Development Notes

The binary tree algorithm is a simple, yet an intriguing one. It is also a treasure trove if you want to exercise with software. So far I have been able to practice with JavaScript, SVG and the data visualization library D3. [Here's the reference for that dollop](https://codepen.io/borntofrappe/pen/OJVyMNR).

Here, I set out to use the algorithm to draw a similar maze. Just with Python and ASCII characters.

## Update

The logic formatting the maze through dashes and pipes was too good to just relegate the code to the terminal, and as the maze is actually printed:

```py
print(maze)
"""
+---+---+---+---+
+               +
+---+   +---+   +
+       +       +
+   +---+   +   +
+   +       +   +
+---+---+---+---+
"""
```

So I decided to add a function to also write the maze locally, and to a `maze.txt` function.
