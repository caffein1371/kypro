##########################################
import io
import sys

_INPUT = """\
3
5
7



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
crypto = "iVBORw0KGgoAAAANSUhEUgAAAJ4AAAAPCAIAAACa3eHKAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFtSURBVFhH7VhBDsMwCOv/P91VisQINi6ptkMjeurSQIwNjrTj7GdTBo5N6+qyzpZ22yZoabeW9pifq9ZrIas4fPKhPuQfOUP++s9QC8UWCsEyBy1Y7+1OO52GC2zjk88f3i2hP+L7ToUsSkurQkDZCgc0d1WGRBytWxOpzBhATjMVscmoHoJVSkXgLdPY45/2LEk7Ii2eYg17BGgPXedEC7ntqiUecTOt9Jm0xlgR0pjFwFuxlYm0YbT1rKAM1Bl+mNNSWdlhRXCBsdTo/DYUw5QO23AwaGdn4bQuHNYgdnZodO/61Aoc+lYQhryUE30PLSETkvpw3Qa1YNqQl6aWVnRLLx3FyWC1eS65BB7Gj190ngwhGglt2azJNFpvFQ9UpNjwisluVqRdTO0EL5taalC0MG1lXozHOYt3bb2fEInGJgx5EGiPKRRWwjba6D620sT0iG9g1j69/nYG+i+LtyuY4m9pW9ptGdi2sA8yqI+0aNaAmAAAAABJRU5ErkJggg=="
caesar = 13
plain = ''

#cry = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"

for code in list(crypto):
    ASC = ord(code)
    #大文字の処理
    if ASC > 64 and ASC < 91:
        ASC -= 3
        if ASC < 64:
            ASC += 26

    #小文字の処理
    if ASC < 123 and ASC > 97:
        ASC -= 3
        if ASC < 97:
            ASC += 26

    print(chr(ASC), end="")