conda create -n xpdconf --yes
conda install -n xpdconf --file requirements/build.txt --file requirements/run.txt --file requirements/test.txt --yes
conda run -n xpdconf pip instal -e ./ --no-deps --no-capture-output
