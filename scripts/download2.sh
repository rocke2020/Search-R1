export HF_ENDPOINT=https://hf-mirror.com
save_path=/data/comm/
file=scripts/download.py
nohup python $file --save_path $save_path > $file.log 2>&1 &