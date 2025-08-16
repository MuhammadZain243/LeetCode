# LeetCode 30-Day Challenge

This document summarizes the tasks completed each day, along with the core logic and solution approaches used.

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

## ✅ Day 9: 231. Power of Two

**Problem Statement:**  
Given an integer `n`, return `True` if it is a power of two. Otherwise, return `False`.  
An integer `n` is a power of two if there exists an integer `x` such that:  
`n == 2^x`

**Constraints:**

- `-2^31 <= n <= 2^31 - 1`

### **Concepts Used**

- Bit manipulation (`<<` operator for left shift)
- Loop iteration for checking powers
- Edge case handling for negatives and zero

### **Approach**

1. **Edge Case Check:**

   - If `n <= 0`, immediately return `False` since powers of two are strictly positive.

2. **Iterative Power Generation:**

   - Start with `i = 1` (i.e., `2^0`).
   - Keep left-shifting (`i <<= 1`) which multiplies `i` by `2` on each step.
   - Compare with `n` at each step.

3. **Final Check:**
   - If `i == n` at any point, return `True`.
   - If `i` exceeds `n`, return `False`.

### **Complexity**

- **Time:** `O(log₂ n)` – Each left shift doubles `i`, so the loop runs ~log₂(n) times.
- **Space:** `O(1)` – Only a single variable is used.

## ✅ Day 10: 869. Reordered Power of 2

**Problem Statement:**  
You are given an integer `n`. Return `True` if the digits of `n` can be reordered to form a power of two. Otherwise, return `False`.

**Constraints:**

- `1 <= n <= 10^9`

### **Concepts Used**

- String manipulation
- Sorting digits
- Powers of two with bitwise left shift (`1 << i`)
- Brute-force digit comparison

### **Approach**

1. **Convert to Digits:**

   - Convert `n` into a string and sort its digits (`target = sorted(str(n))`).
   - This gives a canonical representation of `n`’s digits.

2. **Generate Powers of Two:**

   - Iterate over possible powers of two up to `2^29` (since `2^30 = 1,073,741,824` > `10^9`).
   - For each `2^i`, convert it into a string and sort its digits.

3. **Compare Digits:**
   - If the sorted digits of any power of two match the sorted digits of `n`, return `True`.
   - Otherwise, after the loop ends, return `False`.

### **Complexity**

- **Time:** `O(30 * k log k)` – At most 30 powers of two are checked, each requiring sorting of at most 10 digits (`k = number of digits`).
- **Space:** `O(k)` – For storing digit arrays.

## ✅ Day 11: 2438. Range Product Queries of Powers

**Problem Statement:**  
You are given a positive integer `n` and an array of queries, where each query is a pair `[l, r]`.

1. Convert `n` into a list of powers of two based on its binary representation.
   - For example: `n = 15 (1111 in binary)` → powers = `[1, 2, 4, 8]`
2. For each query `[l, r]`, compute the product of all powers from index `l` to `r`, modulo `10^9 + 7`.

Return the results as a list.

**Constraints:**

- `1 <= n <= 10^9`
- `1 <= queries.length <= 10^4`
- `queries[i] = [l, r]` with `0 <= l <= r < k` (`k` = number of set bits in `n`)

### **Concepts Used**

- Binary representation
- Modular arithmetic (modular inverse with Fermat’s little theorem)
- Prefix product array for efficient range queries

### **Approach**

1. **Build Powers Array:**

   - Traverse the binary representation of `n`.
   - For every set bit, record the corresponding power of two.

2. **Prefix Product Computation:**

   - Precompute prefix products of the powers array modulo `10^9 + 7`.
   - This allows efficient range multiplication queries.

3. **Answer Queries:**
   - For each `[l, r]`, compute:
     ```
     product = (prefix[r+1] * mod_inverse(prefix[l])) % MOD
     ```
   - `mod_inverse` is computed using Fermat’s Little Theorem:
     ```
     pow(x, MOD-2, MOD)
     ```
     since `MOD` is prime.

### **Complexity**

- **Time:** `O(k + q * log MOD)`
  - `k` = number of set bits in `n`
  - `q` = number of queries
- **Space:** `O(k)` – For storing powers and prefix products

## ✅ Day 12: 2787. Ways to Express an Integer as Sum of Powers

**Problem Statement:**  
Given two positive integers `n` and `x`, return the number of ways `n` can be expressed as the sum of the `x`th power of **unique** positive integers.  
In other words, count the sets `[n1, n2, ..., nk]` such that:

`n = n1^x + n2^x + ... + nk^x`

Since the result can be very large, return it modulo `10^9 + 7`.

**Constraints:**

- `1 <= n <= 300`
- `1 <= x <= 5`

**Concepts Used:**

- Dynamic Programming (Bottom-Up)
- 2D DP State Definition
- Iterative Table Filling
- Modular Arithmetic

**Approach:**

1. **DP State Definition:**  
   Let `dp[k][j]` be the number of ways to form sum `k` using integers ≤ `j` (where each integer is raised to the power `x`).

