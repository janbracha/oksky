OTA = int(input('zadej OTA '))
vzletova_hmotnost = int(input('zadej payload'))


def closest_1(temp_range, OTA):

    return temp_range[min(range(len(temp_range)), key = lambda i: abs(temp_range[i]-OTA))]

temp_range = [5, 15, 25, 35, 45]
closest_temperature= (closest_1(temp_range, OTA))


def closest_2(payload_range, vzletova_hmotnost):

    return payload_range[min(range(len(payload_range)), key = lambda i: abs (payload_range[i]-vzletova_hmotnost))]

payload_range = [7500, 6500, 5500, 4500]
closest_payload= (closest_2(payload_range, vzletova_hmotnost))
print("closest_temperature", closest_temperature)
print("closest_payload", closest_payload)
