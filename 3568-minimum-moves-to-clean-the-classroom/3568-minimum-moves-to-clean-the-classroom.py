class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Number each litter cell from 0 .. k-1
        litter_id = {}
        start = None

        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        # No litter to collect.
        if k == 0:
            return 0

        target = (1 << k) - 1

        # best[(cell, mask)] = maximum remaining energy reached.
        #
        # Encode (r, c) as r*n+c to reduce tuple overhead.
        states = m * n
        best = {}

        sr, sc = start
        start_pos = sr * n + sc
        start_mask = 0

        # (position, remaining_energy, mask)
        q = deque([(start_pos, energy, start_mask)])
        best[(start_pos, start_mask)] = energy

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        moves = 0

        while q:
            # BFS layer = same number of moves
            for _ in range(len(q)):
                pos, rem, mask = q.popleft()

                if mask == target:
                    return moves

                r, c = divmod(pos, n)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # A move always costs 1 energy.
                    if rem == 0:
                        continue

                    new_rem = rem - 1
                    new_pos = nr * n + nc

                    # Collect litter.
                    new_mask = mask
                    lid = litter_id.get((nr, nc))
                    if lid is not None:
                        new_mask |= 1 << lid

                    # Reset immediately upon entering R.
                    if classroom[nr][nc] == 'R':
                        new_rem = energy

                    key = (new_pos, new_mask)

                    # Dominance:
                    # If we've already reached this cell/mask with
                    # at least as much energy, this state cannot help.
                    old = best.get(key, -1)
                    if new_rem <= old:
                        continue

                    best[key] = new_rem
                    q.append((new_pos, new_rem, new_mask))

            moves += 1

        return -1
