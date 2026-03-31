# secret-algo-pa1

- **Legasse Remon** (UFID: 16447883)
- **Brynn Li** (UFID: 14196126)

## Structure

## Requirements/Compilation

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Q1 Comparison

## Q2 Reccurance

## Q3 Performance
Let `m = |A|`, `n = |B|`, and `v(c)` be the value of a character `c`. Then, we define `dp[i][j]` as the maximum value of any common subsequence of `A[1..i]` and `B[1..j]`. The psuedocode given below is described as:

```
HVLCS(A, B, v):
    m = len(A),  n = len(B)

    // base case
    for i = 0 to m:  dp[i][0] = 0
    for j = 0 to n:  dp[0][j] = 0

    // fill the DP table
    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                // subsequence traceback
                dp[i][j] = max(dp[i-1][j-1] + v(A[i]), dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```
Note: the traceback (reconstructing the subsequence) adds an O(m + n) walk back through the table and does not change the overall complexity.

| Resource | Cost |
|----------|------|
| Time     | **O(mn)**, two nested loops with each cell computed in O(1) |
| Space    | **O(mn)**, the full DP table is reducible to O(min(m,n)) if and only if the value is needed and is not the traceback |

