import hashlib
sort = hashlib.sha256(b"1234").hexdigest()
reza = "e254ad19d679ecdad2bb3fe08f1b14ab6ff988679c86f8b3e9ed2b7275dbd522"
ali = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
a= dict()

for counter in range(1236):
    a[str(counter)] = hashlib.sha256(str(counter).encode()).hexdigest()
m = list(a.values())



    
