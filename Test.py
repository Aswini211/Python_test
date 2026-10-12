import re
import string
from collections import Counter


# 1. Second-highest distinct salary (no sort/sorted)
def second_highest(salaries):
    first = second = None
    for s in salaries:
        if first is None or s > first:
            second = first          # old max becomes second
            first = s
        elif s != first and (second is None or s > second):
            second = s
    return second


# 2. Character frequency
def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 3. Remove duplicates, keep order, no set()
def remove_duplicates(items):
    seen = {}                       # dict gives O(1) lookup
    result = []
    for x in items:
        if x not in seen:
            seen[x] = True
            result.append(x)
    return result


# 4. Missing number from 1..N
def find_missing(nums):
    n = len(nums) + 1               # one number is missing
    return n * (n + 1) // 2 - sum(nums)


# 5. Anagram checker (ignore spaces and case)
def is_anagram(a, b):
    clean = lambda s: s.replace(" ", "").lower()
    return char_frequency(clean(a)) == char_frequency(clean(b))


# 6. Group employees by department
def group_by_department(employees):
    groups = {}
    for e in employees:
        groups.setdefault(e["department"], []).append(e["name"])
    return groups


# 7. Merge two price dictionaries (add prices on clash)
def merge_prices(d1, d2):
    merged = dict(d1)               # copy, don't touch the original
    for product, price in d2.items():
        merged[product] = merged.get(product, 0) + price
    return merged


# 8. Common elements without duplicates
def common_elements(a, b):
    in_a = {x: True for x in a}
    added = {}
    result = []
    for x in b:
        if x in in_a and x not in added:
            added[x] = True
            result.append(x)
    return result


# 9. Flatten nested list (recursion)
def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


# 10. Most frequent element (tie -> first encountered)
def most_frequent(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    best, best_count = None, 0
    for n in nums:                  # walk in original order
        if counts[n] > best_count:  # strict > keeps the earliest on ties
            best, best_count = n, counts[n]
    return best


# 11. Sort employees by salary desc, original untouched
def sort_by_salary(employees):
    return sorted(employees, key=lambda e: e["salary"], reverse=True)


# 12. Transaction summary
def transaction_summary(transactions):
    credits = debits = 0
    for t in transactions:
        if t["type"] == "credit":
            credits += t["amount"]
        elif t["type"] == "debit":
            debits += t["amount"]
    return {"credits": credits, "debits": debits, "net": credits - debits}


# 13. Duplicate employee IDs with counts
def duplicate_ids(records):
    counts = {}
    for r in records:
        counts[r["id"]] = counts.get(r["id"], 0) + 1
    return {i: c for i, c in counts.items() if c > 1}


# 14. Password validation
def validate_password(pw):
    return (
        len(pw) >= 8
        and any(c.isupper() for c in pw)
        and any(c.islower() for c in pw)
        and any(c.isdigit() for c in pw)
        and any(c in string.punctuation for c in pw)
    )


# 15. Top-5 word frequency
def top_words(paragraph, n=5):
    words = re.findall(r"[a-z0-9']+", paragraph.lower())
    return Counter(words).most_common(n)


# 16. CSV-like parsing with invalid-record handling
def parse_records(lines):
    valid, invalid = [], []
    for line in lines:
        try:
            emp_id, name, salary = [p.strip() for p in line.split(",")]
            if not name:
                raise ValueError("empty name")
            valid.append({"id": int(emp_id), "name": name, "salary": float(salary)})
        except ValueError:          # wrong field count or bad number
            invalid.append(line)
    return valid, invalid


# 17. Longest run of consecutive failures
def longest_failure_streak(statuses):
    longest = current = 0
    for s in statuses:
        if s.lower() == "failure":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


# 18. Inventory update
def update_inventory(stock, sales):
    inventory = dict(stock)
    for product, qty in sales:
        inventory[product] = inventory.get(product, 0) - qty
    out = [p for p, q in inventory.items() if q <= 0]
    return inventory, out


# 19. Group anagrams
def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w.lower()))
        groups.setdefault(key, []).append(w)
    return list(groups.values())


