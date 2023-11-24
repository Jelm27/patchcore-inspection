import torch
from .ifw import IFWDataset
from .njust import NJUSTDataset

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


class DatasetSplit(Enum):
    TRAIN = "train"
    VAL = "val"
    TEST = "test"

class JointDataset(torch.utils.data.Dataset):
    def __init__(self, source_ifw, classname_ifw, source_njust, classname_njust, **kwargs):
        """
        Initialize both datasets.
        Args:
            source_ifw: Path to the IFW dataset.
            classname_ifw: Classname for IFW dataset.
            source_njust: Path to the njust dataset.
            classname_njust: Classname for njust dataset.
            kwargs: Additional arguments to pass to the dataset constructors.
        """
        self.ifw_dataset = IFWDataset(source=source_ifw, classname=classname_ifw, **kwargs)
        self.njust_dataset = NJUSTDataset(source=source_njust, classname=classname_njust, **kwargs)

        self.total_length = len(self.ifw_dataset) + len(self.njust_dataset)

    def __getitem__(self, idx):
        """
        Fetch an item from the appropriate dataset.
        """
        if idx < len(self.ifw_dataset):
            return self.ifw_dataset[idx]
        else:
            # Adjust index for the second dataset
            return self.njust_dataset[idx - len(self.ifw_dataset)]

    def __len__(self):
        """
        Return the combined length of both datasets.
        """
        return self.total_length
