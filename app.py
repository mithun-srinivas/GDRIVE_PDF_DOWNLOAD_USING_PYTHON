import gdown
url0='https://drive.google.com/file/d/1izvcQ8ib-AYMACfde9bdl51KMFllkMZC/view?usp=sharing'
url1=url0.split('d/')
url2=url1[1].split('/')
url=' https://drive.google.com/uc?id='+str(url2[0])
output='trail.pdf'
gdown.download(url,output,quiet=False)