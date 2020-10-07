/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265	
typedef float (*FuncPointer)(float);

//-----
float function(float x) 
{	
	//return (1 / sqrt(2*(1+tanh(x)))) * (1 / pow(cosh(x),2));//FUNCAO TESTE P/ CALIBRAR SISTEMA
  
  //FUNCAO 2 EXPONENCIAL SIMPLES
  return (1 / sqrt(4 - pow((-1 + tanh(x)),2))) * (1 / pow(cosh(x),2)) ;

}

//-----

// 4 Pontos
float integralGaussLegendre(float a,float b,FuncPointer f,int n)
{
	int j;
	float integral = 0;
	float xi;
	float xf;
	float delta = (b-a)/n;
  float xa1;
  float xa2;
  float xa3;
  float xa4;
  float fxa1;
  float fxa2;
  float fxa3;
  float fax4;
  float w1;
  float w2;
  float w3;
  float w4;


  w1 = 0.3478548451374538;
  w2 = 0.6521451548625461;
  w3 = 0.6521451548625461;
  w4 = 0.3478548451374538;
  //printf("w1=%f w2=%f w3=%f w4=%f\n",w1,w2,w3,w4);

	//loop limitado por n	
	for (j=0;j<n;j++) 
	{
    //calculo o xi e xf para cada divisao
		xi = a + j*delta;
		xf = xi + delta;
    //printf("xi=%f xf=%f\n",xi,xf);

    //calculo de x(a1),x(a2),x(a3) e x(a4)
    xa1 = ((xi+xf)/2 - (((xf-xi)/2) * sqrt(30 + 4*sqrt(30))/sqrt(70) ));
    xa2 = ((xi+xf)/2 - (((xf-xi)/2) * sqrt(30 - 4*sqrt(30))/sqrt(70) ));
    xa3 = ((xi+xf)/2 + (((xf-xi)/2) * sqrt(30 - 4*sqrt(30))/sqrt(70) ));
    xa4 = ((xi+xf)/2 + (((xf-xi)/2) * sqrt(30 + 4*sqrt(30))/sqrt(70) ));

    //printf("xa1=%f xa2=%f xa3=%f xa4=%f\n",xa1,xa2,xa3,xa4);

		fxa1 = f(xa1);
    fxa2 = f(xa2);
    fxa3 = f(xa3);
    fax4 = f(xa4);
    //printf("fxa1=%f fxa2=%f fxa3=%f fxa4=%f\n",fxa1,fxa2,fxa3,fax4);

		integral = integral + (xf-xi)/2 * (fxa1*w1 + fxa2*w2 + fxa3*w3 + fax4*w4);
		//printf("I: %f\n",integral);
		
	}
	return integral;
}

//----

int main () {

  //loop por c
	//-------

  float c = 1;
	float erro = 0.01;
    //----- loop por n
    int count = 0;
    int n = 1;
    float oldintegral = integralGaussLegendre(-c,c,function,n);	
    //printf("p/ n=%d, Integral e: %.8f\n\n",n,oldintegral);
    count++;
    n = n*2;
    float newintegral = integralGaussLegendre(-c,c,function,n);
    //printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
    count++;
    while(fabs((newintegral-oldintegral)/newintegral)>erro)
    {
      oldintegral = newintegral;
      n = n*2;
      newintegral = integralGaussLegendre(-c,c,function,n);
      count++;
      //printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
    }
    //printf("Para o intervalo [%.8f,%.8f] e %f de erro a ",-c,c,erro);
    //printf("Integral e: %.8f\n\n",newintegral);

    float finalintegral;

    do
    { 
      c++;
      finalintegral = newintegral;
      count = 0;
      n = 1;
      oldintegral = integralGaussLegendre(-c,c,function,n);	
      count++;
      n = n*2;
      newintegral = integralGaussLegendre(-c,c,function,n);
      count++;
      while(fabs((newintegral-oldintegral)/newintegral)>erro)
      {
        oldintegral = newintegral;
        n = n*2;
        newintegral = integralGaussLegendre(-c,c,function,n);
        count++;
      }
      //printf("Para o intervalo [%.8f,%.8f] e %f de erro a ",-c,c,erro);
      //printf("Integral e: %.8f\n\n",newintegral);
    }
    while (fabs((newintegral-finalintegral)/finalintegral)>erro);
    //while (c>2);

  finalintegral = newintegral;


	printf("Para o intervalo [%.8f,%.8f] e %f de erro a ",-c,c,erro);
	printf("Integral e: %.8f\n\n",finalintegral);

	return 0;
}
*/