# pip install bing-image-downloader

from bing_image_downloader import downloader
name=input("Enter Name of Image= ")
n_o_i=int(input("Enter number of image You Want to download= "))
downloader.download(name,limit=n_o_i,output_dir="images",adult_filter_off=True)

print("Download successfully")