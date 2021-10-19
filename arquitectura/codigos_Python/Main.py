# Python 3 program for Bresenham’s Line Generation
# Assumptions :
# 1) Line is drawn from left to right.
# 2) x1 < x2 and y1 < y2
# 3) Slope of the line is between 0 and 1.
# We draw a line from lower left to upper
# right.


# function for line generation
def bresenhamAbajoArriba(x1, y1, x2, y2):
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):
        print(slope_error_new)
        print("(", x, ",", y, ")")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new
        print("+new "+str(slope_error_new))
        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
            print("en if "+str(slope_error_new))

def bresenhamXAbajoArriba(x1, y1, x2, y2):
    m_new = 2 * (x2 - x1)
    slope_error_new = m_new - (y2 - y1)

    x = x1
    for y in range(y1, y2 + 1):
        print(slope_error_new)
        print("(", x, ",", y, ")")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new
        print("+new "+str(slope_error_new))
        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            x = x + 1
            slope_error_new = slope_error_new - 2 * (y2 - y1)
            print("en if "+str(slope_error_new))


def bresenhamArribaAbajo(x1, y1, x2, y2):
    m_new = 2 * (y1 - y2)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        print("(", x, ",", y, ")")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if ( 0 > slope_error_new):
            print("no")
        else:
            y = y - 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
x1 = 0
y1 = 0
x2 = 4
y2 = 2
bresenhamAbajoArriba(x1, y1, x2, y2)
x1 = 0
y1 = 0
x2 = 2
y2 = 4
bresenhamXAbajoArriba(x1, y1, x2, y2)
#bresenhamArribaAbajo(x1, y2, x2, y1)


# This code is contributed by ash264


def drawCircle(xc, yc, x, y):
    print(xc + x, yc + y)
    print(xc - x, yc + y)
    print(xc + x, yc - y)
    print(xc - x, yc - y)
    print(xc + y, yc + x)
    print(xc - y, yc + x)
    print(xc + y, yc - x)
    print(xc - y, yc - x)


def circleBres(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y)
    while (y >= x):
        x += 1
        if (d > 0):
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y)


xc = 2
yc = 2
r = 2
#circleBres(xc, yc, r)
