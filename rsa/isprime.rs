use std::env;

fn main() {
    println!("{}", is_prime(env::args().nth(1).unwrap().parse().unwrap()));
}

fn is_prime(n: usize) -> bool {
    let sqrt_ish = (n as f32).sqrt() as usize + 1;
    if n % 2 == 0 {
        false
    } else {
        (3..sqrt_ish).step_by(2).all(|i|{
                n % i != 0
        })
    }
}
