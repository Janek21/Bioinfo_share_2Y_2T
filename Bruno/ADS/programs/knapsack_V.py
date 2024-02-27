def knapsack(weights, values, current_item, max_w, min_v, cand, cand_w, cand_v):
    if current_item == -1:
        if cand_v >= min_v and cand_w <= max_w:
            return cand
        else: return list()
    else:
        sol = knapsack(weights, values, current_item - 1,
        max_w, min_v, cand, cand_w, cand_v)
    if sol: return sol
    else:
        return knapsack( weights, values, current_item - 1,
        max_w, min_v,
        cand + [ current_item ],
        cand_w + weights[current_item],
        cand_v + values[current_item] )
