from rest_framework import generics
from .serializers import PartnerSerializer
from .models import Partner
from urllib.request import urlopen
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.gis.geos import GEOSGeometry
import json

# Database Views
class PartnersView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnersDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnersClosestView(generics.ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        distanceLimit = 0
        point = GEOSGeometry('POINT(%s %s)' % (self.kwargs['lat'], self.kwargs['lon']), srid=4326)

        outputClosest = ""
        for x in Partner.objects.all():
            if(outputClosest == "" and x):
                outputClosest = x
            if(GEOSGeometry(x.coverageArea).distance(point) < GEOSGeometry(outputClosest.coverageArea).distance(point) and x):
                outputClosest = x
        return Partner.objects.all().filter(document=outputClosest.document)

# Git Json Views Test
class gitJsonView(APIView):
    def get(self, request, num=0):
        data = urlopen("https://raw.githubusercontent.com/ZXVentures/code-challenge/master/files/pdvs.json").read()
        output = json.loads(data)
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        output_dict = [x for x in output['pdvs'] if x['id'] == str(num)]
        output_json = json.dumps(output_dict)
        return Response(output['pdvs'])

class gitJsonDetailsView(APIView):
    def get(self, request, num=0):
        data = urlopen("https://raw.githubusercontent.com/ZXVentures/code-challenge/master/files/pdvs.json").read()
        output = json.loads(data)
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        output_dict = [x for x in output['pdvs'] if x['id'] == str(num)]
        output_json = json.dumps(output_dict)
        return Response(output_dict)

class gitJsonClosest(APIView):
    def get(self, request, lat="", lon=""):
        data = urlopen("https://raw.githubusercontent.com/ZXVentures/code-challenge/master/files/pdvs.json").read()
        output = json.loads(data)
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        output_dict = output['pdvs']
        point = GEOSGeometry('POINT(%s %s)' % (lat, lon))
        outputClosest = ""
        for x in output['pdvs']:
            if(outputClosest == ""):
                outputClosest = x
            if(GEOSGeometry(str(x['coverageArea'])).distance(point) < GEOSGeometry(str(outputClosest['coverageArea'])).distance(point)):
                outputClosest = x
        return Response(outputClosest)