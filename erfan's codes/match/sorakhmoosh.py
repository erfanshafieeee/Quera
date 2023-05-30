import math
moosh,soorakh=map(int, input().split())
alamat=soorakh-moosh
meghdar=abs(alamat)
if alamat>0:
    print("R"*meghdar)
if alamat<0:
    print("L"*meghdar)
elif alamat==0:
    print("Saal Noo Mobarak!")