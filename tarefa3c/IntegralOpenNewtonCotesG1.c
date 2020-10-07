/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265	
typedef double (*FuncPointer)(double);

//-----
double function(double x) 
{	
	//RECEBO EM RADIANOS
	return pow((sin(2*x) + 4*x*x + 3*x),2);
}

//-----


double integralnOpenNewtonCotes(double a,double b,FuncPointer f,int n)
{
	int j;
	double integral = 0;
	double xi;	
	double x1;
	double x2;
	double fx;
	double delta = (b-a)/n;
	double h = delta/3;
	//loop limitado por n	
	for (j=0;j<n;j++) 
	{
		xi = a + j*delta;
		x1 = xi + h;
		x2 = x1 + h;

		fx = (f(x1)+f(x2))*delta/2;
		//printf("f(x): %f\n",fx);

		integral = integral + fx;
		//printf("I: %f\n",integral);
		
	}
	return integral;
}

//----

int main () {

	float a = 0;
	float b = 1;
	float erro = 0.000001;

	//-------
	//----- loop por erro
  int count = 0;
	int n = 1;
	double oldintegral = integralnOpenNewtonCotes(a,b,function,n);	
  count++;
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,oldintegral);
	n = n*2;
	double newintegral = integralnOpenNewtonCotes(a,b,function,n);
  count++;
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
	while(fabs((newintegral-oldintegral)/newintegral)>erro)
	{
		oldintegral = newintegral;
		n = n*2;
		newintegral = integralnOpenNewtonCotes(a,b,function,n);
    count++;
		//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
	}
	
	printf("Com %d it.;para o intervalo [%.8f,%.8f] e %.8f de erro a ",count,a,b,erro);
	printf("Integral e: %.8f\n\n",newintegral);
	return 0;
}
*/