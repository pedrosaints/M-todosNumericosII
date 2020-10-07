/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265	
typedef float (*FuncPointer)(float);

//-----
float function(float x) 
{	
	//RECEBO EM RADIANOS
	return pow((sin(2*x) + 4*x*x + 3*x),2);
}

//-----


float integralnCloseNewtonCotes(float a,float b,FuncPointer f,int n)
{
	int j;
	float integral = 0;
	float x1;
	float x2;
	float fx;
	float delta = (b-a)/n;
	//loop limitado por n	
	for (j=0;j<n;j++) 
	{

		x1 = a + j*delta;
		x2 = x1 + delta;

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
	float oldintegral = integralnCloseNewtonCotes(a,b,function,n);	
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,oldintegral);
  count++;
	n = n*2;
	float newintegral = integralnCloseNewtonCotes(a,b,function,n);
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
  count++;
	while(fabs((newintegral-oldintegral)/newintegral)>erro)
	{
		oldintegral = newintegral;
		n = n*2;
		newintegral = integralnCloseNewtonCotes(a,b,function,n);
    count++;
		//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
	}
	
	printf("Com %d it.;para o intervalo [%.8f,%.8f] e %.8f de erro a ",count,a,b,erro);
	printf("Integral e: %.8f\n\n",newintegral);
	return 0;
}
*/