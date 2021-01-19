valor=int(input("Quanto você deseja sacar? R$ "))
total=valor
ced=50
totaldeced=0
while True:
    if total >= ced:
        total=total-ced
        totaldeced=totaldeced+1
    else:
        print(f'total de {totaldeced} cedulas de RS {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totaldeced=0
        if total==0:
            break