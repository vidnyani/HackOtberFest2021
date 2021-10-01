#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int max(int a,int b) 
{ 
	return (a>b)?a:b; 
}
int main()
{
    string c1,c2;
    cout<<"Enter the Sequence:\n";
    cin>>c2;
    cout<<"Enter the Subsequence:\n";
    cin>>c1;
    char s1[c1.length()+1],s2[c2.length()+1];
    for(int i=1;i<c1.length()+1;i++)
    s1[i] = c1.at(i-1);
    for(int i=1;i<c2.length()+1;i++)
    s2[i] = c2.at(i-1);
    int dp[c1.length()+1][c2.length()+1];
    for(int i=0;i<c1.length()+1;i++)
    for(int j=0;j<c2.length()+1;j++) 
        dp[i][j]=0;
    for(int i=1;i<c1.length()+1;i++)
    for(int j=1;j<c2.length()+1;j++)
    {
        if(s1[i]==s2[j])
        {
            dp[i][j] = 1 + dp[i-1][j-1];
        }
        else
        {
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
        }
    }
    cout<<"The length of the longest Common Subsequence is "<<dp[c1.length()][c2.length()]<<endl;
    int i=c1.length(),j=c2.length();
    string lcs = " ";
    while(dp[i][j]!=0)
    {
        if(dp[i][j]!=dp[i][j-1])
        {
            lcs += s2[j];
            i--;
            j--;
        }
        else
            j--;
    }
    reverse(lcs.begin(),lcs.end()); 
    cout<<"The longest Common Subsequence is "<<lcs<<endl;
}