# coding=utf-8
"""
@Author:lts
@Time:2024/3/13 14:48
@description:
"""
from torchvision import transforms
from torchvision.transforms import functional as F
from torch import Tensor

class RandomAffine(transforms.RandomAffine):

    def __init__(self, degrees, translate=None, scale=None, shear=None, interpolation=transforms.InterpolationMode.NEAREST, fill=0, center=None):
        super().__init__(degrees, translate, scale, shear, interpolation, fill, center)
        self.ret = None

    def forward(self, img):
        """
            img (PIL Image or Tensor): Image to be transformed.

        Returns:
            PIL Image or Tensor: Affine transformed image.
        """
        fill = self.fill
        channels, height, width = F.get_dimensions(img)
        if isinstance(img, Tensor):
            if isinstance(fill, (int, float)):
                fill = [float(fill)] * channels
            else:
                fill = [float(f) for f in fill]

        img_size = [width, height]  # flip for keeping BC on get_params call

        ret = self.get_params(self.degrees, self.translate, self.scale, self.shear, img_size)
        self.ret = ret

        return F.affine(img, *ret, interpolation=self.interpolation, fill=fill, center=self.center)
