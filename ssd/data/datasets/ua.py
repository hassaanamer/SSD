import os
import torch.utils.data
import numpy as np
from PIL import Image

from ssd.structures.container import Container


class UADataset(torch.utils.data.Dataset):
    class_names = ('__background__','car', 'bus', 'van')
    # class_names = ('__background__','car', 'others')


    def __init__(self, data_dir, ann_file, transform=None, target_transform=None, remove_empty=False):
        from pycocotools.coco import COCO
        # self.coco = COCO(ann_file)
        self.ua = COCO(ann_file)

        # print('111111111111111111111')

        self.data_dir = data_dir
        # print(self.data_dir)
        # print('aaaaaaaaaaaaaaaaaaaaaaaaa')
        self.transform = transform
        self.target_transform = target_transform
        self.remove_empty = remove_empty
        if self.remove_empty:
            # when training, images without annotations are removed.
            self.ids = list(self.ua.imgToAnns.keys())#####################
        else:
            # when testing, all images used.
            self.ids = list(self.ua.imgs.keys())##############################
        coco_categories = sorted(self.ua.getCatIds())######################
        # print(coco_categories)
        # print('abbbbbbbbbbbbbbbbbbbbb')
        self.coco_id_to_contiguous_id = {coco_id: i + 1 for i, coco_id in enumerate(coco_categories)}
        # print(self.coco_id_to_contiguous_id)
        self.contiguous_id_to_coco_id = {v: k for k, v in self.coco_id_to_contiguous_id.items()}


    def __getitem__(self, index):
        image_id = self.ids[index]
        # print(image_id)
        boxes, labels = self._get_annotation(image_id)
        image = self._read_image(image_id)
        if self.transform:
            image, boxes, labels = self.transform(image, boxes, labels)
        if self.target_transform:
            boxes, labels = self.target_transform(boxes, labels)
        targets = Container(
            boxes=boxes,
            labels=labels,
        )
        return image, targets, index

    def get_annotation(self, index):
        image_id = self.ids[index]
        return image_id, self._get_annotation(image_id)

        image_id = self.ids[index]
        return image_id, self._get_annotation(image_id)

    def __len__(self):
        return len(self.ids)

    def _get_annotation(self, image_id):
        ann_ids = self.ua.getAnnIds(imgIds=image_id)
        ann = self.ua.loadAnns(ann_ids)
        # filter crowd annotations
        ann = [obj for obj in ann if obj["iscrowd"] == 0]
        boxes = np.array([self._xywh2xyxy(obj["bbox"]) for obj in ann], np.float32).reshape((-1, 4))
        labels = np.array([self.coco_id_to_contiguous_id[obj["category_id"]] for obj in ann], np.int64).reshape((-1,))
        # remove invalid boxes
        keep = (boxes[:, 3] > boxes[:, 1]) & (boxes[:, 2] > boxes[:, 0])
        boxes = boxes[keep]
        labels = labels[keep]

        # label_map = {}
        # labels = open(label_file, 'r')
        # for line in labels:
        #     ids = line.split(',')
        #     label_map[int(ids[0])] = int(ids[1])

        return boxes, labels

    def _xywh2xyxy(self, box):
        x1, y1, w, h = box
        return [x1, y1, x1 + w, y1 + h]

    def get_img_info(self, index):
        image_id = self.ids[index]
        img_data = self.ua.imgs[image_id]
        return img_data

    def _read_image(self, image_id):
        file_name = self.ua.loadImgs(image_id)[0]['file_name']
        image_file = os.path.join(self.data_dir, file_name)
        image = Image.open(image_file).convert("RGB")
        image = np.array(image)
        return image
