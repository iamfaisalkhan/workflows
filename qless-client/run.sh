
type qless-py-worker > /dev/null 2>&1 || export PATH=../qless-py/bin:$PATH
export PYTHONPATH=../qless-py/:.
export EXE_DIR=`pwd`

qless-py-worker -q gridftp -q multitau -q plot -w 6 -p . -v -i 10
