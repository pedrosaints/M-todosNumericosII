#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265	
typedef float (*FuncPointer)(float,float);

//-----
float function(float x,float y) 
{	

  //teste do problema1
  //return pow(40*x,2)-pow(20 * y,2);

	return (320*pow(0.5*(x+1),2)*pow(cos((PI*(y+1))),2))-(80*pow(0.5*(x+1),2)*pow(sin((PI*(y+1))),2));
}

//-----


float integralGaussLegendre(float a,float b,FuncPointer f,int n)
{
	int j,i;
	float integral = 0;
	float xi;
	float xf;
	float delta = (b-a)/n;
  float xa1;
  float xa2;
  float xa3;
  float yi;
	float yf;
  float ya1;
  float ya2;
  float ya3;
  float fxa1;
  float fxa2;
  float fxa3;
  float fxa4;
  float fxa5;
  float fxa6;
  float fxa7;
  float fxa8;
  float fxa9;
  float w1;
  float w2;
  float w3;
  w1 = 5/sqrt(81);
  w2 = 8/sqrt(81);
  w3 = 5/sqrt(81);

	//loop limitado por n	
  
    for (j=0;j<n;j++) 
    {
      //calculo o xi e xf para cada divisao
      xi = a + j*delta;
      xf = xi + delta;
      yi = a + j*delta;
      yf = yi + delta;
      //printf("xi=%f xf=%f\n",xi,xf);

      //calculo de x(a1),x(a2) e x(a3)
      xa1 = ((xi+xf)/2 - (((xf-xi)/2)*sqrt(3)/sqrt(5)));
      xa2 = (xi+xf)/2 + ((xf-xi)/2)*0;
      xa3 = ((xi+xf)/2 + (((xf-xi)/2)*sqrt(3)/sqrt(5)));
      ya1 = ((yi+yf)/2 - (((yf-yi)/2)*sqrt(3)/sqrt(5)));
      ya2 = (yi+yf)/2 + ((yf-yi)/2)*0;
      ya3 = ((yi+yf)/2 + (((yf-yi)/2)*sqrt(3)/sqrt(5)));

      //printf("xa1=%f xa2=%f xa3=%f\n",xa1,xa2,xa3);

      fxa1 = f(xa1,ya1);
      fxa2 = f(xa1,ya2);
      fxa3 = f(xa1,ya3);
      fxa4 = f(xa2,ya1);
      fxa5 = f(xa2,ya2);
      fxa6 = f(xa2,ya3);
      fxa7 = f(xa3,ya1);
      fxa8 = f(xa3,ya2);
      fxa9 = f(xa3,ya3);
      //printf("fxa1=%f fxa2=%f fxa3=%f\n",fxa1,fxa2,fxa3);

      integral = integral + (xf-xi)/2 * (fxa1*w1*w1 + fxa2*w1*w2 + fxa3*w1*w3 + fxa4*w2*w1 + fxa5*w2*w2 + fxa6*w2*w3 + fxa7*w3*w1 + fxa8*w3*w2 + fxa9*w3*w3);
      //printf("I: %f\n",integral);
      
    }
  
	return integral;
}

//----

float GaussLegendre (float a, float b, float erro, FuncPointer func) {

	//-------
	//----- loop por erro
  int count = 0;
	int n = 1;
	float oldintegral = integralGaussLegendre(a,b,func,n);	
	printf("p/ n=%d, Integral e: %.8f\n\n",n,oldintegral);
  count++;
	n = n*2;
	float newintegral = integralGaussLegendre(a,b,func,n);
	printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
  count++;
	
  while(fabs((newintegral-oldintegral)/newintegral)>erro)
	{
		oldintegral = newintegral;
		n = n*2;
		newintegral = integralGaussLegendre(a,b,func,n);
    count++;
		printf("p/ n=%d, Integral e: %.8f\n\n",n,newintegral);
    printf(".\n");
	}
  
	
	//printf("Com %d it.;para o intervalo [%.8f,%.8f] e %.8f de erro \n",count,a,b,erro);
	//printf("Integral e: %.8f\n\n",newintegral);
	return newintegral;
}


int main () {

float integral = GaussLegendre(-1,1,0.000001,function);

printf("Volume e: %.8f\n\n",integral*PI/2);



 return 0; 
}