# pip install bing-image-downloader

from bing_image_downloader import downloader
name=input("Which Image You  Want To Download Enter Name = ")
num_img=int(input("Enter how Many Image Download= "))
downloader.download(name,limit=num_img,output_dir='images', adult_filter_off=True)
print("downloaded succcessfully")
