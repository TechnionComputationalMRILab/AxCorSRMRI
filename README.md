# AxCorSRMRI
Self-Supervised Realistic Through-Plane MRI Super Resolution from Clinical 2D Axial and Coronal Acquisition.


## Instruction 

**A full example can be seen in `sample.ipynb`**.

- First create isotropicaly resampled coronal data.  
```
path_to_data_files = "/path/to/data/"
coronal_files_prefix = None # not mandatory
ResampleCases(path_dir = path_to_data_files ,prefix = coronal_files_prefix)
```
- Create .csv file database with the coronal axial and isotropical files. 
```
path_to_data_files = "/path/to/data/"
CreateDateBase(path_to_data_files,cor_prefix=None,ax_prefix=None,train_frac=0.8,test_frac=0.1,num_folds = 1)
```
- Define main parameters and  model parameters. Explanation on the possible parameters can be found at `parameter_dictionary.txt`.    
```
override_args = {
    "path_to_set":"/tcmldrive/shared/RambamMRE082022/new2/",
    "path_to_results":"/argusdata/users/jenny075/JennySh/results/",
    "batch_size":12,
    "gpu_device":"0,1",
    "amount_of_slices":3,
    }
parser = setup_parser()
args, _ = parser.parse_known_args([])
vars(args).update(override_args)
```
- Create the datasets
```
dl_train , dl_valid_lr,dl_valid_hr,dl_test_lr,dl_test_hr,result_dir,writer,config  = Data_Inittializaion(args)
```
- Train, valid and test the model.
```
training_validation_test(dl_train , dl_valid_lr,dl_valid_hr,dl_test_lr,dl_test_hr,result_dir,writer,config)
```
- If you already have trained model and you went to apply it on all the files in the folder
```
override_args_test = {
    "path_to_set":"/tcmldrive/shared/RambamMRE082022/new2/",
    "path_to_results":"/argusdata/users/jenny075/JennySh/results/",
    "gpu_device":"0,1",
    "title":"Test",
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






