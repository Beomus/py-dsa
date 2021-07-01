"""
Run-length encoding: write a function that takes in a non-empty string and
returns its run-length encoding.

Run-length encoding: "AAAA" => "4A", "AAAAAAAAAAAA" => "9A3A" (instead of "12A")
"""


def runLengthEncoding_s(string):
    tracker = ""
    count = 1
    cur = string[0]
    for char in string[1:]:
        if char == cur:
            count += 1
            if count > 9:
                # update tracker
                tracker = tracker + str(count - 1) + cur
                count = 1
        elif char != cur:
            # update tracker
            tracker = tracker + str(count) + cur

            # reset count and char
            cur = char
            count = 1

    # handle the last count
    tracker = tracker + str(count) + cur
    return tracker


def runLengthEncoding_l(string):
    # Write your code here.
    encoded = []
    currentLength = 1

    for i in range(1, len(string)):
        current = string[i]
        previous = string[i - 1]

        if current != previous or currentLength == 9:
            encoded.append(str(currentLength))
            encoded.append(previous)
            currentLength = 0

        currentLength += 1
    encoded.append(str(currentLength))
    encoded.append(string[len(string) - 1])
    result = "".join(encoded)

    return result
