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
cout<<"Operacion: suma(s), resta(r), multiplica(m), divide(d) = ";
cin>>c;

if (c=="s")
{
cout<<"Resultado de la suma es : "<<(a+b)<<endl;
}
if (c=="r")
{
cout<<"Resultado de la resta es : "<<(a-b)<<endl;
}
if (c=="m")
{
cout<<"Resultado de la multiplicacion es: "<<(a*b)<<endl;
}
if (c=="d")
{
cout<<"Resultado de la divicion es : "<<(a/b)<<endl;
}
cout<<"Fin ----"<<endl;

return 0;
}
