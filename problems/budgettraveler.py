def min_countries_to_visit(n, countries):
    total_attractions = sum(y for _, y in countries)
    countries.sort(key=lambda x: x[1], reverse=True)
    attractions_count = 0
    countries_visited = 0
    half_attractions = total_attractions / 2
    
    for _, attractions in countries:
        attractions_count += attractions
        countries_visited += 1
        if attractions_count >= half_attractions:
            break
    
    return countries_visited

n = int(input())
countries = [tuple(map(int, input().split())) for _ in range(n)]
print(min_countries_to_visit(n, countries))
