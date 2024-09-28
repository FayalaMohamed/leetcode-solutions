class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2

        def partition(left, right, pivot_idx):
            pivot = distance(points[pivot_idx])
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if distance(points[i]) < pivot:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        def select(left, right, k):
            if left == right:
                return

            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if k == pivot_idx:
                return
            elif k < pivot_idx:
                select(left, pivot_idx - 1, k)
            else:
                select(pivot_idx + 1, right, k)

        if not points or k <= 0:
            return []

        select(0, len(points) - 1, k)
        return points[:k]