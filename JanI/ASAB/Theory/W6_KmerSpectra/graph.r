#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
split_args <- strsplit(args, ",")
kmers <- split_args[[1]]
reps <- split_args[[2]]
print(kmers)
print(reps)
