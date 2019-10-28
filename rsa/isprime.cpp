#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

bool isPrime(unsigned long long n, vector<int> &primes) {
   for(int i = 3; i < sqrt((double) n)  + 1; i+=2) {
      bool in_list = find(primes.begin(), primes.end(), i) != primes.end();
      if (in_list || isPrime(i, primes)) {
         if (!in_list)
            primes.push_back(i);
         if (n % i == 0) {
            return false;
         }
      }
   }
   return true;
}

bool isPrime(unsigned long long n) {
   vector<int> primes = {2, 3, 5};
   cout << n << "\n";
   return isPrime(n, primes);
}

int main(int argc, char *argv[]) {
   cout << isPrime(atoll(argv[1])) << "\n";
}
