1.print message-write a program to print

#include<stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;   
}

2.add two numbers-take two number from the user and print their sum

#include<stdio.h>
int main() {
    printf("Enter two numbers: ");
    int a, b;
    scanf("%d %d", &a, &b);
    printf("Sum: %d\n", a + b);
    return 0;
}

3.even or odd-check whether a number is even or odd

#include<stdio.h>
int main() {
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    if (num % 2 == 0) {
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }
    return 0;
}

4.check leap year-check whether a year is leap year or not

#include<stdio.h>
int main() {
    printf("Enter a year: ");
    int year;
    scanf("%d", &year);
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("%d is a leap year.\n", year);
    } else {
        printf("%d is not a leap year.\n", year);
    }
    return 0;
}

5.print pi value

#include<stdio.h>
int main() {
    const float pi = 3.14159;
    printf("Value of Pi: %.5f\n", pi);
    return 0;
}

6.store and print constant value

#include<stdio.h>
int main() {
    const int constantValue = 42;
    printf("Constant Value: %d\n", constantValue);
    return 0;
}

7.calculate square of a number

#include<stdio.h>
int main() {
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    printf("Square of %d is %d\n", num, num * num);
    return 0;
}

8.calculate area of circle

#include<stdio.h>
#define PI 3.14159
int main() {
    printf("Enter radius of the circle: ");
    float radius;
    scanf("%f", &radius);
    float area = PI * radius * radius;
    printf("Area of the circle: %.2f\n", area);
    return 0;
}

9.check data type

#include<stdio.h>
int main() {
    printf("Size of int: %zu bytes\n", sizeof(int));
    printf("Size of float: %zu bytes\n", sizeof(float));
    printf("Size of double: %zu bytes\n", sizeof(double));
    printf("Size of char: %zu bytes\n", sizeof(char));
    return 0;
}

10.use math functions

#include<stdio.h>
#include<math.h>
int main() {
    double num;
    printf("Enter a number: ");
    scanf("%lf", &num);
    printf("Square root of %.2f is %.2f\n", num, sqrt(num));
    printf("Power of %.2f raised to 2 is %.2f\n", num, pow(num, 2));
    return 0;
}

11.find power of a number

#include<stdio.h>
#include<math.h>
int main() {    
    double base, exponent;
    printf("Enter base and exponent: ");
    scanf("%lf %lf", &base, &exponent);
    printf("%.2f raised to the power of %.2f is %.2f\n", base, exponent, pow(base, exponent));
    return 0;
}   

12.check positive or negative

#include<stdio.h>
int main() {
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    if (num > 0) {
        printf("%d is positive.\n", num);
    } else if (num < 0) {
        printf("%d is negative.\n", num);
    } else {
        printf("The number is zero.\n");
    }
    return 0;
}