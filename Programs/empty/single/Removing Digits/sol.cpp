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

lll recur(lll n, lll dp[])
{
	if (dp[n] != -1)
	{
		return dp[n];
	}
	string s = to_string(n);
	lll ans = INT_MAX;
	for (char i : s)
	{
		lll temp = i - '0';
		if (temp == 0 || n - temp < 0)
		{
			continue;
		}
		ans = min(ans, 1 + recur(n - temp, dp));
	}
	return dp[n] = ans;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	lll n;
	cin >> n;
	lll dp[max(n + 1, (lll)12)];
	memset(dp, -1, sizeof dp);
	dp[0] = 0;
	for (int i = 1; i <= 9; i++)
	{
		dp[i] = 1;
	}
	if (n <= 9)
	{
		cout << dp[n];
		return 0;
	}
	cout << recur(n, dp);
}