import gdown
from zipfile import ZipFile

# download rl_oa model
dataset_url = 'https://drive.google.com/uc?id=' + "1rKZs1whD04Mx5Guy8jHr2ikPSDHuHUcz"
dataset_name = "experiment.zip"
gdown.download(dataset_url, output = dataset_name, quiet=False)
zip_file = ZipFile(dataset_name)
zip_file.extractall() # depends on how to zip it
zip_file.close()