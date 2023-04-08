#include <stdio.h>

int main () {
	
	
	int vize;
	int final;
	float ort;
	
	printf("vize:");
	scanf("%d\n",&vize);
	
	printf("final:");
	scanf("%d\n\n",&final);
	
	ort= (vize*100.0/40.0) + final*100.0/40.0;
		printf("ortalamaniz %.2f'dir\n",ort);
	
	if(ort>= 40){
		
		printf("Hayirli olsun :)");
	}
	
	else {
		
		printf("gecmis olsun :(");
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}