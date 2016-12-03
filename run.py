#!usr/bin/python

import machine_learning_project
import sys
import argparse

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="input file (csv)", required=True)
    parser.add_argument("-o", "--outfile", help="output file", required=True)
    parser.add_argument("-lf", "--logfile", help="log file to store the training time & RMSE value")
    parser.add_argument("-nl", "--nlayers", help="number of layers", type=int)
    parser.add_argument("-ndl", "--ndroplayers", help="number of dropout layers", type=int)
    parser.add_argument("-ld", "--layerdim", help="layer dimensions", nargs="+", type=int)
    parser.add_argument("-opt", "--optimizer", help="name of the optimizer")
    parser.add_argument("-lr", "--learnrate", help="the learning rate", type=float)
    parser.add_argument("-m", "--momentum", help="the momentum", type=float)
    parser.add_argument("-trp", "--trainpct", help="training percent (0.0, 1.0]", type=float)
    parser.add_argument("-em", "--errmetric", help="type of error metric")
    parser.add_argument("-a", "--append", help="append run configuration to logfile", type=bool, default=False, const=True, nargs="?")
    return parser

if __name__ == "__main__":
    parser = init_args()
    args = parser.parse_args()
    # Checking for required fields
    if not args.infile or not args.outfile:
        parser.print_help()
    else:
        given = {
            "input_filename": args.infile,
            "output_filename": args.outfile,
            "n_layers": 3,
	    "n_dropout_layers": 0,
            "layer_dimensions": [1,4,1],
            "optimizer": "adam",
            "learning_rate": 0.0,
            "momentum": 0.0,
            "training_percent": 0.7,
            "err_metric": "mean_squared_error",
	    "logfile": None,
        }
        if args.nlayers:
            given["n_layers"] = args.nlayers
        if args.ndroplayers:
            given["n_dropout_layers"] = args.ndroplayers
        if args.layerdim:
            given["layer_dimensions"] = args.layerdim
        if args.optimizer:
            given["optimizer"] = args.optimizer
        if args.learnrate:
            given["learning_rate"] = args.learnrate
        if args.momentum:
            given["momentum"] = args.momentum
        if args.trainpct:
            given["training_percent"] = args.trainpct
        if args.errmetric:
            given["err_metric"] = args.errmetric
	if args.logfile:
	    given["logfile"] = args.logfile

	# set configuration
	machine_learning_project.set_configuration(input_filename=given["input_filename"],
            output_filename=given["output_filename"], n_layers=given["n_layers"], n_dropout_layers=given["n_dropout_layers"], layer_dimensions=given["layer_dimensions"],
            optimizer=given["optimizer"], learning_rate=given["learning_rate"], momentum=given["momentum"], training_percent=given["training_percent"],
            err_metric=given["err_metric"], logfile=given["logfile"])
	# run
	machine_learning_project.run()
	# checking whether to append run configuration to run_configs file
	if args.append:
	    machine_learning_project.append_config()
