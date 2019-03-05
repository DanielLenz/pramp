def find_grants_cap(grants, budget):
    if not grants:
        return budget

    n_grants = len(grants)

    # Keep this up to date as we loop
    remaining_cash = budget

    # N log(N) time, in-place sort
    grants.sort()

    for i, grant in enumerate(grants):
        curr_n_grants = n_grants - i

        available_per_grant = float(remaining_cash) / curr_n_grants
        if available_per_grant < grant:
            return available_per_grant

        remaining_cash -= grant

    return grants[-1]


if __name__ == '__main__':
    grantsArray = [2, 100, 50, 120, 1000]
    newBudget = 190

    print(find_grants_cap(grantsArray, newBudget))