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
