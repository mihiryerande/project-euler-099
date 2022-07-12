# Problem 99:
#     Largest Exponential
#
# Description:
#     Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
#       as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
#
#     However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
#       as both numbers contain over three million digits.
#
#     Using base_exp.txt (right click and 'Save Link/Target As...'),
#       a 22K text file containing one thousand lines with a base/exponent pair on each line,
#       determine which line number has the greatest numerical value.
#
#     NOTE: The first two lines in the file represent the numbers in the example given above.

from math import log
from typing import Tuple


def main(filename: str) -> Tuple[int, int, int]:
    """
    Given a text file `filename`, where each line containing a base/exponent pair (`b` and `e`),
      return the line number for which the number b^e is greatest,
      as well as the `b` and `e` themselves.

    Args:
        filename (str): Name of text file containing base/exponent pairs

    Returns:
        (Tuple[int, int, int]):
            Tuple of ...
              * Line number representing containing the greatest value b^e
              * b from that line
              * e from that line

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(filename) == str

    log_val_best = i_best = b_best = e_best = 0

    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            b, e = map(int, line.strip().split(','))
            log_val = e * log(b)
            if log_val > log_val_best:
                log_val_best = log_val
                i_best = i
                b_best = b
                e_best = e
            else:
                continue

    return i_best+1, b_best, e_best


if __name__ == '__main__':
    base_exp_filename = 'base_exp.txt'
    best_line, best_base, best_exp = main(base_exp_filename)
    print('Line in "{}" containing the largest exponentiated value:'.format(base_exp_filename))
    print('  Line # = {}'.format(best_line))
    print('       b = {}'.format(best_base))
    print('       e = {}'.format(best_exp))
