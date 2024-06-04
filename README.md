# AxCorSRMRI
Self-Supervised Realistic Through-Plane MRI Super Resolution from Clinical 2D Axial and Coronal Acquisition.


## Instruction 

**A full example can be seen in `sample.ipynb`**.
- Organize Your Data: Start by making sure your Axial and Coronal files for each case 
share the same case ID at the beginning of their filenames. For instance, both Axial and 
Coronal files for a case numbered "001" should begin with "001". For example: 001_ax.nii.gz and 001_cor.nii.gz.
- Preprocess the data: For model input resample the coronal data isotropically.  
```
path_to_data_files = "/path/to/data/"
coronal_files_prefix = None # not mandatory
ResampleCases(path_dir = path_to_data_files ,prefix = coronal_files_prefix)
```
- Create a Database: Make a CSV file that acts as a database. Include the file paths for the coronal, axial, and isotropic files.
```
path_to_data_files = "/path/to/data/"
CreateDateBase(path_to_data_files,cor_prefix=None,ax_prefix=None,train_frac=0.8,test_frac=0.1,num_folds = 1)
```
- Set the main framework and  model hyperparameters . For detailed explanations of each parameter, 
check the parameter_dictionary.txt file. The default training parameters are already established in setup_parser().        
```
override_args = {
    "path_to_set":"/tcmldrive/shared/RambamMRE082022/new2/",
    "path_to_results":"/argusdata/users/jenny075/JennySh/results/",
    "batch_size":12,
    "gpu_device":"0,1",
    }
parser = setup_parser()
args, _ = parser.parse_known_args([])
vars(args).update(override_args)
```
- Prepare Your Data for Training: To get your data ready for training your model, you'll need to create three sets:
  - Training Set: This is the largest part of your data and is used to teach your model.
  - Validation Set: This set helps you fine-tune your model's performance during training without overfitting.
  - Test Set: After training, you'll use this set to check how well your model performs on new, unseen data.

```
dl_train , dl_valid_lr,dl_valid_hr,dl_test_lr,dl_test_hr,result_dir,writer,config  = Data_Inittializaion(args)
```
- Train, valid and test the model.
```
training_validation_test(dl_train , dl_valid_lr,dl_valid_hr,dl_test_lr,dl_test_hr,result_dir,writer,config)
```
- If you've got a trained model and want to use it on all the files in a folder,
making sure they're isotropically resampled 
```
override_args_test = {
    "path_to_set":"/tcmldrive/shared/RambamMRE082022/new2/",
    "path_to_results":"/argusdata/users/jenny075/JennySh/results/",
    "path_to_trained_model":"/argusdata/users/jenny075/JennySh/results/Test_03_06_2024_22_21/Saved/FID/best.pth",
    "gpu_device":"0,1",
    "title":"Rec_all_files",
}

parser = setup_parser_test()
args_, _ = parser.parse_known_args([])
vars(args_).update(override_args_test)

reconstract_SR_volumes_in_folder(args_)
```
_______________________________________________________________________
## License
For this work we used the codes from the following works -

[1] Transformer for Single Image Super-Resolution
Zhisheng Lu, Juncheng Li, Hong Liu, Chaoyan Huang, Linlin Zhang, Tieyong Zeng

[2] Direct Unsupervised Super-Resolution Using Generative Adversarial Network
(DUS-GAN) for Real-World Data Kalpesh Prajapati , Vishal Chudasama

[3]  InceptionV3 implementation is taken from 
https://github.com/mseitzer/pytorch-fid

[4] FID and KID calculation are made by PIQ package - PyTorch Image Quality: Metrics for Image Quality Assessment by Kastryulin, Sergey and Zakirov, Jamil and Prokopenko, Denis and Dylov, Dmitry V. 






