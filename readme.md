# Quick test for graph for pyg

## Data

**Align data with the following:**
+ x: `torch.tensor` and **normalization** # [num_nodes, num_features]
+ edge_index: `torch.tensor`  #[2, K]
+ train_mask, val_mask, test_mask: `torch.tensor dtype=bool`  # [num_nodes]
+ y: `torch.tensor`
