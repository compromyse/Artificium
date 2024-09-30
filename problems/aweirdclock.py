def transform_time(readable_text):
    mapping = {
        'O': '0', '0': '0',
        'i': '1', '1': '1',
        '2': '2',
        'E': '3',
        'h': '4',
        'S': '5', '5': '5',
        '9': '6',
        'L': '7',
        '8': '8',
        '6': '9'
    }

    reversed_text = readable_text[::-1]
    reversed_hours, reversed_minutes = reversed_text.split(":")
    
    hours = int("".join(mapping[c] for c in reversed_hours))
    minutes = int("".join(mapping[c] for c in reversed_minutes))
    
    if hours >= 24:
        print(f"Error {hours} hours")
    if minutes >= 60:
        print(f"Error {minutes} minutes")
    
    if hours < 24 and minutes < 60:
        print(f"{hours}:{minutes:02d}")

readable_text = input()
transform_time(readable_text)
