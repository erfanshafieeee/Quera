#include <iostream>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int main()
{
	string s;
	cin >> s;
	int ans = 1;
	for(int i = 0; i < s.size(); i++)
		switch (s[i])
		{
			case 'L':
			case 'F': 
			case 'T':
			case 'D': ans *= 2; break;
		};

	cout << ans << endl;
}