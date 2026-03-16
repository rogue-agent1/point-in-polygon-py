#!/usr/bin/env python3
"""Point-in-polygon — ray casting and winding number algorithms."""

def ray_cast(point, polygon):
    x, y = point; n = len(polygon); inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]; xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi):
            inside = not inside
        j = i
    return inside

def winding_number(point, polygon):
    x, y = point; n = len(polygon); wn = 0
    for i in range(n):
        x1, y1 = polygon[i]; x2, y2 = polygon[(i+1)%n]
        if y1 <= y:
            if y2 > y and (x2-x1)*(y-y1)-(x-x1)*(y2-y1) > 0: wn += 1
        else:
            if y2 <= y and (x2-x1)*(y-y1)-(x-x1)*(y2-y1) < 0: wn -= 1
    return wn != 0

def main():
    poly = [(0,0),(4,0),(4,4),(0,4)]
    for p in [(2,2),(5,5),(0,0),(2,0)]:
        print(f"{p}: ray={ray_cast(p,poly)}, winding={winding_number(p,poly)}")

if __name__ == "__main__": main()