# 20. Log analysis
def analyze_logs(logs):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    errors = []
    for line in logs:
        for level in counts:
            if level in line:
                counts[level] += 1
                if level == "ERROR":
                    errors.append(line)
                break
    return counts, errors


# 21. Bank account
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance


# 22. Keep asking until a valid number is entered
def get_number(prompt="Enter a number: ", input_fn=input):
    while True:
        try:
            return float(input_fn(prompt))
        except ValueError:
            print("Invalid input, try again.")


# 23. Overlapping time slots (two-pointer, lists of (start, end))
def find_overlaps(a, b):
    a, b = sorted(a), sorted(b)
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append((start, end))
        if a[i][1] < b[j][1]:       # advance the interval that ends first
            i += 1
        else:
            j += 1
    return result


# 24. API response processing
def process_responses(responses):
    success, failed = [], 0
    for r in responses:
        if r.get("status") == 200 and r.get("data") is not None:
            success.append(r["data"])
        else:
            failed += 1
    return success, failed


# 25. Sales report
def sales_report(sales):
    revenue = {}
    for s in sales:
        revenue[s["product"]] = revenue.get(s["product"], 0) + s["quantity"] * s["price"]
    top = max(revenue, key=revenue.get) if revenue else None
    return revenue, top


if __name__ == "__main__":
    print(1, second_highest([50, 90, 90, 70, 60]))
    print(2, char_frequency("hello"))
    print(3, remove_duplicates([3, 1, 3, 2, 1, 4]))
    print(4, find_missing([1, 2, 4, 5, 6]))
    print(5, is_anagram("Dormitory", "Dirty Room"))
    emps = [
        {"name": "A", "department": "IT", "salary": 50},
        {"name": "B", "department": "HR", "salary": 70},
        {"name": "C", "department": "IT", "salary": 60},
    ]
    print(6, group_by_department(emps))
    print(7, merge_prices({"pen": 10, "book": 50}, {"book": 20, "bag": 100}))
    print(8, common_elements([1, 2, 2, 3, 4], [2, 2, 4, 5]))
    print(9, flatten([1, [2, 3], [4, [5, 6]]]))
    print(10, most_frequent([4, 1, 2, 1, 2, 4, 3]))
    print(11, [e["name"] for e in sort_by_salary(emps)], [e["name"] for e in emps])
    print(12, transaction_summary([
        {"type": "credit", "amount": 500},
        {"type": "debit", "amount": 200},
        {"type": "credit", "amount": 100}]))
    print(13, duplicate_ids([{"id": 1}, {"id": 2}, {"id": 1}, {"id": 1}, {"id": 2}]))
    print(14, validate_password("Abcd@123"), validate_password("abcd1234"))
    print(15, top_words("The cat and the dog. The CAT ran! A dog, a cat.", 5))
    print(16, parse_records(["1, Ravi, 5000", "2, Sita", "x, Ram, 100", "3, Anu, abc"]))
    print(17, longest_failure_streak(
        ["success", "failure", "failure", "success", "failure", "failure", "failure"]))
    print(18, update_inventory({"pen": 10, "book": 5}, [("pen", 10), ("book", 7)]))
    print(19, group_anagrams(["listen", "silent", "enlist", "google", "gogole", "cat"]))
    print(20, analyze_logs(["INFO start", "ERROR db down", "WARNING slow", "ERROR timeout"]))
    acc = BankAccount(100)
    acc.deposit(50)
    try:
        acc.withdraw(500)
    except ValueError as e:
        print(21, e, acc.get_balance())
    inputs = iter(["abc", "", "42"])
    print(22, get_number(input_fn=lambda _: next(inputs)))
    print(23, find_overlaps([(1, 5), (8, 12)], [(4, 9), (11, 15)]))
    print(24, process_responses([
        {"status": 200, "data": {"id": 1}},
        {"status": 500},
        {"data": {"id": 2}},
        {"status": 200, "data": {"id": 3}}]))
    print(25, sales_report([
        {"date": "d1", "product": "pen", "quantity": 10, "price": 5},
        {"date": "d2", "product": "book", "quantity": 2, "price": 100},
        {"date": "d3", "product": "pen", "quantity": 5, "price": 5}]))