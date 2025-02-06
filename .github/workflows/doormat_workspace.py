import random
import time
import math
import shutil

max_runtime = 60
start_time = time.time()

terminal_width = shutil.get_terminal_size().columns
disp=int(math.floor(((terminal_width-22)/2)))

while 1==1:
    print(("-"*disp+" Welcome Mat Designer "+"-"*disp).center(terminal_width))
    print("#It must be a odd number only.".rjust(terminal_width))
    S=str(random.randint(0, 20))
    print("Enter the width of the mat you want to design: "+S)

    while S.isdigit()==False or 3*int(S)>terminal_width or int(S)%2==0:
        print("TRY AGAIN! DESIGN NOT POSSIBLE!".center(terminal_width))
        S=str(random.randint(0, 20))
        print("Enter the width of the mat you want to design: "+S)
        time.sleep(3)
    N=int(S)
    M=3*N

    for i in range(1,N+1):
        if i<((N+1)/2):
            Z=int(((M-3*(2*i-1))/2))
            print(("-"*Z+".|."*(2*i-1)+"-"*Z).center(terminal_width))
        if i==((N+1)/2):
            Z=int(((M-7)/2))
            print(("-"*Z+"WELCOME"+"-"*Z).center(terminal_width))
        if i>((N+1)/2):
            i=N-i+1
            Z=int(((M-3*(2*i-1))/2))
            print(("-"*Z+".|."*(2*i-1)+"-"*Z).center(terminal_width))
    print(" ")
    print(" ")
    time.sleep(3)
    if time.time() - start_time > max_runtime:
        break
