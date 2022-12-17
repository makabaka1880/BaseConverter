#!/usr/bin/python3

import typer

numbersLower = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

numbersUpper = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

def convertTo(number: int, toUnit: int = 10, upper: bool = True):
    convertedStr = "";
    while number != 0:
        temp = number % 16;
        if upper:
            convertedStr = numbersUpper[temp] + convertedStr;
        else:
            convertedStr = numbersLower[temp] + convertedStr;
        number //= 16;
    return convertedStr;

def convertFrom(number: str, fromUnit: int = 10):
    _number = number[::-1].upper(); # reverse String number
    numberReturned = 0
    place = 0
    for i in _number:
        numberReturned += numbersUpper.index(i) * (fromUnit ** place)
        place += 1
    return numberReturned

def main(number: str = typer.Argument(...), i: int = typer.Option(10, "--input", "-i"), o: int = typer.Option(10, "--output", "-o"), upper: bool = typer.Option(True)):
    # num = convertFrom(number, i);
    # print(convertTo(num, o, upper));
    print(convertFrom("F1023", 16));

if __name__ == "__main__":
    typer.run(main);