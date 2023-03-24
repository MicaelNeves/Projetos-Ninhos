
class Funcionario:
    def __init__(self,nome, cpf,salario):
        self.nome = nome
        self._cpf = cpf
        self.salario = salario
    def getCPF(self):
        return self._cpf
    
    def set(self, cpf):
        
        if len(cpf) != 11:
            print("CPF invalido")
        else:
            print("Válido")
            self._cpf = cpf
            return self._cpf
        
if __name__ == '__main__':
    novo1 = Funcionario("Micael","12345667",1200)
    novo1.set("12345678910")
    print(novo1.__dict__)
    print(novo1.getCPF())
