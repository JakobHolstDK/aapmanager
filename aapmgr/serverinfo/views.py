# api/views.py
import pprint
import json
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Asset, Server
from .serializers import AssetSerializer, ServerSerializer
from django.shortcuts import render
from django.views.generic import ListView

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
    
   



class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AssetSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'AssetList.html', {'assets': assets})

def server_list(request):
    servers = Server.objects.all()
    return render(request, 'ServerList.html', {'servers': servers})

def server_info(request, pk):
    server = Server.objects.get(pk=pk)
    return render(request, 'ServerInfo.html', {'server': server})





@api_view(['POST'])
def upload_json(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['file']
    
    try:
        # Load the JSON data from the uploaded file
        data = json.load(file)
        
        # List to hold successfully saved assets
        saved_assets = []
        # List to hold errors for items that were ignored
        ignored_items = []

        # Validate and save each asset in the JSON data
        for item in data:
            # Check for required fields (customize this based on your requirements)
            if not item.get("Host Name"):
                ignored_items.append(item)
                continue  # Skip this item if required fields are missing
            try:
              item['host_name'] = item.pop('Host Name')
            except KeyError:
              item['host_name'] = None
            try:
              item['computer_name'] = item.pop('Computer Name')
            except KeyError:
              item['computer_name'] = None
            try:  
              item['environment'] = item.pop('Environment')
            except KeyError:
              item['environment'] = None
            try:
               item['data_center_location'] = item.pop('Data Center Location')
            except KeyError:
              item['data_center_location'] = None
            try:
              item['vmware_datacenter'] = item.pop('VMware Datacenter')
            except KeyError:
              item['vmware_datacenter'] = None
            try:  
              item['function'] = item.pop('Function')
            except KeyError:
              item['function'] = None
            try:  
              item['technical_contacts'] = item.pop('Technical Contacts')
            except KeyError:
              item['technical_contacts'] = None
            try:   
              item['country'] = item.pop('Country')
            except KeyError:
              item['country'] = None
            try:  
              item['support_hours'] = item.pop('Support Hours') 
            except KeyError:
              item['support_hours'] = None
            try:  
              item['guard'] = item.pop('Guard')
            except KeyError:
              item['guard'] = None
            try:
              item['application_id'] = item.pop('Application ID')
            except KeyError:
              item['application_id'] = None
            try:  
              item['application_name'] = item.pop('Application Name')
            except KeyError:
              item['application_name'] = None
            try:  
              item['a_number'] = item.pop('A Number')
            except KeyError:
              item['a_number'] = None
            try:  
              item['deploy_date'] = item.pop('Deploy Date')
            except KeyError:
              item['deploy_date'] = None
            try:  
              item['asset_status'] = item.pop('Asset Status')
            except KeyError:
              item['asset_status'] = None

            


            
            serializer = AssetSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                saved_assets.append(serializer.data)
            else:
                ignored_items.append(item)  # Add invalid items to ignored list

        response_data = {
            'saved_assets': saved_assets,
            'ignored_items': ignored_items,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# serverinfo/urls.py

