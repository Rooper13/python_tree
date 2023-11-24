A = []
ST = []

def build(node, L, R):
    global A, ST
    if L == R:
        ST[node] = A[L]
    else:
        mid = (L + R) // 2
        build(2 * node, L, mid)
        build(2 * node + 1, mid + 1, R)
        ST[node] = ST[2 * node] + ST[2 * node + 1]

def update(node, L, R, idx, val):
    global A, ST
    if L == R:
        A[idx] += val
        ST[node] += val
    else:
        mid = (L + R) // 2
        if L <= idx and idx <= mid:
            update(2 * node, L, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, R, idx, val)
        ST[node] = ST[2 * node] + ST[2 * node + 1]

def query(node, tl, tr, l, r):
    global A, ST
    if r < tl or tr < l:
        return 0
    if l <= tl and tr <= r:
        return ST[node]
    tm = (tl + tr) // 2
    return query(2 * node, tl, tm, l, r) + query(2 * node + 1, tm + 1, tr, l, r)

if __name__ == "__main__":
    n = 6
    A = [0, 1, 3, 5, -2, 3]
    ST = [0 for _ in range(4 * n)]
    build(1, 0, n - 1)
    print(f"Sum of values in range 0-4 are: {query(1, 0, n - 1, 0, 4)}")
    update(1, 0, n - 1, 1, 100)
    print("Value at index 1 increased by 100")
    print(f"Sum of values in range 1-3 are: {query(1, 0, n - 1, 1, 3)}")
