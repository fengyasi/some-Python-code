###
#import pydicom
#filename = r"E:\PengChen\000001.dcm"
#dcm = dicom.read_file(filename)
#print(dcm)
###
import pydicom
ds = pydicom.read_file('E:\PengChen\000001.dcm')
print(ds)
