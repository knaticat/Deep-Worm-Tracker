import torch
import torchvision
from torchreid import models, utils
from torchreid.utils import load_pretrained_weights

weight_path = "./worm_reid.pt"
model = models.build_model(name='osnet_x0_25', num_classes=32, pretrained= False)
load_pretrained_weights(model, weight_path)
model.eval()
# example = torch.rand(1, 3, 256, 120)
# traced_script_module = torch.jit.script(model)
# traced_script_module.save("wormmodel.pt")