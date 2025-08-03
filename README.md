# LeetCode 30-Day Challenge

This document summarizes the tasks completed each day, along with the core logic and solution approaches used.

---

## ✅ Day 1: Pascal's Triangle

**Problem Statement:**  
Generate the first `numRows` of Pascal's Triangle.

**Constraints:**

- `1 <= numRows <= 30`

**Approach:**

- Start with an empty list `output`.
- For each row, use the last row to compute the new values.
- Each value is the sum of two adjacent values from the previous row.
- First and last elements of every row are `1`.

---

## ✅ Day 2: Rearranging Fruits

**Problem Statement:**
You are given two fruit baskets. You can swap fruits between them. Find the minimum total cost required to make both baskets identical.

**Constraints & Concepts:**

- Use counters to find frequencies of fruits in each basket.
- Check if it's possible to make both baskets equal (all counts must be even).
- Use greedy strategy with sorting for minimum cost swaps.

**Approach:**

- Calculate frequency difference between baskets.
- Find extra fruits in each.
- Sort and match from both baskets, considering smallest swap cost or double the global minimum.

---

## ✅ Day 3: Maximum Fruits Harvested After at Most K Steps

**Problem Statement:**
Given a list of fruit positions and amounts on the x-axis, determine the maximum fruits you can collect by taking at most k steps starting from startPos.

**Concepts:**

- Two pointer (sliding window)
- Range summation
- Custom distance calculation depending on walking direction

**Approach:**

- Use a sliding window from left to right.
- At each step, check if the current window is valid based on minimal distance calculation.
- Update the running total and keep track of the max.

---

✅ Progress: 3/30 Days Complete
📅 Stay tuned for more daily challenges!
