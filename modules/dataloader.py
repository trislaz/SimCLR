from torch.utils.data import Dataset
import os
from glob import glob
from PIL import Image

class dataset(Dataset):
    imext = set(['.png', '.jpg'])
    def __init__(self, path, transform=None):
        self.path = path
        self.imext = set(['.png', '.jpg'])
        self.files = self._collect_files(args.path)
        self.transform = transform
    
    def _collect_file_path(self, path):
        out = []
        files = os.listdir(path)
        files = [os.path.splitext(x) for x in files]
        for name, ext in files:
            if ext in self.imext:
                out.append(os.path.join(path, name+ext))  
        return out
    
    def _collect_files(self, path):
        return self._collect_file_path(path)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        impath = self.files[idx]
        image = Image.open(impath)
        if self.transform is not None:
            image = self.transform(image)
        return image

class datasetWSI_simple(dataset):
    def __init__(self, path, transform=None):
        super(datasetWSI_simple, self).__init__(path, transform)

    def _collect_files(self, path):
        out = []
        paths = glob(os.path.join(path, '*'))
        for p in paths:
            out += self._collect_file_path(p)
        return out

