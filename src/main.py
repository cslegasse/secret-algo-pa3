import sys
from typing import Dict, Tuple

def parse_input(text: str) -> Tuple[Dict[str, int], str, str]:
  l = text.strip().split('\n')
  idx = 0
  k = int(l[idx]); idx += 1
  vals: Dict[str, int] = {}
  for _ in range(k):
    part = l[idx].split(); idx += 1
    vals[part[0]] = int(part[1])
  A = l[idx]; idx += 1
  B = l[idx]
  return vals, A, B

def print_output(val: int, subseq: str) -> None:
  print(val)
  print(subseq)

def is_subsequence(x: str, y: str) -> bool:
  it = iter(y)
  return all(c in it for c in x)

def is_common_subsequence(s: str, A: str, B: str) -> bool:
  return is_subsequence(s, A) and is_subsequence(s, B)

def compute(s: str, values: Dict[str, int]) -> int:
  return sum(values.get(c, 0) for c in s)

# Compute the highest value common sequence of A and B
def solve(values: Dict[str, int], A: str, B: str) -> Tuple[int, str]:
  # initialize commonly used variables
  n = len(A)
  m = len(B)

  # initialize DP table
  dp = [[0 for _  in range(m + 1)] for _ in range(n + 1)]

  # fill in DP table

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if A[i - 1] == B[j - 1]:
        val = values.get(A[i - 1], 0)
        dp[i][j] = dp[i - 1][j - 1] + val
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
  # find max value of common subsequence
  max_value = dp[n][m]

  # reconstruct optimal subsequence
  optimal_subsequence = ""
  i, j = n, m

  while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
      optimal_subsequence += A[i - 1]
      i -= 1
      j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
      i -= 1
    else:
      j -= 1
  
  optimal_subsequence = optimal_subsequence[::-1]

  return max_value, optimal_subsequence

def main() -> None:
  values, A, B = parse_input(sys.stdin.read())
  val, subseq = solve(values, A, B)
  print_output(val, subseq)

if __name__ == "__main__":
  main()
