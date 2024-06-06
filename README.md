# AxCorSRMRI
Self-Supervised Realistic Through-Plane MRI Super Resolution from Clinical 2D Axial and Coronal Acquisition.


## Instruction 

**A full example can be seen in `sample.ipynb`**.

- Organize your data: Start by making sure your Axial and Coronal files for each case share the same case ID at the beginning of their filenames. For instance, both Axial and Coronal files for a case numbered "001" should begin with "001". For example: 001_ax.nii.gz and 001_cor.nii.gz.
- Preprocess the data: For the model, the coronal data must be resampled isotropically.  

```
from axcorsrmri import resample_cases

path_to_data_files = r"./data/"
resample_cases(path_dir = path_to_data_files)
```

- Create database: Creates a CSV file that acts as a database. This will include the file paths for the coronal, axial, and isotropic files.

```
from axcorsrmri import create_database

path_to_data_files = r"./data/"
create_database(
    path_to_data_files,
    train_frac=0.8,
    test_frac=0.1,
    num_folds=1
)
```

- Set the main framework and model hyperparameters. For a detailed explanation of each parameter, check the `parameter_dictionary.txt` file. The default training parameters are already established in setup_parser().        
```
from axcorsrmri import parser_setup

override_args = {
    "path_to_set": r"./data/",
    "path_to_results": r"./results/",
    ...
}

args = parser_setup(override_args)

```
- Prepare your data for training: To get your data ready for training your model, you will need to create three datasets:
  - Training Set: This is the largest part of your data and is used to teach your model.
  - Validation Set: This set helps you fine-tune your model's performance during training without overfitting.
  - Test Set: After training, you'll use this set to check how well your model performs on new, unseen data.

```
from axcorsrmri import initialize_data
dl_train, dl_valid_lr, dl_valid_hr, dl_test_lr, dl_test_hr, result_dir, writer, config = initialize_data(args)
```

- Train, valid and test the model.

```
from axcorsrmri import training_validation_test
training_validation_test(dl_train , dl_valid_lr,dl_valid_hr,dl_test_lr,dl_test_hr,result_dir,writer,config)
```

- If you have a trained model and want to use it on all the files in a folder, making sure they're isotropically resampled 

```
from axcorsrmri import test_parser_setup, reconstruct_SR_volumes_in_folder

override_args_test = {
    "path_to_set": r"./data/",
    "path_to_results": r"./results/",
    ...
}

test_args = test_parser_setup(override_args_test)
reconstruct_SR_volumes_in_folder(test_args)
```
_______________________________________________________________________

## License
For this work, we used code from the following works -

[1] Transformer for Single Image Super-Resolution
Zhisheng Lu, Juncheng Li, Hong Liu, Chaoyan Huang, Linlin Zhang, Tieyong Zeng

[2] Direct Unsupervised Super-Resolution Using Generative Adversarial Network
(DUS-GAN) for Real-World Data Kalpesh Prajapati , Vishal Chudasama

[3]  InceptionV3 implementation is taken from 
https://github.com/mseitzer/pytorch-fid

[4] FID and KID calculation are made by PIQ package - PyTorch Image Quality: Metrics for Image Quality Assessment by Kastryulin, Sergey and Zakirov, Jamil and Prokopenko, Denis and Dylov, Dmitry V. 
