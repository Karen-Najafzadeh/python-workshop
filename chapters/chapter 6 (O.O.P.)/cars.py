class Particle:
    def __init__(self,M,V,Q):
        self.mass = M
        self.velosity = V
        self.charge = Q

    
    def momentum(self):
        self.P = self.mass * self.velosity
        print(f" momentum is equal to {self.P}")


p1 = Particle(1,2,4)
p2 = Particle(2,5,1)
p3 = Particle(3,2,0.5)
p4 = Particle(0.5,5,1)

print(Particle.objects.all())
