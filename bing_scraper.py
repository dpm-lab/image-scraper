import os

print("Bing Image Downloader")

from bing_image_downloader import downloader

query_string = input("Enter query string: ")
num_photos = input("Number of images: ")
downloader.download(query_string, limit=int(num_photos), output_dir='images/' + query_string, adult_filter_off=True, force_replace=False, timeout=60, verbose=False)

print("Done! Please check the images folder.")
exit()