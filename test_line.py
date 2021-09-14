import pytest

@pytest.mark.parametrize("point1, point2, x, expected",
    [((0, 0), (5, 0), 10, 0), 
    ((0, 0), (100, 100), 50, 50),
    ((3, 5), (5, 10), 9, 20),
    ((1.2, 5.25), (2.6, -5.75), 1.9, -0.25)])
def test_on_line(point1, point2, x, expected):
    from line import on_line
    result = on_line(point1, point2, x)
    assert result == expected