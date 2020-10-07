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

float integralGaussHermite2(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - 1/sqrt(2);
  float x2 = 1/sqrt(2);
  float w1 = sqrt(PI)/2;
  float w2 = sqrt(PI)/2;

	integral = f(x1)*w1 + f(x2)*w2;

	return integral;
}

float integralGaussHermite3(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - sqrt(3)/sqrt(2);
  float x2 = 0;
  float x3 = sqrt(3)/sqrt(2);
  float w1 = sqrt(PI)/6;
  float w2 = 2*sqrt(PI)/3;
  float w3 = sqrt(PI)/6;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3;

	return integral;
}

float integralGaussHermite4(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - sqrt(3+sqrt(6))/sqrt(2);
  float x2 = - sqrt(3-sqrt(6))/sqrt(2);
  float x3 = sqrt(3-sqrt(6))/sqrt(2);
  float x4 = sqrt(3+sqrt(6))/sqrt(2);
  float w1 = 0.0813128354;
  float w2 = 0.8049140900;
  float w3 = 0.8049140900;
  float w4 = 0.0813128354;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3 + f(x4)*w4;

	return integral;
}

//----

int main () {

	float newintegral; 

  newintegral = integralGaussHermite2(function);
	printf("Integral por Hermite2 e: %.8f\n\n",newintegral);  
  
  newintegral = integralGaussHermite3(function);
	printf("Integral por Hermite3 e: %.8f\n\n",newintegral);

  newintegral = integralGaussHermite4(function);
	printf("Integral por Hermite4 e: %.8f\n\n",newintegral);

	return 0;
}
*/