#include<stdio.h>
#include<math.h>

// define function
double f(double x, double a, double b, double c) //Tạo hàm x^3-x^2+2
{
    return a*x*x+b*x+c  ;
}
//deriviate
double df(double x, double a, double b, double c)
{
    double del=0.0001;
    return (f(x+del, a, b, c)-f(x-del, a, b, c))/(2*del);
}
//Root-finding(Newton Raphson)
double Newt(double x, double a, double b, double c)
{
    double del=0.0001, dx=del+1;
    while(dx>del){
        double x0=x;
        x=x-f(x, a, b, c)/df(x, a, b, c);
        dx=x-x0;
        if(dx < 0 )
        {
            dx=-dx;
        }
    }
    return x;
}

int main()
{
    //doc thong tin
    FILE *fp;
    double a, b, c, x;
    fp = fopen("parameter.txt", "r");
    fscanf(fp, "%lf\n%lf\n%lf\n%lf", &a, &b, &c, &x);
    fclose(fp);
    
    //tim nghiem
    x=Newt(x, a, b, c);
    printf("Nghiem cua bai toan la: %lf\n", x);
    
    //Ghifile
    fp = fopen("result.txt","w");
    fprintf(fp, "Nghiem la x=%lf", x);
    fclose(fp);
    return 0;
}


