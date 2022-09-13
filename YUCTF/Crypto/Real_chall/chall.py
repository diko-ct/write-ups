from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes , getPrime , bytes_to_long
Flag = bytes_to_long(b'flagflagfalg')

e = 0x10001

n = 21834392376036708811228147577736892946221656878362989506541202607899086080496115476373305675256978315376138633766659899398733321675891283593097366368545236158428844392069577569821642902360689738630484552337772743634427988041805896179177903785504086527601131289233627385348872054076863619038294956190951338101627445902532691518624915081971627771681764329595799268000414035053506341321664481623459731701795970511378258455370525920613583052102124748854047634164201228185675685947231539737069464308570132579603082540473473618888107118651757906470284392087247216177100858859184261228161265047487421986966068525231252986843



print(n ,e ) 
print(pow(Flag,e,n))
#O1 = (2*p + 3*q)**W1 mod N
#O2 = (5*p + 7*q)**W2 mod N
