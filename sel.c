#include <stdio.h>
#include <stdlib.h>
 #define MAX 50

  void selectionsort(int arr[],int size){
  	int i,j;
  	int min;
  	
  	for(i=0; i<size ;i++){
  		min=i;
  		for(j=i; j<size ;j++){
  			
  			if( arr[j]<arr[min]){
  				
  				min=j;
			  }
		  }	  
		  
		 
		  

 int temp=arr[i];
  arr[i]= arr[min];
  arr[min]=temp;
  }
  }
 
 
int main(){
	
	int array[MAX],size;
	int i;
	printf("kac elemanli");
	scanf("%d",&size);
	 for (i=0; i<size ; i++){
	 	
	 	scanf("%d",&array[i]);
	 }
	 selectionsort(array,size);
	  for(i=0; i<size;i++){
	  	
	  	printf("%d\n",array[i] );
	  }
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	system("pause");
	return 0;
}