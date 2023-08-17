def BLACK(c=100, r=0,   g=0,   b=0,   a=255):
    return [r*(c/100),g*(c/100),b*(c/100),a]

def RED  (c=100, r=255, g=0,   b=0,   a=255):
    return [r*(c/100),g*(c/100),b*(c/100),a]

def GREEN(c=100, r=0,   g=255, b=0,   a=255):
    return [r*(c/100),g*(c/100),b*(c/100),a]

def BLUE (c=100, r=0,   g=0,   b=255, a=255):
    return [r*(c/100),g*(c/100),b*(c/100),a]

def WHITE(c=100, r=255, g=255, b=255, a=255):
    return [r*(c/100),g*(c/100),b*(c/100),a]