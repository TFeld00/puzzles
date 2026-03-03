def area(points:list):
    a=0
    for i in range(len(points)):
        a+=(points[i-1][1]+points[i][1])*(points[i-1][0]-points[i][0])
    return a//2

def area_pixels(points:list, includePerimeter:bool=True):
    a=0
    perimeter = 0
    for i in range(len(points)):
        a+=(points[i-1][1]+points[i][1])*(points[i-1][0]-points[i][0])
        perimeter+=abs(points[i-1][1]-points[i][1])+abs(points[i-1][0]-points[i][0])
    
    if includePerimeter:
        return a//2+perimeter//2+1
    else:
        return a//2-perimeter//2+1