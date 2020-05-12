import os


class DatasetCatalog:
    DATA_DIR = '/home/hamer/data'
    DATASETS = {
        'gram_train': {
            "data_dir": "GRAM-M-30",
            "split": "train"
        },
        'gram_test': {
            "data_dir": "GRAM-M-30",
            "split": "test"
        },
        'voc_2007_train': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "train"
        },
        'voc_2007_val': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "val"
        },
        'voc_2007_trainval': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "trainval"
        },
        'voc_2007_test': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "test"
        },
        'voc_2012_train': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "train"
        },
        'voc_2012_val': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "val"
        },
        'voc_2012_trainval': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "trainval"
        },
        'voc_2012_test': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "test"
        },
        'coco_2014_valminusminival': {
            "data_dir": "val2014",
            "ann_file": "annotations/instances_valminusminival2014.json"
        },
        'coco_2014_minival': {
            "data_dir": "val2014",
            "ann_file": "annotations/instances_minival2014.json"
        },
        'coco_2014_train': {
            "data_dir": "images/train2014",
            "ann_file": "coco/annotations/annotations/instances_train2014.json"
        },
        'coco_2014_val': {
            "data_dir": "images/val2014",
            "ann_file": "coco/annotations/annotations/instances_val2014.json"
        },
        'uadetrac_train': {
            "data_dir": "UA_detrac/DETRAC-train-data/Insight-MVT_Annotation_Train", ##############
            "ann_file": "UA_detrac/DETRAC-Train-Annotations-XML"
        },
        # 'uadetrac_test': {
        #     "data_dir": "UA_detrac/DETRAC-test-data/Insight-MVT_Annotation_Test", ##############
        #     "ann_file": "UA_detrac/DETRAC-Test-Annotations-XML"
        'ua_train': {
            "data_dir": "UA_detrac/DETRAC-train-data/Insight-MVT_Annotation_Train", ##############
            "ann_file": "UA_detrac/annotations.json"
        },
        'ua_test': {
            "data_dir": "UA_detrac/DETRAC-test-data/Insight-MVT_Annotation_Test", ##############
            "ann_file": "UA_detrac/annotations_test.json"
        },
        'ua_train_subsample': {
            "data_dir": "UA_detrac/DETRAC-modified/train", ##############
            "ann_file": "UA_detrac/DETRAC-modified/train/annotations_train_subsample.json"
        },
        'ua_test_subsample': {
            "data_dir": "UA_detrac/DETRAC-modified/test", ##############
            "ann_file": "UA_detrac/DETRAC-modified/test/annotations_test_subsample.json"
        },
    }

    @staticmethod
    def get(name):
        if "voc" in name:
            voc_root = DatasetCatalog.DATA_DIR
            if 'VOC_ROOT' in os.environ:
                voc_root = os.environ['VOC_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(voc_root, attrs["data_dir"]),
                split=attrs["split"],
            )
            return dict(factory="VOCDataset", args=args)
        elif "coco" in name:
            coco_root = DatasetCatalog.DATA_DIR
            if 'COCO_ROOT' in os.environ:
                coco_root = os.environ['COCO_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(coco_root, attrs["data_dir"]),
                ann_file=os.path.join(coco_root, attrs["ann_file"]),
            )
            return dict(factory="COCODataset", args=args)
        elif "uadetrac" in name:
            uadetrac_root = DatasetCatalog.DATA_DIR
            if 'UADETRAC_ROOT' in os.environ:
                uadetrac_root = os.environ['UADETRAC_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(uadetrac_root, attrs["data_dir"]),
                ann_file=os.path.join(uadetrac_root, attrs["ann_file"]),
            )
            return dict(factory="uadetracDataset", args=args)

        elif "ua" in name:
            ua_root = DatasetCatalog.DATA_DIR
            if 'UA_ROOT' in os.environ:
                ua_root = os.environ['UA_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(ua_root, attrs["data_dir"]),
                ann_file=os.path.join(ua_root, attrs["ann_file"]),
            )
            return dict(factory="UADataset", args=args)

        elif "gram" in name:
            gram_root = DatasetCatalog.DATA_DIR
            if 'GRAM_ROOT' in os.environ:
                gram_root = os.environ['GRAM_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(gram_root, attrs["data_dir"]),
                split=attrs["split"],
            )
            return dict(factory="GRAMDataset", args=args)

        raise RuntimeError("Dataset not available: {}".format(name))
