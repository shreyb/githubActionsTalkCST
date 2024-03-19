import pytest

from awesome import add_two_ints, subtract_two_ints


@pytest.mark.parametrize(["int1", "int2", "expected"],
    (
        [3,4,7],
        [1,1,2],
        [-4,5,1],
        [-2,-5,-7],
        [0,0,0]
    )
)
@pytest.mark.unit
def test_add_two_ints_good(int1, int2, expected):
    assert add_two_ints(int1, int2) == expected


@pytest.mark.parametrize(["int1", "int2"],
    (
        [0.5, 0],
        [0, 0.6],
        [0.6, 0.6],
        ["foo", 5],
        [add_two_ints, "whatamidoing???"]
    )
)
@pytest.mark.unit
def test_add_two_ints_bad_type(int1, int2):
    with pytest.raises(TypeError, match="One of the input values is NOT an int!!"):
        add_two_ints(int1, int2)

@pytest.mark.unit
def test_subtract_two_ints():
    assert subtract_two_ints(4,3) == 1

