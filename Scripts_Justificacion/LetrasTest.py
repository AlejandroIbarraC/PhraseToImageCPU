def bresenhamYArribaAbajo(x1, y1, x2, y2):
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):
        listaBitsLetra[x + y*6] = "0"

        slope_error_new = slope_error_new + m_new
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)

def bresenhamXArribaAbajo(x1, y1, x2, y2):
    m_new = 2 * (x2 - x1)
    slope_error_new = m_new - (y2 - y1)

    x = x1
    for y in range(y1, y2 + 1):
        listaBitsLetra[x + y*6] = "0"

        slope_error_new = slope_error_new + m_new
        if (slope_error_new >= 0):
            x = x + 1
            slope_error_new = slope_error_new - 2 * (y2 - y1)


def bresenhamYAbajoArriba(x1, y1, x2, y2):
    m_new = 2 * (y1 - y2)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        listaBitsLetra[x + y*6] = "0"

        slope_error_new = slope_error_new + m_new

        if slope_error_new >= 0:
          y = y - 1
          slope_error_new = slope_error_new - 2 * (x2 - x1)


def bresenhamXAbajoArriba(x1, y1, x2, y2):
    m_new = 2 * (x1 - x2)
    slope_error_new = m_new - (y2 - y1)

    x = x1
    for y in range(y1, y2 + 1):

        listaBitsLetra[x + y*6] = "0"
        slope_error_new = slope_error_new + m_new

        if (slope_error_new >= 0):
            x = x - 1
            slope_error_new = slope_error_new - 2 * (y2 - y1)

def bresenhamAbajoArriba(x1,y1,x2,y2):
    if (y1-y2) >= x2-x1:
        bresenhamYAbajoArriba(x1,y1,x2,y2)
    else:
        bresenhamXAbajoArriba(x1, y2, x2, y1)

def bresenhamArribaAbajo(x1,y1,x2,y2):
    if (y2-y1)>=x2-x1:
        bresenhamYArribaAbajo(x1,y1,x2,y2)
    else:
        bresenhamXArribaAbajo(x1, y1, x2, y2)


def drawCircle(xc, yc, x, y):
    xbits=xc + x
    ybits= (yc + y)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc - x
    ybits= (yc + y)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc + x
    ybits= (yc - y)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc - x
    ybits= (yc - y)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc + y
    ybits= (yc + x)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc - y
    ybits= (yc + x)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc + y
    ybits= (yc - x)*6
    listaBitsLetra[xbits+ybits]="0"
    xbits=xc - y
    ybits= (yc - x)*6
    listaBitsLetra[xbits+ybits]="0"

def lineaHorizontal(xi,yi,xf):
    for x in range(xi,xf+1):
        listaBitsLetra[x + yi*6] = "0"
def lineaVertical(xi,yi,yf):
    for y in range(yi,yf+1):
        listaBitsLetra[xi + y*6] = "0"


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
def printLetra():
    for i in range (6):
        print("".join(listaBitsLetra[i*6:(i+1)*6]))

listaBitsLetra=["1"]*6*6

def dibujarW():
    lineaVertical(0,0,4)
    lineaVertical(4,0,4)
    bresenhamAbajoArriba(0,4,2,2)
    bresenhamArribaAbajo(2,2,4,4)


xc = 2
yc = 2
r = 2
circleBres(xc, yc, r)
printLetra()
print("")
listaBitsLetra=["1"]*6*6
dibujarW()
printLetra()

