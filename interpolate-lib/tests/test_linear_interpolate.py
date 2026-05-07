from interpolate_lib import linear_interpolate


def test_linear_interpolate():
    """Test linear interpolation of normalized value."""
    assert linear_interpolate(0.25, 0, 1, 10, 18) == 12
