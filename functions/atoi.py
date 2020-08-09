def myAtoi(self, str: str) -> int:
        val = 0
        neg = False
        moved = False
        for x in str:
            if ord(x) >= 48 and ord(x) <= 57:
                val = (val * 10) + ord(x)-48
                if not moved:
                    moved = True
                
            elif ord(x) == 45 and not moved and not neg and val == 0:
                neg = True
                if not moved:
                    moved = True
                
            elif ord(x) == 43 and not moved and val == 0:
                if not moved:
                    moved = True
                
            elif ord(x) == 32 and not moved  and val == 0:
                continue
                
            else:
                break
        if neg:
            val *= -1
            
        if val < -2147483648:
            return  -2147483648
        
        elif val > 2147483647:
            return  2147483647
        
        return val 