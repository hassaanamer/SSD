from torch.utils.data import ConcatDataset

from ssd.config.path_catlog import DatasetCatalog
from .voc import VOCDataset
from .coco import COCODataset
from .gram import GRAMDataset
from .uadetrac import uadetracDataset
from .ua import UADataset
# from .ua_ssd import uaDetection
# from .detrac import Track_Dataset




_DATASETS = {
    'VOCDataset': VOCDataset,
    'COCODataset': COCODataset,
    'GRAMDataset': GRAMDataset,
    'uadetracDataset': uadetracDataset,
    'UADataset': UADataset,
    # 'Track_Dataset': Track_Dataset,
    # 'uaDetection': uaDetection,
}

def build_dataset(dataset_list, transform=None, target_transform=None, is_train=True):
    assert len(dataset_list) > 0
    datasets = []
    for dataset_name in dataset_list:
        data = DatasetCatalog.get(dataset_name)
        args = data['args']
        factory = _DATASETS[data['factory']]
        args['transform'] = transform
        args['target_transform'] = target_transform
        if factory == VOCDataset:
            args['keep_difficult'] = not is_train
        elif factory == COCODataset:
            args['remove_empty'] = is_train
        elif factory == uadetracDataset:
            args['remove_empty'] = is_train
        elif factory == UADataset:
            args['remove_empty'] = is_train
        # elif factory == uaDetection:
        #     args['remove_empty'] = is_train

        dataset = factory(**args)
        datasets.append(dataset)
        # print(datasets)
    # for testing, return a list of datasets
    if not is_train:
        return datasets
    dataset = datasets[0]
    if len(datasets) > 1:
        dataset = ConcatDataset(datasets)

    return [dataset]
