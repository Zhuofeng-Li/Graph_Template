import numpy as np
import torch
from dgl.data import CoraGraphDataset


class Cora_data:
    def __init__(self):
        dataset = CoraGraphDataset()
        dataset = dataset[0].ndata
        self.x = dataset['feat']

        self.train_mask = dataset['train_mask']
        self.val_mask = dataset['val_mask']
        self.test_mask = dataset['test_mask']

        self.y = dataset['label']
        self.edge_index = torch.stack(CoraGraphDataset()[0].edges(), dim=0)


