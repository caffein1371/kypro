#include<bits/stdc++.h>

using namespace std;
int a[10010];

//main関数
int main(){
	int n;
    //入力
	cin >> n;
    //リスト入力　
	for(int i=0;i<n;i++)cin >> a[i];
	int ans=0;
	for(int l=0;l<n;l++){
        //区間最小値を定義
		int x=a[l];
		for(int r=l;r<n;r++){
			x=min(x,a[r]);
			ans=max(ans,x*(r-l+1));
		}
	}
	cout << ans;
}