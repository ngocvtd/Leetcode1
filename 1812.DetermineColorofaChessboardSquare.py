class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        letter = coordinates[0]
        num = int(coordinates[1])

        if (letter in 'aceg' and num % 2 == 0) or (letter in 'bdfh' and num % 2 != 0):
            return True
        else:
            return False
