from collections import defaultdict

def groupby(sequence, by):
    """Group elements in a sequence by a specific key.

    Parameters
    ----------
    sequence : iterable
        The input sequence.
    by : callable
        Function mapping each element in `sequence` to a
        hashable value.

    Returns
    -------
    dict
        The sequence grouped by a value.
    """
    grouped = defaultdict(list)
    for elem in sequence:
        grouped[by(elem)].append(elem)
    return grouped


def aggregate(grouped, aggregator):
    return {key: aggregator(seq) for key, seq in grouped.items()}

if __name__ == '__main__':
    print("I'm foo and I'm being run")
