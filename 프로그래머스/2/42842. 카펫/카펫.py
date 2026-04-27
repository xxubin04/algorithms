def solution(brown, yellow):
    x = ((brown/2-2) + ((brown/2-2)**2 - 4*yellow)**(1/2))/2
    if x != int(x):
        x = ((brown/2-2) - ((brown/2-2)**2 - 4*yellow)**(1/2))/2
    
    y = (brown/2) - x - 2
    if y > x:
        x, y = y, x
    return [x+2, y+2]