# LeetCode 30-Day Challenge

This document summarizes the tasks completed each day, along with the core logic and solution approaches used.

---

## ✅ Day 1: 118. Pascal's Triangle

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

## ✅ Day 2: 2561. Rearranging Fruits

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

## ✅ Day 3: 2106. Maximum Fruits Harvested After at Most K Steps

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

## ✅ Day 4: 904. Fruit Into Baskets

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

## ✅ Day 5: 3477. Fruits Into Baskets II

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

## ⏳ Day 6: 3479. Fruits Into Baskets III

Pending

## ⏳ Day 7: 3363. Find the Maximum Number of Fruits Collected

Pending

## ✅ Day 8: 808. Soup Servings

**Problem Statement:**  
There are two types of soup: A and B. Initially, each has `n` mL. Every turn, one of the following four operations is chosen with equal probability (0.25):

1. Serve 100 mL of A and 0 mL of B
2. Serve 75 mL of A and 25 mL of B
3. Serve 50 mL of A and 50 mL of B
4. Serve 25 mL of A and 75 mL of B

The process continues until either soup A or B becomes empty. Return the probability that soup A will become empty **before** soup B, **plus half the probability** that both soups become empty at the same time.

**Constraints:**

- `0 <= n <= 10^9`
- You may assume n is a multiple of 25 for optimization purposes.

**Concepts Used:**

- Dynamic Programming with memoization (top-down approach)
- State reduction by dividing `n` into blocks of 25 mL
- Base case handling for edge states
- Probabilistic state transitions
- Pruning with large `n` (optimization for `n >= 4800`)

**Approach:**

1. **Optimization for Large `n`:**  
   For `n >= 4800`, the result converges to 1 with high precision, so we return 1 directly for performance.

2. **State Normalization:**  
   Convert `n` to `(n + 24) // 25` to reduce the number of states by considering units of 25 mL.

3. **Recursive Function with Memoization:**  
   Define a recursive function `recursive_function(a, b)`:

   - If both A and B are empty: return `0.5`
   - If A is empty: return `1.0`
   - If B is empty: return `0.0`
   - Otherwise, calculate the expected value by exploring all four operations, each with 0.25 probability.

4. **Memoization:**  
   Use a dictionary `memory` to store results of already computed states to avoid redundant computation.

---

✅ Progress: 5/30 Days Complete
📅 Stay tuned for more daily challenges!
