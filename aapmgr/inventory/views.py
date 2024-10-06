from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.views.generic import ListView
from rest_framework.decorators import api_view
from .models import server, zone, region, appid, environment, serverrole
from .serializers import ServerSerializer, ZoneSerializer, RegionSerializer, AppidSerializer, EnvironmentSerializer, ServerroleSerializer
from .models import organization, project
from .serializers import OrganizationSerializer, ProjectSerializer
from rest_framework import status


import time
import subprocess
import tempfile
import os
import json

class ServerViewSet(viewsets.ModelViewSet):
    queryset = server.objects.all()
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
    queryset = server.objects.all()
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
    
class ZoneViewSet(viewsets.ModelViewSet):
    queryset = zone.objects.all()
    serializer_class = ZoneSerializer

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
        serializer = ZoneSerializer(queryset, many=True)
        return Response(serializer.data)
    
class RegionViewSet(viewsets.ModelViewSet):
    queryset = region.objects.all()
    serializer_class = RegionSerializer

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
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)
    
class AppidViewSet(viewsets.ModelViewSet):
    queryset = appid.objects.all()
    serializer_class = AppidSerializer

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
        serializer = AppidSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ServerroleViewSet(viewsets.ModelViewSet):
    queryset = serverrole.objects.all()
    serializer_class = ServerroleSerializer

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
        serializer = ServerroleSerializer(queryset, many=True)
        return Response(serializer.data)
    

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer

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
        serializer = OrganizationSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer

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
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    
        
class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = environment.objects.all()
    serializer_class = EnvironmentSerializer

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
        serializer = EnvironmentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    


