import distutils.version
from PreprocessUtils import resample_cases, create_database
from main import setup_parser, initialize_data, training_validation_test, setup_parser_test, reconstruct_SR_volumes_in_folder

def parser_setup(override_args):
    parser = setup_parser()
    args, _ = parser.parse_known_args([])
    vars(args).update(override_args)
    
    return args

def test_parser_setup(override_args):
    parser = setup_parser_test()
    args, _ = parser.parse_known_args([])
    vars(args).update(override_args)
    
    return args
