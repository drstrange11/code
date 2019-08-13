#include<iostream>
#include<cstdio>
#define MAXN 200005
using namespace std;
int n,q,m;
int a[MAXN];
int T[MAXN],L[MAXN],R[MAXN];
int main()
{
	scanf("%d%d%d",&n,&q,&m);
	for(int i=1;i<=n;i++) scanf("%d",&a[i]);
	for(int i=1;i<=q;i++) scanf("%d%d%d",&T[i],&L[i],&R[i]);
	int b;
	while(m--)
	{
		scanf("%d",&b);
		int tar=b;
		for(int i=q;i>=1;i--)
		{
			int l=L[i],r=R[i];
			if(T[i]==1)
			{
				if(tar>=l&&tar<=r)
				{
					if(tar!=l)
					{
						tar--;
					}
					else
					{
						tar=r;
					}
				}
			}
			else
			{
				if(tar>=l&&tar<=r) tar=r+l-tar;
			}
		}
		if(m-1==0)
		printf("%d",a[tar]);
		else
		printf("%d ",a[tar]);
	}
	return 0;
}
