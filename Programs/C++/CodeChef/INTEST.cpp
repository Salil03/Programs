#include<bits/stdc++.h>
using namespace std;

#define debug(x) cerr << "\n" << (#x) << " is " << (x) << endl
const double PI  = 3.141592653589793238463;
const int INF = 0x3f3f3f3f;
const int MOD = 1000000007;

/*
$alil03
Solution Begins here
*/

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n,k;
	cin >> n >> k;
	int ans = 0, temp;
	while(n--)
	{
		cin >> temp;
		if(temp%k == 0)
		{
			ans++;
		}
	}
	cout << ans;
	debug(ans);
}