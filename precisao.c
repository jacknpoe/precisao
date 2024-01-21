#include <stdio.h>
#include <math.h>

int main(void){
	double precisao = pow(0.1, 15);
	if(fabs(0.4+0.2-0.6) < precisao){
		printf("True");
	} else {
		printf("False");
	}
}
