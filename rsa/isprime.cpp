#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(unsigned long long n) {
   if (n % 2 == 0) {
      return false;
   }
   for(int i = 3; i < sqrt((double) n)  + 1; i+=2) {
      if (n % i == 0) {
         return false;
      }
   }
   return true;
}

int main(int argc, char *argv[]) {
   cout << isPrime(atoll(argv[1])) << "\n";
}
