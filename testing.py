import gspread

from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    '/content/norse-voice-417000-0633d3d9fab6.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

sh = gc.open("tester")
worksheet = sh.get_worksheet(0)

worksheet1 = sh.get_worksheet(1)
k=worksheet1.acell('A1').value
worksheet1.update_acell('A1', str(int(k)+1))
print(worksheet.update_acell('A'+str(k), k))
