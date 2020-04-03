#!/bin/bash
#SBATCH -J test
#SBATCH --no-requeue
#SBATCH --mem 80960
#SBATCH -p gpu-cbio	
#SBATCH --gres=gpu:1
echo "$HOSTNAME"
module load cuda10.0
conda activate cbio
python main.py
echo "Fin du job"