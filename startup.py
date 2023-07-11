import os

# env
print("FreshTemplate | by @macl2189 | github: https://github.com/EdamAme-x/FreshTemplate/")
print("\n Linux/Mac: 0 | Window: 1 \n")
t = input("OS : ")
if t == 0:
  os.system("curl -fsSL https://deno.land/x/install/install.sh | sh")
else:
  os.system("irm https://deno.land/install.ps1 | iex")
  
os.system("deno upgrade")
app_name = input("AppName:")
os.system("$ deno run -A --no-check https://raw.githubusercontent.com/lucacasonato/fresh/main/init.ts " + app_name)
os.system("cd ./" + app_name)
os.system("deno task start")
