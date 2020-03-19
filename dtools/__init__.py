import os
import sys
import click
from fdfs_client.client import *
import cv2
import numpy as np

@click.group()
def filter_command():
	pass

@click.command()
@click.argument('path')
def upload(path):
	tracker_path = get_tracker_conf("/etc/fdfs/client.conf")
	client = Fdfs_client(tracker_path)
	img = cv2.imread(path)
	img_encode = cv2.imencode('.jpg', img)[1]
	data_encode = np.array(img_encode)
	str_encode = data_encode.tostring()
	subimg_key = client.upload_by_buffer(str_encode, 'jpg')
	img_id = subimg_key['Remote file_id'].decode()
	print(img_id)

@click.command()
@click.argument('key')
@click.argument('filename', type=click.Path(exists=True))
def download(key, filename):
	#print(filename)
	#print(key)
	tracker_path = get_tracker_conf('/etc/fdfs/client.conf')
	client = Fdfs_client(tracker_path)
	fn = key.split('/')[-1]
	#print(filename+fn)
	ret_read = client.download_to_file(str(filename+fn), key.encode())
	print(str(filename+fn))

filter_command.add_command(upload)
filter_command.add_command(download)
		
def choose():
	filter_command()

def upload_buffer(thumbnail):
	tracker_path = get_tracker_conf('/etc/fdfs/client.conf')
	client = Fdfs_client(tracker_path)
	img_encode = cv2.imencode('.jpg', thumbnail)[1]
	data_encode = np.array(img_encode)
	str_encode = data_encode.tostring()
	subimg_key = client.upload_by_buffer(str_encode)
	thumbnail_id = subimg_key['Remote file_id'].decode()
	return thumbnail_id

def read_buffer(imgId):
	tracker_path = get_tracker_conf('/etc/fdfs/client.conf')
	client = Fdfs_client(tracker_path)
	ret_read = client.download_to_buffer(imgId.encode())
	nparr = np.fromstring(ret_read['Content'], np.uint8)
	img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	return img_decode

if __name__ == "__main__":
	filter_command()
