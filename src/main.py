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

# TO DO
def solve(values: Dict[str, int], A: str, B: str) -> Tuple[int, str]:
  # Returns (max_value, optimal_subsequence)
  # Compute the highest value common sequence of A and B
  # This is LC Med: https://leetcode.com/problems/longest-common-subsequence/description/
  # Approach: fill in DP table, traceback, find max value of common subseq., reconstruct  optimal subseq from DP

  raise NotImplementedError("implement solve()")

def main() -> None:
  values, A, B = parse_input(sys.stdin.read())
  val, subseq = solve(values, A, B)
  print_output(val, subseq)

if __name__ == "__main__":
  main()
