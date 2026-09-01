from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        N = m * n

        start = 0
        litter = [-1] * N
        litter_count = 0
        reset = bytearray(N)
        blocked = bytearray(N)

        # Encode the grid once.
        for r in range(m):
            row = classroom[r]
            base = r * n

            for c, ch in enumerate(row):
                p = base + c

                if ch == 'S':
                    start = p
                elif ch == 'L':
                    litter[p] = litter_count
                    litter_count += 1
                elif ch == 'R':
                    reset[p] = 1
                elif ch == 'X':
                    blocked[p] = 1

        # Nothing to collect.
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1

        # best[state] = maximum remaining energy seen for
        # (position, mask).
        #
        # Store energy + 1:
        #   0 -> never visited
        #   1 -> 0 energy
        #   2 -> 1 energy
        #   ...
        #
        # Maximum value is 51, so bytearray is sufficient.
        total_states = N * (1 << litter_count)
        best = bytearray(total_states)

        start_state = start
        best[start] = energy + 1

        # Queue entries:
        # (position, mask, remaining_energy)
        q = deque([(start, 0, energy)])

        moves = 0

        while q:
            # Process one BFS level.
            for _ in range(len(q)):
                pos, mask, rem = q.popleft()

                if mask == full_mask:
                    return moves

                # If no energy remains, this state cannot move.
                if rem == 0:
                    continue

                r = pos // n
                c = pos - r * n

                # ---- Up ----
                if r:
                    np = pos - n

                    if not blocked[np]:
                        new_rem = rem - 1
                        new_mask = mask

                        lid = litter[np]
                        if lid >= 0:
                            new_mask |= 1 << lid

                        if reset[np]:
                            new_rem = energy

                        idx = new_mask * N + np

                        if new_rem + 1 > best[idx]:
                            best[idx] = new_rem + 1
                            q.append((np, new_mask, new_rem))

                # ---- Down ----
                if r + 1 < m:
                    np = pos + n

                    if not blocked[np]:
                        new_rem = rem - 1
                        new_mask = mask

                        lid = litter[np]
                        if lid >= 0:
                            new_mask |= 1 << lid

                        if reset[np]:
                            new_rem = energy

                        idx = new_mask * N + np

                        if new_rem + 1 > best[idx]:
                            best[idx] = new_rem + 1
                            q.append((np, new_mask, new_rem))

                # ---- Left ----
                if c:
                    np = pos - 1

                    if not blocked[np]:
                        new_rem = rem - 1
                        new_mask = mask

                        lid = litter[np]
                        if lid >= 0:
                            new_mask |= 1 << lid

                        if reset[np]:
                            new_rem = energy

                        idx = new_mask * N + np

                        if new_rem + 1 > best[idx]:
                            best[idx] = new_rem + 1
                            q.append((np, new_mask, new_rem))

                # ---- Right ----
                if c + 1 < n:
                    np = pos + 1

                    if not blocked[np]:
                        new_rem = rem - 1
                        new_mask = mask

                        lid = litter[np]
                        if lid >= 0:
                            new_mask |= 1 << lid

                        if reset[np]:
                            new_rem = energy

                        idx = new_mask * N + np

                        if new_rem + 1 > best[idx]:
                            best[idx] = new_rem + 1
                            q.append((np, new_mask, new_rem))

            moves += 1

        return -1
