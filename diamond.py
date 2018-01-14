# print a simple diamond pattern
# width input from user
def diamond(width=5, edge='*', fill='*'):
    mid = width // 2 + 1
    for x in list(range(mid)) + list(reversed(range(mid-1))):
        print(' '*(mid-x)+edge+fill*(x*2-1)+edge*(x!=0))

def main():
    diamond(int(input("Width (odd): ")), '*', '.')
    diamond()
    
if __name__ == "__main__":
    main()