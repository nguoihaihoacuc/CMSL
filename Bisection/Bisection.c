#include<stdio.h>
#include<math.h>
#define Epsilon 0.0001
//Define function
double func(double x, double a, double b, double c)
{    return a*x*x+b*x+c;}
//Root Finding
double bisection(double a, double b, double a1, double b1, double c1) 
{
    double c=0;
    if(func(a,a1,b1,c1)*func(b,a1,b1,c1)>=0) 
        printf("Mien khong co nghiem duy nhat tai a=%.1lf\n", a1);
    else{
        int i=1;
        while((b-a)>Epsilon)               
        {
            c=(a+b)/2;
            if(func(c,a1,b1,c1)*func(a,a1,b1,c1)>0)     
                a=c;
            else                                                        
                b=c;
            printf("c=%lf tai vong thu %d \n", c, i);
            i++;
        }
    }
    return c;
}

//main
int main()
{
    //doc thong tin
    FILE *fp;
    double a, b, c, x;
    fp = fopen("parameter.txt", "r");
    fscanf(fp, "%lf\n%lf\n%lf\n%lf", &a, &b, &c, &x);
    fclose(fp);

    double a=1,b=-5,c=6;
    double a1 =-200, b1 = 2.5, x0; 
    x0=bisection(a1, b1, a, b, c);
    if(x0!=0)
        printf("Nghiem x0=%lf tai a = %.1lf\n", x0, a);


}
