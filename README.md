# terminal-christmas-tree

Here is an **animated Christmas tree**, which is launched in the terminal, for the upcoming New Year.

## How to run:
To run the project, you need a UV package and project manager – [Installing UV](https://docs.astral.sh/uv/getting-started/installation/)
```
uv run christmas_tree.py
```
## How to change a Christmas tree:
- Сhange the symbols on the Christmas tree:
  ```
  def func():
    symbols = ['*', '.', '+', 'o', 'O', '@', '^', '~', '°', '·', '%',
         '$', '№', '&', '8', '0', '3', '{', '}', '✶', '❄', '❉']
  ```
- Change the ratio of colored and green characters:
  > The higher the percentage, the more color symbols there are.
  ```
    if randint(1, 100) <= 60:
        color_idx = randint(0, len(colors) - 1)
        return f"{colors[color_idx]}{symbol}"
    else:
        return f"{green}{symbol}"
  ```
- Change the speed of changing symbols:
  ```
  sleep_time = 0.4 - (end_time - start_time)
  ```
- Change the color of the trunk:
  ```
  brown = "\033[38;5;52m"
  ```
- Change the main symbol:
  ```
  tree_char = '*'
  ```

### ***HAPPY NEW YEAR 2026 TO ALL!***
