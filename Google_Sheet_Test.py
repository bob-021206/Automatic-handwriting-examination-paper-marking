import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
import io

# 配置Google Drive API凭据
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = None
token_filename = 'token.json'

if os.path.exists(token_filename):
    creds = creds.from_authorized_user_file(token_filename, SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(r'C:\Users\sunbinyan\Desktop\SRS\Software\credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open(token_filename, 'w') as token:
        token.write(creds.to_json())

# 创建 Google Drive API 客户端
drive_service = build('drive', 'v3', credentials=creds)

def download_xlsx_file(file_id, output_folder):
    request = drive_service.files().get_media(fileId=file_id)
    file_name = drive_service.files().get(fileId=file_id).execute()['name']
    output_path = os.path.join(output_folder, file_name)
    
    with io.FileIO(output_path, 'wb') as output_file:
        downloader = MediaIoBaseDownload(output_file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f'Download {int(status.progress() * 100)}%')

    print(f'File downloaded and saved to {output_path}')

if __name__ == '__main__':
    file_id = '1eEeC8WxYoXmDTpphtIjBMoqxEHKy5MZWy6PPpEk3W5g'  # 替换为要下载的文件的ID
    output_folder = r'C:\Users\sunbinyan\Desktop\SRS\Software'   # 本地文件夹的路径，确保文件夹已创建

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    download_xlsx_file(file_id, output_folder) 