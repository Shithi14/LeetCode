#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    sort(v.rbegin(), v.rend()); // Sort in ascending order

    int d = v[0] - v[1]; // Calculate the common difference
    bool result = true;

    for (int i = 1; i < n-1; i++) { // Start from the third element
        if (v[i] - v[i + 1] != d) { // Check if the difference is consistent
            result = false;
            break;
        }
    }

    if (result) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}
/*  bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.rbegin(),arr.rend());
        int d=arr[0]-arr[1];
        for(int i=1;i<arr.size()-1;i++)
        {
            if(d!=arr[i]-arr[i+1])
            {
                return false ;
            }
        }
        return  true;*/
