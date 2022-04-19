# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

    # Sort all segments first
    segments.sort()
    curr_node = segments[0]
    processed_segments = []
    # Check common points
    for i in range(len(segments) - 1):
        if segments[i].end >= segments[i + 1].start:
            processed_segments.append(segments[i + 1])
            maximum = max(segments[i].start, segments[i + 1].start)
            curr_node.start = maximum
            curr_node.end = min(segments[i].end, segments[i + 1].end)
        else:
            break
    del segments[0:len(processed_segments)]
    points.append(curr_node.end)

    if len(segments) != 0:
        point = optimal_points(segments)
        points.append(point.pop())

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
