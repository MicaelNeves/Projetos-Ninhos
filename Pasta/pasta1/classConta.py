class Conta:
    def __init__ (self, saldo, conta):
        self._saldo = saldo
        self._conta = conta

    def getConta(self):
      return self._conta
    
    def getSaldo(self):
       return self._saldo
    
    def saquesaldo(self ,valor):
        self._saldo += valor
        if self._saldo <= 0:
           print("saldo invalido")
        else:
           return self._saldo
    
    def set(self,novosaldo):
        if novosaldo <= 0:
          print("saldo invalido")
        else:
          self._saldo = novosaldo
          return self._saldo
        
conta1 = Conta(1200,"53456")
conta1.saquesaldo(-1300)
print(conta1.getConta())
print(conta1.getSaldo())
print(conta1.set(56))