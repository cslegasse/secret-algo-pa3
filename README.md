# secret-algo-pa3

- **Legasse Remon** (UFID: 16447883)
- **Brynn Li** (UFID: 14196126)

## Requirements/Compilation
- Python 3.6 or higher

The project can be run simply by piping an example test case with the main file:
```
python src/main.py < tests/example.in
```

To run all tests and diff against expected output, copy the following into the terminal or create a script:
```
for f in tests/test*.in; do
    expected="tests/$(basename $f .in).out"
    actual=$(python src/main.py < "$f")
    if [ "$actual" = "$(cat $expected)" ]; then
        echo "PASS: $f"
    else
        echo "FAIL: $f"
        echo "  expected: $(cat $expected)"
        echo "  actual:   $actual"
    fi
done
```

## Q1 Comparison
TO DO

## Q2 Reccurance
Let `m = |A|`, `n = |B|`, and `v(c)` be the value of a character `c`. Then, we define `dp[i][j]` as the maximum value of any common subsequence of `A[1..i]` and `B[1..j]`. The base cases are dp[i][0] = 0 for all 0 <= i <= m, and dp[0][j] = 0 for all 0 <= j <= n. A common subsequence of any string with an empty string must itself be empty so its value is 0. The recurrence for 1 <= i <= m and 1 <= j <= n is directly in the psuedocode and code implementation which accounts for it:

```
    if A[i] == B[j]:
        dp[i][j] = max(dp[i-1][j-1] + v(A[i]),  dp[i-1][j],  dp[i][j-1])
    else:
        dp[i][j] = max(dp[i-1][j],  dp[i][j-1])
```

At position (i, j), the optimal common subsequence of A[1..i] and B[1..j] either uses the last characters A[i] and B[j] together or it does not. If A[i] != B[j], they cannot both appear as the last matched pair. The optimal subsequence answer must come from ignoring A[i] or ignoring B[j] which we would take the max of those two. If A[i] == B[j] then we match these two characters and collect their shared value v(A[i]) on top of the best common subsequence of A[1..i-1] and B[1..j-1]. This gives dp[i-1][j-1] + v(A[i]). Always taking the max yields dp[m][n].

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
                // subsequence traceback (recurrance)
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
