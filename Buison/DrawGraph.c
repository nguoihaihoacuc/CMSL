#include <stdio.h>
#define ISCR 60 //Number of horizontal and vertical positions in display.
#define JSCR 21
#define BLANK ' '
#define ZERO '-'
#define YY 'l'
#define XX '-'
#define FF 'x'
void scrsho(float (*fx)(float))
//For interactive CRT terminal use. Produce a crude graph of the function fx over the promptedfor interval x1,x2. Query for another plot until the user signals satisfaction.
{
    int jz,j,i;
    float ysml,ybig,x2,x1,x,dyj,dx,y[ISCR+1];
    char scr[ISCR+1][JSCR+1];
    for (;;) {
        printf("\nEnter x1 x2 (x1=x2 to stop):\n"); //Query for another plot, quit
        scanf("%f %f",&x1,&x2);                     //if x1=x2.
        if (x1 == x2) break;
        for (j=1;j<=JSCR;j++) //Fill vertical sides with character ’l’.
            scr[1][j]=scr[ISCR][j]=YY;
        for (i=2;i<=(ISCR-1);i++) {
            scr[i][1]=scr[i][JSCR]=XX; //Fill top, bottom with character ’-’.
            for (j=2;j<=(JSCR-1);j++) //Fill interior with blanks.
            scr[i][j]=BLANK;}
        dx=(x2-x1)/(ISCR-1);
        x=x1;
        ysml=ybig=0.0; //Limits will include 0.
        for (i=1;i<=ISCR;i++) { //Evaluate the function at equal intervals.
                            //Find the largest and smallest values.
            if (y[i] < ysml) ysml=y[i];
            if (y[i] > ybig) ybig=y[i];
            x += dx;
            }
        if (ybig == ysml) ybig=ysml+1.0; //Be sure to separate top and bottom.
        dyj=(JSCR-1)/(ybig-ysml);
        jz=1-(int) (ysml*dyj); //Note which row corresponds to 0.
        for (i=1;i<=ISCR;i++) { //Place an indicator at function height and
            scr[i][jz]=ZERO; //0.
            j=1+(int) ((y[i]-ysml)*dyj);
            scr[i][j]=FF;
            }
        printf(" %10.3f ",ybig);
        for (i=1;i<=ISCR;i++) printf("%c",scr[i][JSCR]);
        printf("\n");
        for (j=(JSCR-1);j>=2;j--) { //Display.
        printf("%12s"," ");
        for (i=1;i<=ISCR;i++) printf("%c",scr[i][j]);
        printf("\n");
            }
        printf(" %10.3f ",ysml);
        for (i=1;i<=ISCR;i++) printf("%c",scr[i][1]);
        printf("\n");
        printf("%8s %10.3f %44s %10.3f\n"," ",x1," ",x2);
        }
}
void main()
{
    sch
}
