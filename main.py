from pathlib import Path 

import rasterio

import hashlib

import json

from datetime import datetime

  #part:1 reading the path 
folder_path = Path(r"C:\Users\Tamiz\OneDrive\Desktop\GEOSPATIAL TECHNOLOGY\track_2 assignments\Pandas_datas")

project_folder = folder_path/"Geo_pandas_datas"

#part:2 


checksum_store={}# storing hashvalues for each file with name
    
if project_folder.exists():# checking folder exists or not
  
     
    for check in project_folder.rglob("*"): # getting every files form folders and sub_folders
        
        if check.is_file():
           
            with check.open("rb")as binary_fromat: # reading the file in binary format
                 
                data = binary_fromat.read()
                       
                checksum = hashlib.sha256 (data).hexdigest() # hasing the bianry file
                       
                checksum_store[check.name] = checksum #adding each hashvalues with name of the file
    
  
  # CHECKING THE RASTERDATA
      
    try:
       raster_metadata = {}         
       for raster_check in project_folder.rglob("./TIFF"):
        
         if raster_check.exists() :
           
          
           with rasterio.open(raster_check)as raster_file :
           
           
               dataset=raster_file.read()       
               
               metadata = {"check.name":check.name,
                 
                  "crs": str(dataset.crs),
                  
                  "width": dataset.width,
                  
                  "height": dataset.height,
                  
                  "band_count": dataset.count,
                  
                  "data_type": dataset.dtypes,
                  
                  "bounds": tuple(dataset.bounds),
                  
                  "transform": tuple(dataset.transform),
              } 
               
                     
               raster_metadata[dataset.name]=metadata
         else:
           raise FileNotFoundError("No raster files found")
       
       
    except Exception as error :  
         
          print("problem in tiff")    
                           
   
                           
else:
    print("file not exists")    
  
    
#writing the hash values in json

baseline_path=Path(r"C:\Users\Tamiz\OneDrive\Spatial_checksum\spatial_store")
                       
baseline_folder=baseline_path/"baseline.json"
                       
final_output={ "scan_time": datetime.now().isoformat(timespec="seconds"),
              "checksum":checksum_store,
              
              "metadata":raster_metadata }  
                 
with baseline_folder.open("w",encoding="utf-8")as write_file: # opening the file for writing the hashvalues with name
                           
    json.dump(final_output,write_file,indent=4)# writing the values in our output value
    

    






