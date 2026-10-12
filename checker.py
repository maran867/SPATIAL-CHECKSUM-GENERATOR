from pathlib import Path

import json





baseline_path=Path(r"C:\Users\Tamiz\OneDrive\Spatial_checksum\spatial_store")
                       
baseline_folder=baseline_path/"baseline.json"
                       
checking_folder=Path(r"C:\Users\Tamiz\OneDrive\Spatial_checksum\spatial_store")

checking=checking_folder/"checking.json"
                           
changes={"new":[],
         "unchanged":[],
         "changed":[],
         "missing":[]
         }

with checking.open("r",encoding="utf-8")as checking:  
    
    checking=json.load(checking)   

with baseline_folder.open("r", encoding="utf-8") as baseline:
    
    baseline = json.load(baseline)

    for file,values in baseline.items():
       
       if file not in checking:
           
           changes["missing"].append(file)
           
       elif  values != checking[file]:

           changes["changed"].append(file)
                           
       else :
            changes["unchanged"].append(file)                
                                                    
                     
                           
    for file_path,valuess in checking.items():
    
      if file_path not in baseline:
          
        changes["new"].append(file_path)
        
        
print(changes)



#FINAL REPORT
report_path=Path(r"C:\Users\Tamiz\OneDrive\Spatial_checksum\spatial_store")

report_file=report_path/"report.json"

report={"new_file":len(changes["new"]),
        "changed_file":len(changes["changed"]),
        "unchanged_file":len(changes["unchanged"]),
        "missing_file":len(changes["missing"]),
        "details": changes}

with report_file.open("w",encoding="utf-8")as report_file:
    
    report_write=json.dump(report,report_file,indent=4)
    
    print(report_write)