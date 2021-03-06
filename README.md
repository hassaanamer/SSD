# SSD
Deep learning with hardware efficiency. Experimenting with different models for the specilaised use case of utililising them for real time traffic surveillance. Pytorch Implementation.

## Datasets Supported:
* [Coco](http://cocodataset.org/#download)

* PASCAL VOC
```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
tar xvf VOCtest_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
tar xvf VOCtrainval_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
tar xvf VOCtrainval_11-May-2012.tar
```
* [UA-Detrac](http://detrac-db.rit.albany.edu/download)
  - [Train](https://drive.google.com/open?id=1_9ka5OmpQ7XPFndgcJnJp-59B74rp2u5)
  - [Test](https://drive.google.com/file/d/1cJsle-JCYZ8fXf7dEzxRuLXryrXEHRgW/view?usp=sharing)
* UA-Detrac Subset (temporal subsampling 1/10 of all locations other than 12,19 and 24 (mentioned in the seq_location.txt) taken as the train set, temporal subsampling 1/40 of the locations 12,19 and 24 (mentioned in the seq_location.txt) are taken as the test set)
  - [Train](https://drive.google.com/open?id=18yNRIxRzhdMG14IjkFRyRgIu9i48iTGS)
  - [Test](https://drive.google.com/open?id=1JUGbdARG8SIJnjHg_Glpak_uJmSM7iB_)
* [GRAM-RTM](http://agamenon.tsc.uah.es/Personales/rlopez/data/rtm/)
* GRAM-RTM Subset M-30

## Backbones Supported:
* EfficientNet
* MobilenetV2

## Installation:
Conda Environment [Download](https://drive.google.com/open?id=1CRqwv78Phu6uaFNbRPTNiE3IwdHZBi1Q)

## Single GPU:
```
python train.py --config-file configs/mobilenet_v2_ssd320_ua_custom_anchor_settings.yaml
```
## Multiple GPUs:
```
export NGPUS=4
```
```
python -m torch.distributed.launch --nproc_per_node=$NGPUS train.py --config-file configs/mobilenet_v2_ssd320_ua_custom_anchor_settings.yaml 
```
## Results:

### UA Detrac
| Model variations | Number of parameters (M) | Mean AP50 | Mean AP50 car | Mean AP50 bus | Mean AP50 van | Small Mean AP |
|       :---:      |     :---:      |     :---:     |     :---:     |     :---:     |     :---:     |    :---:   |
| EfficentNetSSDLite300   | 4.66     | 0.602    |0.66    |0.759    |0.387      |0.033      |
| MobileNetV2SSDLite320   | 3.05     | 0.406    |0.494   |0.532    |0.191      |0.011      |

### UA Detrac subset
| Model variations | Number of parameters (M) | Mean AP50 | Mean AP50 car | Mean AP50 bus | Mean AP50 van | Small Mean AP |
|       :---:      |     :---:      |     :---:     |     :---:     |     :---:     |     :---:     |    :---:   |
| EfficentNetSSDLite300   | 4.66     | 0.627    |0.748    |0.827   |0.307     |0.049      |
| MobileNetV2SSDLite320   | 3.05     | 0.490    |0.538   |0.703    |0.230      |0.004     |
