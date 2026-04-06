def summarize_response_times(times: list[int]) -> dict[str, float]:
    """Return min, max, average for non-negative response times.

    Output schema:
    {"min": float, "max": float, "avg": float}

    For empty valid values, return all zeros.
    """
    filtered = [value for value in times if value >= 0]
    if not filtered:
        return {"min": 0.0, "max": 0.0, "avg": 0.0}

    return {
        "min": float(min(filtered)),
        "max": float(max(filtered)),
        "avg": float(sum(filtered) / len(filtered)),
    }