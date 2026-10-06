from math import comb


def number_of_ways(start_pos: int, end_pos: int, k: int) -> int:
    """
    Solving Leetcode Problem below.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    
    Given two positive integers start_pos and end_pos
    Initially, you are standing at position startPos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.
    
    Given a positive integer k, return the number of different ways to
    reach the position endPos starting from startPos, such that you
    perform exactly k steps.    
    """
    distance = abs(end_pos - start_pos)

    # Each step changes the position by one, so the distance must not
    # exceed k and must have the same parity as k.
    if distance > k or (k - distance) % 2:
        return 0

    right_steps = (k + end_pos - start_pos) // 2
    return comb(k, right_steps)


def test_number_of_ways():
    """
    Example 1:

    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps
    in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
    """
    print(number_of_ways(1, 2, 3))


if __name__ == "__main__":
    test_number_of_ways()
