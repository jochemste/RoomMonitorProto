#!/bin/bash

file=${BASH_SOURCE}
dname=$(dirname ${file})

touch ${dname}/stop
