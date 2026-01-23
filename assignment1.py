1.calculate simple interest

#include<stdio.h>
int main() {
    float p,r,t;
    scanf("%f%f%f",&p,&r,&t);
    float si=(p*r*t)/100;
}

2.find maximum of two numbers

#include<stdio.h>
int main() {
    int a,b;
    scanf("%d%d",&a,&b);
    printf("%d", (a>b)?a:b);
}

3.print number 1 to 5

#include<stdio.h>
int main() {
    for(int i=1;i<=5;i++) {
        printf("%d\n",i);
    }
}

4.find length of a string

#include<stdio.h>
#include<string.h>
int main() {
    char str[50];
    gets(s);
    printf("length=%lu",strlen(str));
}

5.print a welcome message

#include<stdio.h>
int main() {
    printf("Welcome");
}

6.print first character of a string

#include<stdio.h>
int main() {
    char str[50];
    gets(str);
    printf("%c",str[0]);
}

7.print last character of a string

#include<stdio.h>
int main()
{
    char str[50];
    gets(str);
    printf("%c,s[strlen(str)-1]");
}

8.check positive number and negative number

#include<stdio.h>
int main() {
    int n;
    scanf("%c",&n);
    if(n>=0)
        printf("positive");
    else
        printf("negative");
}

9.add three numbers

#include<stdio.h>
int main() {
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    printf("sum=%d",a+b+c);
}

10.take input from the user

#include<stdio.h>
int main() {
    int x;
    scanf("%d",&x);
    printf("you entered=%d",x);
}]
