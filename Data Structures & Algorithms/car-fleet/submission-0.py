class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [4,1,0,7] position
        [2,2,1,1] speed

        """
        fleet = []
        posSpeed = []
        for n in range(len(position)):
            posSpeed.append([position[n], speed[n]])
        posSpeed = sorted(posSpeed, reverse=True)
        print(posSpeed)
        

        for position,speed in posSpeed:
            time = (target-position)/speed
            if len(fleet) == 0:
                fleet.append(time)
            elif(time > fleet[-1]):
                fleet.append(time)
            continue
        
        return len(fleet)




