import time, random, tempfile, os, string
from main import solve, parse_input
import matplotlib.pyplot as plt

def read_and_solve(filepath):
    with open(filepath, 'r') as f:
        lines = f.read()
    vals, A, B = parse_input(lines)
    return solve(vals, A, B)

def write_input(path, char_values, A, B):
    with open(path, 'w') as f:
        f.write(f"{len(char_values)}\n")
        for char, val in char_values.items():
            f.write(f"{char} {val}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")

def write_output(path, max_val, subseq):
    with open(path, 'w') as f:
        f.write(f"{max_val}\n")
        f.write(f"{subseq}\n")

def gen(n):
    # for all 26 lowercase letters in alphabet
    alphabet = string.ascii_lowercase
    char_values = {c: random.randint(1, 100) for c in alphabet}
    
    A = "".join(random.choices(alphabet, k=n))
    B = "".join(random.choices(alphabet, k=n))
    
    return char_values, A, B

def bench():
    sizes = [25, 50, 100, 200, 300, 400, 500, 750, 1000, 1500]
    results = []

    print(f"{'n':>15} {'dp_ms':>15} {'max_val':>12}")
    print("-" * 40)

    for n in sizes:
        char_values, A, B = gen(n)

        with tempfile.NamedTemporaryFile(mode='w', suffix='.in', delete=False) as f:
            inp = f.name
        with tempfile.NamedTemporaryFile(mode='w', suffix='.out', delete=False) as f:
            out = f.name

        write_input(inp, char_values, A, B)

        t0 = time.perf_counter()
        max_val, subseq = read_and_solve(inp)
        t_solve = (time.perf_counter() - t0) * 1000

        write_output(out, max_val, subseq)

        results.append((n, t_solve))
        print(f"{n:>15} {t_solve:>15.3f} {max_val:>12}")

        os.unlink(inp); os.unlink(out)

    return results

def plot(results):
    try:
        ns = [r[0] for r in results]
        t_solve = [r[1] for r in results]

        plt.figure(figsize=(10, 6))
        plt.plot(ns, t_solve, 'o-', label='Highest Value Longest Common Sequence Solver')
        plt.xlabel('n (string length)')
        plt.ylabel('Time (ms)')
        plt.title('HVLCS Solver Benchmark Tests')
        plt.legend()
        plt.grid(True)
        plt.savefig('benchmark.png', dpi=150)
    except ImportError:
        print("\npip install matplotlib")

if __name__ == "__main__":
    print("Use python benchmark.py, do not use 'RUN' in IDE.\n")
    results = bench()
    plot(results)