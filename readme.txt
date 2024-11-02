forked from:
https://github.com/riscv-software-src/riscv-tests

How to use:
git clone git@github.com:exaithrg/riscv_tests_collection.git
git submodule update --init --recursive
autoupdate
autoconf
./configure --prefix=$RV_DEFAULT/target
cd isa
make rv32ui
# sudo make install
