







/*Pedestrian*/
# 1. generate the ground truth database: /gt_database/train_gt_database_3level_Car.pkl 
python generate_gt_database.py --class_name 'Pedestrian' --split train

# 2. train the first proposal generation : RPN
python train_rcnn.py --cfg_file cfgs/pedestrian.yaml --gt_database gt_database/train_gt_database_3level_Pedestrian.pkl \
--output_dir ../trainedModel/pedestrian/rpn --batch_size 8 --train_mode rpn --epochs 50  --ckpt_save_interval 5 
 

# 3. train the second part: RCNN
python train_rcnn.py --cfg_file cfgs/pedestrian.yaml --gt_database gt_database/train_gt_database_3level_Pedestrian.pkl \
--rpn_ckpt ../trainedModel/pedestrian/rpn/ckpt/checkpoint_epoch_50.pth --output_dir ../trainedModel/pedestrian/rcnn \
--batch_size 3 --train_mode rcnn --epochs 18  --ckpt_save_interval 2




/*bus */
# 1. generate the ground truth database: /gt_database/train_gt_database_3level_Car.pkl 
python generate_gt_database.py --class_name 'Bus' --split train

# 2. train the first proposal generation : RPN
python train_rcnn.py --cfg_file cfgs/bus.yaml --gt_database gt_database/train_gt_database_3level_Bus.pkl \
--output_dir ../trainedModel/bus/rpn --batch_size 8 --train_mode rpn --epochs 50  --ckpt_save_interval 5 
 

# 3. train the second part: RCNN
python train_rcnn.py --cfg_file cfgs/bus.yaml --gt_database gt_database/train_gt_database_3level_Bus.pkl \
--rpn_ckpt ../trainedModel/bus/rpn/ckpt/checkpoint_epoch_50.pth --output_dir ../trainedModel/bus/rcnn \
--batch_size 2 --train_mode rcnn --epochs 18  --ckpt_save_interval 2



/*car */
# 1. generate the ground truth database: /gt_database/train_gt_database_3level_Car.pkl 
python generate_gt_database.py --class_name 'Car' --split train

# 2. train the first proposal generation : RPN
python train_rcnn.py --cfg_file cfgs/car.yaml --gt_database gt_database/train_gt_database_3level_Car.pkl \
--output_dir ../trainedModel/car/rpn --batch_size 8 --train_mode rpn --epochs 200  --ckpt_save_interval 1 \
--ckpt ../trainedModel/car/rpn/ckpt/checkpoint_epoch_30.pth
 

# 3. train the second part: RCNN
python train_rcnn.py --cfg_file cfgs/car.yaml --gt_database gt_database/train_gt_database_3level_Car.pkl \
--rpn_ckpt ../trainedModel/car/rpn/ckpt/checkpoint_epoch_30.pth --output_dir ../trainedModel/car/rcnn \
--batch_size 2 --train_mode rcnn --epochs 50  --ckpt_save_interval 1
