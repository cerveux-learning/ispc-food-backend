from rest_framework import serializers
from .models import Carrito, DetallePedido

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['id', 'producto', 'cantidad', 'usuario']

class DetallePedidoSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(source='id_producto.nombre_producto', read_only=True)
    class Meta:
        model = DetallePedido
        fields = ["cantidad_productos", "precio_producto", "subtotal", "nombre_producto"]

class ModificarCantidadSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(min_value=1)        
