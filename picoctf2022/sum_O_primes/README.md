# sum_O_primes

![Screenshot_20220331_171219](https://user-images.githubusercontent.com/75040566/161075992-3c4cfb99-de4e-4a84-a019-6e6f7a28c2a3.png)


```
x = 17fef88f46a58da13be8083b814caf6cd8d494dd6c21ad7bf399e521e14466d51a74f51ad5499731018b6a437576e72bd397c4bb07bfbb699c1a35f1f4fa1b86dee2a1702670e9cea45aa7062f9569279d6d4b964f3df2ff8e38cf029faad57e42b831bde21132303e127cba4e80cd3c9ff6a7bad5b399a18252dc35460471ea8
n = 85393637a04ec36e699796ac16979c51ecea41cfd8353c2a241193d1d40d02701b34e9cd4deaf2b13b6717757f178ff75249f3d675448ec928aef41c39e4be1c8ba2ba79c4ada36c607763d7dc8543103acfe1027245acda2208f22fcabe0f37bdadf077e4f943c4f4178cedeb5279a4ebc86323356e23a58b6666ac6ffbf4f1c8229117ffb9071a94dfb724957f10d6664e4ee02e16bed29eb922f126e2082e2f73b5c5b7817e0543155eb9673f4de3de8c91707c1261e8ba6e7348d930293f7796679218c2b1dabe41527eccd72ec3e7284344622eff81ae0541769fb70b6146b54bd092c2dfbe7f8e9653cad80d0fb4f3ef288778927b3852f9ff3a4076d7
c = 42cafbc77ed8396a681dac328701ee02cd746488ae084f15a3e6a5b8f666c595a372a69bbca0dae934fd5ed2292d4393912ee10a22a3b57de9cee2f30b5dc7c67f574b0453f6074171cca37bd407529cb30ba17f152ef5b2484d94b38cf0a513a723255d725e5c3b3f3c985f9223095be3fa148afedf91e4ed37720c3d97dd29cf07830efa8a557a9da68d3095fc3b31f3763e030b62c70d94c3d2951e163e48683f3b9611d562ea06bf1e5d8465e8bf5a6345050a5e7b0c175faf136562cf2a196fdb61ac6503446616cffa9ed85015b86dda73f6eda4d688d3e719a07439d98f95fb5dcf675948ec58d9af83fa29afa4375213ec48f09a6c8cbc431cfe7c6a

```

i have n so if i tried to factor it i can get p , q . 


```python
from binascii import hexlify

import math
import os
import sys
from Crypto.Util.number import bytes_to_long , long_to_bytes

x = '17fef88f46a58da13be8083b814caf6cd8d494dd6c21ad7bf399e521e14466d51a74f51ad5499731018b6a437576e72bd397c4bb07bfbb699c1a35f1f4fa1b86dee2a1702670e9cea45aa7062f9569279d6d4b964f3df2ff8e38cf029faad57e42b831bde21132303e127cba4e80cd3c9ff6a7bad5b399a18252dc35460471ea8'

n =bytes_to_long(bytes.fromhex('85393637a04ec36e699796ac16979c51ecea41cfd8353c2a241193d1d40d02701b34e9cd4deaf2b13b6717757f178ff75249f3d675448ec928aef41c39e4be1c8ba2ba79c4ada36c607763d7dc8543103acfe1027245acda2208f22fcabe0f37bdadf077e4f943c4f4178cedeb5279a4ebc86323356e23a58b6666ac6ffbf4f1c8229117ffb9071a94dfb724957f10d6664e4ee02e16bed29eb922f126e2082e2f73b5c5b7817e0543155eb9673f4de3de8c91707c1261e8ba6e7348d930293f7796679218c2b1dabe41527eccd72ec3e7284344622eff81ae0541769fb70b6146b54bd092c2dfbe7f8e9653cad80d0fb4f3ef288778927b3852f9ff3a4076d7'))
c = bytes_to_long(bytes.fromhex('42cafbc77ed8396a681dac328701ee02cd746488ae084f15a3e6a5b8f666c595a372a69bbca0dae934fd5ed2292d4393912ee10a22a3b57de9cee2f30b5dc7c67f574b0453f6074171cca37bd407529cb30ba17f152ef5b2484d94b38cf0a513a723255d725e5c3b3f3c985f9223095be3fa148afedf91e4ed37720c3d97dd29cf07830efa8a557a9da68d3095fc3b31f3763e030b62c70d94c3d2951e163e48683f3b9611d562ea06bf1e5d8465e8bf5a6345050a5e7b0c175faf136562cf2a196fdb61ac6503446616cffa9ed85015b86dda73f6eda4d688d3e719a07439d98f95fb5dcf675948ec58d9af83fa29afa4375213ec48f09a6c8cbc431cfe7c6a'))

e = 65537
p = bytes_to_long(bytes.fromhex('8b8fb49184e98029504fcd38633252d869f653f6504f8d325cf93f2778986dea53f6c58c6507448cff3cd6001ffd56aea7168e985481f30bd2441b5ddeadff3d5e8502ee7e7fc5e0c89f459b391804d17522bce675b00e3e938e244290f5c51afe73f8fbc9fb44cd26d20819147929bf40c530d4f6074a72ee80b28e7c6816e9'))
q =bytes_to_long(bytes.fromhex('f45fd462e56f59ea6e30b67fb198a3f52352f9e071cb4a8cdca512f69badff6753588c20ef922e831979ce3737711c0e9265bd182779c38def5f43c170f3b9308fa51413e88ed7097d0b2ac7c03e8da861b1fc7e7e2f21ba4ffecbe769b792c92d0f22e25717de36ba55c38bd393aa0abea54ad865324fa536ad10c5e3df07bf'))


m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

m = pow(c,d,n)
print(long_to_bytes(m))

```



flag : picoCTF{3921def5}