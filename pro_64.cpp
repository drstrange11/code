#include<bits/stdc++.h>
using namespace std;
 //
int a[200000+50]={0};
 
struct zxttql
{
	int t,l,r;
} que[200000+50];
 
int main()
{
	ios::sync_with_stdio(false);
	//cin.tie(0);
	
	int n,q,m;
	cin>>n>>q>>m;
	for (int i=1;i<=n;i++) cin>>a[i];
	for (int i=1;i<=q;i++) cin>>que[i].t>>que[i].l>>que[i].r;
	
	for (int z=1;z<=m;z++)
	{
		int x;
		cin>>x;
		for (int i=q;i>=1;i--)
		{
			if (que[i].l<=x && x<=que[i].r)
			{
				if (que[i].t==1)
				{
					if (x==que[i].l) x=que[i].r;
					else x--;
				}
				else x=que[i].r+que[i].l-x;
			}
		}
		cout<<a[x]<<" ";
	}
	cout<<" ";
	return 0;
}
