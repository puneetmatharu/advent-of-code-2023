import numpy as np
from pathlib import Path


def load(fpath: Path) -> list[str]:
    return [np.in1d(*[np.array(list(map(int, sa.split()))) for sa in l.split(": ")[1].split(" | ")]).sum() for l in fpath.read_text().splitlines()]


def part1(fpath: Path):
    return sum([((1 << ic) >> 1) for ic in load(fpath)])


def part2(fpath: Path):
    w = np.ones(len(load(fpath)), dtype=int)
    for (i, c) in enumerate(load(fpath)):
        w[i + 1:i + 1 + c] += w[i]
    return sum(w)


if __name__ == "__main__":
    output = part1(Path("example_data.txt"))
    print(f"[EXAMPLE] Part 1 output: {output}")
    assert output == 13

    output = part1(Path("test_data.txt"))
    print(f"[TEST] Part 1 output: {output}")
    assert output == 25231

    output = part2(Path("example_data.txt"))
    print(f"[EXAMPLE] Part 2 output: {output}")
    assert output == 30

    output = part2(Path("test_data.txt"))
    print(f"[TEST] Part 2 output: {output}")
    assert output == 9721255
