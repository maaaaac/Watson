# stage 0: train/dev/eval split
python  ../../mksubset.py BZNSYP/Wave data/biaobei --train-dev-test-split --dev-size 10 --test-size 10 --limit=1000000

# stage 1: Feature Generation
python  ../../preprocess.py wavallin data/biaobei/train_no_dev dump/biaobei/logmelspectrogram/org/train_no_dev --hparams=global_gain_scale=1.0 --preset=conf/biaobei.json
python  ../../preprocess.py wavallin data/biaobei/dev dump/biaobei/logmelspectrogram/org/dev --hparams=global_gain_scale=1.0 --preset=conf/biaobei.json
python  ../../preprocess.py wavallin data/biaobei/eval dump/biaobei/logmelspectrogram/org/eval --hparams=global_gain_scale=1.0 --preset=conf/biaobei.json
(ls dump/biaobei/logmelspectrogram/org/train_no_dev/*-feats.npy).FullName > train_list.txt
# Bash: find dump/biaobei/logmelspectrogram/org/train_no_dev -type f -name *feats.npy > train_list.txt
python  ../../compute-meanvar-stats.py train_list.txt dump/biaobei/logmelspectrogram/org/meanvar.joblib
rm train_list.txt

# stage 2: WaveNet training
python  ../../train.py --dump-root dump/biaobei/logmelspectrogram/norm --preset conf/biaobei.json --checkpoint-dir=exp/biaobei_train_no_dev_biaobei --log-event-path=tensorboard/biaobei_train_no_dev_biaobei