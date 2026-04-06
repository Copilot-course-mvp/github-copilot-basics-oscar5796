# Copilot Evidence — Step 04

## Prompt used for test generation

Create a file called student_tests.py and create unit tests for sanitize_tags function, include these edge cases:

Empty input
Duplicate tags with mixed case
Tags containing punctuation

## Extra edge case Copilot missed

I asked copilot which additional tests were wort to implement.

- Yes, which other tests you think are worth trying to implement?

Copilot answer:

Here are suggested additional tests for sanitize_tags:

- Empty-Cleanup Tags: input like ["!!!", "@@@", "   "] -> expect they are removed.
- Internal Spaces: "multi word" -> becomes "multiword".
- Numeric Tags: ["123", "00123", "v2"] -> numeric content preserved and deduped properly.
- Unicode/Accents: ["naïve", "café"] -> accents removed per current regex (expect "nave", "caf").
- Punctuation-caused Duplicates: ["c++", " C# ", "c"] -> check dedupe when cleaning makes them equal.
- Hyphen Edge Cases: leading/trailing/multiple hyphens like ["-lead", "trail-", "--"] -> verify hyphen preservation.
- Non-string Items: list containing non-strings (e.g., None, 123) -> decide whether to expect a TypeError or handle gracefully.
- Very Long Tag: extremely long string -> ensure function returns it (or document expected behavior).

I told copilot to only implement the first five.

## Final test count

9
