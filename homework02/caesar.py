def find_shift(ciphertext):
    print("Problem 2:")
    d = [0]*26
    frequencies = [.08, .015, .03, .04, .130, .02, .015, .06, .065, .005, .005, .035, .03, .07, .08, .02, .002, .065, .06, .09, .03, .01, .015, .005, .02, .002]
    for c in ciphertext:
        d[ord(c)-65]+=1
    for c in range(len(d)):
        d[c]/=len(ciphertext)
        
    shifts={}
    for i in range(26):
        p=0
        for c in range(26):
            p+=d[c]*frequencies[(c-i)%26]
        shifts[i]=p

    shifts = dict(sorted(shifts.items(), key = lambda x:x[1], reverse=True))
    for key, value in shifts.items():
        print(f"{key:2.0f}: {value:.4f}") 
        
    shift = list(shifts.keys())[0]
    plaintext=''
    for c in ciphertext:
        plaintext+=chr((ord(c)-65-shift)%26+65)
        
    print(f"\nThe key is {shift} and the plaintext is {plaintext}\n")
    
        
def main():
    find_shift("JVTWBALYZJPLUJL")
    
if __name__ == "__main__":
    main()