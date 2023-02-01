def printbord(xseat,zseat):
    
    zero="X" if xseat[0] else("0" if zseat[0] else 0)
    one="X" if xseat[1] else("0" if zseat[1] else 1)
    two="X" if xseat[2] else("0" if zseat[2] else 2)
    three="X" if xseat[3] else("0" if zseat[3] else 3)
    four="X" if xseat[4] else("0" if zseat[4] else 4)
    five="X" if xseat[5] else("0" if zseat[5] else 5)
    six="X" if xseat[6] else("0" if zseat[6] else 6)
    seven="X" if xseat[7] else("0" if zseat[7] else 7)
    eight="X" if xseat[8] else("0" if zseat[8] else 8)
    
    print(f"     {zero} | {one} | {two} ")
    print(f"    ---|---|---")
    print(f"     {three} | {four} | {five} ")
    print(f"    ---|---|---")
    print(f"     {six} | {seven} | {eight} ")
    
def sum(a,b,c):
    return a+b+c
def checkwins(xseat,zseat):

    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins :
        if (sum(xseat[win[0]],xseat[win[1]],xseat[win[2]])==3):
            print("    +-------------+")
            print("    |             |")
            print("    |  X's Win!   |")
             
            return 1
        if (sum(zseat[win[0]],zseat[win[1]],zseat[win[2]])==3):
            print("    +-------------+")
            print("    |             |")
            print("    |  Z's Win!   |")
             
            return 0
    return -1

if __name__=="__main__":
    
    xseat=[0,0,0,0,0,0,0,0,0]
    zseat=[0,0,0,0,0,0,0,0,0]
    turn=1#1 for x and 0 for zero
    print("+-------------------------+")
    print("|                         |")
    print("|  Welcome To Tic Tac Toe |")
    print("|                         |")
    print("+-------------------------+")
    print()
    while True:
        printbord(xseat,zseat)
        if turn==1:
            print()
            print("+----------------+")
            print("| X's chance     |")
            value=int(input("| enter a value:"))
            print("+----------------+")
            print()
            xseat[value]=1
         
        else:
            print()
            print("+----------------+")
            print("| Z's chance     |")
            value=int(input("| enter a value:"))
            print("+----------------+")
            
            print()
            zseat[value]=1
        chek=checkwins(xseat,zseat)
        if chek!=-1:
            print("    |  Game Over  |")
            print("    |             |")
            print("    +-------------+")
            
            break
        turn=1-turn
        
 