2. **State Transition:**  
    For each `j` (from `1` to `max_num` where `max_num^x <= n`):

   - **Exclude `j`**: Use only numbers ≤ `j-1` → `dp[k][j-1]`
   - **Include `j`**: If `k >= j^x`, add `dp[k - j^x][j-1]`

   Thus:

   - `dp[k][j] = dp[k][j-1] + dp[k - j^x][j-1] (if k >= j^x)`
   - `dp[k][j] = dp[k][j-1]` (otherwise)

3. **Base Case:**

- `dp[0][j] = 1` for all `j` (sum 0 can always be formed by choosing no numbers).

4. **Answer:**  
   The final result is `dp[n][max_num] % (10^9 + 7)`.

**Complexity:**

- **Time:** `O(n * m)` where `m` is the number of integers whose `x`th power ≤ `n`.
- **Space:** `O(n * m)`

## ✅ Day 13: 326. Power of Three

**Problem Statement:**  
Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.  
An integer `n` is a power of three if there exists an integer `x` such that:

`n == 3^x`

**Constraints:**

- `-2^31 <= n <= 2^31 - 1`

### **Concepts Used**

- Loop-based check
- Modular arithmetic
- Division until base case

### **Approach**

1. **Base Check:**

   - If `n <= 0`, it cannot be a power of three, so return `False`.

2. **Division Loop:**

   - While `n` is divisible by 3 (`n % 3 == 0`), divide it by 3.
   - This keeps reducing `n` closer to 1 if it’s a power of three.

3. **Final Check:**
   - If after all divisions `n` becomes 1, then it is a power of three.
   - Otherwise, it is not.

### **Complexity**

- **Time:** `O(log₃ n)` – we keep dividing by 3 until we reach 1.
- **Space:** `O(1)` – constant extra space.

## ✅ Day 14: 2264. Largest 3-Same-Digit Number in String

**Problem Statement:**  
You are given a string `num` representing a large integer.  
A _good integer_ is a substring of length **3** consisting of only **one unique digit**.

Return the largest good integer as a string. If no such integer exists, return an empty string `""`.  
Note: A substring is a contiguous sequence of characters within a string.

**Constraints:**

- `3 <= len(num) <= 1000`
- `num` consists only of digits.

### **Concepts Used**

- String search
- Substring matching
- Loop from high to low for optimization

### **Approach**

1. **Descending Digit Check:**

   - Loop from digit `9` down to `0`.
   - For each digit, create a string of length `3` (e.g., `"999"`, `"888"`, ...).

2. **Substring Search:**

   - Use the `in` operator to check if this 3-digit substring exists in `num`.

3. **Early Return:**

   - Since we start from the largest digit, the first match found is the largest good integer.
   - Return immediately upon finding it.

4. **No Match Case:**
   - If no good integer is found after the loop, return an empty string.

### **Complexity**

- **Time:** `O(10 * n)` → effectively `O(n)`, where `n` is the length of the string.
- **Space:** `O(1)` – only constant extra variables are used.

## ✅ Day 15: 342. Power of Four

**Problem Statement:**  
Given an integer `n`, return `True` if it is a power of four. Otherwise, return `False`.  
An integer `n` is a power of four if there exists an integer `x` such that:
`n == 4^x`

**Constraints:**

- `-2^31 <= n <= 2^31 - 1`

### **Concepts Used**

- Mathematical properties of powers
- Loop-based division
- Edge case handling for negatives and zero

### **Approach**

1. **Edge Case Check:**

   - If `n` is less than `1` (including negatives and zero), immediately return `False` because powers of four are strictly positive.

2. **Division Loop:**

   - While `n` is divisible by `4`, divide it by `4`.
   - This reduces `n` step-by-step, checking if it can be fully broken down into factors of `4`.

3. **Final Check:**
   - If the final reduced number is `1`, `n` is a power of four.
   - Otherwise, it is not.

### **Complexity**

- **Time:** `O(log₄ n)` – Each division reduces `n` by a factor of `4`.
- **Space:** `O(1)` – Only constant extra memory is used.

## ✅ Day 16: 1323. Maximum 69 Number

**Problem Statement:**  
You are given a positive integer `num` consisting only of digits `6` and `9`.  
Return the maximum number you can obtain by changing **at most one digit** (`6` → `9` or `9` → `6`).

**Constraints:**

- `1 <= num <= 10^4`
- Digits of `num` contain only `6` and `9`

### **Concepts Used**

- String manipulation
- Greedy choice (change the leftmost `6`)
- Conversion between string and integer

### **Approach**

1. **Convert Number to List:**

   - Transform `num` into a list of characters so digits can be modified.

2. **Iterate Over Digits:**

   - Traverse from left to right.
   - When the first `'6'` is found, temporarily change it to `'9'`.

3. **Check for Maximum:**

   - Convert the modified list back into an integer.
   - If this new value is greater than the current maximum (`num`), update `num`.
   - Restore the digit back to `'6'` to allow further iterations (if needed).

4. **Return Result:**
   - After scanning all digits, return the maximum number formed.

### **Complexity**

- **Time:** `O(d)` – where `d` is the number of digits in `num` (at most 4).
- **Space:** `O(d)` – list representation of the number.

✅ Progress: `14/30` Days Complete
📅 Stay tuned for more daily challenges!
