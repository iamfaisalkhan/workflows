
type qless-py-worker > /dev/null 2>&1 || export PATH=../qless-py/bin:$PATH
export PYTHONPATH=../qless-py/:.
export EXE_DIR="/home/xpcs/xpcs-0.5.0"
export QLESS_DIR=`pwd`

qless-py-worker -q gridftp -q multitau -w 1 -p . -v -i 10
