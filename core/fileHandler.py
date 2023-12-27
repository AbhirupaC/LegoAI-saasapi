def read(file, max_retries = 3):
	counter = 0
	while counter < max_retries:
		print(counter)
		try:
			with open("./data/"+file, 'r') as _f:
				return _f.read()
		except FileNotFoundError as fe:
			print("File not found: ", file)
			break
		except Exception as e:
			counter = counter + 1
			print("failed to read file: ", file)
			raise(e)

