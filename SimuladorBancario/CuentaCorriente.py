__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class CuentaCorriente:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __saldo = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        # Aqui inicia mi codigo
        return self.__saldo
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite consignar un monto a la cuenta"
    def ConsignarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo+monto
    
    __method__ = "RetirarSaldo"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite retirar un monto a la cuenta"
    def RetirarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo-monto