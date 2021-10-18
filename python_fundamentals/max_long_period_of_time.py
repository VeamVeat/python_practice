
def longest_time(h: int, m: int, s: int) -> str:
    max_time = {
        h: h * 3600,
        m: m * 60,
        s: s,
    }

    return max(max_time, key=max_time.get)


print("Максимально длительный промежуток времени -> ", longest_time(1, 59, 3598))
