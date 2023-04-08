#include <stdio.h>
#include <stdlib.h>



int main(){
	
	int ilksay=1;
	int ikincisay =1;
	int i;
	
	
	printf("%d\n%d\n",ilksay,ikincisay);
 
 for(i=0; i<12 ; i++){
 	
 	
 	int temp = ikincisay;
 	ikincisay+=ilksay;
 	ilksay= temp;
 	
 	printf("%d\n",ikincisay);
 }
 
 	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}