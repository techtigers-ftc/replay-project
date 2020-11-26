def x_y_to_series_conversion(numoflightsperrow, x, y):
    if (Y % 2) == 0:
        return numoflightsperrow*y + x
    else:
        return numoflightsperrow*y + numoflightsperrow - x -1

print(x_y_to_series_conversion(11,0,1))
