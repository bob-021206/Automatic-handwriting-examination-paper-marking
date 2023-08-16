import requests
import os

url = 'https://app.nanonets.com/api/v2/OCR/Model/6a2bdf1d-9b80-441f-b91b-6db6ecfb8c32/LabelFile/' #To use the API of nanonets
#data = {'file': open(r'C:\Users\sunbinyan\Desktop\SRS\Software\Marked Paper\Handwrite_P1.jpg', 'rb')}
#response = requests.post(url, auth=requests.auth.HTTPBasicAuth('ca2f59f8-10f3-11ee-ac84-1a0e265d7a5b', ''), files=data)
#print(response.text)

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            #if f.endswith('.png'):
                fullname = os.path.join(root, f)
                yield fullname
    
def main():
    base = r'C:\Users\sunbinyan\Desktop\SRS\Software\Final_Test' #Your path for the paper folder
    for i in findAllFile(base):
        print(i)
        data = {'file': open(i, 'rb')}
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth('ca2f59f8-10f3-11ee-ac84-1a0e265d7a5b', ''), files=data)
        #print(response.text)
        

if __name__ == '__main__':
    
    main()