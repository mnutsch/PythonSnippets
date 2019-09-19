import os
for filename in os.listdir("c:/test"): # filename is a string
	if filename.endswith(".test"): # notice the indent
		with open(filename,'r') as f:
			with open('tempFile.txt','w') as f2:
				f2.write("/* Copyright (C) Company Name, Inc. - All Rights Reserved\n* Unauthorized copying of this file, via any medium is strictly prohibited\n* Proprietary and confidential\n*/\n\n")
				f2.write(f.read())
				f2.close()
				f.close()
				os.remove(filename)
				os.rename('tempFile.txt',filename)
