#include<iostream> 
#include<algorithm> 
#include<set>
using namespace std; 
int minsum = 0;
int minvalue(int value[], bool mstSet[]) 
{ 
	int min = INT_MAX, min_index; 
	for (int v = 0; v < 5; v++) 
		if (mstSet[v] == false && value[v] < min) 
			min = value[v], min_index = v; 
	return min_index; 
} 
void printMST(int conMST[], int tree[5][5]) 
{ 
	cout<<"Edge \tcost\n"; 
	for (int i = 1; i < 5; i++) 
    {
	cout<<conMST[i]<<" - "<<i<<" \t"<<tree[i][conMST[i]]<<" \n"; 
    minsum+=tree[i][conMST[i]];
    }
    cout<<"\nThe Minimum cost is:"<<minsum<<endl;
} 
void primMST(int tree[5][5],int n) 
{ 
	int conMST[n]; 
	int value[n]; 
	bool mstSet[n]; 
	for (int i = 0; i<n; i++) 
		value[i] = INT_MAX, mstSet[i] = false; 
	value[0] = 0; 
	conMST[0] = -1; 
	for (int count = 0; count <n-1; count++) 
	{ 
		int u = minvalue(value, mstSet); 
		mstSet[u] = true; 
		for (int v = 0; v < n; v++) 
			if (tree[u][v] && mstSet[v] == false && tree[u][v] < value[v]) 
				conMST[v] = u, value[v] = tree[u][v]; 
	} 
	printMST(conMST, tree); 
} 
int main() 
{ 
    long n;
    cout<<"Enter the number of nodes\n";
    cin>>n;
    int tree[5][5];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        {
            if(j==i)
            tree[i][j]=0;
            else
            {
                cout<<"Enter the cost of going from node "<<i <<" to "<< j <<endl;
                cin>>tree[i][j];
            }
        }
	primMST(tree,n);
	return 0;
} 