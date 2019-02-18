def root(x, n=2):
    if x < 0:
        raise ValueError()
    if x == 0:
        return 0

    lo, hi = 0, max(1, x)
    guess = (lo + hi) / 2.

    while abs(guess - lo) >= 1.e-3:

        # Catch accidental match, even for floats
        if pow(guess, n) == x:
            return guess

        # Guess too small
        elif pow(guess, n) < x:
            lo = guess
        # Guess too large
        elif pow(guess, n) > x:
            hi = guess

        # Something went wrong
        else:
            raise RuntimeError()

        guess = (lo + hi) / 2.

    return guess

if __name__ == '__main__':
    print(root(18))