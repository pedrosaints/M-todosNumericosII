/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265	
typedef float (*FuncPointer)(float);

//-----
// PRECISA COLOCAR UMA FUNCAO COM OS LIMITES CERTOS, ESTOU USANDO ESSA ERRADA SO PARA TESTE
float function(float x) 
{	
	//RECEBO EM RADIANOS
	return pow((sin(2*x) + 4*x*x + 3*x),2);
}

//-----

float integralGaussLaguerre2(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = 2 - sqrt(2);
  float x2 = 2 + sqrt(2);
  float w1 = (2 + sqrt(2))/4;
  float w2 = (2 - sqrt(2))/4;

	integral = f(x1)*w1 + f(x2)*w2;

	return integral;
}

float integralGaussLaguerre3(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = 0.4157745568;
  float x2 = 2.2942803603;
  float x3 = 6.2899450829;
  float w1 = 0.7110930099;
  float w2 = 0.2785177336;
  float w3 = 0.0103892565;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3;

	return integral;
}

float integralGaussLaguerre4(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = 0.3225476442;
  float x2 = 1.7457611561;
  float x3 = 4.5366201401;
  float x4 = 9.3950710297;
  float w1 = 0.6031541043;
  float w2 = 0.3574186924;
  float w3 = 0.0388879085;
  float w4 = 0.0005392947;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3 + f(x4)*w4;

	return integral;
}

//----

int main () {

	float newintegral; 

  newintegral = integralGaussLaguerre2(function);
	printf("Integral por Laguerre2 e: %.8f\n\n",newintegral);  
  
  newintegral = integralGaussLaguerre3(function);
	printf("Integral por Laguerre3 e: %.8f\n\n",newintegral);

  newintegral = integralGaussLaguerre4(function);
	printf("Integral por Laguerre4 e: %.8f\n\n",newintegral);

	return 0;
}
*/