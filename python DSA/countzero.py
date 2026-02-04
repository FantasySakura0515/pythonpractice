def main():
    num = input("輸入數字來計算最多連續的0數：")
    counter = 0
    max_times = 0
    
    for char in num:
        if char == '0':  # Compare with string character '0'
            counter += 1
        else:
            counter = 0
        max_times = max(max_times, counter)
    print(max_times)

if __name__ == "__main__":
    main()