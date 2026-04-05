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