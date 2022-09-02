from os.path import join
from pandas import concat, read_csv
from glob import glob

# ------------------------------ Constants ----------------------------------- #
DIRECTORY        = "src/csv-files"
MERGE_DIRECTORY  = "merged"
MERGED_FILE_NAME = "merged"
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    files_in_bytes = join(DIRECTORY, "*.csv")
    files          = glob(files_in_bytes)
    merge          = concat(map(read_csv, files), ignore_index=True)

    merge.to_csv(
        f"{DIRECTORY}/{MERGE_DIRECTORY}/{MERGED_FILE_NAME}.csv",
        index    = False, 
        encoding = 'utf-8'
    )
