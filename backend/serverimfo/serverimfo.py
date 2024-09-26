# this python script is the main script for the serverinfo collector.
# it runs kinit to authenticate to the kerberos server, then runs klist to get the ticket information.
# the kinit credentials are stored in hashicorp vault.
#!/usr/bin/python3

import json
import subprocess

def load_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            username = data.get('username')
            password = data.get('password')
            return username, password
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {file_path}. Ensure it is valid JSON.")
    return None, None

def run_kinit(username, password):
    if not username or not password:
        print("Error: Username or password is missing.")
        return

    # Start the kinit process
    process = subprocess.Popen(['kinit', username],
                               stdin=subprocess.PIPE,  # We need to send the password to stdin
                               stdout=subprocess.PIPE,  # Capture the output (optional)
                               stderr=subprocess.PIPE,  # Capture any error messages
                               universal_newlines=True)  # Ensure we are working with text, not bytes

    # Send the password to stdin and close stdin to signal end of input
    stdout, stderr = process.communicate(input=password + '\n')

    # Check if kinit succeeded by examining the return code
    if process.returncode == 0:
        output = f"kinit succeeded for user {username}"
        return output
    else:
        output = f"kinit failed: {stderr}"
        return output

def run_module():
    file_path = '/etc/cmdb.json'
    username, password = load_credentials(file_path)
    kinitstat = run_kinit(username, password)
    script_path = '/usr/local/bin/serverinfo.ps1'
    save_powershell_script(script_path)
    output = subprocess.check_output(['pwsh', '-File', script_path], text=True)
    print(output)

if __name__ == '__main__':
    run_module()


### embed the powershell script in the python script
# this python script is the main script for the serverinfo collector.
# it runs kinit to authenticate to the kerberos server, then runs klist to get the ticket information.
# the kinit credentials are stored in hashicorp vault.
def save_powershell_script(file_path):
  powershellscript = '''
#!/usr/bin/pwsh
function Invoke-SQL {
    param(
        [string] $dataSource = "i06711",
        [string] $database = "ServerInfoReports",
        [string] $sqlCommand = "
        USE ServerInfoReports
        Exec DSV_SCSM2Unix_All
        "
    )

    $connectionString = "Data Source=$dataSource; " +
    "Integrated Security=SSPI; " +
    "Initial Catalog=$database"

    $connection = new-object system.data.SqlClient.SQLConnection($connectionString)
    $command = new-object system.data.sqlclient.sqlcommand($sqlCommand, $connection)
    $connection.Open()

    $adapter = New-Object System.Data.sqlclient.sqlDataAdapter $command
    $dataset = New-Object System.Data.DataSet
    $adapter.Fill($dataSet) | Out-Null

    $connection.Close()
    $dataSet.Tables
}

$result = Invoke-SQL

$arrayList = New-Object System.Collections.ArrayList
Foreach($row in $result.DataSet.Tables[0]) {
    $arrayList.Add(($row | Select-Object 'Host Name','Computer Name',Environment,DataCenterLocation,'VMWare Datacenter',Function,'Technical Contacts',Country,'Support Hours',Guard,'Application ID','Application Name',A-Number,DeployDate,'Asset Status')) > $null;
}

$Json =  ConvertTo-Json $arrayList
$Json
'''
  with open(file_path, 'w') as file:
    file.write(file_path)


