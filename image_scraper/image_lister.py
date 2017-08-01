
'''' This is a non-functional script for taking the full list of CDIAC files (fullData.csv) and writing the paths of all
image files to its own 'cdiac_images2017.txt' file. 

    @Author: Tyler J. Skluzacek (skluzacek@uchicago.edu)
    @LastEdited: 07/31/2017 

'''''


with open('fullData.csv', 'rb') as f:

    pic_files = [] #Place to hold the pic paths we find on our journey through CDIAC.

    print("Reading Lines... ")
    for line in f:

        #Get the path and force to lower-case.
        path = line.split(",")[0].lower()

        #Add image filetypes to this set that you'd like to extract.
        img_set = {'bmp', 'jpg', 'png', 'gif'}
        extension = path.split('.')[-1] #Just gets the file extension from the path.

        if extension in img_set: #NoneTypes automatically disqualified in this if-statement, so no concern here.
            pic_files.append(path)

        else:
            pass

# Write to the textfile.
with open('cdiac_images2017.txt', 'wb') as g:

    for pic_path in pic_files:
        g.writelines(pic_path + '\n')

g.close()