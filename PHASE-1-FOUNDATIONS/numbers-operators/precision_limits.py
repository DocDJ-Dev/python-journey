threshold = 10**80
candidates = [50, 100, 130, 133, 200, 300, 500, 511, 512]

for n in candidates:
    int_val = 4**n
    print(f"n={n}: int exceeds threshold? {int_val > threshold}")
    try:
        float_val = 4.0**n
        print(f"n={n}: float value -> {float_val:.6e}")
    except OverflowError:
        print(f"n={n}: float -> OverflowError, can't represent it")
