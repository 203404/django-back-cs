from rest_framework import routers, serializers, viewsets

from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ( 'nombre', 'edad')