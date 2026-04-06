from typing import Optional


def parse_scoreboard(raw: str) -> dict[str, int]:
    """Parse 'name:score' pairs separated by commas.

    Example: "alice:10,bob:9,alice:14" -> {"alice": 14, "bob": 9}

    Invalid segments should be skipped.
    """
    board: dict[str, int] = {}
    if raw == "":
        return board

    parts = raw.split(",")
    for part in parts:
        part = part.strip()
        if not part or ":" not in part:
            continue
        name_part, score_part = part.split(":", 1)
        name = name_part.strip().lower()
        if not name:
            continue
        try:
            value = int(score_part.strip())
        except ValueError:
            continue
        board[name] = value
    return board


def top_player(board: dict[str, int]) -> Optional[tuple[str, int]]:
    """Return the player with the highest score, else None.

    Keep this deterministic by sorting names alphabetically when scores tie.
    """
    # Empty board -> no top player
    if not board:
        return None

    # Sort by score descending, then name ascending for deterministic tie-breaks
    name, score = sorted(board.items(), key=lambda kv: (-kv[1], kv[0]))[0]
    return name, score