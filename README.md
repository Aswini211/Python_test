# Python Final Test: 25 Solutions

A collection of 25 beginner-to-intermediate Python problems covering lists, dictionaries, strings, classes, exception handling and data processing. All solutions are in `final_test_solutions.py`.

## How to Run

```bash
python final_test_solutions.py
```

Requires Python 3.6+. No external libraries are needed (only the standard `re`, `string` and `collections` modules).

Running the file prints a demo result for every problem. Each solution is a separate function, so you can also import one:

```python
from final_test_solutions import second_highest
print(second_highest([50, 90, 90, 70]))   # 70
```

## Problems and Approaches

| # | Problem | Function | Approach |
|---|---------|----------|----------|
| 1 | Second-highest salary | `second_highest` | Track `first` and `second` in one pass, no sorting |
| 2 | Character frequency | `char_frequency` | Dictionary with `get(ch, 0) + 1` |
| 3 | Remove duplicates | `remove_duplicates` | Dict as a "seen" lookup, list keeps order |
| 4 | Missing number | `find_missing` | Expected sum `n(n+1)/2` minus actual sum |
| 5 | Anagram checker | `is_anagram` | Clean spaces and case, compare frequency dicts |
| 6 | Group by department | `group_by_department` | `setdefault(dept, []).append(name)` |
| 7 | Merge dictionaries | `merge_prices` | Copy first dict, add prices on key clash |
| 8 | Common elements | `common_elements` | Lookup of list A, scan B, skip already-added |
| 9 | Flatten nested list | `flatten` | Recursion on list items |
| 10 | Most frequent element | `most_frequent` | Count, then walk in order with strict `>` for ties |
| 11 | Sort by salary | `sort_by_salary` | `sorted(..., reverse=True)` returns a new list |
| 12 | Transaction summary | `transaction_summary` | Sum credits and debits, net = credits - debits |
| 13 | Duplicate employee IDs | `duplicate_ids` | Count IDs, keep those with count > 1 |
| 14 | Validate password | `validate_password` | Length check plus `any()` for each character type |
| 15 | Word frequency | `top_words` | Regex tokenizing plus `Counter.most_common(5)` |
| 16 | CSV-like data | `parse_records` | `try/except ValueError`, returns valid and invalid lists |
| 17 | Failure streak | `longest_failure_streak` | Running counter, reset on success |
| 18 | Inventory management | `update_inventory` | Subtract sales, report stock <= 0 |
| 19 | Group anagrams | `group_anagrams` | Sorted letters as dict key |
| 20 | Log file analysis | `analyze_logs` | Count each level, collect ERROR lines |
| 21 | Bank account class | `BankAccount` | Validates amounts, blocks overdraft with `ValueError` |
| 22 | Handle invalid input | `get_number` | `while True` plus `try/except` until valid |
| 23 | Overlapping time slots | `find_overlaps` | Two pointers: overlap = `max(starts)` to `min(ends)` |
| 24 | API response processing | `process_responses` | `.get()` for safe access, status 200 means success |
| 25 | Sales report | `sales_report` | Revenue = quantity x price per product, then `max` |

## Input Formats

- **Employees** (Q6, Q11): `{"name": "A", "department": "IT", "salary": 50}`
- **Transactions** (Q12): `{"type": "credit" | "debit", "amount": 500}`
- **Records** (Q13): `{"id": 1}`
- **CSV lines** (Q16): `"1, Ravi, 5000"`
- **Statuses** (Q17): `"success"` or `"failure"`
- **Sales for inventory** (Q18): list of `(product, quantity)` tuples
- **Intervals** (Q23): list of `(start, end)` tuples
- **API responses** (Q24): `{"status": 200, "data": {...}}`
- **Sales records** (Q25): `{"date": "...", "product": "pen", "quantity": 10, "price": 5}`

## Interview Tips

- **Q1:** Be ready to explain how you find the second-highest without `sort()`. The two-variable approach is O(n).
- **Q3:** A dict gives O(1) lookups, so the whole function is O(n) rather than O(n^2).
- **Q10:** Using a strict `>` while iterating in original order is what makes ties return the first element.
- **Q11:** `sorted()` returns a new list, while `list.sort()` changes the original in place.
- **Q23:** The two-pointer technique is O(n + m), better than comparing every pair.

## Notes

- Functions that must not modify their input (Q7, Q11, Q18) work on copies.
- Q22 accepts an `input_fn` parameter so it can be tested without typing. By default it uses the normal `input`.
