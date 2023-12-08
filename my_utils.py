import torch
import numpy as np
import random

def set_seed(seed):
    """
    设置随机种子以确保结果可重复。
    :param seed: 随机种子的值。
    """
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # if 使用多个 GPU
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


