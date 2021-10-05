
def longest_time(h: int, m: int, s: int) -> str:
    time_hour_minute_second = {
        f'{h}': h * 3600,
        f'{m}': m * 60,
        f'{s}': s,
    }
    return max(time_hour_minute_second, key=time_hour_minute_second.get)


t = longest_time(15, 955, 59400)
print("Максимально длительный промежуток времени -> ", t)
