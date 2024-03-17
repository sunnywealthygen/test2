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
gc = gspread.authorize(credentials)

sh = gc.open("tester")
worksheet = sh.get_worksheet(0)
k=1
while True : 
  val = worksheet.acell('A'+str(k)).value
  if val=='' :
    worksheet.update_acell('A'+str(k), str(k))
    print(k)
    break
  k=k+1
