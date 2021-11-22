%%cu
/* Pract 8 PS 1.1 */

#include<stdio.h>
#include<cuda.h>
#define row1 10 
#define col1 10  

#define col2 10 

_global_ void matrix_multiply(int *l,int *m, int *n)
{
    int x=blockIdx.x;
    int y=blockIdx.y;
    int k;
  
n[col2*y+x]=0;
for(k=0;k<col1;k++)
   {
    n[col2*y+x]=n[col2*y+x]+l[col1*y+k]*m[col2*k+x];
   }
}

int main()
{
    int a[row1][col1];
    int b[col2];
    int c[row1][col2];
    int *d,*e,*f;
    int i,j;

    for(i=0;i<row1;i++)
    {
        for(j=0;j<col1;j++)
            {
                a[i][j]=i;
            }
    }
    
        for(i=0;i<col2;i++)
        {
           b[i]=2;
        }

    double time_spent = 0.0;
    clock_t begin = clock();
 
    cudaMalloc((void **)&d,row1*col1*sizeof(int));
    cudaMalloc((void **)&e,col2*sizeof(int));
    cudaMalloc((void **)&f,row1*col2*sizeof(int));

 cudaMemcpy(d,a,row1*col1*sizeof(int),cudaMemcpyHostToDevice);
 cudaMemcpy(e,b,col2*sizeof(int),cudaMemcpyHostToDevice);

dim3 grid(col2,row1);
    matrix_multiply<<<grid,1>>>(d,e,f);

 cudaMemcpy(c,f,row1*col2*sizeof(int),cudaMemcpyDeviceToHost);

 printf("\nVector:\n");
 for(i=0;i<col2;i++)
 printf("%d\t",b[i]);

 printf("\nMatrix:\n");
 for(i=0;i<row1;i++)
 {
     for(j=0;j<col1;j++)
     {
         printf("%d\t",a[i][j]);
     }
  printf("\n");
 }
  printf("\nProduct of vector and matrix:\n ");
    for(i=0;i<row1;i++)
    {
        for(j=0;j<col2;j++)
        {
              printf("%d\t",c[i][j]);
        }
        printf("\n");
    }
    cudaFree(d);
    cudaFree(e);
    cudaFree(f);
 
  

    return 0;
}