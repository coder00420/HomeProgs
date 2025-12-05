def points_combinations(n, k, sequence = {}, variations_count = 0,  immovable_points = 0, free_numbers = []):
    if immovable_points == k: exclude_immovable_points = True
    else: exclude_immovable_points = False
    if not free_numbers: free_numbers = [i for i in range(1, n + 1)]

    if len(sequence) == n: return variations_count + 1

    if exclude_immovable_points:
         

n, k = map(int, input().split())
