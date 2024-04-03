#!/bin/bash

file=${BASH_SOURCE}
dname=$(dirname ${file})

touch ${dname}/stop
sleep 20
rm ${dname}/stop
