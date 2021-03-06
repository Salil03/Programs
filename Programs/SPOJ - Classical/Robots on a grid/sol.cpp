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
const int INF = 0x3f3f3f3f;

/*
$alil03

URL: url

Solution Begins here
*/

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		char mp[n][n];
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> mp[i][j];
			}
		}
		lll dp[n][n] = {{0}};
		if (mp[0][0] == '#')
		{
			dp[0][0] = 0;
		}
		else
		{
			dp[0][0] = 1;
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == 0 && j == 0)
				{
					continue;
				}
				if (mp[i][j] = '#')
				{
					dp[i][j] = 0;
					continue;
				}
				if (i == 0)
				{
					dp[i][j] = dp[i][j - 1] % MOD;
				}
				else if (j == 0)
				{
					dp[i][j] = dp[i - 1][j] % MOD;
				}
				else
				{
					dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;
				}
			}
		}
		cout << dp[n - 1][n - 1] % MOD << "\n";
	}
}