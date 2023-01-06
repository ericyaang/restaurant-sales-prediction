def split_data(data, val_size):
    """Split the data based on a test split factor."""
    l = len(data)
    t_idx = round(l * (1 - val_size))
    train, val = data[:t_idx], data[t_idx:]
    print(f"train: {len(train)} , test: {len(val)}")
    return train, val


def split_label(dataset, target_feature):
    X = dataset.drop([target_feature], axis=1)
    y = dataset[[target_feature]]
    return X, y
