import re


class Date:
    """
    A class that represents the date
    
    Parameters
    ----------
    d : str
        String of the date in month, day, year order
    
    Attributes
    ----------
    date : tuple
        Tuple of (year, month, day), month reprsented as a prefix
    valid : bool
        If the date is a valid date
    """
    
    DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """List of number of days of each month with the first index equal to 0 (`list`).
    """
    
    MONTHS = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    """List of month prefixes wiht the first index equal to '' (`list`).
    """
    
    def __init__(self, d):
        results = re.search('^(\w+)\W*(\w+)\W*(\w*)\W*$', d)
        self.date = start = (int(results.group(3)),
                              int(results.group(1)) if results.group(1).isdigit() else self.months.index(
                                  results.group(1)[:3].lower()),
                              int(results.group(2)))
        self.valid = start[2] < self.days[start[1]] and not (not start[0] % 4 and start[1] == 2 and start[2] == 29)
    
    def __sub__(self, other):
        """
        Method that subtracts one Date object from another
        
        Parameters
        ----------
        other : Date
            Date object that is being subtracted
        
        Returns
        --------
        int
            Number of days between two Dates or -1 if one of the dates is invalid
        """
        
        if not self.valid or not other:
            return -1
        end = other.start
        start = self.start
        s = start[0] * 365 + sum(self.days[:start[1]]) + start[2] + (start[0] - 1) // 4
        s += 1 if start[0] * 365 + 60 < s and not start[0] % 4 else 0
        e = end[0] * 365 + sum(self.days[:end[1]]) + end[2] + (end[0] - 1) // 4
        e += 1 if end[0] * 365 + 60 < e and not end[0] % 4 else 0
        return s - e
    
    def __bool__(self):
        """
        Determine whether the Date is valid
        
        Returns
        -------
        bool
            Whether the start date of the Date object is valid
        """
        
        return self.valid
