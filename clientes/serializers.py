from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não coloque números nesse campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir o formato: 11 91234-1234, (respeitando o espaço e traço)"})
        return data
        
   
    