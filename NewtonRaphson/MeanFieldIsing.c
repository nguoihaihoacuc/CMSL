#include<stdio.h>
#include<math.h>

// define function
double f(double x, double T, double h, double z) //Tạo hàm ax^2+bx+c
{
    return tanh(1/T*(h+z*x))-x  ;
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
    double T, h, z, x0;
    fp = fopen("parameter.txt", "r");
    fscanf(fp, "%lf\n%lf\n%lf", &h, &z, &x0);
    printf("h=%lf\t z=%lf\t x0=%lf", h, z, x0);
    fclose(fp);
    //tim nghiem'
    int i=0, n=100;
    double tmax=10, del=tmax/n; 
    double t[n][2];
    
    for(T=del; T<tmax; T+=del){
        t[i][0]=Newt(x0, T, h, z);
        t[i][1]=T;        
        i++;
    }
    
    //Ghifile
    fp = fopen("result.txt","w");
    fprintf(fp,"T\tm\n");
    for(i=0; i<n;i++) fprintf(fp, "%lf\t%lf\n", t[i][1], t[i][0]);
    fclose(fp);
    return 0;
}


