use std::env;
use std::cell::RefCell;

fn main() {
    println!("{}", isPrime(env::args().nth(1).unwrap().parse().unwrap(), &[]));
}

fn isPrime(n: usize, primes: &[usize]) -> bool {
    let prime_vec: RefCell<Vec<usize>> = RefCell::new(primes.into());
    if prime_vec.borrow().len() < 3 {
        *prime_vec.borrow_mut() = vec![2, 3, 5];
    }
    
    (3..(n as f32).sqrt() as usize + 1).step_by(2).filter(|n| prime_vec.borrow().contains(n) || isPrime(*n, &prime_vec.borrow())).all(|i|{
        if !prime_vec.borrow().contains(&i) {
            prime_vec.borrow_mut().push(i);
        }
        n % i != 0
    })
}
