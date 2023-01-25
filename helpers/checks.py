class Checks:
    @staticmethod
    def is_int(num):
        try: 
            int(num)
            
            return True
        except Exception:
            return False