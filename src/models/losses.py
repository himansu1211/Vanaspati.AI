"""
Vanaspati.AI - Advanced Deep Learning Loss Functions
Implements Focal Loss for combating extreme class imbalance between common crops
and rare spinach/vegetable disease classes in multi-task computer vision models.
"""

from typing import Optional

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    class FocalLoss(nn.Module):
        """
        Focal Loss addresses class imbalance by down-weighting easy examples
        and focusing training on hard negatives/rare species classes.
        Formula: FL(p_t) = -alpha_t * (1 - p_t)^gamma * log(p_t)
        """
        def __init__(self, alpha: Optional[float] = 0.25, gamma: float = 2.0, reduction: str = 'mean'):
            super(FocalLoss, self).__init__()
            self.alpha = alpha
            self.gamma = gamma
            self.reduction = reduction

        def forward(self, inputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
            ce_loss = F.cross_entropy(inputs, targets, reduction='none')
            pt = torch.exp(-ce_loss)
            focal_loss = ((1.0 - pt) ** self.gamma) * ce_loss

            if self.alpha is not None:
                alpha_t = self.alpha
                focal_loss = alpha_t * focal_loss

            if self.reduction == 'mean':
                return focal_loss.mean()
            elif self.reduction == 'sum':
                return focal_loss.sum()
            return focal_loss

except (ImportError, OSError):
    class FocalLoss:
        def __init__(self, alpha: Optional[float] = 0.25, gamma: float = 2.0, reduction: str = 'mean'):
            self.alpha = alpha
            self.gamma = gamma
            self.reduction = reduction
