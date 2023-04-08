#include <stdio.h>
 
 int main(){
 	
 	int vize1,vize2,final;
 	float dersort;
 	float ortalama;
 	printf ("1.vize:");
 	scanf("%d",&vize1);
 	printf ("2.vize:");
 	scanf("%d",&vize2);
 	printf ("final:");
 	scanf("%d",&final);
 	printf("ortalama:");
 	scanf("%f",&ortalama);
 	 
	dersort=(vize1+vize2+final)/3.0;  
	  if(dersort>60){
 		printf("gectin");
	 }
	 
	 
 	else if (dersort>=50) {
 		printf("but\n");
 		 if (ortalama<2.5){
 		 	printf("seneye al");
		  }
	 }
	 
	 else{
	 	
	 	printf("kaldiniz");
	 }
 	
 	
return 0; 	
 }