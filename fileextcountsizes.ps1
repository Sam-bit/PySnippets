$directory = "E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\INSTA"
#Get all items
Get-ChildItem -Path $directory -Recurse |
#Get only files
Where-Object { !$_.PSIsContainer } |
#Group by extension
Group-Object Extension |
#Get data
Select-Object @{n="Extension";e={$_.Name -replace '^\.'}}, @{n="Size (MB)";e={[math]::Round((($_.Group | Measure-Object Length -Sum).Sum / 1MB), 2)}}, Count

