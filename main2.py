def testMul(x, y):
    ans = x * y
    ans += 15
    return ans


def test_answer():
    assert testMul(3, 10) == 15