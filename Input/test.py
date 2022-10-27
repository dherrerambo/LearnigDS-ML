import msvcrt, time

start = time.time()
x = list()
aa = ""
while time.time()-start<10:
    x = x + [msvcrt.kbhit()]
    if msvcrt.kbhit():
        aa = input("Ingrese un valor:")
        break
print(aa, time.time()-start)