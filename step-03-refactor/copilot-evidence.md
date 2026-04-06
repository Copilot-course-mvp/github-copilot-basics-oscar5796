# Copilot Evidence — Step 03

Refactored duplicated discount calculation into a single helper function named `apply_discount`.

## Refactor prompt

Extract the duplicated discount computation from `checkout_total` and `invoice_total` into a shared helper function `apply_discount(subtotal, discount_percent)` and update both functions to call it.

## Why behavior is preserved

The logic and rounding are unchanged: subtotals are summed, discounts applied when `discount_percent > 0`, totals floored at 0, and results rounded to 2 decimals. Both public functions delegate to the new helper.

## Before vs after summary

Before: `checkout_total` and `invoice_total` each contained identical discount calculation code.
After: A single `apply_discount` helper centralizes the calculation, reducing duplication and improving maintainability.
