Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
$VMName = "PROJET"
$VMPath = "C:\HyperV\VMs\$VMName"
$ISOPath = "C:\Users\Lagia\Downloads\lubuntu-25.10-desktop-amd64.iso" 

New-Item -Path $VMPath -ItemType Directory -Force

New-VM -Name $VMName -MemoryStartupBytes 1GB -Generation 2 -Path $VMPath -SwitchName "Default Switch"
Set-VMProcessor -VMName $VMName -Count 2
New-VHD -Path "$VMPath\$VMName.vhdx" -SizeBytes 20GB -Dynamic
Add-VMHardDiskDrive -VMName $VMName -Path "$VMPath\$VMName.vhdx"

Add-VMDvdDrive -VMName $VMName -Path $ISOPath

Set-VMFirmware -VMName $VMName -EnableSecureBoot On -SecureBootTemplate MicrosoftUEFICertificateAuthority
Set-VMSecurity -VMName $VMName -VirtualizationBasedSecurity $true

Start-VM -Name $VMName

Write-Host "VM $VMName démarrée.lance deploy.ps1"