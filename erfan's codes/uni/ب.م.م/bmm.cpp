#include<iostream>
using namespace std;
int bmm (long long int a , long long int b);
int main()
{
    long long int a , b ;
    cin>>a;
    cin>>b;
    cout<<bmm(a,b);
}
int bmm (long long int a , long long int b)
{
    if(b==0)
        return(a);
    else if (a<b)
        return(bmm(b,a));
    else
        return(bmm(b,a%b));
}