#include <iostream>
#include <cstdlib>
#include <math.h>
using namespace std;

int main()
{
float a;
float b;
string c;

cout<<"N°: ";
cin>>a;
cout<<"N°: ";
cin>>b;
cout<<"Operacion: s(+), r(-), m(*), d(/) = ";
cin>>c;

if (c=="s")
{
cout<<"Resultado: "<<(a+b)<<endl;
}
if (c=="r")
{
cout<<"Resultado: "<<(a-b)<<endl;
}
if (c=="m")
{
cout<<"Resultado: "<<(a*b)<<endl;
}
if (c=="d")
{
cout<<"Resultado: "<<(a/b)<<endl;
}
cout<<"Fin ----"<<endl;

return 0;
}
