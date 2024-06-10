## Imports
import torch
assert torch.cuda.is_available()

import warnings
warnings.filterwarnings("ignore", category=UserWarning) 


from axcorsrmri import parser_setup

override_args = {
    "path_to_set": r"./data/",
    "path_to_results": r"./results/",
    "amount_of_files":20,
    "batch_size":12,
    "loss":"L2",
    "gpu_device":"0",
    "amount_of_slices":3,
    "title":"Test",
    "total_samples":100,
    "patch_size":48,
    "epochs": 20,
    "lr_g":0.0001,
    "lr_d": 0.0001,
    "scheduler": "const",
    "max_workers_train": 12,
    "max_workers_valid": 30,
    "valid_batch_size": 40,
    "adversarial_weight_I": 0.02,
    "adversarial_weight_E": 0.02,
    "d_optimizer_step_size":40 ,
    "g_optimizer_step_size": 160,
    "val_epoch": 5,
    "image_save_freq_batch": 100,
    "mage_save_freq_epoch": 5,
    "save_tensor":True,
    "save_nifti":True
}

args = parser_setup(override_args)

from axcorsrmri import initialize_data
dl_train, dl_valid_lr, dl_valid_hr, dl_test_lr, dl_test_hr, result_dir, writer, config = initialize_data(args)


from axcorsrmri import training_validation_test
training_validation_test(dl_train, dl_valid_lr, dl_valid_hr, dl_test_lr, dl_test_hr, result_dir, writer, config)