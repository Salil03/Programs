//OPTIMIZATIONS
#pragma GCC optimize("O3")
//(UNCOMMENT WHEN HAVING LOTS OF RECURSIONS)
//#pragma comment(linker, "/stack:200000000")
//(UNCOMMENT WHEN NEEDED)
//#pragma GCC optimize("Ofast,unroll-loops,no-stack-protector,fast-math")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,tune=native")
//OPTIMIZATIONS
#include <bits/stdc++.h>
typedef long long ll;
typedef unsigned long long uu;
typedef long long int lll;
typedef unsigned long long int uuu;
using namespace std;

#define watch(x) cerr << "\n" \
					  << (#x) << " is " << (x) << endl
#define cel(x, y) 1 + ((x - 1) / y)
const double PI = 3.141592653589793238463;
const int MOD = 1000000007;
const long long int INF = 0x3f3f3f3f3f3f3f3f;

/*
$alil03

URL: url

Solution Begins here
*/

int x = 0, y = 0;
int n;
string s;
void recur(int idx, bool up, bool left)
{
	if (idx == n)
	{
		return;
	}
	if (s[idx] == 'L')
	{
		if (!left)
		{
			x--;
		}
		recur(idx + 1, 0, 1);
	}
	if (s[idx] == 'R')
	{
		if (!left)
		{
			x++;
		}
		recur(idx + 1, 0, 1);
	}
	if (s[idx] == 'U')
	{
		if (!up)
		{
			y++;
		}
		recur(idx + 1, 1, 0);
	}
	if (s[idx] == 'D')
	{
		if (!up)
		{
			y--;
		}
		recur(idx + 1, 1, 0);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;
	while (t--)
	{
		cin >> n >> s;
		recur(0, 0, 0);
		cout << x << " " << y << "\n";
		x = 0;
		y = 0;
	}
}