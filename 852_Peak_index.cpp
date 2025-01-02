#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define endl "\n"

int main()
{
   int n;
   cin>>n;
   vector<int >v(n);
   for(int i=0;i<n;i++)
   {
    cin>>v[i];
   }
   auto it=max_element(v.begin(),v.end());
cout<<it-v.begin();
return 0;
}