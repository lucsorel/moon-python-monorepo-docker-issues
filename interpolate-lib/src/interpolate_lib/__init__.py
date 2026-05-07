from numpy import interp


def linear_interpolate(x_to_interpolate: float, x_min: float, x_max: float, y_min: float, y_max: float) -> float:
    """Return the linear interpolation at x between points (x_min, x_max) into (y_min, y_max)."""
    return interp(x_to_interpolate, [x_min, x_max], [y_min, y_max])
