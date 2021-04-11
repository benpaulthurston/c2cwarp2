from PIL import Image
output = Image.new("RGB", (1000, 1000))
input = Image.open("mona.png")

points = [[52,168],[93,148],[133,144],[169,136],
          [205,148],[238,166],[271,198],[289,241],
          [291,268],[300,300],[304,330],[306,357],
          [304,381],[304,411],[298,460],[289,505],
          [261,529],[228,546],[201,556],[174,558],
          [144,549],[115,534],[93,516],[69,495],
          [51,468],[36,435],[33,388],[33,355],
          [31,320],[21,286],[25,243], [40,211]]
pointsout = [[610,331],[657,315],[688,312],[721,312],
             [756,307],[804,307],[829,307],[862,303],
             [886,298],[901,322],[910,354],[922,382],
             [928,414],[940,444],[951,472],[954,501],
             [964,526],[925,531],[874,535],[822,544],
             [774,550],[727,549],[694,550],[654,553],
             [612,567],[610,537],[610,505],[607,480],
             [601,454],[606,415],[604,380],[603,342]]
def transform(p0, p1, p2, q0, q1, q2, steps, input, output):
    
    m = [p1[0]-(p0[0]+p2[0])/2, p1[1]-(p0[1]+p2[1])/2]
    m = [m[0]/steps, m[1]/steps]
    n = [q1[0]-(q0[0]+q2[0])/2, q1[1]-(q0[1]+q2[1])/2]
    n = [n[0]/steps, n[1]/steps]
    for i in range(0, steps):
        x = (i/steps)*p0[0]+(1-(i/steps))*p2[0]
        y = (i/steps)*p0[1]+(1-(i/steps))*p2[1]
        u = (i/steps)*q0[0]+(1-(i/steps))*q2[0]
        v = (i/steps)*q0[1]+(1-(i/steps))*q2[1]
        for j in range(0, steps):
            color = input.getpixel((int(x +j*m[0]), int(y+j*m[1])))
            if ptInTriangle((int(u +j*n[0]), int(v+j*n[1])), q0, q1, q2):
                output.putpixel((int(u +j*n[0]), int(v+j*n[1])), color)
            
def ptInTriangle(p, p0, p1, p2):
    dX = p[0]-p2[0]
    dY = p[1]-p2[1]
    dX21 = p2[0]-p1[0]
    dY12 = p1[1]-p2[1]
    D = dY12*(p0[0]-p2[0]) + dX21*(p0[1]-p2[1])
    s = dY12*dX + dX21*dY
    t = (p2[1]-p0[1])*dX + (p0[0]-p2[0])*dY
    if (D<0):
        return s<=0 and t<=0 and s+t>=D
    return s>=0 and t>=0 and s+t<=D
    return newpoints, newpointsout

def midpoint(points):
    s, t = 0, 0
    for i in range(0, len(points)):
        s+=points[i][0]
        t+=points[i][1]
    return s/len(points), t/len(points)
m = midpoint(points)
n = midpoint(pointsout)
for i in range(0, len(points)-1):
    transform(points[i], points[i+1], m, pointsout[i], pointsout[i+1], n, 1000, input, output)
transform(points[len(points)-1], points[0], m, pointsout[len(pointsout)-1], pointsout[0], n, 1000, input, output)
output.save("monaout.png")
