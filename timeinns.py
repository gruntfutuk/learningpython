    import time

    for _ in range(1000):
        print("\r", time.time_ns(), end="")
    print()