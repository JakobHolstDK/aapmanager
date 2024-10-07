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
      # if the row is not empty
      if row:
          # pass if the row is the header
          if row[0] == "Identifier":
              continue
          
          # create a dictionary
          data = {
              "Identifier": row[0],
              "Name": row[1],
              "Application_Lifecycle_Stage": row[2],
              "SLA_Applications": row[3],
              "Crown_Jewel": row[4],
              "Application_is_owned_by_IT_Vertical": row[5],
              "Application_has_Service_Owner_Name": row[6],
              "Application_has_Service_Owner_E_Mail": row[7],
              "Planned_Retiring_Date": row[8],
              "Actual_Retiring_Date": row[9],
              "TIME_Evaluation": row[10],
              "Justification_for_Tolerate_TIME": row[11],
              "Application_Subtype": row[12],
              "Application_has_IT_Service_ApnlId": row[13],
              "Application_has_IT_Service_IT_Service_Name": row[14],
              "Description": row[15],
              "Application_has_primary_Capability": row[16],
              "Application_has_primary_Capability_IT_Owner": row[17],
              "Application_has_primary_Capability_Business_Owner": row[18],
              "Application_has_secondary_Capability": row[19],
              "Deployment": row[20],
              "Developed_Purchased": row[21],
              "Application_has_Business_Releationship_Manager_Name": row[22],
              "Application_has_Business_Releationship_Manager_E_Mail": row[23],
              "Application_has_Business_Owner_Name": row[24],
              "Application_has_Business_Owner_E_Mail": row[25],
              "Application_has_Technical_Subject_Matter_Expert_Name": row[26],
              "Application_has_Technical_Subject_Matter_Expert_E_Mail": row[27],
              "Application_has_Product_Owner_Name": row[28],
              "Application_has_Product_Owner_E_Mail": row[29],
              "Application_has_Release_Manager_Name": row[30],
              "Application_has_Release_Manager_E_Mail": row[31],
              "Application_has_Application_Subject_Matter_Expert_Name": row[32],
              "Application_has_Application_Subject_Matter_Expert_E_Mail": row[33],
              "Application_has_Contract_ContractNumber": row[34],
              "Application_has_Company_Code_Code": row[35],
              "Application_has_Company_Code_Name": row[36],
              "Application_is_used_by_Division": row[37],
              "Application_is_used_by_Country_Iso": row[38],
              "Application_is_used_by_Country_Name": row[39],
              "Origin": row[40],
              "Recovery_Time_Objective": row[41],
              "Recovery_Point_Objective": row[42],
              "Application_requires_Application": row[43],
              "Application_is_required_by_Application": row[44],
              "Alias": row[45],
              "System_of_Record": row[46],
              "System_of_Record_Source_Date": row[47],
              "Top_Supporting_Top": row[48],
              "Application_is_supplied_by_Vendor": row[49],
              "BRM_Comment": row[50]

            }
          headers = {
              'Content-Type': 'application/json',
          } 
          # send the data to the server
          response = requests.post('http://aapmanager.dsv.com:9990/application/api/applications/', headers=headers, data=json.dumps(data), verify=False)

          if response.status_code == 201:
              pass
          else:
              print("Error sending data")
              print(response.text)
              print(response.status_code)
          time.sleep(0.1)


