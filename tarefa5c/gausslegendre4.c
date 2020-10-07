
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef float (*FuncPointer)(float);

//-----
float function(float x) 
{	
	//RECEBO EM RADIANOS
	return pow((sin(2*x) + 4*x*x + 3*x),2);
}

//-----


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

  //  FALTA CALCULAR OS PESOS


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

	float a = 0;
	float b = 1;
	float erro = 0.000001;

	//-------
	//----- loop por erro
  int count = 0;
	int n = 1;
	float oldintegral = integralGaussLegendre(a,b,function,n);	
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,oldintegral);
  count++;
	n = n*2;
	float newintegral = integralGaussLegendre(a,b,function,n);
	//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
  count++;
	while(fabs((newintegral-oldintegral)/newintegral)>erro)
	{
		oldintegral = newintegral;
		n = n*2;
		newintegral = integralGaussLegendre(a,b,function,n);
    count++;
		//printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
	}
	
	printf("Com %d it.;para o intervalo [%.8f,%.8f] e %.8f de erro a ",count,a,b,erro);
	printf("Integral e: %.8f\n\n",newintegral);
	return 0;
}
