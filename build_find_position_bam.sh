#!/bin/bash
if [ ! -d "bamtools" ]; then
  # http://stackoverflow.com/questions/7292584/how-to-check-if-git-is-installed-from-bashrc
  git --version 2>&1 >/dev/null
  GIT_IS_AVAILABLE=$?
  if [ $GIT_IS_AVAILABLE -eq 0 ]; then
    git clone https://github.com/pezmaster31/bamtools
  else
    wget https://github.com/pezmaster31/bamtools/archive/master.zip
    unzip master.zip 2>&1 > /dev/null
    rm master.zip;mv bamtools-master bamtools
  fi
fi

if [ ! -d "bamtools_build" ]; then
  mkdir bamtools_build
fi

if [ ! -f "bamtools_build/lib/libbamtools.a" ]; then
  cd bamtools_build
  cmake ../bamtools
  make
  cd ..
fi

g++ -O3 1.find_position_bam.cpp -o 1.find_position_bam -Ibamtools/include -Lbamtools/lib -lbamtools -lz -Ibamtools/src -Ibamtools_build/src
