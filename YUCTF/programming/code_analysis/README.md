# code_analysis

![code_analysis](https://user-images.githubusercontent.com/75040566/189969057-6824ca6d-2b83-4e93-ba52-a461c50f7af0.png)

```cpp
#include <iostream>
using namespace std;

int main() {
	string flag;
	cout << "Enter the flag: ";
	cin >> flag;

	for (int i=0; i < flag.length(); i++) {
		for (int j=i; j < flag.length() - 1; j++) {
			char x = flag[j];
			flag[j] = flag[j+1];
			flag[j+1] = x;
		}
	}

	if (flag == "ut{4c_3i_0_4}cch_YcytfNMfu")
		cout << "Congrats. That's the flag!" << endl;
	else
		cout << "Wrong flag. Bye" << endl;

	return 0;
}
```

```
cipher = list('ut{4c_3i_0_4}cch_YcytfNMfu')
for i in range(len(cipher) , -1 , -1):
    for j in range(  len(cipher) - 2  , i-1 , -1):
        cipher[j] , cipher[j+1] = cipher[j+1],cipher[j]
print(''.join(cipher))

```

flag = yuctf{c4tch_M3_if_Y0u_c4N}