class inventory(ListView):
    model = server
    template_name = 'inventory/inventory.html'
    context_object_name = 'lines'
    ordering = ['name']
    def get_queryset(self):
        appids = appid.objects.all()
        environments = environment.objects.all()
        regions = region.objects.all()
        zones = zone.objects.all()
        serverroles = serverrole.objects.all()
        servers = server.objects.all()

        payload = {}
        for myappid in appids:
            payload[myappid.appid] = {}
            for myenvironment in environments:
                payload[myappid.appid][myenvironment.name] = {}
                for myregion in regions:
                    payload[myappid.appid][myenvironment.name][myregion.name] = {}
                    for myzone in zones:
                        payload[myappid.appid][myenvironment.name][myregion.name][myzone.name] = {}
                        for myserverrole in serverroles:
                            payload[myappid.appid][myenvironment.name][myregion.name][myzone.name][myserverrole.name] = []
                            for myserver in server.objects.filter(appid=myappid, environment=myenvironment):
                                payload[myappid.appid][myenvironment.name][myregion.name][myzone.name][myserverrole.name].append(myserver.name)
        fulltekst = []
        parsedinv = ""
        # create temporary directory
        tempdir = tempfile.TemporaryDirectory()
        # clone git repository to temporary directory
        subprocess.run(["git", "clone", "https://github.com/JakobHolstDK/common.inventory.git"], cwd=tempdir.name)
        # read the inventory file

        for key in payload:
            tekst = []
            if appid.objects.get(appid=key).aapstatus =='Active':
                myline = f"[{key}]"
                tekst.append(myline)
                myline = f"[{key}:children]"
                children = {}
                for myenvironment in environments:
                    for myregion in regions:
                        for myzone in zones:
                            myline = f"{key}_{myenvironment.name}_{myregion.name}_{myzone.name}"
                            #check if the server exists
                            for myserver in servers:
                                if myserver.appid.appid == key and myserver.environment.name == myenvironment.name and myserver.region.name == myregion.name and myserver.zone.name == myzone.name:
                                    children[myline] = True
                myline = f"[{key}:children]"
                tekst.append(myline)
                for mykey in children:
                    tekst.append(mykey)
                myline = f"[{key}:vars]"
                tekst.append(myline)
                tekst.append('appname="' +appid.objects.get(appid=key).appname + '"')
                tekst.append('appowner="' + appid.objects.get(appid=key).appowner + '"')
                tekst.append('appcontact="' +appid.objects.get(appid=key).appcontact + '"')
                myapconfig = appid.objects.get(appid=key).configitems
                if myapconfig is not None:
                    for mykey in myapconfig:
                        myline = f"{mykey}={myapconfig[mykey]}"
                        tekst.append(myline)
                for myenvironment in environments:  
                    myline = f"[{key}_{myenvironment.name}]"
                    tekst.append(myline)
                    children = {}
                    for myregion in regions:
                        for myzone in zones:
                            myline = f"{key}_{myenvironment.name}_{myregion.name}_{myzone.name}"
                            #check if the server exists
                            for myserver in servers:
                                if myserver.appid.appid == key and myserver.environment.name == myenvironment.name and myserver.region.name == myregion.name and myserver.zone.name == myzone.name:
                                    children[myline] = True
                    if len(children) > 0:
                        myline = f"[{key}_{myenvironment.name}:children]"
                        tekst.append(myline)
                        for mykey in children:
                            tekst.append(mykey)
                        myline = f"[{key}_{myenvironment.name}:vars]"
                        tekst.append(myline)
                        if myenvironment.configitems is not None:
                            for mykey in myenvironment.configitems:
                                myline = f"{mykey}={myenvironment.configitems[mykey]}"
                                tekst.append(myline)
                    for myregion in regions:
                        myline = f"[{key}_{myenvironment.name}_{myregion.name}]"
                        tekst.append(myline)
                        children = {}
                        for myzone in zones:
                            myline = f"{key}_{myenvironment.name}_{myregion.name}_{myzone.name}"
                            #check if the server exists
                            for myserver in servers:
                                if myserver.appid.appid == key and myserver.environment.name == myenvironment.name and myserver.region.name == myregion.name and myserver.zone.name == myzone.name:
                                    children[myline] = True
                        if len(children) > 0:
                            myline = f"[{key}_{myenvironment.name}_{myregion.name}:children]"
                            tekst.append(myline)
                            for mykey in children:
                                tekst.append(mykey)

                            myline = f"[{key}_{myenvironment.name}_{myregion.name}:vars]"
                            tekst.append(myline)
                            tekst.append('region="' + myregion.name + '"')
                        if myregion.configitems is not None:
                            for mykey in myregion.configitems:
                                myline = f"{mykey}={myregion.configitems[mykey]}"
                                tekst.append(myline)
                        for myzone in zones:
                            myserverlist = {}
                            for myserver in servers:
                                if myserver.appid.appid == key and myserver.environment.name == myenvironment.name and myserver.region.name == myregion.name and myserver.zone.name == myzone.name:
                                    myline = f"{myserver.name}"
                                    myserverlist[myline] = True
                            if len(myserverlist) > 0:
                                myline = f"[{key}_{myenvironment.name}_{myregion.name}_{myzone.name}]"
                                tekst.append(myline)
                                for mykey in myserverlist:
                                    tekst.append(mykey)
                                myline = f"[{key}_{myenvironment.name}_{myregion.name}_{myzone.name}:vars]"
                                tekst.append(myline)
                                tekst.append('zone="' + myzone.name + '"')
                            if myzone.configitems is not None:
                                for mykey in myzone.configitems:
                                    myline = f"{mykey}={myzone.configitems[mykey]}"
                                    tekst.append(myline)



                            for myserverrole in serverroles:
                                myserverlist = {}
                                for myserver in servers:
                                    if myserver.appid.appid == key and myserver.environment.name == myenvironment.name and myserver.region.name == myregion.name and myserver.zone.name == myzone.name:
                                        for myrole in myserver.serverrole.all():
                                            if myrole.name == myserverrole.name:
                                                myline = f"{myserver.name}"
                                                myserverlist[myline] = True
                                myline = f"[{key}_{myenvironment.name}_{myregion.name}_{myzone.name}_{myserverrole.name}]".replace(" ", "_")
                                tekst.append(myline)
                                if len(myserverlist) > 0:
                                    myline = f"[{key}_{myenvironment.name}_{myregion.name}_{myzone.name}_{myserverrole.name}]".replace(" ", "_")
                                    tekst.append(myline)
                                    for mykey in myserverlist:
                                        tekst.append(mykey)
                                    myline = f"[{key}_{myenvironment.name}_{myregion.name}_{myzone.name}_{myserverrole.name}:vars]".replace(" ", "_")
                                    tekst.append(myline)
                                    if myserverrole.configitems is not None:
                                        for mykey in myserverrole.configitems:
                                            myline = f"{mykey}={myserverrole.configitems[mykey]}"
                                            tekst.append(myline)

                            f = open(os.path.join(tempdir.name + "/common.inventory", key), "w")
                for myline in tekst:
                    f.write(myline + "\n")
                f.close()
                subprocess.run(["git", "add", os.path.join(tempdir.name + "/common.inventory", key)], cwd=tempdir.name +"/common.inventory")
                #gitdif = subprocess.run(["git", "diff", "--minimal"], cwd=tempdir.name +"/common.inventory", stdout=subprocess.PIPE)
                #itdiff = gitdif.stdout.decode('utf-8')
                

                subprocess.run(["git", "commit", "-m", "updated inventory"], cwd=tempdir.name +"/common.inventory")
                subprocess.run(["git", "push"], cwd=tempdir.name +"/common.inventory")
                ansinv = subprocess.run(["ansible-inventory", "--list", "-i", os.path.join(tempdir.name + "/common.inventory", key)], cwd=tempdir.name +"/common.inventory", stdout=subprocess.PIPE)
                print( json.loads(ansinv.stdout))
                humandate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if ansinv.returncode == 0:
                    fulltekst.append("<li>" + humandate + " : Inventory for <B>" + key + "</B> successfully updated in git repository</li>\n")
                else:
                    fulltekst.append("<li>" + humandate + " : Inventory for <B>" + key + "</B> failed to update in git repository </li>\n")

                # we need to save the tekst in a file
        tempdir.cleanup()

        return fulltekst

#appid_6661:children]
#appid_6661_production_afri_cdc
#appid_6661_production_amer_cdc
#appid_6661_production_apac_cdc
#appid_6661_production_emea_cdc
#appid_6661_test_emea_cdc




