# Copilot Evidence — Step 05

## Documentation prompt

Generate a concise docstring for each function on this file, this docstring must include the following:

- Function purpose
- Function parameters and return type if necessary
- A meaningful example depicting the way the function works.

## What you edited after Copilot output

I didn't do edits

## Accuracy check

By running this on the terminal:

```bash
python3 - <<'PY'
import importlib.util, inspect
spec = importlib.util.spec_from_file_location("exercise", "step-05-documentation-generation/exercise.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print("chunk_list:\n", inspect.getdoc(mod.chunk_list))
print("\nmoving_average:\n", inspect.getdoc(mod.moving_average))
PY
```
