class RomanNumerals:
    romans ={
        1000: "M",
        500:  "D",
        100:  "C",
        50:   "L",
        10:   "X",
        5:    "V",
        1:    "I"
    }
    
    ints = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1
    }
    @staticmethod
    def to_roman(val : int) -> str:
        WORD = ""
        digits = [0] * len(str(val))
        temp_dig = val
        c=0
        while temp_dig > 0:
            digits[len(digits) - c - 1] = (temp_dig % 10) * (10**c)
            temp_dig = temp_dig // 10
            c+=1
        for dig in digits:
            if dig in RomanNumerals.romans:
                WORD += RomanNumerals.romans[dig]
                
            else:
                for roman in RomanNumerals.romans.keys():
                    if str(roman)[0] == "5":
                        subtract_numeral = roman // 5 #subtract = 100
                        if roman - subtract_numeral == dig: # roman = 500; dig = 400; 500-100 == 400   if dig is made with subtracting(starts with 4)
                            WORD += RomanNumerals.romans[subtract_numeral] + RomanNumerals.romans[roman] #CD
                            
                        else: # if dig is made with adding(starts with 2-3)
                            for add_blank in range(subtract_numeral*2, subtract_numeral*4, subtract_numeral):
                                if add_blank == dig:
                                    WORD += RomanNumerals.romans[subtract_numeral] * (add_blank//subtract_numeral)
                                    
                            for add_with_base in range(subtract_numeral, subtract_numeral*4, subtract_numeral):
                                if add_with_base + roman == dig: #dig = 700; add_with_base = 200; roman = 500; 200 + 500 == 700
                                    WORD += RomanNumerals.romans[roman] + (RomanNumerals.romans[subtract_numeral] * (add_with_base//subtract_numeral))
                            
                    elif str(roman)[0] == "1":
                        subtract_numeral = roman // 10 #subtract = 100
                        if roman == 1000:
                            WORD += RomanNumerals.romans[roman] * (dig//roman)
                        if roman - subtract_numeral == dig: # roman = 1000; dig = 900; 1000-100 == 900   if dig is made with subtracting(starts with 9)
                            WORD += RomanNumerals.romans[subtract_numeral] + RomanNumerals.romans[roman] #CM
                            
        return WORD                    
                    


    @staticmethod
    def from_roman(roman : str) -> int:
        #get a list of chars
        numerals = roman.split("")
        
        return 0
    
print(RomanNumerals.to_roman(int(input())))