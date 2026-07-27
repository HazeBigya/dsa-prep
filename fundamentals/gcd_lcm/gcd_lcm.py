def gcd_lcm(a: int,b: int):
    product = a * b
    while b != 0:
        a, b = b, a % b
    GCD = a
    LCM = product // GCD
    print("GCD :", GCD, "LCM :", LCM)
    
gcd_lcm(48, 18)
        
def gcd_lcm_recursion(a, b):
    def get_gcd(x, y):
        if y == 0:
            return x
        return get_gcd(y, x % y)
    
    product = a * b
    GCD = get_gcd(a, b)
    LCM = product // GCD
    
    print("GCD :", GCD, "LCM :", LCM)
    
gcd_lcm_recursion(48, 18)