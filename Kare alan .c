#include <stdio.h>
#define PI 3.14
 int main (){
 	
 
 	
 	int a;
 	int b;
 	int alan;
 	
 	printf("dikdortgenin alani:");
 	 scanf("%d",&a);
 	 scanf("%d",&b);
 	 
	  alan= (a*b);
 	printf("dikdortgenin alani %d'dir\n\n",alan);
 	
 	
 	int kenar;
 	int alan2;
 	
 	printf("karenin alani:");
 	scanf("%d",&kenar);
 	
 	alan2=(kenar*kenar);
 	 printf("karenin alani %d'dir\n\n",alan2);
 	 
 	 
 	 int dik;
 	 int yatay;
 	 int alan3;
 	 
 	 printf("ucgenin alani:");
 	  scanf("%d",&dik);
 	  scanf("%d",&yatay);
 	  
 	  alan3=(dik*yatay)/2;
 	  printf("ucgenin alani %d'dir\n\n",alan3);
 	  
 	  
 	  int r;
 	  float alan4;
 	  
 	  printf("dairenin alani:");
 	  scanf("%d",&r);
 	  
 	  alan4 =(PI*r*r);
 	  printf("dairenin alani %f'dir:",alan4);
 	
 	
 	
 	
 	
 	return 0;
 }