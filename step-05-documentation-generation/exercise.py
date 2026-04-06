def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """Split a list of integers into consecutive chunks of a given size.

    Parameters
    - values: list[int] -- the list to split
    - size: int -- the maximum size of each chunk (must be > 0)

    Returns
    - list[list[int]] -- a list of chunks; the last chunk may be smaller

    Raises
    - ValueError: if `size` is not greater than 0

    Example
    >>> chunk_list([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """Compute the simple moving average over a sliding window.

    Parameters
    - values: list[float] -- input numeric sequence
    - window: int -- window size for averaging (must be > 0)

    Returns
    - list[float] -- moving averages for each full window; empty if
      `window` is larger than the number of values

    Raises
    - ValueError: if `window` is not greater than 0

    Example
    >>> moving_average([1.0, 2.0, 3.0, 4.0], 2)
    [1.5, 2.5, 3.5]
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result