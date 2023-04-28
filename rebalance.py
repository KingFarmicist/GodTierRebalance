def rebalance(weights, portfolio, targets, threshold):\\n    diff = {c: (weights[c] - targets[c]) / targets[c] for c in weights}\\n    to_sell = {c: v*diff[c] for c, v in portfolio.items() if diff[c] > threshold}\\n    to_buy = {c: -v*diff[c] for c, v in portfolio.items() if diff[c] < -threshold}\\n    return to_sell, to_buy