#include <stdio.h>
 char * gun(char *gundi[],int uzunluk, int hangi){
 	
 	if (hangi >=1 && hangi <=7){
 	
	 return gundi[hangi-1]	;
	 
	 } 
	 else {
	 	return NULL;
	 }
	 }


int main (){
	
	
	char *gunler[7]  = {"pzt","sl","cr","pr","cm","cmt","pz"};
	 
	 
	 char *p=gun(gunler,7,5);
	 
	 
	 if(p== NULL){
	 	
	 	printf("Null");
	 	
	 }
	else {
		printf("%s",p);
	}
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}