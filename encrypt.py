input_str = "00102030405060708090A0B0C0D0E0F0"
s_box = [
    "63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76",
    "CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0",
    "B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15",
    "04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75",
    "09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84",
    "53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF",
    "D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8",
    "51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2",
    "CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73",
    "60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB",
    "E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79",
    "E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08",
    "BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A",
    "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E",
    "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF",
    "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
mixColKey = [[0b10, 0b11, 0b01, 0b01], [0b01, 0b10, 0b11, 0b01], [0b01, 0b01, 0b10, 0b11], [0b11, 0b01, 0b01, 0b10]]

def main():
  state = input_str.lower()
  state = toMatrice(state)
  print("Matrice d'entrée")
  printPropre(state)
  state = subBytes(state)
  print("Après passage dans subBytes")
  printPropre(state)
  state = shiftRows(state)
  print("Après passage dans shiftRows")
  printPropre(state)
  state = mixColumns(state)
  print("Matrice de sortie")
  printPropre(state)

def printPropre(input):
  for i in range(4):
    print(input[i])
  print("\n")

def fromLetterToDec(char):
  char = char.lower()
  if char == 'a':
    return 10
  elif char == 'b':
    return 11
  elif char == 'c':
    return 12
  elif char == 'd':
    return 13
  elif char == 'e':
    return 14
  elif char == 'f':
    return 15
  else:
    return char
  
def toMatrice(entree):
  matrice = [[0]*4 for _ in range(4)]
  step = 0
  for i in range(4):
    for j in range(4):
      matrice[i][j] = entree[step:step+2]
      step += 2
  return matrice

def subBytes(input):
  output = [[0]*4 for _ in range(4)]
  step_x = 0
  step_y = 0

  for i in input:
    for z in i:
      x = fromLetterToDec(z[0])
      y = fromLetterToDec(z[1])
      output[step_x][step_y] = s_box_16x16[int(x)][int(y)]
      if step_x < 3:
        step_x += 1
      else:
        step_x = 0
        step_y += 1
  return output

def shiftRows(input):
  output = [0]*4
  for z in range(4):
    temp = input[z]
    output[z] = temp[z:] + temp[:z]
  return output

def mixColumns(input):
  output = [[0] * 4 for _ in range(4)]
  output_hex = [[0] * 4 for _ in range(4)]

  for col in range(4):
      for row in range(4):
          output[row][col] = multiply(input[0][col], mixColKey[row][0]) ^ \
                              multiply(input[1][col], mixColKey[row][1]) ^ \
                              multiply(input[2][col], mixColKey[row][2]) ^ \
                              multiply(input[3][col], mixColKey[row][3])
          
  for i in range(4):
    for z in range(4):
      output_hex[i][z] = hex(output[i][z])[-2:]

  return(output_hex)


def multiply(a, b):
    a = int(a, 16)
    result = 0

    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x1B
        b >>= 1

    return result


s_box_16x16 = [s_box[i:i+16] for i in range(0, len(s_box), 16)]
main()