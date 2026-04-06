# Usage Guide

<!-- Replace this file with generated + refined documentation -->

## Quickstart

This folder provides two helper functions in `exercise.py`:

- `chunk_list(values: list[int], size: int) -> list[list[int]]` — split a
	list into consecutive chunks of maximum `size`.
- `moving_average(values: list[float], window: int) -> list[float]` — compute
	the simple moving average over a sliding window.

Examples

1) Chunking a list

```py
from step_05_documentation_generation.exercise import chunk_list

chunks = chunk_list([1,2,3,4,5], 2)
# chunks == [[1,2], [3,4], [5]]
```

2) Moving average

```py
from step_05_documentation_generation.exercise import moving_average

avgs = moving_average([1.0, 2.0, 3.0, 4.0], 2)
# avgs == [1.5, 2.5, 3.5]
```

## Edge Cases

- `size` or `window` must be > 0 — otherwise a `ValueError` is raised.
- If `window` > len(values) then `moving_average` returns an empty list.

