# mle_training
#creation of conda environment
conda create -n mle_dev python
#activation of conda environment
conda activate mle-dev
#export of library's to environment.yml
conda export --h mle-dev > environment.yml

