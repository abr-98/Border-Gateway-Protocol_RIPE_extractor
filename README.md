# Border-Gateway-Protocol_RIPE_extractor
A modified version that uses a python script to automate the libbgpdump library of c to extract file to a json

Dataset can be obtained from:https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris/ris-raw-data

Original bgpdump repository:https://github.com/RIPE-NCC/bgpdump

How to use(For Ubuntu):

Extract into home folder

Setup the c executables using

cd /bgpdump-master
sh ./bootstrap.sh
make
./bgpdump -T

Replace the user name in the /bgpdump-master/bgp_lister.py

Place the required source in the BGP_Data(as shown in the folder)

Instruction to execute:

cd /bgpdump-master
python3 BGP_lister.py

It will produce results in the BGP_details folders


2 json format output are shown in the repo in .txt format.
