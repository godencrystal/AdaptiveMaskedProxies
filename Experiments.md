
* Download [PASCAL VOC 2012 dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#devkit)
* Download [SBD dataset](http://home.bharathh.info/pubs/codes/SBD/download.html) + Use [rain.txt](http://home.bharathh.info/pubs/codes/SBD/train_noval.txt) provided by SBD instead of PASCAL.
* Modify config.json path to your SBD_PATH
* In all Experiments modify in the config files "path" to the PASCAL_VOC_PATH

# Reproducing experiments in Table 2 with finetuning

1. Unzip runs.zip in the same code folder

2.  For 1-shot experiments , modify the fold in configs/fcn8s_pascal_imprinted_finetune.yml and use the corresponding weights.
Use weights in path: runs/dilatedfcn8s_pascal/

3. Run:
```
python fewshot_imprinted_finetune.py --config configs/fcn8s_pascal_imprinted_finetune.yml --model_path runs/dilatedfcn8s_pascal/dilated_fcn_fold"$foldNo"/dilated_fcn8s_pascal_best_model.pkl --binary 2
```

4. For 5-shot experiments modify the fold in configs/fcn8s_pascal_imprinted_finetune_5shot.yml and use the corresponding weights.
Use weights in path: runs/dilatedfcn8s_pascal/

5. Run:
```
python fewshot_imprinted_finetune.py --config configs/fcn8s_pascal_imprinted_finetune_5shot.yml --model_path runs/dilatedfcn8s_pascal/dilated_fcn_fold"$foldNo"/dilated_fcn8s_pascal_best_model.pkl --binary 2
```

# Reproducing experiments in Table 3 without finetuning for Reduced-DFCN8s
1.  For 1-shot experiments, modify the fold in configs/redfcn8s_pascal_imprinted.yml and use the corresponding weights.
Use weights in path: runs/reddilatedfcn8s_pascal/

2. Run:
```
python fewshot_imprinted.py --config configs/redfcn8s_pascal_imprinted.yml --model_path runs/reddilatedfcn8s_pascal/reduced_fcn_fold"$foldNo"/dilated_fcn8s_pascal_best_model.pkl --binary 1
```
3.  For 5-shot experiments , modify kshot to 5 and the fold in configs/redfcn8s_pascal_imprinted.yml and use the corresponding weights.
Use weights in path: runs/reddilatedfcn8s_pascal/

4. Run similar to 2

# Reproducing experiments in Table 4 without finetuning for Dilated-FCN8s
1.  For 1-shot experiments, modify the fold in configs/fcn8s_pascal_imprinted.yml and use the corresponding weights.
Use weights in path: runs/dilatedfcn8s_pascal/

2. Run:
```
python fewshot_imprinted.py --config configs/fcn8s_pascal_imprinted.yml --model_path runs/dilatedfcn8s_pascal/dilated_fcn_fold"$foldNo"/dilated_fcn8s_pascal_best_model.pkl --binary 1
```
3.  For 5-shot experiments, modify the kshot to 5 and the fold in configs/fcn8s_pascal_imprinted.yml and use the corresponding weights.
Use weights in path: runs/dilatedfcn8s_pascal/

4. Run similar to 2

