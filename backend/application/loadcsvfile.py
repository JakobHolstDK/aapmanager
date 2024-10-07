# load csv file to database
#
import time
import csv
from sys import argv
import requests
import json
from pathlib import Path  
import os


# filename is in argument one
filename = argv[1]

# open the file
with open(filename, newline='') as csvfile:
  # read the file
  reader = csv.reader(csvfile)
# for each row in the file
#Identifier = models.CharField(max_length=255)
#    Name = models.CharField(max_length=255)
#    Application_Lifecycle_Stage = models.CharField(max_length=255)
#    SLA_Applications = models.CharField(max_length=255)
#    Crown_Jewel = models.CharField(max_length=255)
#    Application_is_owned_by_IT_Vertical = models.CharField(max_length=255)
#    Application_has_Service_Owner_Name = models.CharField(max_length=255)
#    Application_has_Service_Owner_E_Mail = models.CharField(max_length=255)
#    Planned_Retiring_Date = models.CharField(max_length=255)
#    Actual_Retiring_Date = models.CharField(max_length=255)
#    TIME_Evaluation = models.CharField(max_length=255)
#    Justification_for_Tolerate_TIME = models.CharField(max_length=255)
#    Application_Subtype = models.CharField(max_length=255)
#    Application_has_IT_Service_ApnlId = models.CharField(max_length=255)
#    Application_has_IT_Service_IT_Service_Name = models.CharField(max_length=255)
#    Description = models.TextField()
#    Application_has_primary_Capability = models.CharField(max_length=255)
#    Application_has_primary_Capability_IT_Owner = models.CharField(max_length=255)
#    Application_has_primary_Capability_Business_Owner = models.CharField(max_length=255)
#    Application_has_secondary_Capability = models.CharField(max_length=255)
#    Deployment = models.CharField(max_length=255)
#    Developed_Purchased = models.CharField(max_length=255)
#    Application_has_Business_Releationship_Manager_Name = models.CharField(max_length=255)
#    Application_has_Business_Releationship_Manager_E_Mail = models.CharField(max_length=255)
#    Application_has_Business_Owner_Name = models.CharField(max_length=255)
#    Application_has_Business_Owner_E_Mail = models.CharField(max_length=255)
#    Application_has_Technical_Subject_Matter_Expert_Name = models.CharField(max_length=255)
#    Application_has_Technical_Subject_Matter_Expert_E_Mail = models.CharField(max_length=255)
#    Application_has_Product_Owner_Name = models.CharField(max_length=255)
#    Application_has_Product_Owner_E_Mail = models.CharField(max_length=255)
#    Application_has_Release_Manager_Name = models.CharField(max_length=255)
#    Application_has_Release_Manager_E_Mail = models.CharField(max_length=255)
#    Application_has_Application_Subject_Matter_Expert_Name = models.CharField(max_length=255)
#    Application_has_Application_Subject_Matter_Expert_E_Mail = models.CharField(max_length=255)
#    Application_has_Contract_ContractNumber = models.CharField(max_length=255)
#    Application_has_Company_Code_Code = models.CharField(max_length=255)
#    Application_has_Company_Code_Name = models.CharField(max_length=255)
#    Application_is_used_by_Division = models.CharField(max_length=255)
#    Application_is_used_by_Country_Iso = models.CharField(max_length=255)
#    Application_is_used_by_Country_Name = models.CharField(max_length=255)
#    Origin = models.CharField(max_length=255)
#    Recovery_Time_Objective = models.CharField(max_length=255)
#    Recovery_Point_Objective = models.CharField(max_length=255)
#    Application_requires_Application = models.CharField(max_length=255)
#    Application_is_required_by_Application = models.CharField(max_length=255)
#    Alias = models.CharField(max_length=255)
#    System_of_Record = models.CharField(max_length=255)
#    System_of_Record_Source_Date = models.CharField(max_length=255)
#    Top_Supporting_Top = models.CharField(max_length=255)
#    Application_is_supplied_by_Vendor = models.CharField(max_length=255)
#    BRM_Comment = models.CharField(max_length=255)
#    configitems = models.JSONField(blank=True,null=True)
  data = {}
  for row in reader:
      # print the row
      print(row)
      time.sleep(10)
      
      # if the row is not empty
      """
      if row:
          # pass if the row is the header
          if row[0] == "Identifier":
              continue
          
          # create a dictionary
          data = {
              "Identifier": 
            }
          headers = {
              'Content-Type': 'application/json',
          } 
          # send the data to the server
          response = requests.post('http://aapmanager.dsv.com:9990/application/api/applications/', headers=headers, data=json.dumps(data), verify=False)

          if response.status_code == 201:
              print("Data sent successfully")
          else:
              print("Error sending data")
              print(response.text)
              print(response.status_code)
          print(response.text)
          print(response.status_code)
          time.sleep(10)



"""