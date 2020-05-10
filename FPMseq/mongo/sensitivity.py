# coding: utf-8


class calculation:
    def __init__(self, reads, IC):
        self.reads = reads
        self.IC = IC
        self.hum = 3.3*490000000*401*self.reads/(6000000000*self.IC)
    
    # def hum(self):
    #     hum_int = self.hum

    def bac(self):
        bac = 6000000000*self.hum/(4000000*self.reads)
        bac = round(bac)
        return bac

    def fun(self):
        fun = 6000000000*self.hum/(10000000*self.reads)
        fun = round(fun)
        return fun

    def vir(self):
        vir = 6000000000*self.hum/(10000*self.reads)
        vir = round(vir)
        return vir

    def par(self):
        par = 6000000000*self.hum/(1000000000*self.reads)
        par = round(par)
        return par
    pass


reads = float(input("输入数据量："))
IC = float(input("请输入内参："))
cal = calculation(reads, IC)
hum = cal.hum
bac = cal.bac()
fun = cal.fun()
vir = cal.vir()
par = cal.par()
print("人源细胞含量：", '%.2E' % hum)
print("细菌理论灵敏度：", bac)
print("真菌理论灵敏度：", fun)
print("病毒理论灵敏度：", vir)
print("寄生虫理论灵敏度：", par)
input("Press <enter>")