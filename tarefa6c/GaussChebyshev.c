
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

float integralGaussChebyshev2(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - 1/sqrt(2);
  float x2 = 1/sqrt(2);
  float w1 = PI/2;
  float w2 = PI/2;

	integral = f(x1)*w1 + f(x2)*w2;

	return integral;
}

float integralGaussChebyshev3(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - sqrt(3)/2;
  float x2 = 0;
  float x3 = sqrt(3)/2;
  float w1 = PI/3;
  float w2 = PI/3;
  float w3 = PI/3;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3;

	return integral;
}

float integralGaussChebyshev4(FuncPointer f)
{
	int j;
	float integral = 0;
  float x1 = - sqrt(2+sqrt(2))/sqrt(4);
  float x2 = - sqrt(2-sqrt(2))/sqrt(4);
  float x3 = sqrt(2-sqrt(2))/sqrt(4);
  float x4 = sqrt(2+sqrt(2))/sqrt(4);
  float w1 = PI/4;
  float w2 = PI/4;
  float w3 = PI/4;
  float w4 = PI/4;

	integral = f(x1)*w1 + f(x2)*w2 + f(x3)*w3 + f(x4)*w4;

	return integral;
}

//----

int main () {

	float newintegral; 

  newintegral = integralGaussChebyshev2(function);
	printf("Integral por Chebyshev2 e: %.8f\n\n",newintegral);  
  
  newintegral = integralGaussChebyshev3(function);
	printf("Integral por Chebyshev3 e: %.8f\n\n",newintegral);

  newintegral = integralGaussChebyshev4(function);
	printf("Integral por Chebyshev4 e: %.8f\n\n",newintegral);

	return 0;
}
