#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin >> n;
	if(n&1)
	{
		cout << -1;
	}
	else
	{
		for(int i = 2; i<=n; i+=2)
		{
			cout << i << " " << i-1 << " ";
		}
	}
}