import textwrap

def wrap(string, max_width):
    k = textwrap.fill(string,max_width)
    return k

if __name__ == '__main__':
