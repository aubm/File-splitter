import os

filename = input("Enter file name : ")

chunks_size = 512000 # 500 Ko

try:
	file_fullname = "files/{0}".format(filename)
	res = open(file_fullname, "rb")
	data = res.read()
	res.close()
	bytes = len(data)
	number_of_chunks = bytes/chunks_size

	output_dir = "chunks/{0}".format(filename)
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	chunk_names = []
	part_number = 1
	for i in range(0, bytes+1, chunks_size):
		chunk_name = "{0}.{1}.part".format(filename, part_number)
		chunk_names.append(chunk_name)
		res = open("{0}/{1}".format(output_dir, chunk_name), "wb")
		res.write(data[i: i + chunks_size])
		res.close()
		part_number += 1


except FileNotFoundError as e:
	print('File not found')