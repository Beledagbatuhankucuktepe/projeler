#include <stdio.h>
#include <stdlib.h>



int main (){
	
	int ders;
    int vize;
	float vizeetk;
	int final;
	float finaletk;
	float ort; 
	
	
		 
		 printf("dersler\n1:is hukuku -SGK\n2:Sigorta \n3:Diger\n\n\n\n");
		 
		 printf("Dersi seciniz:");
		 scanf("%d",&ders);
		 
		 switch(ders){

case 1 : 

	printf("vize:");
	scanf("%d",&vize);
	
	
	vizeetk=vize*40/100 ;
	printf("vizeetk %f'dir\n",vizeetk);
	
	
	
	printf("final:");
	scanf("%d",&final);
	
	if(final<50){
		printf("kaldiniz:(");
	}		 
		 else {
		 		finaletk=final*60/100;
	printf("finaletk %f'dir\n",finaletk);
	
	
	ort= finaletk + vizeetk;
	printf("ortalamaniz %.2f'dir\n",ort);}
	
	break;
		
	case 2:
		
		
		printf("vize:");
	scanf("%d",&vize);
	
	
	vizeetk=vize*30/100 ;
	printf("vizeetk %f'dir\n",vizeetk);
	
	
	
	printf("final:");
	scanf("%d",&final);
		
		
			finaletk=final*70/100;
	printf("finaletk %f'dir\n",finaletk);
	
	
	ort= finaletk + vizeetk;
	printf("ortalamaniz %.2f'dir\n",ort);
		 
		 break;
		
		 case 3:
		
			
		printf("vize:");
	scanf("%d",&vize);
	
	
	vizeetk=vize*40/100 ;
	printf("vizeetk %f'dir\n",vizeetk);
	
	
	
	printf("final:");
	scanf("%d",&final);
		
		
			finaletk=final*60/100;
	printf("finaletk %f'dir\n",finaletk);
	
	
	ort= finaletk + vizeetk;
	printf("ortalamaniz %.2f'dir\n",ort);
	
	
	break;
		
	}
		 

	
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 		 
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		 system("pause");
		 return 0;

		 
		 
		 }
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
