from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve ter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "O Nome deve ter apenas caracteres alfabéticos"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve possuir 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O número do celular deve ser válido, no seguinte modelo: 83 91234-1234"})
        return data

    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O RG deve conter 9 dígitos")
    #     return rg
                
    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve conter no mínimo 11 dígitos")
    #     return celular