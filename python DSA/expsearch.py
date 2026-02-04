class tool:
    def __init__(self):
        self.result = 0

    def search(self, arr, target, left, right):
        # 基本邊界檢查
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        
        while left <= right:
            mid = (right + left) // 2  # 使用 // 進行整數除法更簡潔
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                return mid
        return -1

def main():
    t = tool()

    # 建立測試資料
    arr = [i for i in range(0, 5000, 2)]
    target = 6000
    
    # 1. 早期檢查：如果目標大於最大值，直接結束
    if target > arr[len(arr)-1]:
        print("-1")
        return 0

    # 2. 指數搜尋邏輯 (Exponential Search)
    counter = 1
    while True:
        right = pow(2, counter)
        
        # 額外保護：防止 index 超出 arr 範圍
        if right >= len(arr):
            print(t.search(arr, target, int(right/2), len(arr)-1))
            break
            
        if arr[right] > target:
            print(t.search(arr, target, int(right/2), min(len(arr)-1, right)))
            break
            
        counter += 1

# 這是 Python 的標準進入點寫法
if __name__ == "__main__":
    main()

