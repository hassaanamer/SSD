# SSD
Deep learning with hardware efficiency. Experimenting with different models for the specilaised use case of utililising them for real time traffic surveillance. 

## Datasets Supported:
* [Coco](http://cocodataset.org/#download)

* PASCAL VOC
```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
```
```
tar xvf VOCtest_06-Nov-2007.tar
```
```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
```
```
tar xvf VOCtrainval_06-Nov-2007.tar
```
```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
```
```
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

