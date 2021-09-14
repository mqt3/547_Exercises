def on_line(point1, point2, x):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    slope = (y2-y1) / (x2-x1)
    y_intercept = y1 - slope * x1
    y = slope * x + y_intercept
    return y