#Barcode Manager

Generates non-traditional custom barcodes using product details containing Name, Price, and Production Date.

##Features

 Uses the 'hashlib' module for generating fixed-length hexadecimal characters, which are converted into binary, where the 0's and 1's are mapped into │(U+2502) and ▌(U+258C).
 The 'hashlib' module has been used for encoding passwords as well.
 Includes features such as Creation, Searching, Updating, and Deletion.
 Enables Multiple Access levels for security purposes.

##Technical Highlights

 Implemented various logical input validations, such as Date validation and Price validation, to enable a wide range of input acceptance, ensuring user flexibility.

##Note

 Does not follow the Traditional Barcode System(requires a Custom Scanner).

##Running the program:

 Run the program using Python 3.6 or higher versions
 You will be prompted for access level:
  For admin access: Use the password 'adMin@123'
  For employee access: Use the password 'Hello World'
