# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    folder = "./subject6/"
    for count, filename in enumerate(os.listdir(folder)): 
        dst ="sub6_" + filename
        src = filename 
        
        print(src, dst)
          
        # rename() function will 
        # rename all the files 
        os.rename(folder + src, folder+dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 