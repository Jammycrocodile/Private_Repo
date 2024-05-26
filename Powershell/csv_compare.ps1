#Author:      Chester Lütscher
#Scriptname:  csv_compare.ps1
#Date:        February 2023
#Description: Checks which Hosts are missing from the Inventory file in the Central Reference
#Info: Wichtig, die Spalte mit den Servern muss bei beiden CSVs "Name" lauten, damit diese miteinander verglichen werden können. 

$CUS_export = Import-Csv -Path '\\ss002207\TAALUCH9$\Desktop\Customers\EOS\Inventarliste\cmdb_ci_hardware.csv' -Delimiter ',' -Encoding UTF8 #| select name
$inventory_liste = Import-Csv -Path '\\ss002207\TAALUCH9$\Desktop\Customers\EOS\Inventarliste\inventar_liste.csv'  -Delimiter ';' -Encoding utf8 #| select name

$missing_central=Compare-Object -ReferenceObject $CUS_export -DifferenceObject $inventory_liste -Property {$_.name -replace '(\.\w).*'} -PassThru | Where-Object -FilterScript {$_.SideIndicator -eq "=>" -and $_.name -ne ""}


if ($missing_central.Count -ne 0) {
    write-host "These Hosts are not in the central reference but they are in the inventory list:" -ForegroundColor Red
    
    $missing_central | ft #| out-file -FilePath \\ss002207\TAALUCH9$\Desktop\Customers\EOS\Inventarliste\difference.txt

    }
    else {
    write-host "Nice, all hosts which are in the inventory list are in the central reference" -ForegroundColor Green
    } 

