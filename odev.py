points = [(2, 3), (4, 7), (1, 5), (9, 6)]

def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Noktalar:", points)
print("Tüm Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
