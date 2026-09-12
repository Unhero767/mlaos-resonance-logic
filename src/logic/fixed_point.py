def compute_fixed_point(operator_func, initial_state=0, max_iterations=100):
    current = initial_state
    for _ in range(max_iterations):
        nxt = operator_func(current)
        if nxt == current:
            return current
        current = nxt
    return current
