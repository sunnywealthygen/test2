import gspread

from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'norse-voice-417000-0633d3d9fab6.json',
    scopes=scopes
)
file1 = open('thepower.txt', 'r')
Lines = file1.readlines()
count=0
k=''
for line in Lines:
  k=line


gc = gspread.authorize(credentials)

sh = gc.open("tester")
worksheet = sh.get_worksheet(0)
worksheet.update_acell('A'+k, k)

with open('thepower.txt', 'w') as file_obj:
    file_obj.write(str(int(k)+1))
    print(str(int(k)+1))

print(k)
file1 = open('thepower.txt', 'r')
Lines = file1.readlines()
for line in Lines:
  print(k)
