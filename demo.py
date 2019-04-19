import torch
from Attention import Attention1, Attention2, Multihead_Attention

features = torch.arange(0, 24)
features = torch.where(features < 20, features, torch.zeros_like(features))
features = features.view([2, 3, 4]).float()

attention1 = Attention1(hidden_dim=features.size()[-1])
print(attention1(features))

attention2 = Attention2(hidden_dim=features.size()[-1])
print(attention2(features))

attention3 = Multihead_Attention(hidden_dim=features.size()[-1])
print(attention3(features, features, features, 2))
