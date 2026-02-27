#update with 2023 data
import sys
sys.path.append(r"C:\Users\cmg0530\Code Library\lodes-dataset-construction\main")
from download_and_unzip import *
from build_database import *
import os

#define paths
wkd = r"C:\Users\cmg0530\Code Library\lodes-dataset-construction\examples\update_2023"
# --- processing
#get all the potential files
fps = get_all_possible_files(save=True,
                             savepath=wkd,
                             savename="state_dict")

#trim down to just 2023
for x in fps['tx'].keys():
    if x in ['od','rac','wac']:
        fps['tx'][x] = [q for q in fps['tx'][x] if '2023' in q]

#this downloads everything in that state's lodes
state_fold = download_state_lodes_file(save_loc=wkd,
                          st='tx',
                          links_dict=fps)

#this unzips everything 
unzip_state_lodes_file(state_fold= state_fold)

# loads downloaded data into spatialite 
lodes = r"C:\Users\cmg0530\Projects\lodes_package\lodes_tx_slim.db"


#state_fold = r"C:\Users\cmg0003\Desktop\TX_Lodes_Download\tx"
load_lodes_into_db(folder_path =state_fold,
    spath = lodes, 
    base_only = True)
#load_geometries_into_db(spath=spath) #note - this is basically a custom function for texas geometries - will need work for other states