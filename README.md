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

## ✅ Day 4: Fruit Into Baskets

**Problem Statement:**
You are given an array fruits where fruits[i] represents the type of fruit on the i-th tree in a single row of trees. You can only carry fruits of at most two different types, but you can pick as many fruits as you want as long as they fit into your two baskets. Starting from any tree, collect fruits moving strictly to the right, picking exactly one fruit from each tree until you reach a tree with a third fruit type.

**Constraints:**

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

**Concepts:**

- Sliding window (two-pointer technique)
- Hash map (dictionary) to track the count of each fruit type in the window

**Approach:**

- Use two pointers left and right to maintain a valid sliding window that contains at most 2 fruit types.
- Initialize an empty dictionary basket to track the count of fruit types within the window.
- Expand the window by moving the right pointer and updating the count.
- If the window exceeds two types, shrink it by moving left until it becomes valid.
- Keep track of the maximum window size throughout the iteration.

---

## ✅ Day 5: Fruits Into Baskets II

**Problem Statement:**
You are given two arrays of integers, fruits and baskets, both of length n. fruits[i] represents the quantity of the i-th type of fruit. baskets[j] represents the capacity of the j-th basket. From left to right, place each fruit into the leftmost basket whose capacity is greater than or equal to that fruit. Each basket can hold only one type of fruit. If no basket can hold a fruit, it remains unplaced.

Goal: Return the number of fruit types that remain unplaced after allocation.

**Constraints:**

- n == fruits.length == baskets.length
- 1 <= n <= 100
- 1 <= fruits[i], baskets[i] <= 1000

**Concepts:**

- Greedy placement (left-to-right)
- Linear search for the first valid position
- Used-slot tracking (similar to bipartite matching logic)

**Approach:**

- Iterate over each fruit from left to right.
- For each fruit, find the leftmost available basket that can hold it.
- Mark the basket as used once occupied.
- Count the number of fruits that could not be placed in any basket.

---

✅ Progress: 5/30 Days Complete
📅 Stay tuned for more daily challenges!
