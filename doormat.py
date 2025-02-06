import shutil
terminal_width = shutil.get_terminal_size().columns

print("Square Welcome Mat Designer".center(terminal_width))
print("#It must be a odd number only.".rjust(terminal_width))
N=int(input("Enter the dimension of the mat you want to design: "))
M=3*N
while M>terminal_width or N%2==0:
    print("TRY AGAIN! DESIGN NOT POSSIBLE!".center(terminal_width))
    N=int(input("Enter the dimension of the mat you want to design: "))
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