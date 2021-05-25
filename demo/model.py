import torch
from neural_genesis import nn


class Model(nn.Module):
    def __init__(self,  ):
        super(Model, self).__init__()
        self.Conv2d_g8 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=2, padding=1)
        self.Conv2d_g10 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=1, stride=1)
        self.Conv2d_g12 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=2, padding=1)
        self.Conv2d_g14 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=1, stride=1)
        self.AdaptiveAvgPool2d_g19 = nn.AdaptiveAvgPool2d(output_size=1)
        self.Flatten_g22 = nn.Flatten(start_dim=1)
        self.Linear_g25 = nn.Linear(in_features=128, out_features=10)

    def forward(self, x):
        g8 = self.Conv2d_g8(x)
        g10 = self.Conv2d_g10(g8)
        g12 = self.Conv2d_g12(g10)
        g14 = self.Conv2d_g14(g12)
        g19 = self.AdaptiveAvgPool2d_g19(g14)
        g22 = self.Flatten_g22(g19)
        g25 = self.Linear_g25(g22)
        return g25


def my_model():
    return Model()
