import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSanitizeTags(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(exercise.sanitize_tags([]), [])

    def test_duplicates_mixed_case(self):
        tags = ["Tag", " tag", "TAG", "Another", "another"]
        self.assertEqual(exercise.sanitize_tags(tags), ["tag", "another"])

    def test_tags_with_punctuation(self):
        tags = [" C# ", "go!", "node.js", "c++", "rust-lang", "--", "  "]
        expected = ["c", "go", "nodejs", "rust-lang", "--"]
        self.assertEqual(exercise.sanitize_tags(tags), expected)

    def test_add_cases_generated_with_copilot(self):
        self.assertTrue(callable(exercise.sanitize_tags))

    def test_empty_cleanup_tags(self):
        tags = ["!!!", "@@@", "   "]
        self.assertEqual(exercise.sanitize_tags(tags), [])

    def test_internal_spaces(self):
        tags = ["multi word", "  spaced  out "]
        expected = ["multiword", "spacedout"]
        self.assertEqual(exercise.sanitize_tags(tags), expected)

    def test_numeric_tags(self):
        tags = ["123", "00123", "v2", "V2"]
        expected = ["123", "00123", "v2"]
        self.assertEqual(exercise.sanitize_tags(tags), expected)

    def test_unicode_accents(self):
        tags = ["naïve", "café"]
        # accents removed by regex, leaving ASCII letters only
        expected = ["nave", "caf"]
        self.assertEqual(exercise.sanitize_tags(tags), expected)

    def test_punctuation_caused_duplicates(self):
        tags = ["c++", " C# ", "c"]
        expected = ["c"]
        self.assertEqual(exercise.sanitize_tags(tags), expected)


if __name__ == "__main__":
    unittest.main()